import type { Client } from "@hey-api/client-fetch";
import { getPlaylist } from "../generated/sdk.gen";
import type {
	GetPlaylistData,
	GetPlaylistResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";

type PlaylistBody = GetPlaylistData["body"];
export type PlaylistOptions = Omit<PlaylistBody, "playlistUrl">;

export function playlist(
	client: Client,
	urlOrBody: string | PlaylistBody,
	options: PlaylistOptions = {},
): Promise<GetPlaylistResponse> {
	const body =
		typeof urlOrBody === "string"
			? { playlistUrl: urlOrBody, ...options }
			: urlOrBody;
	return getPlaylist({ client, body }).then(unwrap);
}
