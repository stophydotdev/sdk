import type { Client } from "@hey-api/client-fetch";
import { youtubeMusic } from "../generated/sdk.gen";
import type {
	MusicAlbumData,
	MusicArtistData,
	MusicLyricsData,
	MusicPlaylistData,
	MusicSearchData,
	MusicSongData,
	MusicSuggestData,
	YoutubeMusicData,
} from "../generated/types.gen";
import { unwrap } from "../transport";
import type { MeteredResponse } from "./response";

type GeneratedMusicBody = YoutubeMusicData["body"];
type SearchType = NonNullable<GeneratedMusicBody["searchType"]>;

export type MusicInput =
	| {
			type: "search";
			q: string;
			searchType?: SearchType;
			continuationToken?: string;
	  }
	| { type: "suggest"; q: string }
	| { type: "song" | "lyrics"; videoUrl: string }
	| { type: "album"; albumUrl: string }
	| { type: "artist"; artistUrl: string }
	| {
			type: "playlist";
			playlistUrl: string;
			continuationToken?: string;
	  };

export type MusicDataFor<T extends MusicInput["type"]> = T extends "search"
	? MusicSearchData
	: T extends "suggest"
		? MusicSuggestData
		: T extends "song"
			? MusicSongData
			: T extends "lyrics"
				? MusicLyricsData
				: T extends "album"
					? MusicAlbumData
					: T extends "artist"
						? MusicArtistData
						: MusicPlaylistData;

export function music<T extends MusicInput>(
	client: Client,
	body: T,
): Promise<MeteredResponse<MusicDataFor<T["type"]>>> {
	return youtubeMusic({ client, body }).then(unwrap) as Promise<
		MeteredResponse<MusicDataFor<T["type"]>>
	>;
}
