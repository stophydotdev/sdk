import { describe, expect, test } from "bun:test";
import { Stophy, StophyError } from "../../packages/typescript/src/index";
import { makeClient } from "./helpers";

const ok = { json: { success: true, data: { credits: 1 } } };

describe("retries", () => {
	test("retries a 429 then succeeds", async () => {
		const { client, calls } = makeClient(
			[{ status: 429, json: { success: false } }, ok],
			{
				maxRetries: 2,
				retryInitialDelayMs: 0,
			},
		);
		const res = await client.credits();
		expect(res.data?.credits).toBe(1);
		expect(calls.length).toBe(2);
	});

	test("retries 5xx up to maxRetries, then throws", async () => {
		const { client, calls } = makeClient(
			{
				status: 503,
				json: { success: false, code: "INTERNAL_ERROR", error: "down" },
			},
			{ maxRetries: 2, retryInitialDelayMs: 0 },
		);
		const err = await client.credits().catch((e) => e);
		expect(err).toBeInstanceOf(StophyError);
		expect(err.status).toBe(503);
		expect(calls.length).toBe(3); // initial + 2 retries
	});

	test("does not retry when maxRetries is 0", async () => {
		const { client, calls } = makeClient({
			status: 429,
			json: { success: false },
		});
		await client.credits().catch(() => {});
		expect(calls.length).toBe(1);
	});

	test("does not retry non-retryable statuses (400)", async () => {
		const { client, calls } = makeClient(
			{
				status: 400,
				json: { success: false, code: "INVALID_INPUT", error: "bad" },
			},
			{ maxRetries: 3, retryInitialDelayMs: 0 },
		);
		await client.search({ q: "x" }).catch(() => {});
		expect(calls.length).toBe(1);
	});

	test("retries network errors", async () => {
		let n = 0;
		const fetchImpl = async () => {
			if (n++ === 0) throw new TypeError("network down");
			return new Response(JSON.stringify({ success: true, data: {} }), {
				status: 200,
				headers: { "content-type": "application/json" },
			});
		};
		const client = new Stophy({
			apiKey: "sk_test",
			fetch: fetchImpl as typeof fetch,
			maxRetries: 2,
			retryInitialDelayMs: 0,
		});
		await client.credits();
		expect(n).toBe(2);
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
		await client.credits();
		expect(calls.length).toBe(2);
		// Retry-After "0" should win over the 9999ms base delay.
		expect(Date.now() - started).toBeLessThan(500);
	});
});
