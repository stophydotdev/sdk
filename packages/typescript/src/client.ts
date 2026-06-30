import type { Client } from "@hey-api/client-fetch";
import type {
	CommentsData,
	GetChannelData,
	GetChannelResponse,
	GetCreditsResponse,
	GetLogsData,
	GetLogsResponse,
	GetPlaylistData,
	GetPlaylistResponse,
	GetSuggestionsData,
	GetSuggestionsResponse,
	GetUsageData,
	GetUsageResponse,
	GetVideoData,
	GetVideoResponse,
	LiveChatData,
	SearchVideosData,
	SearchVideosResponse,
	TranscriptResult,
	VideoDetailsData,
} from "./generated/types.gen";
import * as accountMethods from "./methods/account";
import { type ChannelOptions, channel as getChannel } from "./methods/channel";
import {
	playlist as getPlaylist,
	type PlaylistOptions,
} from "./methods/playlist";
import { type SearchOptions, search as searchVideos } from "./methods/search";
import {
	suggest as getSuggestions,
	type SuggestOptions,
} from "./methods/suggest";
import type {
	CommentsOptions,
	LiveChatOptions,
	VideoResponseFor,
} from "./methods/video";
import * as videoMethods from "./methods/video";
import { createTransport } from "./transport";

export interface StophyOptions {
	/** Defaults to `STOPHY_API_KEY`. */
	apiKey?: string;
	/** Defaults to `STOPHY_BASE_URL` or `https://api.stophy.dev`. */
	baseUrl?: string;
	fetch?: typeof globalThis.fetch;
	headers?: Record<string, string>;
	maxRetries?: number;
	retryInitialDelayMs?: number;
}

export type StophyClientInput = StophyOptions | string;

function env(name: string): string | undefined {
	return typeof process === "undefined" ? undefined : process.env[name];
}

/** Typed client for the Stophy API. */
export class Stophy {
	readonly client: Client;

	constructor(input: StophyClientInput = {}) {
		const options = typeof input === "string" ? { apiKey: input } : input;
		const apiKey = options.apiKey?.trim() || env("STOPHY_API_KEY")?.trim();
		if (!apiKey) {
			throw new Error(
				"Stophy: provide `apiKey` or set the STOPHY_API_KEY environment variable.",
			);
		}

		this.client = createTransport({
			...options,
			apiKey,
			baseUrl: options.baseUrl ?? env("STOPHY_BASE_URL"),
		});
	}

	async video(
		body: GetVideoData["body"] & { type: "details" },
	): Promise<VideoResponseFor<VideoDetailsData>>;
	async video(
		body: GetVideoData["body"] & { type: "transcript" },
	): Promise<VideoResponseFor<TranscriptResult>>;
	async video(
		body: GetVideoData["body"] & { type: "comments" | "replies" },
	): Promise<VideoResponseFor<CommentsData>>;
	async video(
		body: GetVideoData["body"] & { type: "livechat" },
	): Promise<VideoResponseFor<LiveChatData>>;
	async video(body: GetVideoData["body"]): Promise<GetVideoResponse>;
	async video(body: GetVideoData["body"]): Promise<GetVideoResponse> {
		return videoMethods.video(this.client, body);
	}

	videoDetails(videoUrl: string): Promise<VideoResponseFor<VideoDetailsData>> {
		return videoMethods.videoDetails(this.client, videoUrl);
	}

	transcript(videoUrl: string): Promise<VideoResponseFor<TranscriptResult>> {
		return videoMethods.transcript(this.client, videoUrl);
	}

	comments(
		videoUrl: string,
		options?: CommentsOptions,
	): Promise<VideoResponseFor<CommentsData>> {
		return videoMethods.comments(this.client, videoUrl, options);
	}

	replies(continuationToken: string): Promise<VideoResponseFor<CommentsData>> {
		return videoMethods.replies(this.client, continuationToken);
	}

	liveChat(
		videoUrl: string,
		options?: LiveChatOptions,
	): Promise<VideoResponseFor<LiveChatData>> {
		return videoMethods.liveChat(this.client, videoUrl, options);
	}

	async search(body: SearchVideosData["body"]): Promise<SearchVideosResponse>;
	async search(
		query: string,
		options?: SearchOptions,
	): Promise<SearchVideosResponse>;
	async search(
		queryOrBody: string | SearchVideosData["body"],
		options?: SearchOptions,
	): Promise<SearchVideosResponse> {
		return searchVideos(this.client, queryOrBody, options);
	}

	async channel(body: GetChannelData["body"]): Promise<GetChannelResponse>;
	async channel(
		channelUrl: string,
		options?: ChannelOptions,
	): Promise<GetChannelResponse>;
	async channel(
		urlOrBody: string | GetChannelData["body"],
		options?: ChannelOptions,
	): Promise<GetChannelResponse> {
		return getChannel(this.client, urlOrBody, options);
	}

	async playlist(body: GetPlaylistData["body"]): Promise<GetPlaylistResponse>;
	async playlist(
		playlistUrl: string,
		options?: PlaylistOptions,
	): Promise<GetPlaylistResponse>;
	async playlist(
		urlOrBody: string | GetPlaylistData["body"],
		options?: PlaylistOptions,
	): Promise<GetPlaylistResponse> {
		return getPlaylist(this.client, urlOrBody, options);
	}

	async suggest(
		query: GetSuggestionsData["query"],
	): Promise<GetSuggestionsResponse>;
	async suggest(
		query: string,
		options?: SuggestOptions,
	): Promise<GetSuggestionsResponse>;
	async suggest(
		queryOrOptions: string | GetSuggestionsData["query"],
		options?: SuggestOptions,
	): Promise<GetSuggestionsResponse> {
		return getSuggestions(this.client, queryOrOptions, options);
	}

	credits(): Promise<GetCreditsResponse> {
		return accountMethods.credits(this.client);
	}

	logs(query?: GetLogsData["query"]): Promise<GetLogsResponse> {
		return accountMethods.logs(this.client, query);
	}

	usage(query?: GetUsageData["query"]): Promise<GetUsageResponse> {
		return accountMethods.usage(this.client, query);
	}
}
