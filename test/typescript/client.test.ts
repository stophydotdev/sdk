import { describe, expect, test } from "bun:test";
import { Stophy } from "../../packages/typescript/src/index";
import { makeClient } from "./helpers";

describe("Stophy client construction", () => {
	test("throws when apiKey is missing", () => {
		// @ts-expect-error — exercising the runtime guard
		expect(() => new Stophy({})).toThrow("apiKey");
		expect(() => new Stophy({ apiKey: "" })).toThrow("apiKey");
	});

	test("defaults to the production base URL", async () => {
		const { client, calls } = makeClient({
			json: { success: true, data: { credits: 1 } },
		});
		await client.credits();
		expect(calls[0]?.url).toStartWith("https://api.stophy.dev/");
	});

	test("honors a custom base URL", async () => {
		const { client, calls } = makeClient(
			{ json: { success: true, data: { credits: 1 } } },
			{ baseUrl: "https://staging.stophy.dev" },
		);
		await client.credits();
		expect(calls[0]?.url).toStartWith("https://staging.stophy.dev/");
	});

	test("sends the API key as a Bearer token on every request", async () => {
		const { client, calls } = makeClient({ json: { success: true, data: {} } });
		await client.credits();
		expect(calls[0]?.authorization).toBe("Bearer sk_test");
	});

	test("includes custom headers on requests", async () => {
		const { client, calls } = makeClient(
			{ json: { success: true, data: {} } },
			{ headers: { "x-app": "my-app" } },
		);
		await client.credits();
		expect(calls[0]?.headers.get("x-app")).toBe("my-app");
	});

	test("exposes the underlying client for advanced use", () => {
		const client = new Stophy({ apiKey: "sk_test" });
		expect(client.client).toBeDefined();
		expect(typeof client.client.get).toBe("function");
	});

	test("accepts an API key string", async () => {
		const client = new Stophy("sk_test");
		expect(client.client).toBeDefined();
	});

	test("reads API key and base URL from the environment", async () => {
		const previousKey = process.env.STOPHY_API_KEY;
		const previousUrl = process.env.STOPHY_BASE_URL;
		process.env.STOPHY_API_KEY = "sk_env";
		process.env.STOPHY_BASE_URL = "https://env.stophy.dev";
		try {
			const calls: string[] = [];
			const client = new Stophy({
				fetch: async (input) => {
					calls.push(input instanceof Request ? input.url : String(input));
					return new Response(
						JSON.stringify({ success: true, data: { credits: 1 } }),
						{ status: 200, headers: { "content-type": "application/json" } },
					);
				},
			});
			await client.credits();
			expect(calls[0]).toStartWith("https://env.stophy.dev/");
		} finally {
			if (previousKey === undefined) delete process.env.STOPHY_API_KEY;
			else process.env.STOPHY_API_KEY = previousKey;
			if (previousUrl === undefined) delete process.env.STOPHY_BASE_URL;
			else process.env.STOPHY_BASE_URL = previousUrl;
		}
	});
});
