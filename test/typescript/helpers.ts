import {
	Stophy,
	type StophyOptions,
} from "../../packages/typescript/src/index";

export interface CapturedRequest {
	url: string;
	method: string;
	headers: Headers;
	authorization: string | null;
	body: unknown;
	signal: AbortSignal | null;
}

export interface MockResponseInit {
	status?: number;
	json?: unknown;
	raw?: string;
	headers?: Record<string, string>;
}

export function createMock(responses: MockResponseInit | MockResponseInit[]) {
	const queue = Array.isArray(responses) ? [...responses] : [responses];
	const calls: CapturedRequest[] = [];

	const fetchImpl = async (input: RequestInfo | URL, init?: RequestInit) => {
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
			signal: init?.signal ?? null,
		});

		const shifted = queue.length > 1 ? queue.shift() : queue[0];
		if (!shifted) throw new Error("mock has no response");
		const payload =
			shifted.raw !== undefined
				? shifted.raw
				: shifted.json !== undefined
					? JSON.stringify(shifted.json)
					: "";
		return new Response(payload, {
			status: shifted.status ?? 200,
			headers: { "content-type": "application/json", ...shifted.headers },
		});
	};

	return { fetchImpl, calls };
}

export function makeClient(
	responses: MockResponseInit | MockResponseInit[],
	opts: Partial<StophyOptions> = {},
) {
	const { fetchImpl, calls } = createMock(responses);
	const client = new Stophy({
		apiKey: "st_test",
		fetch: fetchImpl,
		maxRetries: 0,
		...opts,
	});
	return { client, calls };
}

export function queryOf(url: string): Record<string, string> {
	return Object.fromEntries(new URL(url).searchParams.entries());
}

function isRecord(value: unknown): value is Record<string, unknown> {
	return typeof value === "object" && value !== null && !Array.isArray(value);
}

export async function specPaths(): Promise<string[]> {
	const text = await Bun.file(
		new URL("../../openapi.json", import.meta.url),
	).text();
	const document: unknown = JSON.parse(text);
	if (!isRecord(document) || !isRecord(document.paths)) {
		throw new Error("openapi.json has no paths");
	}
	return Object.keys(document.paths);
}

export function endpointAt(root: object, path: string): unknown {
	const parts = path
		.split("/")
		.filter((part) => part.length > 0 && part !== "v1");
	let node: object = root;
	for (const [index, part] of parts.entries()) {
		const value = Object.getOwnPropertyDescriptor(node, part)?.value;
		if (index === parts.length - 1) return value;
		if (typeof value !== "function" && !isRecord(value)) {
			throw new Error(`${path} is missing ${part}`);
		}
		node = value;
	}
	return node;
}
