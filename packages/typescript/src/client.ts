import type { Client } from "@hey-api/client-fetch";
import type {
	GetChannelData,
	GetLogsData,
	GetPlaylistData,
	GetSuggestionsData,
	GetUsageData,
	GetVideoData,
	GetVideoResponse,
	SearchVideosData,
	VideoResponseComments,
	VideoResponseDetails,
	VideoResponseLivechat,
	VideoResponseReplies,
	VideoResponseTranscript,
} from "./generated/types.gen";
import type {
	CreditsResponse,
	LogsResponse,
	UsageResponse,
} from "./methods/account";
import * as accountMethods from "./methods/account";
import {
	type ChannelOptions,
	type ChannelResponse,
	channel as getChannel,
} from "./methods/channel";
import {
	kids as getKids,
	type KidsDataFor,
	type KidsInput,
} from "./methods/kids";
import {
	music as getMusic,
	type MusicDataFor,
	type MusicInput,
} from "./methods/music";
import {
	playlist as getPlaylist,
	type PlaylistOptions,
	type PlaylistResponse,
} from "./methods/playlist";
import type { MeteredResponse } from "./methods/response";
import {
	type SearchOptions,
	type SearchResponse,
	search as searchVideos,
} from "./methods/search";
import {
	suggest as getSuggestions,
	type SuggestOptions,
	type SuggestResponse,
} from "./methods/suggest";
import type {
	CommentsOptions,
	LiveChatOptions,
	TranscriptOptions,
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
	): Promise<VideoResponseFor<VideoResponseDetails>>;
	async video(
		body: GetVideoData["body"] & { type: "transcript" },
	): Promise<VideoResponseFor<VideoResponseTranscript>>;
	async video(
		body: GetVideoData["body"] & { type: "comments" },
	): Promise<VideoResponseFor<VideoResponseComments>>;
	async video(
		body: GetVideoData["body"] & { type: "replies" },
	): Promise<VideoResponseFor<VideoResponseReplies>>;
	async video(
		body: GetVideoData["body"] & { type: "livechat" },
	): Promise<VideoResponseFor<VideoResponseLivechat>>;
	async video(body: GetVideoData["body"]): Promise<GetVideoResponse>;
	async video(body: GetVideoData["body"]): Promise<GetVideoResponse> {
		return videoMethods.video(this.client, body);
	}

	videoDetails(
		videoUrl: string,
	): Promise<VideoResponseFor<VideoResponseDetails>> {
		return videoMethods.videoDetails(this.client, videoUrl);
	}

	transcript(
		videoUrl: string,
		options?: TranscriptOptions,
	): Promise<VideoResponseFor<VideoResponseTranscript>> {
		return videoMethods.transcript(this.client, videoUrl, options);
	}

	comments(
		videoUrl: string,
		options?: CommentsOptions,
	): Promise<VideoResponseFor<VideoResponseComments>> {
		return videoMethods.comments(this.client, videoUrl, options);
	}

	replies(
		continuationToken: string,
	): Promise<VideoResponseFor<VideoResponseReplies>> {
		return videoMethods.replies(this.client, continuationToken);
	}

	liveChat(
		videoUrl: string,
		options?: LiveChatOptions,
	): Promise<VideoResponseFor<VideoResponseLivechat>> {
		return videoMethods.liveChat(this.client, videoUrl, options);
	}

	async search(body: SearchVideosData["body"]): Promise<SearchResponse>;
	async search(query: string, options?: SearchOptions): Promise<SearchResponse>;
	async search(
		queryOrBody: string | SearchVideosData["body"],
		options?: SearchOptions,
	): Promise<SearchResponse> {
		return searchVideos(this.client, queryOrBody, options);
	}

	async channel(body: GetChannelData["body"]): Promise<ChannelResponse>;
	async channel(
		channelUrl: string,
		options?: ChannelOptions,
	): Promise<ChannelResponse>;
	async channel(
		urlOrBody: string | GetChannelData["body"],
		options?: ChannelOptions,
	): Promise<ChannelResponse> {
		return getChannel(this.client, urlOrBody, options);
	}

	async playlist(body: GetPlaylistData["body"]): Promise<PlaylistResponse>;
	async playlist(
		playlistUrl: string,
		options?: PlaylistOptions,
	): Promise<PlaylistResponse>;
	async playlist(
		urlOrBody: string | GetPlaylistData["body"],
		options?: PlaylistOptions,
	): Promise<PlaylistResponse> {
		return getPlaylist(this.client, urlOrBody, options);
	}

	async suggest(query: GetSuggestionsData["body"]): Promise<SuggestResponse>;
	async suggest(
		query: string,
		options?: SuggestOptions,
	): Promise<SuggestResponse>;
	async suggest(
		queryOrOptions: string | GetSuggestionsData["body"],
		options?: SuggestOptions,
	): Promise<SuggestResponse> {
		return getSuggestions(this.client, queryOrOptions, options);
	}

	music<T extends MusicInput>(
		body: T,
	): Promise<MeteredResponse<MusicDataFor<T["type"]>>> {
		return getMusic(this.client, body);
	}

	kids<T extends KidsInput>(
		body: T,
	): Promise<MeteredResponse<KidsDataFor<T["type"]>>> {
		return getKids(this.client, body);
	}

	credits(): Promise<CreditsResponse> {
		return accountMethods.credits(this.client);
	}

	logs(query?: GetLogsData["query"]): Promise<LogsResponse> {
		return accountMethods.logs(this.client, query);
	}

	usage(query?: GetUsageData["query"]): Promise<UsageResponse> {
		return accountMethods.usage(this.client, query);
	}
}
