import { describe, expect, test } from "bun:test";
import { StophyError } from "../../packages/typescript/src/index";
import { makeClient } from "./helpers";

describe("error handling", () => {
	test("throws StophyError on 401 with code and message", async () => {
		const { client } = makeClient({
			status: 401,
			json: { success: false, code: "UNAUTHORIZED", error: "Invalid API key" },
		});

		const err = await client.credits().catch((e) => e);
		expect(err).toBeInstanceOf(StophyError);
		expect(err.status).toBe(401);
		expect(err.code).toBe("UNAUTHORIZED");
		expect(err.message).toBe("Invalid API key");
		expect(err.name).toBe("StophyError");
	});

	test("maps INSUFFICIENT_CREDITS (402)", async () => {
		const { client } = makeClient({
			status: 402,
			json: {
				success: false,
				code: "INSUFFICIENT_CREDITS",
				error: "Out of credits",
			},
		});
		const err = await client.search({ q: "x" }).catch((e) => e);
		expect(err).toBeInstanceOf(StophyError);
		expect(err.status).toBe(402);
		expect(err.code).toBe("INSUFFICIENT_CREDITS");
	});

	test("surfaces validation details on 400", async () => {
		const { client } = makeClient({
			status: 400,
			json: {
				success: false,
				code: "INVALID_INPUT",
				error: "videoUrl is required",
				details: { field: "videoUrl" },
			},
		});
		const err = await client
			.video({ type: "details", videoUrl: "" })
			.catch((e) => e);
		expect(err.code).toBe("INVALID_INPUT");
		expect(err.details).toEqual({ field: "videoUrl" });
	});

	test("captures the x-request-id header when present", async () => {
		const { client } = makeClient({
			status: 500,
			headers: { "x-request-id": "req_err_99" },
			json: { success: false, code: "INTERNAL_ERROR", error: "boom" },
		});
		const err = await client.credits().catch((e) => e);
		expect(err.requestId).toBe("req_err_99");
	});

	test("falls back to a status-based message when the body is not JSON", async () => {
		const { client } = makeClient({ status: 429, raw: "Too Many Requests" });
		const err = await client.credits().catch((e) => e);
		expect(err).toBeInstanceOf(StophyError);
		expect(err.status).toBe(429);
		expect(err.message).toContain("429");
	});

	test("does not throw on a successful response", async () => {
		const { client } = makeClient({
			json: { success: true, data: { credits: 5 } },
		});
		await expect(client.credits()).resolves.toBeDefined();
	});
});
