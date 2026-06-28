import { createClient, createConfig, type Client } from "@hey-api/client-fetch";
import * as ops from "./generated/sdk.gen";
import type {
  ErrorResponse,
  GetVideoData,
  GetVideoResponse,
  SearchVideosData,
  SearchVideosResponse,
  GetChannelData,
  GetChannelResponse,
  GetPlaylistData,
  GetPlaylistResponse,
  GetSuggestionsData,
  GetSuggestionsResponse,
  GetCreditsResponse,
  GetLogsData,
  GetLogsResponse,
  GetUsageData,
  GetUsageResponse,
  VideoDetailsData,
  TranscriptResult,
  CommentsData,
  LiveChatData,
} from "./generated/types.gen";

/** A video response with `data` narrowed to the shape for a given request `type`. */
type VideoResponseFor<D> = Omit<GetVideoResponse, "data"> & { data: D };

export * from "./generated/types.gen";

export interface StophyOptions {
  /** API key from your dashboard. Sent as `Authorization: Bearer <key>`. */
  apiKey: string;
  /** Defaults to `https://api.stophy.dev`. */
  baseUrl?: string;
  /** Bring your own `fetch` (handy for tests or non-global runtimes). */
  fetch?: typeof globalThis.fetch;
  /** Sent with every request. */
  headers?: Record<string, string>;
  /**
   * Retry attempts for transient failures (network errors and
   * 429/500/502/503/504). Set to `0` to disable. Defaults to `2`.
   */
  maxRetries?: number;
  /** Base delay for backoff, in ms. Defaults to `500`. */
  retryInitialDelayMs?: number;
}

/** Thrown when the API responds with a non-2xx status. */
export class StophyError extends Error {
  readonly code?: ErrorResponse["code"];
  readonly status: number;
  readonly requestId?: string;
  readonly details?: unknown;

  constructor(
    message: string,
    opts: {
      status: number;
      code?: ErrorResponse["code"];
      requestId?: string;
      details?: unknown;
    },
  ) {
    super(message);
    this.name = "StophyError";
    this.status = opts.status;
    this.code = opts.code;
    this.requestId = opts.requestId;
    this.details = opts.details;
  }
}

/**
 * Stophy API client — YouTube context API for AI agents.
 *
 * ```ts
 * const stophy = new Stophy({ apiKey: process.env.STOPHY_API_KEY! });
 * const { data } = await stophy.video({ type: "transcript", videoUrl });
 * ```
 */
export class Stophy {
  /** The underlying fetch client, if you need lower-level access. */
  readonly client: Client;

  constructor(options: StophyOptions) {
    if (!options?.apiKey) {
      throw new Error("Stophy: `apiKey` is required.");
    }
    const baseFetch = options.fetch ?? globalThis.fetch;
    this.client = createClient(
      createConfig({
        baseUrl: options.baseUrl ?? "https://api.stophy.dev",
        auth: () => options.apiKey,
        headers: options.headers,
        fetch: withRetries(
          baseFetch,
          options.maxRetries ?? 2,
          options.retryInitialDelayMs ?? 500,
        ),
      }),
    );
  }

  /** Video details, transcript, comments, replies, or live chat — pick with `type`. */
  async video(
    body: GetVideoData["body"] & { type: "details" },
  ): Promise<VideoResponseFor<VideoDetailsData>>;
  async video(
    body: GetVideoData["body"] & { type: "transcript" },
  ): Promise<VideoResponseFor<TranscriptResult>>;
  async video(
    body: GetVideoData["body"] & { type: "comments" | "replies" },
  ): Promise<VideoResponseFor<CommentsData>>;
  async video(
    body: GetVideoData["body"] & { type: "livechat" },
  ): Promise<VideoResponseFor<LiveChatData>>;
  async video(body: GetVideoData["body"]): Promise<GetVideoResponse>;
  async video(body: GetVideoData["body"]): Promise<GetVideoResponse> {
    return unwrap(await ops.getVideo({ client: this.client, body }));
  }

