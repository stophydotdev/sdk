import type { Client } from "@hey-api/client-fetch";
import { getSuggestions } from "../generated/sdk.gen";
import type {
	GetSuggestionsData,
	GetSuggestionsResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";

type SuggestQuery = GetSuggestionsData["query"];
export type SuggestOptions = Omit<SuggestQuery, "q">;

export function suggest(
	client: Client,
	queryOrOptions: string | SuggestQuery,
	options: SuggestOptions = {},
): Promise<GetSuggestionsResponse> {
	if (typeof queryOrOptions === "string" && !queryOrOptions.trim()) {
		throw new Error("query cannot be empty");
	}
	const query =
		typeof queryOrOptions === "string"
			? { q: queryOrOptions, ...options }
			: queryOrOptions;
	return getSuggestions({ client, query }).then(unwrap);
}
