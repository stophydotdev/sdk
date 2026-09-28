import { version } from "../package.json";
import { StophyError } from "./errors";

const DEFAULT_BASE_URL = "https://api.stophy.dev";
const DEFAULT_TIMEOUT_MS = 30_000;
const MAX_RETRY_WAIT_SECONDS = 60;
const RETRYABLE_STATUS = new Set([429, 500, 502, 503, 504]);
const USER_AGENT = `stophy-typescript/${version}`;

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
	apiKey?: string;
	baseUrl?: string;
	fetch?: FetchLike;
	headers?: Record<string, string>;
	maxRetries?: number;
	retryInitialDelayMs?: number;
	timeoutMs?: number;
}

export function createCaller(options: TransportOptions): Caller {
	const baseFetch: FetchLike = options.fetch ?? globalThis.fetch;
	const baseUrl = (options.baseUrl ?? DEFAULT_BASE_URL).replace(/\/$/, "");
	const retry: RetryPolicy = {
		maxRetries: options.maxRetries ?? 2,
		initialDelayMs: options.retryInitialDelayMs ?? 500,
		timeoutMs: options.timeoutMs ?? DEFAULT_TIMEOUT_MS,
	};

	return async (spec) => {
		const markdown = spec.options?.format === "markdown";
		const headers = new Headers(options.headers);
		if (typeof document === "undefined" && !headers.has("user-agent")) {
			headers.set("user-agent", USER_AGENT);
		}
		if (options.apiKey) {
			headers.set("authorization", `Bearer ${options.apiKey}`);
		}
		headers.set("accept", markdown ? "text/markdown" : "application/json");
		if (spec.body !== undefined)
			headers.set("content-type", "application/json");

		const url = withQuery(`${baseUrl}${spec.path}`, spec.query);
		return send(
			baseFetch,
			url,
			(signal) => ({
				method: spec.method,
				headers,
				body: spec.body === undefined ? undefined : JSON.stringify(spec.body),
				signal,
			}),
			markdown,
			spec.options?.signal,
			retry,
		);
	};
}

interface RetryPolicy {
	maxRetries: number;
	initialDelayMs: number;
	timeoutMs: number;
}

async function send(
	baseFetch: FetchLike,
	url: string,
	init: (signal: AbortSignal) => RequestInit,
	markdown: boolean,
	signal: AbortSignal | undefined,
	retry: RetryPolicy,
): Promise<unknown> {
	for (let n = 0; ; n += 1) {
		const deadline = withDeadline(signal, retry.timeoutMs);
		let waitMs: number;
		try {
			const response = await baseFetch(url, init(deadline.signal)).catch(
				(error: unknown) => {
					if (deadline.signal.aborted || n >= retry.maxRetries) throw error;
					return undefined;
				},
			);
			if (response === undefined) {
				waitMs = backoffMs(n, retry.initialDelayMs);
			} else if (
				n < retry.maxRetries &&
				RETRYABLE_STATUS.has(response.status)
			) {
				const error = await errorFrom(response);
				const seconds = error.retryAfterSeconds;
				if (seconds !== undefined && seconds > MAX_RETRY_WAIT_SECONDS) {
					throw error;
				}
				waitMs =
					seconds === undefined
						? backoffMs(n, retry.initialDelayMs)
						: seconds * 1000;
			} else {
				return await readBody(response, markdown);
			}
		} finally {
			deadline.clear();
		}
		await sleep(waitMs);
	}
}

function withDeadline(signal: AbortSignal | undefined, timeoutMs: number) {
	const controller = new AbortController();
	const abort = () => controller.abort(signal?.reason);
	if (signal?.aborted) abort();
	else signal?.addEventListener("abort", abort, { once: true });
	const timer = setTimeout(
		() =>
			controller.abort(
				new DOMException(
					`Stophy request timed out after ${timeoutMs} ms`,
					"TimeoutError",
				),
			),
		timeoutMs,
	);
	return {
		signal: controller.signal,
		clear: () => {
			clearTimeout(timer);
			signal?.removeEventListener("abort", abort);
		},
	};
}

async function readBody(
	response: Response,
	markdown: boolean,
): Promise<unknown> {
	if (!response.ok) throw await errorFrom(response);
	const text = await response.text();
	if (markdown) return text;
	if (!text) {
		throw failed(response, "Stophy returned an empty response", {});
	}
	try {
		return JSON.parse(text);
	} catch {
		throw failed(response, "Stophy returned a non-JSON response", {});
	}
}

async function errorFrom(response: Response): Promise<StophyError> {
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
	return failed(
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
