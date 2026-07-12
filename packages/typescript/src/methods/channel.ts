import type { Client } from "@hey-api/client-fetch";
import { getChannel } from "../generated/sdk.gen";
import type {
	GetChannelData,
	GetChannelResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";
import type { MeteredResponse } from "./response";

type ChannelBody = GetChannelData["body"];
export type ChannelOptions = Omit<ChannelBody, "channelUrl">;
type GeneratedChannelData = NonNullable<GetChannelResponse["data"]>;
type GeneratedChannelItem = GeneratedChannelData["items"][number];

export interface ChannelCourseItem {
	type: "course";
	id: string;
	url: string;
	courseUrl: string;
	playlistUrl: string;
	title: string | null;
	author: string | null;
	authorId: string | null;
	videoCount: number | null;
	videoCountText: string | null;
	thumbnails: Array<{ url: string; width: number; height: number }>;
}

export type ChannelData = Omit<GeneratedChannelData, "items" | "tab"> & {
	items: Array<GeneratedChannelItem | ChannelCourseItem>;
	tab: ChannelBody["tab"] | "community" | "course";
};

export type ChannelResponse = MeteredResponse<ChannelData>;

export function channel(
	client: Client,
	urlOrBody: string | ChannelBody,
	options: ChannelOptions = {},
): Promise<ChannelResponse> {
	const body =
		typeof urlOrBody === "string"
			? { channelUrl: urlOrBody, ...options }
			: urlOrBody;
	return getChannel({ client, body }).then(unwrap) as Promise<ChannelResponse>;
}
