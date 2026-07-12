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
import type { AccountResponse } from "./response";

export type CreditsResponse = AccountResponse<
	NonNullable<GetCreditsResponse["data"]>
>;
export type LogsResponse = AccountResponse<
	NonNullable<GetLogsResponse["data"]>
>;
export type UsageResponse = AccountResponse<
	NonNullable<GetUsageResponse["data"]>
>;

export function credits(client: Client): Promise<CreditsResponse> {
	return getCredits({ client }).then(unwrap) as Promise<CreditsResponse>;
}

export function logs(
	client: Client,
	query?: GetLogsData["query"],
): Promise<LogsResponse> {
	return getLogs({ client, query }).then(unwrap) as Promise<LogsResponse>;
}

export function usage(
	client: Client,
	query?: GetUsageData["query"],
): Promise<UsageResponse> {
	return getUsage({ client, query }).then(unwrap) as Promise<UsageResponse>;
}
