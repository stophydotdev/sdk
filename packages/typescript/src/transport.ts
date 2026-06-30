import { type Client, createClient, createConfig } from "@hey-api/client-fetch";
import { StophyError } from "./errors";
import type { ErrorResponse } from "./generated/types.gen";

const DEFAULT_BASE_URL = "https://api.stophy.dev";
const RETRYABLE_STATUS = new Set([429, 500, 502, 503, 504]);

export interface TransportOptions {
	apiKey: string;
	baseUrl?: string;
	fetch?: typeof globalThis.fetch;
	headers?: Record<string, string>;
	maxRetries?: number;
	retryInitialDelayMs?: number;
}

export function createTransport(options: TransportOptions): Client {
	const baseFetch = options.fetch ?? globalThis.fetch;
	return createClient(
		createConfig({
			baseUrl: options.baseUrl ?? DEFAULT_BASE_URL,
			auth: () => options.apiKey,
			headers: options.headers,
			fetch: withRetries(
				baseFetch,
				options.maxRetries ?? 2,
				options.retryInitialDelayMs ?? 500,
			),
		}),
	);
}

type FetchFn = (
	input: Request | URL | string,
	init?: RequestInit,
) => Promise<Response>;

function withRetries(
	baseFetch: typeof globalThis.fetch,
	maxRetries: number,
	initialDelayMs: number,
): FetchFn {
	if (maxRetries <= 0) return baseFetch;

	return async (input, init) => {
		for (let attempt = 0; ; attempt++) {
			const request = input instanceof Request ? input.clone() : input;
			try {
				const response = await baseFetch(request, init);
				if (attempt < maxRetries && RETRYABLE_STATUS.has(response.status)) {
					await sleep(
						retryAfterMs(response) ?? backoffMs(attempt, initialDelayMs),
					);
					continue;
				}
				return response;
			} catch (error) {
				if (attempt >= maxRetries) throw error;
				await sleep(backoffMs(attempt, initialDelayMs));
			}
		}
	};
}

function backoffMs(attempt: number, base: number): number {
	const window = base * 2 ** attempt;
	return window / 2 + Math.random() * (window / 2);
}

function retryAfterMs(response: Response): number | null {
	const header = response.headers.get("retry-after");
	if (!header) return null;
	const seconds = Number(header);
	if (!Number.isNaN(seconds)) return seconds * 1000;
	const date = Date.parse(header);
	return Number.isNaN(date) ? null : Math.max(0, date - Date.now());
}

function sleep(ms: number): Promise<void> {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

export function unwrap<T>(result: {
	data?: T;
	error?: unknown;
	response: Response;
}): T {
	if (result.error === undefined && result.data !== undefined)
		return result.data;

	const error = (result.error ?? {}) as Partial<ErrorResponse>;
	throw new StophyError(
		error.error ??
			`Stophy request failed with status ${result.response.status}`,
		{
			status: result.response.status,
			code: error.code,
			requestId: result.response.headers.get("x-request-id") ?? undefined,
			details: error.details,
		},
	);
}
