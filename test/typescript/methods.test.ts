import { describe, expect, test } from "bun:test";
import { endpointAt, makeClient, queryOf, specPaths } from "./helpers";

const envelope = {
	success: true,
	data: { results: [{ type: "video", url: "https://youtu.be/abc" }] },
	creditsUsed: 1,
	requestId: "req_1",
};

describe("namespaced operations", () => {
	test("posts the input to the path derived from the spec", async () => {
		const { client, calls } = makeClient({ json: envelope });
		const result = await client.youtube.search({
			query: "bun runtime",
			limit: 2,
		});
		expect(result.data.results[0]?.url).toBe("https://youtu.be/abc");
		expect(calls[0]?.method).toBe("POST");
		expect(new URL(calls[0]?.url ?? "").pathname).toBe("/v1/youtube/search");
		expect(calls[0]?.body).toEqual({ query: "bun runtime", limit: 2 });
		expect(calls[0]?.headers.get("accept")).toBe("application/json");
	});

	test("calls a nested operation on the parent namespace", async () => {
		const { client, calls } = makeClient({ json: envelope });
		await client.youtube.comments.replies({
			video: "abc",
			cursor: "tok",
			limit: 5,
		});
		expect(new URL(calls[0]?.url ?? "").pathname).toBe(
			"/v1/youtube/comments/replies",
		);
		expect(calls[0]?.body).toEqual({ video: "abc", cursor: "tok", limit: 5 });
	});

	test("returns markdown when format is markdown", async () => {
		const { client, calls } = makeClient({
			raw: "# results",
			headers: { "content-type": "text/markdown" },
		});
		const text = await client.youtube.search(
			{ query: "bun runtime" },
			{ format: "markdown" },
		);
		expect(text).toBe("# results");
		expect(calls[0]?.headers.get("accept")).toBe("text/markdown");
	});

	test("forwards the abort signal", async () => {
		const { client, calls } = makeClient({ json: envelope });
		const controller = new AbortController();
		await client.maps.search({ query: "cairo" }, { signal: controller.signal });
		expect(calls[0]?.signal).toBe(controller.signal);
	});

	test("omits an empty optional body", async () => {
		const { client, calls } = makeClient({ json: envelope });
		await client.crypto.trending();
		expect(calls[0]?.body).toEqual({});
		expect(new URL(calls[0]?.url ?? "").pathname).toBe("/v1/crypto/trending");
	});

	test("lists endpoints with GET", async () => {
		const { client, calls } = makeClient({ json: { endpoints: [] } });
		const catalog = await client.endpoints();
		expect(catalog.endpoints).toEqual([]);
		expect(calls[0]?.method).toBe("GET");
		expect(new URL(calls[0]?.url ?? "").pathname).toBe("/v1/endpoints");
	});

	test("loads usage and logs with an API key", async () => {
		const { client, calls } = makeClient([
			{
				json: { balanceMicros: 1000, creditsUsed: 2, requestCount: 1 },
			},
			{
				json: {
					endpoints: ["youtube.search"],
					logs: [
						{
							apiKeyId: null,
							apiKeyName: null,
							createdAt: "2026-09-28T00:00:00.000Z",
							credits: 1,
							durationMs: null,
							endpoint: "youtube.search",
							id: "log_1",
							method: "POST",
							response: "success",
							status: 200,
						},
					],
					page: 0,
					pageSize: 50,
					total: 1,
					totalPages: 1,
				},
			},
		]);
		expect((await client.usage()).creditsUsed).toBe(2);
		const logs = await client.logs({
			days: 7,
			page: 0,
			endpoint: "youtube.search",
		});
		expect(logs.logs[0]?.endpoint).toBe("youtube.search");
		expect(queryOf(calls[1]?.url ?? "")).toEqual({
			days: "7",
			page: "0",
			endpoint: "youtube.search",
		});
	});

	test("exposes every operation in the spec", async () => {
		const { client } = makeClient({ json: envelope });
		const paths = await specPaths();
		expect(paths.length).toBeGreaterThan(100);
		for (const path of paths) {
			expect(typeof endpointAt(client, path)).toBe("function");
		}
	});
});
