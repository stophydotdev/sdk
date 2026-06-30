import { describe, expect, test } from "bun:test";
import { makeClient, queryOf } from "./helpers";

const ok = (data: unknown) => ({
	json: { success: true, requestId: "req_1", data },
});

describe("video()", () => {
	test("POSTs to /v1/video with the body and returns data", async () => {
		const { client, calls } = makeClient(ok({ text: "hello world" }));
		const res = await client.video({
			type: "transcript",
			videoUrl: "https://youtu.be/abc",
		});

		expect(calls[0]?.method).toBe("POST");
		expect(calls[0]?.url).toEndWith("/v1/video");
		expect(calls[0]?.body).toEqual({
			type: "transcript",
			videoUrl: "https://youtu.be/abc",
		});
		expect(calls[0]?.headers.get("content-type")).toContain("application/json");
		expect(res.data).toEqual({ text: "hello world" });
		expect(res.requestId).toBe("req_1");
	});

	test("supports the replies flow via continuationToken", async () => {
		const { client, calls } = makeClient(ok({ items: [] }));
		await client.video({ type: "replies", continuationToken: "TOKEN" });
		expect(calls[0]?.body).toEqual({
			type: "replies",
			continuationToken: "TOKEN",
		});
	});
});

describe("search()", () => {
	test("POSTs to /v1/search with filters", async () => {
		const { client, calls } = makeClient(
			ok({ items: [], continuationToken: "next" }),
		);
		const res = await client.search({
			q: "lofi",
			sortBy: "popularity",
			duration: "long",
		});

		expect(calls[0]?.method).toBe("POST");
		expect(calls[0]?.url).toEndWith("/v1/search");
		expect(calls[0]?.body).toEqual({
			q: "lofi",
			sortBy: "popularity",
			duration: "long",
		});
		expect(res.data?.continuationToken).toBe("next");
	});
});

describe("channel()", () => {
	test("POSTs to /v1/channel with channelUrl and tab", async () => {
		const { client, calls } = makeClient(ok({ tab: "video", items: [] }));
		await client.channel({
			channelUrl: "https://youtube.com/@mkbhd",
			tab: "video",
		});

		expect(calls[0]?.method).toBe("POST");
		expect(calls[0]?.url).toEndWith("/v1/channel");
		expect(calls[0]?.body).toEqual({
			channelUrl: "https://youtube.com/@mkbhd",
			tab: "video",
		});
	});
});

describe("playlist()", () => {
	test("POSTs to /v1/playlist with playlistUrl", async () => {
		const { client, calls } = makeClient(ok({ items: [] }));
		await client.playlist({
			playlistUrl: "https://youtube.com/playlist?list=PL123",
		});

		expect(calls[0]?.method).toBe("POST");
		expect(calls[0]?.url).toEndWith("/v1/playlist");
		expect(calls[0]?.body).toEqual({
			playlistUrl: "https://youtube.com/playlist?list=PL123",
		});
	});
});

describe("suggest()", () => {
	test("GETs /v1/suggest with query params", async () => {
		const { client, calls } = makeClient(
			ok({ suggestions: ["react", "react native"] }),
		);
		const res = await client.suggest({ q: "react", hl: "en", gl: "US" });

		expect(calls[0]?.method).toBe("GET");
		expect(calls[0]?.url).toContain("/v1/suggest");
		expect(queryOf(calls[0]?.url ?? "https://invalid.local")).toEqual({
			q: "react",
			hl: "en",
			gl: "US",
		});
		expect(calls[0]?.body).toBeUndefined();
		expect(res.data?.suggestions).toContain("react native");
	});

	test("sends only the required q when options omitted", async () => {
		const { client, calls } = makeClient(ok({ suggestions: [] }));
		await client.suggest({ q: "typescript" });
		expect(queryOf(calls[0]?.url ?? "https://invalid.local")).toEqual({
			q: "typescript",
		});
	});
});

describe("credits()", () => {
	test("GETs /v1/credits with no arguments", async () => {
		const { client, calls } = makeClient(ok({ credits: 42 }));
		const res = await client.credits();

		expect(calls[0]?.method).toBe("GET");
		expect(calls[0]?.url).toEndWith("/v1/credits");
		expect(res.data?.credits).toBe(42);
	});
});

describe("logs()", () => {
	test("GETs /v1/logs with no query when called bare", async () => {
		const { client, calls } = makeClient(ok({ logs: [], total: 0 }));
		await client.logs();
		expect(calls[0]?.method).toBe("GET");
		expect(calls[0]?.url).toEndWith("/v1/logs");
	});

	test("forwards query filters", async () => {
		const { client, calls } = makeClient(ok({ logs: [], total: 0 }));
		await client.logs({ days: "30", endpoint: "/video", page: 2 });
		expect(queryOf(calls[0]?.url ?? "https://invalid.local")).toEqual({
			days: "30",
			endpoint: "/video",
			page: "2",
		});
	});
});

describe("usage()", () => {
	test("GETs /v1/usage and forwards query filters", async () => {
		const { client, calls } = makeClient(ok({ items: [] }));
		await client.usage({ days: "7", tz: "-120" });

		expect(calls[0]?.method).toBe("GET");
		expect(calls[0]?.url).toContain("/v1/usage");
		expect(queryOf(calls[0]?.url ?? "https://invalid.local")).toEqual({
			days: "7",
			tz: "-120",
		});
	});
});
