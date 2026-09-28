import type { Caller, CallOptions } from "./transport";

export interface MarkdownOptions {
	format: "markdown";
	signal?: AbortSignal;
}

export interface JsonOptions {
	format?: undefined;
	signal?: AbortSignal;
}

export function post<Body, Response>(path: string, call: Caller) {
	function run(body: Body, options: MarkdownOptions): Promise<string>;
	function run(body: Body, options?: JsonOptions): Promise<Response>;
	function run(body: Body, options?: CallOptions): Promise<unknown> {
		return call({ method: "POST", path, body, options });
	}
	return run;
}

export function postOptional<Body, Response>(path: string, call: Caller) {
	function run(options: MarkdownOptions): Promise<string>;
	function run(
		body: Body | undefined,
		options: MarkdownOptions,
	): Promise<string>;
	function run(body?: Body, options?: JsonOptions): Promise<Response>;
	function run(
		body?: Body | MarkdownOptions,
		options?: CallOptions,
	): Promise<unknown> {
		if (isMarkdownOptions(body) && options === undefined) {
			return call({ method: "POST", path, body: {}, options: body });
		}
		return call({ method: "POST", path, body: body ?? {}, options });
	}
	return run;
}

export function get<Response>(path: string, call: Caller) {
	function run(options: MarkdownOptions): Promise<string>;
	function run(options?: JsonOptions): Promise<Response>;
	function run(options?: CallOptions): Promise<unknown> {
		return call({ method: "GET", path, options });
	}
	return run;
}

function isMarkdownOptions(value: unknown): value is MarkdownOptions {
	if (typeof value !== "object" || value === null) return false;
	return "format" in value && value.format === "markdown";
}