  /** Search YouTube, optionally filtered by type, sort, date, duration, and features. */
  async search(body: SearchVideosData["body"]): Promise<SearchVideosResponse> {
    return unwrap(await ops.searchVideos({ client: this.client, body }));
  }

  /** Channel metadata and content. Switch sections with `tab`. */
  async channel(body: GetChannelData["body"]): Promise<GetChannelResponse> {
    return unwrap(await ops.getChannel({ client: this.client, body }));
  }

  /** Playlist items. Page through long playlists with `continuationToken`. */
  async playlist(body: GetPlaylistData["body"]): Promise<GetPlaylistResponse> {
    return unwrap(await ops.getPlaylist({ client: this.client, body }));
  }

  /** Search autocomplete suggestions. */
  async suggest(query: GetSuggestionsData["query"]): Promise<GetSuggestionsResponse> {
    return unwrap(await ops.getSuggestions({ client: this.client, query }));
  }

  /** Your current credit balance. */
  async credits(): Promise<GetCreditsResponse> {
    return unwrap(await ops.getCredits({ client: this.client }));
  }

  /** Recent API request logs. */
  async logs(query?: GetLogsData["query"]): Promise<GetLogsResponse> {
    return unwrap(await ops.getLogs({ client: this.client, query }));
  }

  /** Daily credit and request counts. */
  async usage(query?: GetUsageData["query"]): Promise<GetUsageResponse> {
    return unwrap(await ops.getUsage({ client: this.client, query }));
  }
}

const RETRYABLE_STATUS = new Set([429, 500, 502, 503, 504]);

type FetchFn = (input: Request | URL | string, init?: RequestInit) => Promise<Response>;

// Wrap a fetch so transient failures (network errors and retryable statuses)
// are retried with exponential backoff + jitter, honoring `Retry-After`.
// Every Stophy endpoint is a read, so retrying is always safe.
function withRetries(
  baseFetch: typeof globalThis.fetch,
  maxRetries: number,
  initialDelayMs: number,
): FetchFn {
  if (maxRetries <= 0) {
    return baseFetch;
  }
  return async (input, init) => {
    for (let attempt = 0; ; attempt++) {
      // Clone so the body survives a retry when `input` is a Request.
      const request = input instanceof Request ? input.clone() : input;
      try {
        const response = await baseFetch(request, init);
        if (attempt < maxRetries && RETRYABLE_STATUS.has(response.status)) {
          await sleep(retryAfterMs(response) ?? backoffMs(attempt, initialDelayMs));
          continue;
        }
        return response;
      } catch (error) {
        if (attempt >= maxRetries) {
          throw error;
        }
        await sleep(backoffMs(attempt, initialDelayMs));
      }
    }
  };
}

function backoffMs(attempt: number, base: number): number {
  const window = base * 2 ** attempt;
  return window / 2 + Math.random() * (window / 2);
}

function retryAfterMs(response: Response): number | null {
  const header = response.headers.get("retry-after");
  if (!header) {
    return null;
  }
  const seconds = Number(header);
  if (!Number.isNaN(seconds)) {
    return seconds * 1000;
  }
  const date = Date.parse(header);
  return Number.isNaN(date) ? null : Math.max(0, date - Date.now());
}

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Pull `data` out of a result, or throw a StophyError if the call failed.
function unwrap<T>(result: {
  data?: T;
  error?: unknown;
  response: Response;
}): T {
  if (result.error !== undefined || result.data === undefined) {
    const err = (result.error ?? {}) as Partial<ErrorResponse>;
    throw new StophyError(err.error ?? `Stophy request failed with status ${result.response.status}`, {
      status: result.response.status,
      code: err.code,
      requestId: result.response.headers.get("x-request-id") ?? undefined,
      details: err.details,
    });
  }
  return result.data;
}

export default Stophy;
