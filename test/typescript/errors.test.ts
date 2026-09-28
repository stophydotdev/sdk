import { describe, expect, test } from "bun:test";
import { StophyError } from "../../packages/typescript/src/index";
import { makeClient } from "./helpers";

const unauthorized = {
	status: 401,
	json: {
		success: false,
		error: {
			code: "unauthorized",
			message: "Invalid API key",
			retryable: false,
			requestId: "req_err",
		},
	},
};

describe("error handling", () => {
	test("throws StophyError from the error envelope", async () => {
		const { client } = makeClient(unauthorized);
		const err = await client.youtube
			.search({ query: "x" })
			.catch((error) => error);
		expect(err).toBeInstanceOf(StophyError);
		expect(err.status).toBe(401);
		expect(err.code).toBe("unauthorized");
		expect(err.message).toBe("Invalid API key");
		expect(err.retryable).toBe(false);
		expect(err.requestId).toBe("req_err");
		expect(err.name).toBe("StophyError");
	});

	test("reads retryAfterSeconds from the body, then the header", async () => {
		const fromBody = makeClient({
			status: 429,
			json: {
				success: false,
				error: {
					code: "rateLimited",
					message: "slow down",
					retryable: true,
					retryAfterSeconds: 9,
					requestId: "req_2",
				},
			},
		});
		const bodyError = await fromBody.client.usage().catch((error) => error);
		expect(bodyError.retryAfterSeconds).toBe(9);
		expect(bodyError.retryable).toBe(true);

		const fromHeader = makeClient({
			status: 429,
			headers: { "retry-after": "4", "x-request-id": "req_header" },
			json: {
				success: false,
				error: { code: "rateLimited", message: "slow down", retryable: true },
			},
		});
		const headerError = await fromHeader.client.usage().catch((error) => error);
		expect(headerError.retryAfterSeconds).toBe(4);
		expect(headerError.requestId).toBe("req_header");
	});

	test("falls back to a status message when the body is not JSON", async () => {
		const { client } = makeClient({ status: 502, raw: "bad gateway" });
		const err = await client.usage().catch((error) => error);
		expect(err).toBeInstanceOf(StophyError);
		expect(err.status).toBe(502);
		expect(err.message).toContain("502");
		expect(err.retryable).toBe(true);
	});

	test("does not throw on a successful response", async () => {
		const { client } = makeClient({
			json: { balanceMicros: 1, creditsUsed: 0, requestCount: 0 },
		});
		await expect(client.usage()).resolves.toEqual({
			balanceMicros: 1,
			creditsUsed: 0,
			requestCount: 0,
		});
	});
});
