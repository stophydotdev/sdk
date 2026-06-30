import type { Client } from "@hey-api/client-fetch";
import { getChannel } from "../generated/sdk.gen";
import type {
	GetChannelData,
	GetChannelResponse,
} from "../generated/types.gen";
import { unwrap } from "../transport";

type ChannelBody = GetChannelData["body"];
export type ChannelOptions = Omit<ChannelBody, "channelUrl">;

export function channel(
	client: Client,
	urlOrBody: string | ChannelBody,
	options: ChannelOptions = {},
): Promise<GetChannelResponse> {
	const body =
		typeof urlOrBody === "string"
			? { channelUrl: urlOrBody, ...options }
			: urlOrBody;
	return getChannel({ client, body }).then(unwrap);
}
