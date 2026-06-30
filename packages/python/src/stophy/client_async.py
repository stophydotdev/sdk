from __future__ import annotations

import os
from typing import Any, List, Literal, Mapping, Optional, overload

import httpx

from .methods import account as account_methods
from .methods import channel as channel_method
from .methods import playlist as playlist_method
from .methods import search as search_method
from .methods import suggest as suggest_method
from .methods import video as video_methods
from .transport import DEFAULT_BASE_URL, AsyncTransport
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


class AsyncStophy:
    """Asynchronous typed client for the Stophy API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: float = 30.0,
        max_retries: int = 2,
        retry_initial_delay: float = 0.5,
        transport: Optional[httpx.AsyncBaseTransport] = None,
    ) -> None:
        resolved_key = (api_key or os.getenv("STOPHY_API_KEY", "")).strip()
        if not resolved_key:
            raise ValueError(
                "Stophy: provide api_key or set the STOPHY_API_KEY environment variable."
            )
        resolved_url = base_url or os.getenv("STOPHY_BASE_URL") or DEFAULT_BASE_URL
        self.client = httpx.AsyncClient(
            base_url=resolved_url,
            headers={"Authorization": f"Bearer {resolved_key}", **(headers or {})},
            timeout=timeout,
            transport=transport,
        )
        self._transport = AsyncTransport(
            self.client,
            max_retries=max_retries,
            retry_initial_delay=retry_initial_delay,
        )

    @overload
    async def video(
        self,
        *,
        type: Literal["details"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> VideoDetailsResponse: ...

    @overload
    async def video(
        self,
        *,
        type: Literal["transcript"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> TranscriptResponse: ...

    @overload
    async def video(
        self,
        *,
        type: Literal["comments", "replies"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> CommentsResponse: ...

    @overload
    async def video(
        self,
        *,
        type: Literal["livechat"],
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> LiveChatResponse: ...

    async def video(
        self,
        *,
        type: str,
        video_url: Optional[str] = None,
        sort_by: Optional[str] = None,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> VideoResponse:
        return await video_methods.video_async(
            self._transport,
            type=type,
            video_url=video_url,
            sort_by=sort_by,
            chat_type=chat_type,
            continuation_token=continuation_token,
        )

    async def video_details(self, video_url: str) -> VideoDetailsResponse:
        return await video_methods.video_details_async(self._transport, video_url)

    async def transcript(self, video_url: str) -> TranscriptResponse:
        return await video_methods.transcript_async(self._transport, video_url)

    async def comments(
        self,
        video_url: str,
        *,
        sort_by: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> CommentsResponse:
        return await video_methods.comments_async(
            self._transport,
            video_url,
            sort_by=sort_by,
            continuation_token=continuation_token,
        )

    async def replies(self, continuation_token: str) -> CommentsResponse:
        return await video_methods.replies_async(self._transport, continuation_token)

    async def live_chat(
        self,
        video_url: str,
        *,
        chat_type: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> LiveChatResponse:
        return await video_methods.live_chat_async(
            self._transport,
            video_url,
            chat_type=chat_type,
            continuation_token=continuation_token,
        )

    async def search(
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
        return await search_method.search_async(
            self._transport,
            q,
            type=type,
            sort_by=sort_by,
            upload_date=upload_date,
            duration=duration,
            features=features,
            continuation_token=continuation_token,
        )

    async def channel(
        self,
        channel_url: str,
        *,
        tab: Optional[str] = None,
        sort_by: Optional[str] = None,
        continuation_token: Optional[str] = None,
    ) -> ChannelResponse:
        return await channel_method.channel_async(
            self._transport,
            channel_url,
            tab=tab,
            sort_by=sort_by,
            continuation_token=continuation_token,
        )

    async def playlist(
        self,
        playlist_url: str,
        *,
        continuation_token: Optional[str] = None,
    ) -> PlaylistResponse:
        return await playlist_method.playlist_async(
            self._transport,
            playlist_url,
            continuation_token=continuation_token,
        )

    async def suggest(
        self,
        q: str,
        *,
        hl: Optional[str] = None,
        gl: Optional[str] = None,
    ) -> SuggestResponse:
        return await suggest_method.suggest_async(self._transport, q, hl=hl, gl=gl)

    async def credits(self) -> CreditsResponse:
        return await account_methods.credits_async(self._transport)

    async def logs(
        self,
        *,
        days: Optional[str] = None,
        endpoint: Optional[str] = None,
        page: Optional[int] = None,
    ) -> LogsResponse:
        return await account_methods.logs_async(
            self._transport, days=days, endpoint=endpoint, page=page
        )

    async def usage(
        self,
        *,
        days: Optional[str] = None,
        tz: Optional[str] = None,
    ) -> UsageResponse:
        return await account_methods.usage_async(self._transport, days=days, tz=tz)

    async def close(self) -> None:
        await self.client.aclose()

    async def __aenter__(self) -> "AsyncStophy":
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.close()
