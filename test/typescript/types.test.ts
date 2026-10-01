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
		limit: 2,
	});
	const first = result.data.results[0];
	if (first?.type === "video") {
		const url: string = first.videoUrl;
		if (url.length < 0) throw new Error(url);
	}
	const credits: number = result.creditsUsed;
	if (credits < 0) throw new Error("unreachable");
	const transcript = await client.transcript({ video: "https://youtu.be/abc" });
	const seconds: number | undefined = transcript.data.transcribedSeconds;
	if (seconds !== undefined && seconds < 0) throw new Error("unreachable");
	await client.walmart.search({ query: "tv", sort: "priceLow" });
	await client.ads.search({ network: "meta", query: "shoes" });
	await client.ads.search({ network: "google", query: "example.com" });
	const profile = await client.tiktok.profile({ profile: "bun" });
	const videos = profile.data.results ?? [];
	if (videos.length < 0) throw new Error("unreachable");
	const instagram = await client.instagram.profile({ profile: "bun" });
	const postTotal: number = instagram.data.posts ?? 0;
	const rows = instagram.data.results ?? [];
	if (postTotal < 0 || rows.length < 0) throw new Error("unreachable");

	// @ts-expect-error query is required
	await client.youtube.search({});
	// @ts-expect-error network is required
	await client.ads.search({ query: "shoes" });
	// @ts-expect-error the video list is results
	profile.data.posts;
	// @ts-expect-error the post count is posts
	instagram.data.postCount;
	// @ts-expect-error hidden endpoints are not in the client
	await client.amazon.product({ product: "B08N5WRWNW" });
	// @ts-expect-error format is gone
	await client.youtube.search({ query: "bun" }, { format: "markdown" });
}
