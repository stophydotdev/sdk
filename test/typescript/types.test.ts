import { Stophy } from "../../packages/typescript/src/index";

const client = new Stophy({ apiKey: "st_test" });

type Expect<T extends true> = T;
type SearchBody = Parameters<Stophy["youtube"]["search"]>[0];
type _QueryRequired = Expect<
	SearchBody extends { query: string } ? true : false
>;

export async function typedCalls(): Promise<void> {
	const result = await client.youtube.search({
		query: "bun runtime",
		cursor: "next",
	});
	const first = result.data.results[0];
	if (first?.type === "video") {
		const url: string = first.videoUrl;
		if (url.length < 0) throw new Error(url);
	}
	const credits: number = result.creditsUsed;
	if (credits < 0) throw new Error("unreachable");
	const transcript = await client.youtube.transcript({
		videoUrl: "https://youtu.be/abc",
	});
	const seconds: number | undefined = transcript.data.transcribedSeconds;
	if (seconds !== undefined && seconds < 0) throw new Error("unreachable");
	await client.amazon.search({ query: "tv", sort: "priceLow" });
	const google = await client.google.search({ query: "bun", page: 2 });
	const page: number | undefined = google.data.page;
	if (page === 0) throw new Error("unreachable");
	await client.meta.ads.page({ advertiser: "nike" });
	await client.meta.ads.search({ query: "shoes" });
	await client.google.ads.search({ domain: "example.com" });
	const profile = await client.tiktok.profile({ username: "bun" });
	const videos = profile.data.results ?? [];
	if (videos.length < 0) throw new Error("unreachable");
	const instagram = await client.instagram.profile({ username: "bun" });
	const postTotal: number = instagram.data.posts ?? 0;
	const rows = instagram.data.results ?? [];
	if (postTotal < 0 || rows.length < 0) throw new Error("unreachable");

	// @ts-expect-error query is required
	await client.youtube.search({});
	// @ts-expect-error limit is gone, results come one page at a time
	await client.youtube.search({ query: "bun", limit: 2 });
	// @ts-expect-error google.search pages by number, not cursor
	await client.google.search({ query: "bun", cursor: "next" });
	// @ts-expect-error the page is named advertiser
	await client.meta.ads.page({ page: "nike" });
	// @ts-expect-error profile is now username or userUrl
	await client.tiktok.profile({ profile: "bun" });
	// @ts-expect-error the sort is named sort
	await client.amazon.search({ query: "tv", sortBy: "priceLow" });
	// @ts-expect-error the video list is results
	profile.data.posts;
	// @ts-expect-error the post count is posts
	instagram.data.postCount;
	// @ts-expect-error retired endpoints are not in the client
	await client.walmart.search({ query: "tv" });
	// @ts-expect-error format is gone
	await client.youtube.search({ query: "bun" }, { format: "markdown" });
}
