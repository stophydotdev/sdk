import type { Client } from "@hey-api/client-fetch";
import { getVideo } from "../generated/sdk.gen";
import type {
	CommentsData,
	GetVideoData,
	GetVideoResponse,
	LiveChatData,
	TranscriptResult,
	VideoDetailsData,
} from "../generated/types.gen";
import { unwrap } from "../transport";

export type VideoResponseFor<T> = Omit<GetVideoResponse, "data"> & { data: T };
type VideoUrlBody = Extract<GetVideoData["body"], { videoUrl: string }>;
export type CommentsOptions = Pick<
	VideoUrlBody,
	"sortBy" | "continuationToken"
>;
export type LiveChatOptions = Pick<
	VideoUrlBody,
	"chatType" | "continuationToken"
>;

export async function video(
	client: Client,
	body: GetVideoData["body"],
): Promise<GetVideoResponse> {
	return unwrap(await getVideo({ client, body }));
}

export function videoDetails(
	client: Client,
	videoUrl: string,
): Promise<VideoResponseFor<VideoDetailsData>> {
	return video(client, { type: "details", videoUrl }) as Promise<
		VideoResponseFor<VideoDetailsData>
	>;
}

export function transcript(
	client: Client,
	videoUrl: string,
): Promise<VideoResponseFor<TranscriptResult>> {
	return video(client, { type: "transcript", videoUrl }) as Promise<
		VideoResponseFor<TranscriptResult>
	>;
}

export function comments(
	client: Client,
	videoUrl: string,
	options: CommentsOptions = {},
): Promise<VideoResponseFor<CommentsData>> {
	return video(client, {
		type: "comments",
		videoUrl,
		...options,
	}) as Promise<VideoResponseFor<CommentsData>>;
}

export function replies(
	client: Client,
	continuationToken: string,
): Promise<VideoResponseFor<CommentsData>> {
	return video(client, {
		type: "replies",
		continuationToken,
	}) as Promise<VideoResponseFor<CommentsData>>;
}

export function liveChat(
	client: Client,
	videoUrl: string,
	options: LiveChatOptions = {},
): Promise<VideoResponseFor<LiveChatData>> {
	return video(client, {
		type: "livechat",
		videoUrl,
		...options,
	}) as Promise<VideoResponseFor<LiveChatData>>;
}
