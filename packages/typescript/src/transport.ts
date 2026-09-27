import { StophyError } from "./errors";

const DEFAULT_BASE_URL = "https://api.stophy.dev";
const RETRYABLE_STATUS = new Set([429, 500, 502, 503, 504]);

export interface CallOptions {
	/** Send `Accept: text/markdown` and return the response body as a string. */
	format?: "markdown";
	signal?: AbortSignal;
}

export interface RequestSpec {
	method: "GET" | "POST";
	path: string;
	body?: unknown;
	query?: Record<string, string | number | undefined>;
	options?: CallOptions;
}

export type Caller = (spec: RequestSpec) => Promise<unknown>;

export type FetchLike = (
	input: RequestInfo | URL,
	init?: RequestInit,
) => Promise<Response>;

export interface TransportOptions {
	apiKey: string;
	baseUrl?: string;
	fetch?: FetchLike;
	headers?: Record<string, string>;
	maxRetries?: number;
	retryInitialDelayMs?: number;
}

export function createCaller(options: TransportOptions): Caller {
	const baseFetch: FetchLike = options.fetch ?? globalThis.fetch;
	const baseUrl = (options.baseUrl ?? DEFAULT_BASE_URL).replace(/\/$/, "");
	const maxRetries = options.maxRetries ?? 2;
	const initialDelayMs = options.retryInitialDelayMs ?? 500;

	return async (spec) => {
		const headers = new Headers(options.headers);
		headers.set("authorization", `Bearer ${options.apiKey}`);
		headers.set(
			"accept",
			spec.options?.format === "markdown"
				? "text/markdown"
				: "application/json",
		);
		if (spec.body !== undefined)
			headers.set("content-type", "application/json");

		const url = withQuery(`${baseUrl}${spec.path}`, spec.query);
		const response = await send(
			baseFetch,
			() => ({
				method: spec.method,
				headers,
				body: spec.body === undefined ? undefined : JSON.stringify(spec.body),
				signal: spec.options?.signal,
			}),
			url,
			maxRetries,
			initialDelayMs,
		);
		return readBody(response, spec.options?.format === "markdown");
	};
}

function send(
	baseFetch: FetchLike,
	init: () => RequestInit,
	url: string,
	maxRetries: number,
	initialDelayMs: number,
): Promise<Response> {
	const attempt = async (n: number): Promise<Response> => {
		try {
			const response = await baseFetch(url, init());
			if (n < maxRetries && RETRYABLE_STATUS.has(response.status)) {
				await sleep(retryDelayMs(response) ?? backoffMs(n, initialDelayMs));
				return attempt(n + 1);
			}
			return response;
		} catch (error) {
			if (isAbort(error) || n >= maxRetries) throw error;
			await sleep(backoffMs(n, initialDelayMs));
			return attempt(n + 1);
		}
	};
	return attempt(0);
}

function readBody(response: Response, markdown: boolean): Promise<unknown> {
	if (!response.ok) return reject(response);
	if (markdown) return response.text();
	return response.text().then((text) => {
		if (!text) {
			throw failed(response, "Stophy returned an empty response", {});
		}
		try {
			return JSON.parse(text);
		} catch {
			throw failed(response, "Stophy returned a non-JSON response", {});
		}
	});
}

async function reject(response: Response): Promise<never> {
	const text = await response.text();
	let body: unknown;
	if (text) {
		try {
			body = JSON.parse(text);
		} catch {
			body = undefined;
		}
	}
	const error = readError(body);
	const retryAfterSeconds =
		error.retryAfterSeconds ?? headerRetryAfter(response);
	throw failed(
		response,
		error.message ?? `Stophy request failed with status ${response.status}`,
		{
			code: error.code,
			retryable: error.retryable ?? RETRYABLE_STATUS.has(response.status),
			retryAfterSeconds,
			requestId: error.requestId ?? headerRequestId(response),
		},
	);
}

function failed(
	response: Response,
	message: string,
	options: {
		code?: string;
		retryable?: boolean;
		retryAfterSeconds?: number;
		requestId?: string;
	},
): StophyError {
	return new StophyError(message, {
		status: response.status,
		code: options.code,
		retryable: options.retryable ?? false,
		retryAfterSeconds: options.retryAfterSeconds,
		requestId: options.requestId ?? headerRequestId(response),
	});
}

interface ErrorFields {
	code?: string;
	message?: string;
	retryable?: boolean;
	retryAfterSeconds?: number;
	requestId?: string;
}

function readError(body: unknown): ErrorFields {
	if (!isRecord(body) || !isRecord(body.error)) return {};
	const error = body.error;
	return {
		code: typeof error.code === "string" ? error.code : undefined,
		message: typeof error.message === "string" ? error.message : undefined,
		retryable:
			typeof error.retryable === "boolean" ? error.retryable : undefined,
		retryAfterSeconds:
			typeof error.retryAfterSeconds === "number"
				? error.retryAfterSeconds
				: undefined,
		requestId:
			typeof error.requestId === "string" ? error.requestId : undefined,
	};
}

function isRecord(value: unknown): value is Record<string, unknown> {
	return typeof value === "object" && value !== null && !Array.isArray(value);
}

function headerRequestId(response: Response): string | undefined {
	return response.headers.get("x-request-id") ?? undefined;
}

function headerRetryAfter(response: Response): number | undefined {
	const header = response.headers.get("retry-after");
	if (!header) return undefined;
	const seconds = Number(header);
	if (Number.isFinite(seconds)) return seconds;
	const date = Date.parse(header);
	if (Number.isNaN(date)) return undefined;
	return Math.max(0, Math.ceil((date - Date.now()) / 1000));
}

function retryDelayMs(response: Response): number | undefined {
	const seconds = headerRetryAfter(response);
	return seconds === undefined ? undefined : seconds * 1000;
}

function withQuery(
	url: string,
	query: Record<string, string | number | undefined> | undefined,
): string {
	if (!query) return url;
	const params = new URLSearchParams();
	for (const [key, value] of Object.entries(query)) {
		if (value !== undefined) params.set(key, String(value));
	}
	const text = params.toString();
	return text ? `${url}?${text}` : url;
}

function backoffMs(attempt: number, base: number): number {
	const window = base * 2 ** attempt;
	return window / 2 + Math.random() * (window / 2);
}

function sleep(ms: number): Promise<void> {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function isAbort(error: unknown): boolean {
	return error instanceof Error && error.name === "AbortError";
}
