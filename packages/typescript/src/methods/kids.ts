import type { Client } from "@hey-api/client-fetch";
import { youtubeKids } from "../generated/sdk.gen";
import type { KidsSearchData, KidsVideoData } from "../generated/types.gen";
import { unwrap } from "../transport";
import type { MeteredResponse } from "./response";

export type KidsInput =
	| { type: "search"; q: string; continuationToken?: string }
	| { type: "video"; videoUrl: string };

export type KidsDataFor<T extends KidsInput["type"]> = T extends "search"
	? KidsSearchData
	: KidsVideoData;

export function kids<T extends KidsInput>(
	client: Client,
	body: T,
): Promise<MeteredResponse<KidsDataFor<T["type"]>>> {
	return youtubeKids({ client, body }).then(unwrap) as Promise<
		MeteredResponse<KidsDataFor<T["type"]>>
	>;
}
