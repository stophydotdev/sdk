import type { Client } from "@hey-api/client-fetch";
import { getVideo } from "../generated/sdk.gen";
import type {
	GetVideoData,
	VideoResponseComments,
	VideoResponseDetails,
	VideoResponseLivechat,
	VideoResponseReplies,
	VideoResponseTranscript,
} from "../generated/types.gen";
import { unwrap } from "../transport";
import type { MeteredResponse } from "./response";

export type VideoResponseFor<T> = MeteredResponse<T>;
type VideoUrlBody = Extract<GetVideoData["body"], { videoUrl: string }>;
export type CommentsOptions = Pick<
	VideoUrlBody,
	"sortBy" | "continuationToken"
>;
export type TranscriptOptions = Pick<VideoUrlBody, "lang">;
export type LiveChatOptions = Pick<
	VideoUrlBody,
	"chatType" | "continuationToken"
>;

export async function video(
	client: Client,
	body: GetVideoData["body"],
): Promise<
	VideoResponseFor<
		| VideoResponseDetails
		| VideoResponseTranscript
		| VideoResponseComments
		| VideoResponseReplies
		| VideoResponseLivechat
	>
> {
	return unwrap(await getVideo({ client, body })) as VideoResponseFor<
		| VideoResponseDetails
		| VideoResponseTranscript
		| VideoResponseComments
		| VideoResponseReplies
		| VideoResponseLivechat
	>;
}

export function videoDetails(
	client: Client,
	videoUrl: string,
): Promise<VideoResponseFor<VideoResponseDetails>> {
	return video(client, { type: "details", videoUrl }) as Promise<
		VideoResponseFor<VideoResponseDetails>
	>;
}

export function transcript(
	client: Client,
	videoUrl: string,
	options: TranscriptOptions = {},
): Promise<VideoResponseFor<VideoResponseTranscript>> {
	return video(client, { type: "transcript", videoUrl, ...options }) as Promise<
		VideoResponseFor<VideoResponseTranscript>
	>;
}

export function comments(
	client: Client,
	videoUrl: string,
	options: CommentsOptions = {},
): Promise<VideoResponseFor<VideoResponseComments>> {
	return video(client, {
		type: "comments",
		videoUrl,
		...options,
	}) as Promise<VideoResponseFor<VideoResponseComments>>;
}

export function replies(
	client: Client,
	continuationToken: string,
): Promise<VideoResponseFor<VideoResponseReplies>> {
	return video(client, {
		type: "replies",
		continuationToken,
	}) as Promise<VideoResponseFor<VideoResponseReplies>>;
}

export function liveChat(
	client: Client,
	videoUrl: string,
	options: LiveChatOptions = {},
): Promise<VideoResponseFor<VideoResponseLivechat>> {
	return video(client, {
		type: "livechat",
		videoUrl,
		...options,
	}) as Promise<VideoResponseFor<VideoResponseLivechat>>;
}
