import type { Client } from "@hey-api/client-fetch";
import { getPlaylist } from "../generated/sdk.gen";
import type {
	GetPlaylistData,
	GetPlaylistResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";
import type { MeteredResponse } from "./response";

type PlaylistBody = GetPlaylistData["body"];
export type PlaylistOptions = Omit<PlaylistBody, "playlistUrl">;
export type PlaylistResponse = MeteredResponse<
	NonNullable<GetPlaylistResponse["data"]>
>;

export function playlist(
	client: Client,
	urlOrBody: string | PlaylistBody,
	options: PlaylistOptions = {},
): Promise<PlaylistResponse> {
	const body =
		typeof urlOrBody === "string"
			? { playlistUrl: urlOrBody, ...options }
			: urlOrBody;
	return getPlaylist({ client, body }).then(
		unwrap,
	) as Promise<PlaylistResponse>;
}
