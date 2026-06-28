import { Stophy, type StophyOptions } from "../../packages/typescript/src/index";

// A request recorded by the mock fetch, so tests can assert on what was sent.
export interface CapturedRequest {
	url: string;
	method: string;
	headers: Headers;
	authorization: string | null;
	body: unknown;
}

// One canned reply. Use `json` for a normal body, `raw` for non-JSON/empty.
export interface MockResponseInit {
	status?: number;
	json?: unknown;
	raw?: string;
	headers?: Record<string, string>;
}

// A fetch that records every request and replies with the given response(s).
// Pass an array to vary the reply per call; the last entry repeats.
export function createMock(responses: MockResponseInit | MockResponseInit[]) {
	const queue = Array.isArray(responses) ? [...responses] : [responses];
	const calls: CapturedRequest[] = [];

	const fetchImpl = async (
		input: Request | string | URL,
		init?: RequestInit,
	): Promise<Response> => {
		const req = input instanceof Request ? input : new Request(input, init);

		let body: unknown;
		const text = await req.clone().text();
		if (text) {
			try {
				body = JSON.parse(text);
			} catch {
				body = text;
			}
		}

		calls.push({
			url: req.url,
			method: req.method,
			headers: req.headers,
			authorization: req.headers.get("authorization"),
			body,
		});

		const next = queue.length > 1 ? (queue.shift() as MockResponseInit) : queue[0];
		const payload =
			next.raw !== undefined ? next.raw : next.json !== undefined ? JSON.stringify(next.json) : "";
		return new Response(payload, {
			status: next.status ?? 200,
			headers: { "content-type": "application/json", ...next.headers },
		});
	};

	return { fetchImpl, calls };
}

// A Stophy client wired to a mock fetch, plus the list it records into.
export function makeClient(
	responses: MockResponseInit | MockResponseInit[],
	opts: Partial<StophyOptions> = {},
) {
	const { fetchImpl, calls } = createMock(responses);
	const client = new Stophy({ apiKey: "sk_test", fetch: fetchImpl, maxRetries: 0, ...opts });
	return { client, calls };
}

// Pull the query string off a URL as a plain object.
export function queryOf(url: string): Record<string, string> {
	return Object.fromEntries(new URL(url).searchParams.entries());
}
