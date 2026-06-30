import type { ErrorResponse } from "./generated/types.gen";

/** Thrown when the Stophy API responds with a non-success status. */
export class StophyError extends Error {
	readonly code?: ErrorResponse["code"];
	readonly status: number;
	readonly requestId?: string;
	readonly details?: unknown;

	constructor(
		message: string,
		options: {
			status: number;
			code?: ErrorResponse["code"];
			requestId?: string;
			details?: unknown;
		},
	) {
		super(message);
		this.name = "StophyError";
		this.status = options.status;
		this.code = options.code;
		this.requestId = options.requestId;
		this.details = options.details;
	}
}
