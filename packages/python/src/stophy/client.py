from __future__ import annotations

import os
from typing import Any, List, Literal, Mapping, Optional, overload

import httpx

from .methods import account as account_methods
from .methods import channel as channel_method
from .methods import kids as kids_method
from .methods import music as music_method
from .methods import playlist as playlist_method
from .methods import search as search_method
from .methods import suggest as suggest_method
from .methods import video as video_methods
from .transport import DEFAULT_BASE_URL, SyncTransport
from .types import (
    ChannelResponse,
    CommentsResponse,
    CreditsResponse,
    KidsResponse,
    LiveChatResponse,
    LogsResponse,
    MusicResponse,
    PlaylistResponse,
    RepliesResponse,
    SearchResponse,
    SuggestResponse,
    TranscriptResponse,
    UsageResponse,
    VideoDetailsResponse,
    VideoResponse,
)


class Stophy:
    """Synchronous typed client for the Stophy API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: float = 30.0,
        max_retries: int = 2,
        retry_initial_delay: float = 0.5,
        transport: Optional[httpx.BaseTransport] = None,
    ) -> None:
        resolved_key = (api_key or os.getenv("STOPHY_API_KEY", "")).strip()
        if not resolved_key:
            raise ValueError(
                "Stophy: provide api_key or set the STOPHY_API_KEY environment variable."
            )
        resolved_url = base_url or os.getenv("STOPHY_BASE_URL") or DEFAULT_BASE_URL
        self.client = httpx.Client(
            base_url=resolved_url,
            headers={"Authorization": f"Bearer {resolved_key}", **(headers or {})},
            timeout=timeout,
            transport=transport,
        )
        self._transport = SyncTransport(
            self.client,
            max_retries=max_retries,
            retry_initial_delay=retry_initial_delay,
        )

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
        lang: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> TranscriptResponse: ...

    @overload
    def video(
        self,
        *,
        type: Literal["comments"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> CommentsResponse: ...

    @overload
    def video(
        self,
        *,
        type: Literal["replies"],
        continuation_token: str,
    ) -> RepliesResponse: ...

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
        lang: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> VideoResponse:
        return video_methods.video(
            self._transport,
            type=type,
            video_url=video_url,
            sort_by=sort_by,
            chat_type=chat_type,
            lang=lang,
            continuation_token=continuation_token,
        )

    def video_details(self, video_url: str) -> VideoDetailsResponse:
        return video_methods.video_details(self._transport, video_url)

    def transcript(self, video_url: str, *, lang: Optional[str] = None) -> TranscriptResponse:
        return video_methods.transcript(self._transport, video_url, lang=lang)

    def comments(
        self,
        video_url: str,
        *,
        sort_by: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> CommentsResponse:
        return video_methods.comments(
            self._transport,
            video_url,
            sort_by=sort_by,
            continuation_token=continuation_token,
        )

    def replies(self, continuation_token: str) -> RepliesResponse:
        return video_methods.replies(self._transport, continuation_token)

    def live_chat(
        self,
        video_url: str,
        *,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> LiveChatResponse:
        return video_methods.live_chat(
            self._transport,
            video_url,
            chat_type=chat_type,
            continuation_token=continuation_token,
        )

    def search(
        self,
        q: str,
        *,
        type: Optional[str] = None,
        sort_by: Optional[str] = None,
        upload_date: Optional[str] = None,
        duration: Optional[str] = None,
        features: Optional[List[str]] = None,
        continuation_token: Optional[str] = None,
    ) -> SearchResponse:
        return search_method.search(
            self._transport,
            q,
            type=type,
            sort_by=sort_by,
            upload_date=upload_date,
            duration=duration,
            features=features,
            continuation_token=continuation_token,
        )

    def channel(
        self,
        channel_url: str,
        *,
        query: Optional[str] = None,
        tab: Optional[str] = None,
        sort_by: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> ChannelResponse:
        return channel_method.channel(
            self._transport,
            channel_url,
            query=query,
            tab=tab,
            sort_by=sort_by,
            continuation_token=continuation_token,
        )

    def playlist(
        self,
        playlist_url: str,
        *,
        continuation_token: Optional[str] = None,
    ) -> PlaylistResponse:
        return playlist_method.playlist(
            self._transport,
            playlist_url,
            continuation_token=continuation_token,
        )

    def suggest(
        self,
        q: str,
        *,
        hl: Optional[str] = None,
        gl: Optional[str] = None,
    ) -> SuggestResponse:
        return suggest_method.suggest(self._transport, q, hl=hl, gl=gl)

    def music(
        self,
        *,
        type: str,
        q: Optional[str] = None,
        search_type: Optional[str] = None,
        video_url: Optional[str] = None,
        album_url: Optional[str] = None,
        artist_url: Optional[str] = None,
        playlist_url: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> MusicResponse:
        return music_method.music(
            self._transport,
            type=type,
            q=q,
            search_type=search_type,
            video_url=video_url,
            album_url=album_url,
            artist_url=artist_url,
            playlist_url=playlist_url,
            continuation_token=continuation_token,
        )

    def kids(
        self,
        *,
        type: str,
        q: Optional[str] = None,
        video_url: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> KidsResponse:
        return kids_method.kids(
            self._transport,
            type=type,
            q=q,
            video_url=video_url,
            continuation_token=continuation_token,
        )

    def credits(self) -> CreditsResponse:
        return account_methods.credits(self._transport)

    def logs(
        self,
        *,
        days: Optional[str] = None,
        endpoint: Optional[str] = None,
        page: Optional[int] = None,
    ) -> LogsResponse:
        return account_methods.logs(self._transport, days=days, endpoint=endpoint, page=page)

    def usage(
        self,
        *,
        days: Optional[str] = None,
        tz: Optional[str] = None,
    ) -> UsageResponse:
        return account_methods.usage(self._transport, days=days, tz=tz)

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> "Stophy":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()
