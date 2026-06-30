from __future__ import annotations

from typing import Optional, cast

from ..transport import AsyncTransport, SyncTransport
from ..types import (
    CommentsResponse,
    LiveChatResponse,
    TranscriptResponse,
    VideoDetailsResponse,
    VideoResponse,
)


def _payload(
    *,
    type: str,
    video_url: Optional[str] = None,
    sort_by: Optional[str] = None,
    chat_type: Optional[str] = None,
    continuation_token: Optional[str] = None,
):
    return {
        "type": type,
        "videoUrl": video_url,
        "sortBy": sort_by,
        "chatType": chat_type,
        "continuationToken": continuation_token,
    }


def video(transport: SyncTransport, **options) -> VideoResponse:
    return cast(VideoResponse, transport.post("/v1/video", _payload(**options)))


async def video_async(transport: AsyncTransport, **options) -> VideoResponse:
    return cast(VideoResponse, await transport.post("/v1/video", _payload(**options)))


def video_details(transport: SyncTransport, video_url: str) -> VideoDetailsResponse:
    return cast(VideoDetailsResponse, video(transport, type="details", video_url=video_url))


async def video_details_async(transport: AsyncTransport, video_url: str) -> VideoDetailsResponse:
    return cast(
        VideoDetailsResponse,
        await video_async(transport, type="details", video_url=video_url),
    )


def transcript(transport: SyncTransport, video_url: str) -> TranscriptResponse:
    return cast(TranscriptResponse, video(transport, type="transcript", video_url=video_url))


async def transcript_async(transport: AsyncTransport, video_url: str) -> TranscriptResponse:
    return cast(
        TranscriptResponse,
        await video_async(transport, type="transcript", video_url=video_url),
    )


def comments(
    transport: SyncTransport,
    video_url: str,
    *,
    sort_by: Optional[str] = None,
    continuation_token: Optional[str] = None,
) -> CommentsResponse:
    return cast(
        CommentsResponse,
        video(
            transport,
            type="comments",
            video_url=video_url,
            sort_by=sort_by,
            continuation_token=continuation_token,
        ),
    )


async def comments_async(
    transport: AsyncTransport,
    video_url: str,
    *,
    sort_by: Optional[str] = None,
    continuation_token: Optional[str] = None,
) -> CommentsResponse:
    return cast(
        CommentsResponse,
        await video_async(
            transport,
            type="comments",
            video_url=video_url,
            sort_by=sort_by,
            continuation_token=continuation_token,
        ),
    )


def replies(transport: SyncTransport, continuation_token: str) -> CommentsResponse:
    return cast(
        CommentsResponse,
        video(transport, type="replies", continuation_token=continuation_token),
    )


async def replies_async(transport: AsyncTransport, continuation_token: str) -> CommentsResponse:
    return cast(
        CommentsResponse,
        await video_async(transport, type="replies", continuation_token=continuation_token),
    )


def live_chat(
    transport: SyncTransport,
    video_url: str,
    *,
    chat_type: Optional[str] = None,
    continuation_token: Optional[str] = None,
) -> LiveChatResponse:
    return cast(
        LiveChatResponse,
        video(
            transport,
            type="livechat",
            video_url=video_url,
            chat_type=chat_type,
            continuation_token=continuation_token,
        ),
    )


async def live_chat_async(
    transport: AsyncTransport,
    video_url: str,
    *,
    chat_type: Optional[str] = None,
    continuation_token: Optional[str] = None,
) -> LiveChatResponse:
    return cast(
        LiveChatResponse,
        await video_async(
            transport,
            type="livechat",
            video_url=video_url,
            chat_type=chat_type,
            continuation_token=continuation_token,
        ),
    )
