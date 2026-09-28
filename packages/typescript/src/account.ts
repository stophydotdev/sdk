import { StophyError } from "./errors";
import type { Caller } from "./transport";

export interface Usage {
	balanceMicros: number;
	creditsUsed: number;
	requestCount: number;
}

export interface LogEntry {
	apiKeyId: string | null;
	apiKeyName: string | null;
	createdAt: string;
	credits: number;
	durationMs: number | null;
	endpoint: string;
	id: string;
	method: string;
	response: string;
	status: number;
}

export interface Logs {
	endpoints: string[];
	logs: LogEntry[];
	page: number;
	pageSize: number;
	total: number;
	totalPages: number;
}

export interface LogsQuery {
	apiKeyId?: string;
	days?: number;
	endpoint?: string;
	page?: number;
}

export function usage(call: Caller): Promise<Usage> {
	return call({ method: "GET", path: "/v1/usage" }).then(parseUsage);
}

export function logs(call: Caller, query?: LogsQuery): Promise<Logs> {
	const params: Record<string, string | number | undefined> = {};
	if (query?.apiKeyId !== undefined) params.apiKeyId = query.apiKeyId;
	if (query?.days !== undefined) params.days = query.days;
	if (query?.endpoint !== undefined) params.endpoint = query.endpoint;
	if (query?.page !== undefined) params.page = query.page;
	return call({ method: "GET", path: "/v1/logs", query: params }).then(
		parseLogs,
	);
}

function parseUsage(value: unknown): Usage {
	if (!isRecord(value)) return unexpected("usage");
	const balanceMicros = numberField(value, "balanceMicros");
	const creditsUsed = numberField(value, "creditsUsed");
	const requestCount = numberField(value, "requestCount");
	return { balanceMicros, creditsUsed, requestCount };
}

function parseLogs(value: unknown): Logs {
	if (
		!isRecord(value) ||
		!Array.isArray(value.logs) ||
		!Array.isArray(value.endpoints)
	) {
		return unexpected("logs");
	}
	return {
		endpoints: value.endpoints.map((item) => {
			if (typeof item !== "string") return unexpected("logs.endpoints");
			return item;
		}),
		logs: value.logs.map(parseLog),
		page: numberField(value, "page"),
		pageSize: numberField(value, "pageSize"),
		total: numberField(value, "total"),
		totalPages: numberField(value, "totalPages"),
	};
}

function parseLog(value: unknown): LogEntry {
	if (!isRecord(value)) return unexpected("logs.logs");
	return {
		apiKeyId: stringOrNull(value, "apiKeyId"),
		apiKeyName: stringOrNull(value, "apiKeyName"),
		createdAt: stringField(value, "createdAt"),
		credits: numberField(value, "credits"),
		durationMs: numberOrNull(value, "durationMs"),
		endpoint: stringField(value, "endpoint"),
		id: stringField(value, "id"),
		method: stringField(value, "method"),
		response: stringField(value, "response"),
		status: numberField(value, "status"),
	};
}

function numberField(record: Record<string, unknown>, field: string): number {
	const value = record[field];
	if (typeof value !== "number") return unexpected(field);
	return value;
}

function numberOrNull(
	record: Record<string, unknown>,
	field: string,
): number | null {
	const value = record[field];
	if (value === null) return null;
	if (typeof value !== "number") return unexpected(field);
	return value;
}

function stringField(record: Record<string, unknown>, field: string): string {
	const value = record[field];
	if (typeof value !== "string") return unexpected(field);
	return value;
}

function stringOrNull(
	record: Record<string, unknown>,
	field: string,
): string | null {
	const value = record[field];
	if (value === null) return null;
	if (typeof value !== "string") return unexpected(field);
	return value;
}

function unexpected(field: string): never {
	throw new StophyError(`Stophy returned an unexpected ${field}`, {
		status: 200,
		retryable: false,
	});
}

function isRecord(value: unknown): value is Record<string, unknown> {
	return typeof value === "object" && value !== null && !Array.isArray(value);
}
