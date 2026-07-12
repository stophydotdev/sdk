import type { Client } from "@hey-api/client-fetch";
import { getSuggestions } from "../generated/sdk.gen";
import type {
	GetSuggestionsData,
	GetSuggestionsResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";
import type { MeteredResponse } from "./response";

type SuggestBody = GetSuggestionsData["body"];
export type SuggestOptions = Omit<SuggestBody, "q">;
export type SuggestResponse = MeteredResponse<
	NonNullable<GetSuggestionsResponse["data"]>
>;

export function suggest(
	client: Client,
	queryOrOptions: string | SuggestBody,
	options: SuggestOptions = {},
): Promise<SuggestResponse> {
	if (typeof queryOrOptions === "string" && !queryOrOptions.trim()) {
		throw new Error("query cannot be empty");
	}
	const body =
		typeof queryOrOptions === "string"
			? { q: queryOrOptions, ...options }
			: queryOrOptions;
	return getSuggestions({ client, body }).then(
		unwrap,
	) as Promise<SuggestResponse>;
}
