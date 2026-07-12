import type { Client } from "@hey-api/client-fetch";
import { searchVideos } from "../generated/sdk.gen";
import type {
	SearchVideosData,
	SearchVideosResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";
import type { MeteredResponse } from "./response";

type SearchBody = SearchVideosData["body"];
export type SearchOptions = Omit<SearchBody, "q">;
export type SearchResponse = MeteredResponse<
	NonNullable<SearchVideosResponse["data"]>
>;

export function search(
	client: Client,
	queryOrBody: string | SearchBody,
	options: SearchOptions = {},
): Promise<SearchResponse> {
	if (typeof queryOrBody === "string" && !queryOrBody.trim()) {
		throw new Error("query cannot be empty");
	}
	const body =
		typeof queryOrBody === "string"
			? { q: queryOrBody, ...options }
			: queryOrBody;
	return searchVideos({ client, body }).then(unwrap) as Promise<SearchResponse>;
}
