import type { Caller } from "./transport";

export interface RequestOptions {
	signal?: AbortSignal;
}

export function post<Body, Response>(path: string, call: Caller) {
	return (body: Body, options?: RequestOptions): Promise<Response> =>
		call({ method: "POST", path, body, options }) as Promise<Response>;
}

export function postOptional<Body, Response>(path: string, call: Caller) {
	return (body?: Body, options?: RequestOptions): Promise<Response> =>
		call({
			method: "POST",
			path,
			body: body ?? {},
			options,
		}) as Promise<Response>;
}

export function get<Response>(path: string, call: Caller) {
	return (options?: RequestOptions): Promise<Response> =>
		call({ method: "GET", path, options }) as Promise<Response>;
}
