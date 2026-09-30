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
	await client.transcript({ video: "https://youtu.be/abc" });
	await client.ads.search({ network: "meta", query: "shoes" });
	await client.suggest({ source: "amazon", query: "bun" });
	await client.google.trends({ by: "region", queries: ["bun"] });

	// @ts-expect-error query is required
	await client.youtube.search({});
	// @ts-expect-error network is required
	await client.ads.search({ query: "shoes" });
	// @ts-expect-error format is gone
	await client.youtube.search({ query: "bun" }, { format: "markdown" });
}
