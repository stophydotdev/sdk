import type { Client } from "@hey-api/client-fetch";
import { searchVideos } from "../generated/sdk.gen";
import type {
	SearchVideosData,
	SearchVideosResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";

type SearchBody = SearchVideosData["body"];
export type SearchOptions = Omit<SearchBody, "q">;

export function search(
	client: Client,
	queryOrBody: string | SearchBody,
	options: SearchOptions = {},
): Promise<SearchVideosResponse> {
	if (typeof queryOrBody === "string" && !queryOrBody.trim()) {
		throw new Error("query cannot be empty");
	}
	const body =
		typeof queryOrBody === "string"
			? { q: queryOrBody, ...options }
			: queryOrBody;
	return searchVideos({ client, body }).then(unwrap);
}
