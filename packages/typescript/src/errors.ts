import type { _Error } from "./generated/types.gen";

export type StophyErrorCode = _Error["error"]["code"];

/** Thrown when the Stophy API responds with a non-success status. */
export class StophyError extends Error {
	readonly code?: string;
	readonly retryable: boolean;
	readonly retryAfterSeconds?: number;
	readonly status: number;
	readonly requestId?: string;

	constructor(
		message: string,
		options: {
			status: number;
			code?: string;
			retryable: boolean;
			retryAfterSeconds?: number;
			requestId?: string;
		},
	) {
		super(message);
		this.name = "StophyError";
		this.status = options.status;
		this.code = options.code;
		this.retryable = options.retryable;
		this.retryAfterSeconds = options.retryAfterSeconds;
		this.requestId = options.requestId;
	}
}
