import { describe, expect, test } from "bun:test";
import { Stophy, StophyError } from "../../packages/typescript/src/index";
import { makeClient } from "./helpers";

const ok = {
	json: {
		success: true,
		data: { results: [] },
		creditsUsed: 1,
		requestId: "req_1",
	},
};

describe("retries", () => {
	test("retries a 429 then succeeds", async () => {
		const { client, calls } = makeClient(
			[
				{ status: 429, json: { success: false, error: { message: "wait" } } },
				ok,
			],
			{ maxRetries: 2, retryInitialDelayMs: 0 },
		);
		const res = await client.youtube.search({ query: "x" });
		expect(res.creditsUsed).toBe(1);
		expect(calls.length).toBe(2);
	});

	test("retries 5xx up to maxRetries, then throws", async () => {
		const { client, calls } = makeClient(
			{
				status: 503,
				json: {
					success: false,
					error: { code: "internalError", message: "down", retryable: true },
				},
			},
			{ maxRetries: 2, retryInitialDelayMs: 0 },
		);
		const err = await client.youtube
			.search({ query: "x" })
			.catch((error) => error);
		expect(err).toBeInstanceOf(StophyError);
		expect(err.status).toBe(503);
		expect(calls.length).toBe(3);
	});

	test("does not retry when maxRetries is 0", async () => {
		const { client, calls } = makeClient({
			status: 429,
			json: { success: false },
		});
		await client.youtube.search({ query: "x" }).catch(() => undefined);
		expect(calls.length).toBe(1);
	});

	test("does not retry a 400", async () => {
		const { client, calls } = makeClient(
			{
				status: 400,
				json: {
					success: false,
					error: { code: "invalidRequest", message: "bad", retryable: false },
				},
			},
			{ maxRetries: 3, retryInitialDelayMs: 0 },
		);
		await client.youtube.search({ query: "x" }).catch(() => undefined);
		expect(calls.length).toBe(1);
	});

	test("retries network errors and does not retry abort", async () => {
		let n = 0;
		const fetchImpl = async () => {
			n += 1;
			if (n === 1) throw new TypeError("network down");
			return new Response(JSON.stringify(ok.json), { status: 200 });
		};
		const client = new Stophy({
			apiKey: "sk_test",
			fetch: fetchImpl,
			maxRetries: 2,
			retryInitialDelayMs: 0,
		});
		await client.youtube.search({ query: "x" });
		expect(n).toBe(2);

		const controller = new AbortController();
		controller.abort();
		const aborted = new Stophy({
			apiKey: "sk_test",
			fetch: async (_input, init) => {
				if (init?.signal?.aborted)
					throw new DOMException("aborted", "AbortError");
				return new Response("{}", { status: 200 });
			},
			maxRetries: 2,
			retryInitialDelayMs: 0,
		});
		await expect(
			aborted.youtube.search({ query: "x" }, { signal: controller.signal }),
		).rejects.toThrow("aborted");
	});

	test("honors the Retry-After header (seconds)", async () => {
		const { client, calls } = makeClient(
			[
				{
					status: 429,
					headers: { "retry-after": "0" },
					json: { success: false },
				},
				ok,
			],
			{ maxRetries: 1, retryInitialDelayMs: 9999 },
		);
		const started = Date.now();
		await client.youtube.search({ query: "x" });
		expect(calls.length).toBe(2);
		expect(Date.now() - started).toBeLessThan(500);
	});

	test("throws instead of waiting more than 60 seconds", async () => {
		const { client, calls } = makeClient(
			[
				{
					status: 429,
					headers: { "retry-after": "120" },
					json: { success: false, error: { code: "rateLimited" } },
				},
				ok,
			],
			{ maxRetries: 2, retryInitialDelayMs: 0 },
		);
		const err = await client.youtube
			.search({ query: "x" })
			.catch((error) => error);
		expect(err).toBeInstanceOf(StophyError);
		expect(err.retryAfterSeconds).toBe(120);
		expect(calls.length).toBe(1);

		const fromBody = makeClient(
			[
				{
					status: 429,
					json: {
						success: false,
						error: { code: "rateLimited", retryAfterSeconds: 3600 },
					},
				},
				ok,
			],
			{ maxRetries: 2, retryInitialDelayMs: 0 },
		);
		const bodyErr = await fromBody.client.youtube
			.search({ query: "x" })
			.catch((error) => error);
		expect(bodyErr.retryAfterSeconds).toBe(3600);
		expect(fromBody.calls.length).toBe(1);
	});

	test("times out after timeoutMs and does not retry", async () => {
		let n = 0;
		const client = new Stophy({
			apiKey: "sk_test",
			fetch: (_input, init) => {
				n += 1;
				return new Promise((_resolve, reject) => {
					init?.signal?.addEventListener("abort", () =>
						reject(init.signal?.reason),
					);
				});
			},
			maxRetries: 2,
			retryInitialDelayMs: 0,
			timeoutMs: 20,
		});
		const err = await client.youtube
			.search({ query: "x" })
			.catch((error) => error);
		expect(err.name).toBe("TimeoutError");
		expect(n).toBe(1);
	});
});
