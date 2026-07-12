export interface MeteredResponse<T> {
	success: true;
	requestId: string;
	cacheState: "hit" | "miss";
	creditsUsed: number;
	creditsRemaining: number;
	warning?: string;
	data: T;
}

export interface AccountResponse<T> {
	success: true;
	requestId: string;
	data: T;
}
