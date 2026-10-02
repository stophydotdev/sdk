import { type Logs, type LogsQuery, logs, type Usage, usage } from "./account";
import { bindSurface, type Surface } from "./generated/surface.gen";
import {
	type Caller,
	type CallOptions,
	createCaller,
	type FetchLike,
} from "./transport";

export interface StophyOptions {
	/** Defaults to `STOPHY_API_KEY`. Without a key, only Google search, Google News and YouTube search, videos and transcripts answer. */
	apiKey?: string;
	/** Defaults to `STOPHY_BASE_URL` or `https://api.stophy.dev`. */
	baseUrl?: string;
	fetch?: FetchLike;
	headers?: Record<string, string>;
	maxRetries?: number;
	retryInitialDelayMs?: number;
	/** Per-attempt timeout. Defaults to 30000. */
	timeoutMs?: number;
}

export type { CallOptions, FetchLike };

export type StophyClientInput = StophyOptions | string;

function env(name: string): string | undefined {
	return typeof process === "undefined" ? undefined : process.env[name];
}

/** Typed client for the Stophy web data API. Namespaces come from the OpenAPI document. */
// The generated surface is copied onto this instance in the constructor.
// biome-ignore lint/suspicious/noUnsafeDeclarationMerging: namespaces are assigned from bindSurface
export class Stophy {
	readonly #call: Caller;

	constructor(input: StophyClientInput = {}) {
		const options = typeof input === "string" ? { apiKey: input } : input;
		const apiKey = options.apiKey?.trim() || env("STOPHY_API_KEY")?.trim();
		this.#call = createCaller({
			...options,
			apiKey,
			baseUrl: options.baseUrl ?? env("STOPHY_BASE_URL"),
		});
		Object.assign(this, bindSurface(this.#call));
	}

	/** Current balance and lifetime usage. Requires an API key. */
	usage(): Promise<Usage> {
		return usage(this.#call);
	}

	/** Recent metered requests. Requires an API key. */
	logs(query?: LogsQuery): Promise<Logs> {
		return logs(this.#call, query);
	}
}

export interface Stophy extends Surface {}
