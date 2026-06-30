import type { Client } from "@hey-api/client-fetch";
import { getCredits, getLogs, getUsage } from "../generated/sdk.gen";
import type {
	GetCreditsResponse,
	GetLogsData,
	GetLogsResponse,
	GetUsageData,
	GetUsageResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";

export function credits(client: Client): Promise<GetCreditsResponse> {
	return getCredits({ client }).then(unwrap);
}

export function logs(
	client: Client,
	query?: GetLogsData["query"],
): Promise<GetLogsResponse> {
	return getLogs({ client, query }).then(unwrap);
}

export function usage(
	client: Client,
	query?: GetUsageData["query"],
): Promise<GetUsageResponse> {
	return getUsage({ client, query }).then(unwrap);
}
