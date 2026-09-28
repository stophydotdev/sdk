import { describe, expect, test } from "bun:test";
import { version } from "../../packages/typescript/package.json";
import { Stophy } from "../../packages/typescript/src/index";
import { makeClient } from "./helpers";

const searchOk = {
	json: {
		success: true,
		data: { results: [] },
		creditsUsed: 1,
		requestId: "req_1",
	},
};

describe("Stophy client construction", () => {
	test("sends no Authorization header without an API key", async () => {
		const previousKey = process.env.STOPHY_API_KEY;
		delete process.env.STOPHY_API_KEY;
		try {
			const { client, calls } = makeClient(searchOk, { apiKey: "" });
			await client.web.search({ query: "bun" });
			expect(calls[0]?.authorization).toBeNull();
		} finally {
			if (previousKey !== undefined) process.env.STOPHY_API_KEY = previousKey;
		}
	});

	test("identifies the SDK in the User-Agent", async () => {
		const { client, calls } = makeClient(searchOk);
		await client.youtube.search({ query: "bun" });
		expect(calls[0]?.headers.get("user-agent")).toBe(
			`stophy-typescript/${version}`,
		);
	});

	test("defaults to the production base URL", async () => {
		const { client, calls } = makeClient(searchOk);
		await client.youtube.search({ query: "bun" });
		expect(calls[0]?.url).toStartWith("https://api.stophy.dev/");
	});

	test("honors a custom base URL", async () => {
		const { client, calls } = makeClient(searchOk, {
			baseUrl: "https://staging.stophy.dev",
		});
		await client.youtube.search({ query: "bun" });
		expect(calls[0]?.url).toStartWith("https://staging.stophy.dev/");
	});

	test("sends the API key as a Bearer token on every request", async () => {
		const { client, calls } = makeClient(searchOk);
		await client.youtube.search({ query: "bun" });
		expect(calls[0]?.authorization).toBe("Bearer sk_test");
	});

	test("includes custom headers on requests", async () => {
		const { client, calls } = makeClient(searchOk, {
			headers: { "x-app": "my-app" },
		});
		await client.youtube.search({ query: "bun" });
		expect(calls[0]?.headers.get("x-app")).toBe("my-app");
	});

	test("accepts an API key string", () => {
		const client = new Stophy("sk_test");
		expect(typeof client.youtube.search).toBe("function");
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
					return new Response(JSON.stringify(searchOk.json), { status: 200 });
				},
			});
			await client.youtube.search({ query: "bun" });
			expect(calls[0]).toStartWith("https://env.stophy.dev/");
		} finally {
			if (previousKey === undefined) delete process.env.STOPHY_API_KEY;
			else process.env.STOPHY_API_KEY = previousKey;
			if (previousUrl === undefined) delete process.env.STOPHY_BASE_URL;
			else process.env.STOPHY_BASE_URL = previousUrl;
		}
	});
});
