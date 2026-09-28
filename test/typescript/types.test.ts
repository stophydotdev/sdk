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
	const url = result.data.results[0]?.url;
	if (url !== undefined && typeof url !== "string") {
		throw new Error(url);
	}
	const markdown: string = await client.youtube.search(
		{ query: "bun runtime" },
		{ format: "markdown" },
	);
	if (markdown.length < 0) throw new Error("unreachable");
	await client.youtube.comments.replies({ video: "abc", cursor: "tok" });
	await client.maps.search({ query: "cairo" });

	// @ts-expect-error query is required
	await client.youtube.search({});
}
