import { describe, expect, test } from "bun:test";
import { endpointAt, makeClient, queryOf, specPaths } from "./helpers";

const envelope = {
	success: true,
	data: {
		results: [
			{
				type: "video",
				videoId: "abc",
				videoUrl: "https://youtu.be/abc",
				channelName: "Bun",
			},
		],
	},
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
		const first = result.data.results[0];
		expect(first?.type === "video" && first.videoUrl).toBe(
			"https://youtu.be/abc",
		);
		expect(calls[0]?.method).toBe("POST");
		expect(new URL(calls[0]?.url ?? "").pathname).toBe("/v1/youtube/search");
		expect(calls[0]?.body).toEqual({ query: "bun runtime", limit: 2 });
		expect(calls[0]?.headers.get("accept")).toBe("application/json");
	});

	test("calls a single-segment operation", async () => {
		const { client, calls } = makeClient({ json: envelope });
		await client.transcript({ video: "https://youtu.be/abc" });
		expect(new URL(calls[0]?.url ?? "").pathname).toBe("/v1/transcript");
		expect(calls[0]?.body).toEqual({ video: "https://youtu.be/abc" });
	});

	test("sends the network discriminator for joined endpoints", async () => {
		const { client, calls } = makeClient({ json: envelope });
		await client.ads.search({ network: "meta", query: "shoes" });
		await client.ads.search({ network: "google", query: "example.com" });
		expect(new URL(calls[0]?.url ?? "").pathname).toBe("/v1/ads/search");
		expect(calls[0]?.body).toEqual({ network: "meta", query: "shoes" });
		expect(new URL(calls[1]?.url ?? "").pathname).toBe("/v1/ads/search");
		expect(calls[1]?.body).toEqual({
			network: "google",
			query: "example.com",
		});
	});

	test("forwards the abort signal", async () => {
		const { client, calls } = makeClient({ json: envelope });
		const controller = new AbortController();
		controller.abort();
		await client.maps
			.search(
				{ query: "cairo", location: "Cairo" },
				{ signal: controller.signal },
			)
			.catch(() => undefined);
		expect(calls[0]?.signal?.aborted).toBe(true);
	});

	test("omits an empty optional body", async () => {
		const { client, calls } = makeClient({ json: envelope });
		await client.upwork.search();
		expect(calls[0]?.body).toEqual({});
		expect(new URL(calls[0]?.url ?? "").pathname).toBe("/v1/upwork/search");
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
		expect(paths).toContain("/v1/web/search");
		expect(paths).not.toContain("/v1/amazon/product");
		for (const path of paths) {
			expect(typeof endpointAt(client, path)).toBe("function");
		}
	});
});
