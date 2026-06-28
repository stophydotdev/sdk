from __future__ import annotations

import random
import time
from email.utils import parsedate_to_datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, overload

import httpx

from .errors import StophyError
from .types import (
    ChannelResponse,
    CommentsResponse,
    CreditsResponse,
    LiveChatResponse,
    LogsResponse,
    PlaylistResponse,
    SearchResponse,
    SuggestResponse,
    TranscriptResponse,
    UsageResponse,
    VideoDetailsResponse,
    VideoResponse,
)

DEFAULT_BASE_URL = "https://api.stophy.dev"
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def _compact(params: Mapping[str, Any]) -> Dict[str, Any]:
    """Drop keys whose value is None so we only send what the caller set."""
    return {k: v for k, v in params.items() if v is not None}


class Stophy:
    """Client for Stophy — YouTube context API for AI agents.

    >>> stophy = Stophy(os.environ["STOPHY_API_KEY"])
    >>> result = stophy.video(type="transcript", video_url=url)
    >>> print(result["data"]["text"])
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        headers: Optional[Mapping[str, str]] = None,
        timeout: float = 30.0,
        max_retries: int = 2,
        retry_initial_delay: float = 0.5,
        transport: Optional[httpx.BaseTransport] = None,
    ) -> None:
        if not api_key:
            raise ValueError("Stophy: api_key is required.")
        self._max_retries = max_retries
        self._retry_base = retry_initial_delay
        self.client = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}", **(headers or {})},
            timeout=timeout,
            transport=transport,
        )

    # --- endpoints ---------------------------------------------------------

    @overload
    def video(
        self,
        *,
        type: Literal["details"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> VideoDetailsResponse: ...

    @overload
    def video(
        self,
        *,
        type: Literal["transcript"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> TranscriptResponse: ...

    @overload
    def video(
        self,
        *,
        type: Literal["comments", "replies"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> CommentsResponse: ...

    @overload
    def video(
        self,
        *,
        type: Literal["livechat"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> LiveChatResponse: ...

    def video(
        self,
        *,
        type: str,
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> VideoResponse:
        """Video details, transcript, comments, replies, or live chat — pick with ``type``.

        The shape of ``data`` depends on ``type`` (details / transcript /
        comments / replies / livechat).
        """
        return self._post(
            "/v1/video",
            {
                "type": type,
                "videoUrl": video_url,
                "sortBy": sort_by,
                "chatType": chat_type,
                "continuationToken": continuation_token,
            },
        )

    def search(
        self,
        *,
        q: str,
        type: Optional[str] = None,
        sort_by: Optional[str] = None,
        upload_date: Optional[str] = None,
        duration: Optional[str] = None,
        features: Optional[List[str]] = None,
        continuation_token: Optional[str] = None,
    ) -> SearchResponse:
        """Search YouTube, optionally filtered by type, sort, date, duration, and features."""
        return self._post(
            "/v1/search",
            {
                "q": q,
                "type": type,
                "sortBy": sort_by,
                "uploadDate": upload_date,
                "duration": duration,
                "features": features,
                "continuationToken": continuation_token,
            },
        )

    def channel(
        self,
        *,
        channel_url: str,
        tab: Optional[str] = None,
        sort_by: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> ChannelResponse:
        """Channel metadata and content. Switch sections with ``tab``."""
        return self._post(
            "/v1/channel",
            {
                "channelUrl": channel_url,
                "tab": tab,
                "sortBy": sort_by,
                "continuationToken": continuation_token,
            },
        )

    def playlist(
        self,
        *,
        playlist_url: str,
        continuation_token: Optional[str] = None,
    ) -> PlaylistResponse:
        """Playlist items. Page through long playlists with ``continuation_token``."""
        return self._post(
            "/v1/playlist",
            {"playlistUrl": playlist_url, "continuationToken": continuation_token},
        )

    def suggest(
        self,
        *,
        q: str,
        hl: Optional[str] = None,
        gl: Optional[str] = None,
    ) -> SuggestResponse:
        """Search autocomplete suggestions."""
        return self._get("/v1/suggest", {"q": q, "hl": hl, "gl": gl})

    def credits(self) -> CreditsResponse:
        """Your current credit balance."""
        return self._get("/v1/credits")

    def logs(
        self,
        *,
        days: Optional[str] = None,
        endpoint: Optional[str] = None,
        page: Optional[int] = None,
    ) -> LogsResponse:
        """Recent API request logs."""
        return self._get("/v1/logs", {"days": days, "endpoint": endpoint, "page": page})

    def usage(
        self,
        *,
        days: Optional[str] = None,
        tz: Optional[str] = None,
    ) -> UsageResponse:
        """Daily credit and request counts."""
        return self._get("/v1/usage", {"days": days, "tz": tz})

    # --- plumbing ----------------------------------------------------------

    def _get(self, path: str, params: Optional[Mapping[str, Any]] = None) -> Any:
        return self._handle(self._send("GET", path, params=_compact(params or {})))

    def _post(self, path: str, body: Mapping[str, Any]) -> Any:
        return self._handle(self._send("POST", path, json=_compact(body)))

    def _send(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        """Send a request, retrying transient failures with backoff + jitter.

        Every Stophy endpoint is a read, so retrying is always safe.
        """
        attempt = 0
        while True:
            try:
                resp = self.client.request(method, path, **kwargs)
            except httpx.TransportError:
                if attempt >= self._max_retries:
                    raise
                time.sleep(self._backoff(attempt))
                attempt += 1
                continue
            if attempt < self._max_retries and resp.status_code in RETRYABLE_STATUS:
                time.sleep(self._retry_after(resp, attempt))
                attempt += 1
                continue
            return resp

    def _backoff(self, attempt: int) -> float:
        window = self._retry_base * (2**attempt)
        return window / 2 + random.random() * (window / 2)

    def _retry_after(self, resp: httpx.Response, attempt: int) -> float:
        header = resp.headers.get("retry-after")
        if header:
            try:
                return float(header)
            except ValueError:
                try:
                    delay = parsedate_to_datetime(header).timestamp() - time.time()
                    return max(0.0, delay)
                except (TypeError, ValueError):
                    pass
        return self._backoff(attempt)

    def _handle(self, resp: httpx.Response) -> Dict[str, Any]:
        try:
            payload = resp.json()
        except ValueError:
            payload = None

        if resp.is_success and isinstance(payload, dict):
            return payload

        err = payload if isinstance(payload, dict) else {}
        raise StophyError(
            err.get("error") or f"Stophy request failed with status {resp.status_code}",
            status=resp.status_code,
            code=err.get("code"),
            request_id=resp.headers.get("x-request-id"),
            details=err.get("details"),
        )

    # --- lifecycle ---------------------------------------------------------

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> "Stophy":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()
