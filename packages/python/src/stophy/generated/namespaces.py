"""Generated from openapi.json by scripts/gen_python.py. Do not edit."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Protocol, overload

from .models import (
    AdsAdResponse,
    AdsAdvertisersResponse,
    AdsSearchOption1MediaType,
    AdsSearchOption3Within,
    AdsSearchResponse,
    AirbnbCalendarResponse,
    AirbnbListingResponse,
    AirbnbReviewsResponse,
    AirbnbSearchResponse,
    AliexpressProductResponse,
    AliexpressSearchResponse,
    AliexpressSearchSort,
    AmazonBestsellersResponse,
    AmazonProductResponse,
    AmazonSearchCountry,
    AmazonSearchResponse,
    AmazonSearchSort,
    AppstoreAppResponse,
    AppstoreReviewsResponse,
    AppstoreReviewsSort,
    AppstoreSearchDevice,
    AppstoreSearchResponse,
    AppstoreTopChart,
    AppstoreTopGenre,
    AppstoreTopResponse,
    BlueskyFollowersResponse,
    BlueskyPostResponse,
    BlueskyProfileResponse,
    CryptoCoinResponse,
    CryptoCoinsResponse,
    CryptoCoinsSort,
    CryptoDexSearchResponse,
    CryptoDexTokenResponse,
    CryptoHistoryResponse,
    CryptoWalletChain,
    CryptoWalletResponse,
    EmailFindResponse,
    EmailVerifyResponse,
    EndpointCatalog,
    FinanceHistoryInterval,
    FinanceHistoryResponse,
    FinanceQuoteResponse,
    FinanceSearchResponse,
    FinanceStockResponse,
    GoogleplayAppResponse,
    GoogleplayReviewsResponse,
    GoogleplayReviewsSort,
    GoogleplaySearchResponse,
    GoogletravelFlightsCabin,
    GoogletravelFlightsResponse,
    GoogleTrendsOption1Resolution,
    GoogleTrendsRelatedResponse,
    GoogleTrendsResponse,
    GoogleTrendsTrendingCategory,
    GoogleTrendsTrendingResponse,
    GoogleTrendsTrendingWithin,
    ImmoscoutListingResponse,
    ImmoscoutSearchResponse,
    ImmoscoutSearchSort,
    ImmoscoutSearchType,
    IndeedJobResponse,
    IndeedSearchCountry,
    IndeedSearchResponse,
    IndeedSearchWithin,
    InstagramCommentsResponse,
    InstagramPostResponse,
    InstagramProfileResponse,
    InstagramSearchResponse,
    InstagramSearchType,
    LinkedinCompanyResponse,
    LinkedinJobsJobResponse,
    LinkedinJobsSearchResponse,
    LinkedinJobsSearchWithin,
    LinkedinPostsResponse,
    LinkedinProfileResponse,
    MapsPlaceResponse,
    MapsReviewsResponse,
    MapsReviewsSort,
    MapsSearchResponse,
    MetaAdsPageResponse,
    MetaAdsPageStatus,
    PinterestBoardResponse,
    PinterestPinResponse,
    PinterestSearchResponse,
    PinterestSearchType,
    PinterestUserResponse,
    RedditDomainResponse,
    RedditPostResponse,
    RedditPostSort,
    RedditSearchResponse,
    RedditSearchSort,
    RedditSearchType,
    RedditSubredditResponse,
    RedditSubredditSort,
    RedditUserResponse,
    RedditUserSort,
    RedditUserTab,
    RightmovePropertyResponse,
    RightmoveSearchResponse,
    RightmoveSearchSort,
    RightmoveSearchStatus,
    ShopifyCollectionsResponse,
    ShopifyProductsResponse,
    ShopifyStoreResponse,
    SiteSeoResponse,
    SuggestOption2Country,
    SuggestResponse,
    TelegramPostResponse,
    TelegramPostsResponse,
    ThreadsPostResponse,
    ThreadsProfileResponse,
    ThreadsSearchResponse,
    TiktokCommentsResponse,
    TiktokHashtagResponse,
    TiktokProfileResponse,
    TiktokSearchResponse,
    TiktokSearchType,
    TiktokVideoResponse,
    TranscriptResponse,
    TripadvisorPlaceResponse,
    TripadvisorReviewsResponse,
    TripadvisorSearchResponse,
    TripadvisorSearchType,
    UpworkJobResponse,
    UpworkSearchExperience,
    UpworkSearchJobType,
    UpworkSearchResponse,
    UpworkSearchSort,
    WalmartProductResponse,
    WalmartSearchResponse,
    WalmartSearchSort,
    WebNewsResponse,
    WebNewsTopic,
    WebNewsWithin,
    WebSearchResponse,
    WebSearchWithin,
    XPostResponse,
    YoutubeChannelResponse,
    YoutubeChannelTab,
    YoutubeCommentsResponse,
    YoutubeCommentsSort,
    YoutubePlaylistResponse,
    YoutubeSearchResponse,
    YoutubeSearchSort,
    YoutubeSearchType,
    YoutubeVideoResponse,
    ZillowPropertyResponse,
    ZillowSearchHomeTypesItem,
    ZillowSearchResponse,
    ZillowSearchSort,
    ZillowSearchStatus,
)


class SyncCall(Protocol):
    def __call__(
        self,
        method: str,
        path: str,
        body: Mapping[str, Any] | None,
    ) -> Any: ...


class AsyncCall(Protocol):
    async def __call__(
        self,
        method: str,
        path: str,
        body: Mapping[str, Any] | None,
    ) -> Any: ...


def _omit_none(values: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in values.items() if value is not None}


class SyncEndpoints:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
    ) -> EndpointCatalog:
        body = None
        return self._call("GET", "/v1/endpoints", body)


class SyncWebSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        within: WebSearchWithin | None = None,
        limit: int | None = None,
    ) -> WebSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "within": within,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/web/search", body)


class SyncWebNews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        topic: WebNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
    ) -> WebNewsResponse:
        body = _omit_none(
            {
                "query": query,
                "topic": topic,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "within": within,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/web/news", body)


class SyncWeb:
    search: SyncWebSearch
    news: SyncWebNews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncWebSearch(call)
        self.news = SyncWebNews(call)


class SyncYoutubeSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        within: WebNewsWithin | None = None,
        sort: YoutubeSearchSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> YoutubeSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "within": within,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/youtube/search", body)


class SyncYoutubeVideo:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video: str,
    ) -> YoutubeVideoResponse:
        body = _omit_none(
            {
                "video": video,
            }
        )
        return self._call("POST", "/v1/youtube/video", body)


class SyncYoutubeComments:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video: str,
        comment: str | None = None,
        sort: YoutubeCommentsSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> YoutubeCommentsResponse:
        body = _omit_none(
            {
                "video": video,
                "comment": comment,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/youtube/comments", body)


class SyncYoutubeChannel:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        channel: str,
        tab: YoutubeChannelTab | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> YoutubeChannelResponse:
        body = _omit_none(
            {
                "channel": channel,
                "tab": tab,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/youtube/channel", body)


class SyncYoutubePlaylist:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        playlist: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> YoutubePlaylistResponse:
        body = _omit_none(
            {
                "playlist": playlist,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/youtube/playlist", body)


class SyncYoutube:
    search: SyncYoutubeSearch
    video: SyncYoutubeVideo
    comments: SyncYoutubeComments
    channel: SyncYoutubeChannel
    playlist: SyncYoutubePlaylist

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncYoutubeSearch(call)
        self.video = SyncYoutubeVideo(call)
        self.comments = SyncYoutubeComments(call)
        self.channel = SyncYoutubeChannel(call)
        self.playlist = SyncYoutubePlaylist(call)


class SyncTranscript:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
    ) -> TranscriptResponse:
        body = _omit_none(
            {
                "video": video,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return self._call("POST", "/v1/transcript", body)


class SyncRedditSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: RedditSearchType | None = None,
        subreddit: str | None = None,
        sort: RedditSearchSort | None = None,
        within: WebNewsWithin | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RedditSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "subreddit": subreddit,
                "sort": sort,
                "within": within,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/reddit/search", body)


class SyncRedditPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post: str,
        sort: RedditPostSort | None = None,
    ) -> RedditPostResponse:
        body = _omit_none(
            {
                "post": post,
                "sort": sort,
            }
        )
        return self._call("POST", "/v1/reddit/post", body)


class SyncRedditSubreddit:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        subreddit: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RedditSubredditResponse:
        body = _omit_none(
            {
                "subreddit": subreddit,
                "sort": sort,
                "within": within,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/reddit/subreddit", body)


class SyncRedditUser:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RedditUserResponse:
        body = _omit_none(
            {
                "profile": profile,
                "tab": tab,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/reddit/user", body)


class SyncRedditDomain:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        domain: str,
        sort: RedditSubredditSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RedditDomainResponse:
        body = _omit_none(
            {
                "domain": domain,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/reddit/domain", body)


class SyncReddit:
    search: SyncRedditSearch
    post: SyncRedditPost
    subreddit: SyncRedditSubreddit
    user: SyncRedditUser
    domain: SyncRedditDomain

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncRedditSearch(call)
        self.post = SyncRedditPost(call)
        self.subreddit = SyncRedditSubreddit(call)
        self.user = SyncRedditUser(call)
        self.domain = SyncRedditDomain(call)


class SyncMapsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        location: str,
        cursor: str | None = None,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
    ) -> MapsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "cursor": cursor,
                "country": country,
                "language": language,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/maps/search", body)


class SyncMapsPlace:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        place: str,
        country: str | None = None,
        language: str | None = None,
    ) -> MapsPlaceResponse:
        body = _omit_none(
            {
                "place": place,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/maps/place", body)


class SyncMapsReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        place: str,
        sort: MapsReviewsSort | None = None,
        cursor: str | None = None,
        language: str | None = None,
        limit: int | None = None,
    ) -> MapsReviewsResponse:
        body = _omit_none(
            {
                "place": place,
                "sort": sort,
                "cursor": cursor,
                "language": language,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/maps/reviews", body)


class SyncMaps:
    search: SyncMapsSearch
    place: SyncMapsPlace
    reviews: SyncMapsReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncMapsSearch(call)
        self.place = SyncMapsPlace(call)
        self.reviews = SyncMapsReviews(call)


class SyncInstagramProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
    ) -> InstagramProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/instagram/profile", body)


class SyncInstagramPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post: str,
    ) -> InstagramPostResponse:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return self._call("POST", "/v1/instagram/post", body)


class SyncInstagramSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: InstagramSearchType | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
    ) -> InstagramSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "within": within,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/instagram/search", body)


class SyncInstagramComments:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post: str,
        comment: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> InstagramCommentsResponse:
        body = _omit_none(
            {
                "post": post,
                "comment": comment,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/instagram/comments", body)


class SyncInstagram:
    profile: SyncInstagramProfile
    post: SyncInstagramPost
    search: SyncInstagramSearch
    comments: SyncInstagramComments

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncInstagramProfile(call)
        self.post = SyncInstagramPost(call)
        self.search = SyncInstagramSearch(call)
        self.comments = SyncInstagramComments(call)


class SyncTiktokProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
    ) -> TiktokProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/profile", body)


class SyncTiktokVideo:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video: str,
    ) -> TiktokVideoResponse:
        body = _omit_none(
            {
                "video": video,
            }
        )
        return self._call("POST", "/v1/tiktok/video", body)


class SyncTiktokHashtag:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        hashtag: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TiktokHashtagResponse:
        body = _omit_none(
            {
                "hashtag": hashtag,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/tiktok/hashtag", body)


class SyncTiktokComments:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video: str,
        comment: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TiktokCommentsResponse:
        body = _omit_none(
            {
                "video": video,
                "comment": comment,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/tiktok/comments", body)


class SyncTiktokSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: TiktokSearchType | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TiktokSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/tiktok/search", body)


class SyncTiktok:
    profile: SyncTiktokProfile
    video: SyncTiktokVideo
    hashtag: SyncTiktokHashtag
    comments: SyncTiktokComments
    search: SyncTiktokSearch

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncTiktokProfile(call)
        self.video = SyncTiktokVideo(call)
        self.hashtag = SyncTiktokHashtag(call)
        self.comments = SyncTiktokComments(call)
        self.search = SyncTiktokSearch(call)


class SyncBlueskyProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
    ) -> BlueskyProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/bluesky/profile", body)


class SyncBlueskyPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post: str,
    ) -> BlueskyPostResponse:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return self._call("POST", "/v1/bluesky/post", body)


class SyncBlueskyFollowers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> BlueskyFollowersResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/bluesky/followers", body)


class SyncBluesky:
    profile: SyncBlueskyProfile
    post: SyncBlueskyPost
    followers: SyncBlueskyFollowers

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncBlueskyProfile(call)
        self.post = SyncBlueskyPost(call)
        self.followers = SyncBlueskyFollowers(call)


class SyncThreadsProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
    ) -> ThreadsProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/threads/profile", body)


class SyncThreadsPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post: str,
        cursor: str | None = None,
    ) -> ThreadsPostResponse:
        body = _omit_none(
            {
                "post": post,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/threads/post", body)


class SyncThreadsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
    ) -> ThreadsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/threads/search", body)


class SyncThreads:
    profile: SyncThreadsProfile
    post: SyncThreadsPost
    search: SyncThreadsSearch

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncThreadsProfile(call)
        self.post = SyncThreadsPost(call)
        self.search = SyncThreadsSearch(call)


class SyncTelegramPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        channel: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TelegramPostsResponse:
        body = _omit_none(
            {
                "channel": channel,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/telegram/posts", body)


class SyncTelegramPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post: str,
    ) -> TelegramPostResponse:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return self._call("POST", "/v1/telegram/post", body)


class SyncTelegram:
    posts: SyncTelegramPosts
    post: SyncTelegramPost

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.posts = SyncTelegramPosts(call)
        self.post = SyncTelegramPost(call)


class SyncMetaAdsPage:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> MetaAdsPageResponse:
        body = _omit_none(
            {
                "page": page,
                "country": country,
                "status": status,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/meta/ads/page", body)


class SyncMetaAds:
    page: SyncMetaAdsPage

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.page = SyncMetaAdsPage(call)


class SyncMeta:
    ads: SyncMetaAds

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.ads = SyncMetaAds(call)


class SyncLinkedinJobsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> LinkedinJobsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "within": within,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/linkedin/jobs/search", body)


class SyncLinkedinJobsJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        job: str,
    ) -> LinkedinJobsJobResponse:
        body = _omit_none(
            {
                "job": job,
            }
        )
        return self._call("POST", "/v1/linkedin/jobs/job", body)


class SyncLinkedinJobs:
    search: SyncLinkedinJobsSearch
    job: SyncLinkedinJobsJob

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncLinkedinJobsSearch(call)
        self.job = SyncLinkedinJobsJob(call)


class SyncLinkedinCompany:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        company: str,
    ) -> LinkedinCompanyResponse:
        body = _omit_none(
            {
                "company": company,
            }
        )
        return self._call("POST", "/v1/linkedin/company", body)


class SyncLinkedinProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
    ) -> LinkedinProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
            }
        )
        return self._call("POST", "/v1/linkedin/profile", body)


class SyncLinkedinPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str | None = None,
        company: str | None = None,
        limit: int | None = None,
    ) -> LinkedinPostsResponse:
        body = _omit_none(
            {
                "profile": profile,
                "company": company,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/linkedin/posts", body)


class SyncLinkedin:
    jobs: SyncLinkedinJobs
    company: SyncLinkedinCompany
    profile: SyncLinkedinProfile
    posts: SyncLinkedinPosts

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.jobs = SyncLinkedinJobs(call)
        self.company = SyncLinkedinCompany(call)
        self.profile = SyncLinkedinProfile(call)
        self.posts = SyncLinkedinPosts(call)


class SyncZillowSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        location: str,
        status: ZillowSearchStatus | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_bedrooms: int | None = None,
        max_bedrooms: int | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        sort: ZillowSearchSort | None = None,
        query: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ZillowSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minBedrooms": min_bedrooms,
                "maxBedrooms": max_bedrooms,
                "homeTypes": home_types,
                "sort": sort,
                "query": query,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/zillow/search", body)


class SyncZillowProperty:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        property: str,
    ) -> ZillowPropertyResponse:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return self._call("POST", "/v1/zillow/property", body)


class SyncZillow:
    search: SyncZillowSearch
    property: SyncZillowProperty

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncZillowSearch(call)
        self.property = SyncZillowProperty(call)


class SyncUpworkSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        sort: UpworkSearchSort | None = None,
        job_type: UpworkSearchJobType | None = None,
        experience: UpworkSearchExperience | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> UpworkSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "jobType": job_type,
                "experience": experience,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/upwork/search", body)


class SyncUpworkJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        job: str,
    ) -> UpworkJobResponse:
        body = _omit_none(
            {
                "job": job,
            }
        )
        return self._call("POST", "/v1/upwork/job", body)


class SyncUpwork:
    search: SyncUpworkSearch
    job: SyncUpworkJob

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncUpworkSearch(call)
        self.job = SyncUpworkJob(call)


class SyncGoogleTrendsRelated:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
    ) -> GoogleTrendsRelatedResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "within": within,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/google/trends/related", body)


class SyncGoogleTrendsTrending:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        country: str | None = None,
        within: GoogleTrendsTrendingWithin | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        limit: int | None = None,
    ) -> GoogleTrendsTrendingResponse:
        body = _omit_none(
            {
                "country": country,
                "within": within,
                "category": category,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/google/trends/trending", body)


class SyncGoogleTrends:
    related: SyncGoogleTrendsRelated
    trending: SyncGoogleTrendsTrending

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.related = SyncGoogleTrendsRelated(call)
        self.trending = SyncGoogleTrendsTrending(call)

    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        within: WebNewsWithin | None = None,
        by: Literal["time"],
        limit: int | None = None,
    ) -> GoogleTrendsResponse: ...
    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        within: WebNewsWithin | None = None,
        resolution: GoogleTrendsOption1Resolution | None = None,
        by: Literal["region"],
        limit: int | None = None,
    ) -> GoogleTrendsResponse: ...
    def __call__(
        self,
        *,
        queries: list[str] | None = None,
        country: str | None = None,
        within: WebNewsWithin | None = None,
        by: Literal["time"] | Literal["region"] | None = None,
        limit: int | None = None,
        resolution: GoogleTrendsOption1Resolution | None = None,
    ) -> GoogleTrendsResponse:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "within": within,
                "by": by,
                "limit": limit,
                "resolution": resolution,
            }
        )
        return self._call("POST", "/v1/google/trends", body)


class SyncGoogle:
    trends: SyncGoogleTrends

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.trends = SyncGoogleTrends(call)


class SyncSiteSeo:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        url: str,
    ) -> SiteSeoResponse:
        body = _omit_none(
            {
                "url": url,
            }
        )
        return self._call("POST", "/v1/site/seo", body)


class SyncSite:
    seo: SyncSiteSeo

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.seo = SyncSiteSeo(call)


class SyncEmailVerify:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        email: str,
    ) -> EmailVerifyResponse:
        body = _omit_none(
            {
                "email": email,
            }
        )
        return self._call("POST", "/v1/email/verify", body)


class SyncEmailFind:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        domain: str,
        name: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
    ) -> EmailFindResponse:
        body = _omit_none(
            {
                "domain": domain,
                "name": name,
                "firstName": first_name,
                "lastName": last_name,
            }
        )
        return self._call("POST", "/v1/email/find", body)


class SyncEmail:
    verify: SyncEmailVerify
    find: SyncEmailFind

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.verify = SyncEmailVerify(call)
        self.find = SyncEmailFind(call)


class SyncCryptoCoins:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        currency: str | None = None,
        category: str | None = None,
        coins: list[str] | None = None,
        sort: CryptoCoinsSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> CryptoCoinsResponse:
        body = _omit_none(
            {
                "currency": currency,
                "category": category,
                "coins": coins,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/coins", body)


class SyncCryptoCoin:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        coin: str,
        platform: str | None = None,
        currency: str | None = None,
    ) -> CryptoCoinResponse:
        body = _omit_none(
            {
                "coin": coin,
                "platform": platform,
                "currency": currency,
            }
        )
        return self._call("POST", "/v1/crypto/coin", body)


class SyncCryptoHistory:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        coin: str,
        currency: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
    ) -> CryptoHistoryResponse:
        body = _omit_none(
            {
                "coin": coin,
                "currency": currency,
                "from": from_,
                "to": to,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/history", body)


class SyncCryptoDexSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
    ) -> CryptoDexSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/dex/search", body)


class SyncCryptoDexToken:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        chain: str | None = None,
        token: str,
    ) -> CryptoDexTokenResponse:
        body = _omit_none(
            {
                "chain": chain,
                "token": token,
            }
        )
        return self._call("POST", "/v1/crypto/dex/token", body)


class SyncCryptoDex:
    search: SyncCryptoDexSearch
    token: SyncCryptoDexToken

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncCryptoDexSearch(call)
        self.token = SyncCryptoDexToken(call)


class SyncCryptoWallet:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        chain: CryptoWalletChain,
        wallet: str,
        cursor: str | None = None,
    ) -> CryptoWalletResponse:
        body = _omit_none(
            {
                "chain": chain,
                "wallet": wallet,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/crypto/wallet", body)


class SyncCrypto:
    coins: SyncCryptoCoins
    coin: SyncCryptoCoin
    history: SyncCryptoHistory
    dex: SyncCryptoDex
    wallet: SyncCryptoWallet

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.coins = SyncCryptoCoins(call)
        self.coin = SyncCryptoCoin(call)
        self.history = SyncCryptoHistory(call)
        self.dex = SyncCryptoDex(call)
        self.wallet = SyncCryptoWallet(call)


class SyncIndeedSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        country: IndeedSearchCountry | None = None,
        remote: bool | None = None,
        within: IndeedSearchWithin | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> IndeedSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "country": country,
                "remote": remote,
                "within": within,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/indeed/search", body)


class SyncIndeedJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        job: str,
        country: IndeedSearchCountry | None = None,
    ) -> IndeedJobResponse:
        body = _omit_none(
            {
                "job": job,
                "country": country,
            }
        )
        return self._call("POST", "/v1/indeed/job", body)


class SyncIndeed:
    search: SyncIndeedSearch
    job: SyncIndeedJob

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncIndeedSearch(call)
        self.job = SyncIndeedJob(call)


class SyncTripadvisorSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        limit: int | None = None,
    ) -> TripadvisorSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/tripadvisor/search", body)


class SyncTripadvisorPlace:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        place: str,
    ) -> TripadvisorPlaceResponse:
        body = _omit_none(
            {
                "place": place,
            }
        )
        return self._call("POST", "/v1/tripadvisor/place", body)


class SyncTripadvisorReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        place: str,
        language: str | None = None,
        ratings: list[int] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TripadvisorReviewsResponse:
        body = _omit_none(
            {
                "place": place,
                "language": language,
                "ratings": ratings,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/tripadvisor/reviews", body)


class SyncTripadvisor:
    search: SyncTripadvisorSearch
    place: SyncTripadvisorPlace
    reviews: SyncTripadvisorReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncTripadvisorSearch(call)
        self.place = SyncTripadvisorPlace(call)
        self.reviews = SyncTripadvisorReviews(call)


class SyncGoogletravelFlights:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        adults: int | None = None,
        cabin: GoogletravelFlightsCabin | None = None,
        limit: int | None = None,
    ) -> GoogletravelFlightsResponse:
        body = _omit_none(
            {
                "origin": origin,
                "destination": destination,
                "departDate": depart_date,
                "returnDate": return_date,
                "adults": adults,
                "cabin": cabin,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/googletravel/flights", body)


class SyncGoogletravel:
    flights: SyncGoogletravelFlights

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.flights = SyncGoogletravelFlights(call)


class SyncAmazonSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        category: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort: AmazonSearchSort | None = None,
        country: AmazonSearchCountry | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AmazonSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "category": category,
                "minPrice": min_price,
                "maxPrice": max_price,
                "sort": sort,
                "country": country,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/amazon/search", body)


class SyncAmazonProduct:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        product: str,
        country: AmazonSearchCountry | None = None,
    ) -> AmazonProductResponse:
        body = _omit_none(
            {
                "product": product,
                "country": country,
            }
        )
        return self._call("POST", "/v1/amazon/product", body)


class SyncAmazonBestsellers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        category: str,
        country: AmazonSearchCountry | None = None,
        cursor: Literal["2"] | None = None,
        limit: int | None = None,
    ) -> AmazonBestsellersResponse:
        body = _omit_none(
            {
                "category": category,
                "country": country,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/amazon/bestsellers", body)


class SyncAmazon:
    search: SyncAmazonSearch
    product: SyncAmazonProduct
    bestsellers: SyncAmazonBestsellers

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncAmazonSearch(call)
        self.product = SyncAmazonProduct(call)
        self.bestsellers = SyncAmazonBestsellers(call)


class SyncShopifyProducts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        store: str,
        collection: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ShopifyProductsResponse:
        body = _omit_none(
            {
                "store": store,
                "collection": collection,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/shopify/products", body)


class SyncShopifyCollections:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        store: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ShopifyCollectionsResponse:
        body = _omit_none(
            {
                "store": store,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/shopify/collections", body)


class SyncShopifyStore:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        store: str,
    ) -> ShopifyStoreResponse:
        body = _omit_none(
            {
                "store": store,
            }
        )
        return self._call("POST", "/v1/shopify/store", body)


class SyncShopify:
    products: SyncShopifyProducts
    collections: SyncShopifyCollections
    store: SyncShopifyStore

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.products = SyncShopifyProducts(call)
        self.collections = SyncShopifyCollections(call)
        self.store = SyncShopifyStore(call)


class SyncWalmartSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        sort: WalmartSearchSort | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> WalmartSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "minPrice": min_price,
                "maxPrice": max_price,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/walmart/search", body)


class SyncWalmartProduct:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        product: str,
    ) -> WalmartProductResponse:
        body = _omit_none(
            {
                "product": product,
            }
        )
        return self._call("POST", "/v1/walmart/product", body)


class SyncWalmart:
    search: SyncWalmartSearch
    product: SyncWalmartProduct

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncWalmartSearch(call)
        self.product = SyncWalmartProduct(call)


class SyncAliexpressSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        sort: AliexpressSearchSort | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AliexpressSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "minPrice": min_price,
                "maxPrice": max_price,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/aliexpress/search", body)


class SyncAliexpressProduct:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        product: str,
    ) -> AliexpressProductResponse:
        body = _omit_none(
            {
                "product": product,
            }
        )
        return self._call("POST", "/v1/aliexpress/product", body)


class SyncAliexpress:
    search: SyncAliexpressSearch
    product: SyncAliexpressProduct

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncAliexpressSearch(call)
        self.product = SyncAliexpressProduct(call)


class SyncAppstoreApp:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
    ) -> AppstoreAppResponse:
        body = _omit_none(
            {
                "app": app,
                "country": country,
            }
        )
        return self._call("POST", "/v1/appstore/app", body)


class SyncAppstoreSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        device: AppstoreSearchDevice | None = None,
        limit: int | None = None,
    ) -> AppstoreSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "device": device,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/appstore/search", body)


class SyncAppstoreReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AppstoreReviewsResponse:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/appstore/reviews", body)


class SyncAppstoreTop:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        chart: AppstoreTopChart | None = None,
        device: AppstoreSearchDevice | None = None,
        genre: AppstoreTopGenre | None = None,
        country: str | None = None,
        limit: int | None = None,
    ) -> AppstoreTopResponse:
        body = _omit_none(
            {
                "chart": chart,
                "device": device,
                "genre": genre,
                "country": country,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/appstore/top", body)


class SyncAppstore:
    app: SyncAppstoreApp
    search: SyncAppstoreSearch
    reviews: SyncAppstoreReviews
    top: SyncAppstoreTop

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.app = SyncAppstoreApp(call)
        self.search = SyncAppstoreSearch(call)
        self.reviews = SyncAppstoreReviews(call)
        self.top = SyncAppstoreTop(call)


class SyncGoogleplayApp:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
    ) -> GoogleplayAppResponse:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/googleplay/app", body)


class SyncGoogleplaySearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
    ) -> GoogleplaySearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/googleplay/search", body)


class SyncGoogleplayReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        sort: GoogleplayReviewsSort | None = None,
        rating: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> GoogleplayReviewsResponse:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "language": language,
                "sort": sort,
                "rating": rating,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/googleplay/reviews", body)


class SyncGoogleplay:
    app: SyncGoogleplayApp
    search: SyncGoogleplaySearch
    reviews: SyncGoogleplayReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.app = SyncGoogleplayApp(call)
        self.search = SyncGoogleplaySearch(call)
        self.reviews = SyncGoogleplayReviews(call)


class SyncAirbnbSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        location: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AirbnbSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "checkIn": check_in,
                "checkOut": check_out,
                "adults": adults,
                "minPrice": min_price,
                "maxPrice": max_price,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/airbnb/search", body)


class SyncAirbnbListing:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        listing: str,
    ) -> AirbnbListingResponse:
        body = _omit_none(
            {
                "listing": listing,
            }
        )
        return self._call("POST", "/v1/airbnb/listing", body)


class SyncAirbnbCalendar:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        listing: str,
        month: str | None = None,
        limit: int | None = None,
    ) -> AirbnbCalendarResponse:
        body = _omit_none(
            {
                "listing": listing,
                "month": month,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/airbnb/calendar", body)


class SyncAirbnbReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        listing: str,
        sort: MapsReviewsSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AirbnbReviewsResponse:
        body = _omit_none(
            {
                "listing": listing,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/airbnb/reviews", body)


class SyncAirbnb:
    search: SyncAirbnbSearch
    listing: SyncAirbnbListing
    calendar: SyncAirbnbCalendar
    reviews: SyncAirbnbReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncAirbnbSearch(call)
        self.listing = SyncAirbnbListing(call)
        self.calendar = SyncAirbnbCalendar(call)
        self.reviews = SyncAirbnbReviews(call)


class SyncRightmoveSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        location: str,
        status: RightmoveSearchStatus | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_bedrooms: int | None = None,
        max_bedrooms: int | None = None,
        sort: RightmoveSearchSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RightmoveSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minBedrooms": min_bedrooms,
                "maxBedrooms": max_bedrooms,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/rightmove/search", body)


class SyncRightmoveProperty:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        property: str,
    ) -> RightmovePropertyResponse:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return self._call("POST", "/v1/rightmove/property", body)


class SyncRightmove:
    search: SyncRightmoveSearch
    property: SyncRightmoveProperty

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncRightmoveSearch(call)
        self.property = SyncRightmoveProperty(call)


class SyncImmoscoutSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        location: str,
        type: ImmoscoutSearchType | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_rooms: float | None = None,
        sort: ImmoscoutSearchSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ImmoscoutSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "type": type,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minRooms": min_rooms,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/immoscout/search", body)


class SyncImmoscoutListing:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        listing: str,
    ) -> ImmoscoutListingResponse:
        body = _omit_none(
            {
                "listing": listing,
            }
        )
        return self._call("POST", "/v1/immoscout/listing", body)


class SyncImmoscout:
    search: SyncImmoscoutSearch
    listing: SyncImmoscoutListing

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncImmoscoutSearch(call)
        self.listing = SyncImmoscoutListing(call)


class SyncPinterestSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> PinterestSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/pinterest/search", body)


class SyncPinterestPin:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        pin: str,
    ) -> PinterestPinResponse:
        body = _omit_none(
            {
                "pin": pin,
            }
        )
        return self._call("POST", "/v1/pinterest/pin", body)


class SyncPinterestBoard:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        board: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> PinterestBoardResponse:
        body = _omit_none(
            {
                "board": board,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/pinterest/board", body)


class SyncPinterestUser:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> PinterestUserResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/pinterest/user", body)


class SyncPinterest:
    search: SyncPinterestSearch
    pin: SyncPinterestPin
    board: SyncPinterestBoard
    user: SyncPinterestUser

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncPinterestSearch(call)
        self.pin = SyncPinterestPin(call)
        self.board = SyncPinterestBoard(call)
        self.user = SyncPinterestUser(call)


class SyncXPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post: str,
    ) -> XPostResponse:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return self._call("POST", "/v1/x/post", body)


class SyncX:
    post: SyncXPost

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.post = SyncXPost(call)


class SyncFinanceQuote:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        symbols: list[str],
        limit: int | None = None,
    ) -> FinanceQuoteResponse:
        body = _omit_none(
            {
                "symbols": symbols,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/finance/quote", body)


class SyncFinanceHistory:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        symbol: str,
        from_: str | None = None,
        to: str | None = None,
        interval: FinanceHistoryInterval | None = None,
        limit: int | None = None,
    ) -> FinanceHistoryResponse:
        body = _omit_none(
            {
                "symbol": symbol,
                "from": from_,
                "to": to,
                "interval": interval,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/finance/history", body)


class SyncFinanceSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
    ) -> FinanceSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/finance/search", body)


class SyncFinanceStock:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        symbol: str,
    ) -> FinanceStockResponse:
        body = _omit_none(
            {
                "symbol": symbol,
            }
        )
        return self._call("POST", "/v1/finance/stock", body)


class SyncFinance:
    quote: SyncFinanceQuote
    history: SyncFinanceHistory
    search: SyncFinanceSearch
    stock: SyncFinanceStock

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.quote = SyncFinanceQuote(call)
        self.history = SyncFinanceHistory(call)
        self.search = SyncFinanceSearch(call)
        self.stock = SyncFinanceStock(call)


class SyncAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        cursor: str | None = None,
        network: Literal["meta"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: AdsSearchOption1MediaType | None = None,
        cursor: str | None = None,
        network: Literal["google"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        cursor: str | None = None,
        network: Literal["tiktok"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        within: AdsSearchOption3Within | None = None,
        cursor: str | None = None,
        network: Literal["linkedin"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        cursor: str | None = None,
        network: Literal["microsoft"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    def __call__(
        self,
        *,
        country: str,
        advertiser: str | None = None,
        cursor: str | None = None,
        network: Literal["pinterest"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        cursor: str | None = None,
        network: Literal["meta"]
        | Literal["google"]
        | Literal["tiktok"]
        | Literal["linkedin"]
        | Literal["microsoft"]
        | Literal["pinterest"]
        | None = None,
        limit: int | None = None,
        advertiser: str | None = None,
        domain: str | None = None,
        media_type: AdsSearchOption1MediaType | None = None,
        within: AdsSearchOption3Within | None = None,
    ) -> AdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "status": status,
                "cursor": cursor,
                "network": network,
                "limit": limit,
                "advertiser": advertiser,
                "domain": domain,
                "mediaType": media_type,
                "within": within,
            }
        )
        return self._call("POST", "/v1/ads/search", body)


class SyncAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        network: Literal["meta"],
    ) -> AdsAdResponse: ...
    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        ad: str,
        network: Literal["google"],
    ) -> AdsAdResponse: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        network: Literal["tiktok"],
    ) -> AdsAdResponse: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        network: Literal["linkedin"],
    ) -> AdsAdResponse: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        network: Literal["microsoft"],
    ) -> AdsAdResponse: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        network: Literal["pinterest"],
    ) -> AdsAdResponse: ...
    def __call__(
        self,
        *,
        ad: str | None = None,
        network: Literal["meta"]
        | Literal["google"]
        | Literal["tiktok"]
        | Literal["linkedin"]
        | Literal["microsoft"]
        | Literal["pinterest"]
        | None = None,
        advertiser: str | None = None,
    ) -> AdsAdResponse:
        body = _omit_none(
            {
                "ad": ad,
                "network": network,
                "advertiser": advertiser,
            }
        )
        return self._call("POST", "/v1/ads/ad", body)


class SyncAdsAdvertisers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        network: Literal["google"],
        limit: int | None = None,
    ) -> AdsAdvertisersResponse: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        network: Literal["microsoft"],
        limit: int | None = None,
    ) -> AdsAdvertisersResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        country: str | None = None,
        network: Literal["google"] | Literal["microsoft"] | None = None,
        limit: int | None = None,
    ) -> AdsAdvertisersResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "network": network,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/ads/advertisers", body)


class SyncAds:
    search: SyncAdsSearch
    ad: SyncAdsAd
    advertisers: SyncAdsAdvertisers

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncAdsSearch(call)
        self.ad = SyncAdsAd(call)
        self.advertisers = SyncAdsAdvertisers(call)


class SyncSuggest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        source: Literal["google"],
        limit: int | None = None,
    ) -> SuggestResponse: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        source: Literal["youtube"],
        limit: int | None = None,
    ) -> SuggestResponse: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: SuggestOption2Country | None = None,
        source: Literal["amazon"],
        limit: int | None = None,
    ) -> SuggestResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        country: str | SuggestOption2Country | None = None,
        language: str | None = None,
        source: Literal["google"] | Literal["youtube"] | Literal["amazon"] | None = None,
        limit: int | None = None,
    ) -> SuggestResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "source": source,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/suggest", body)


class SyncSurface:
    endpoints: SyncEndpoints
    web: SyncWeb
    youtube: SyncYoutube
    transcript: SyncTranscript
    reddit: SyncReddit
    maps: SyncMaps
    instagram: SyncInstagram
    tiktok: SyncTiktok
    bluesky: SyncBluesky
    threads: SyncThreads
    telegram: SyncTelegram
    meta: SyncMeta
    linkedin: SyncLinkedin
    zillow: SyncZillow
    upwork: SyncUpwork
    google: SyncGoogle
    site: SyncSite
    email: SyncEmail
    crypto: SyncCrypto
    indeed: SyncIndeed
    tripadvisor: SyncTripadvisor
    googletravel: SyncGoogletravel
    amazon: SyncAmazon
    shopify: SyncShopify
    walmart: SyncWalmart
    aliexpress: SyncAliexpress
    appstore: SyncAppstore
    googleplay: SyncGoogleplay
    airbnb: SyncAirbnb
    rightmove: SyncRightmove
    immoscout: SyncImmoscout
    pinterest: SyncPinterest
    x: SyncX
    finance: SyncFinance
    ads: SyncAds
    suggest: SyncSuggest

    def __init__(self, call: SyncCall) -> None:
        self.endpoints = SyncEndpoints(call)
        self.web = SyncWeb(call)
        self.youtube = SyncYoutube(call)
        self.transcript = SyncTranscript(call)
        self.reddit = SyncReddit(call)
        self.maps = SyncMaps(call)
        self.instagram = SyncInstagram(call)
        self.tiktok = SyncTiktok(call)
        self.bluesky = SyncBluesky(call)
        self.threads = SyncThreads(call)
        self.telegram = SyncTelegram(call)
        self.meta = SyncMeta(call)
        self.linkedin = SyncLinkedin(call)
        self.zillow = SyncZillow(call)
        self.upwork = SyncUpwork(call)
        self.google = SyncGoogle(call)
        self.site = SyncSite(call)
        self.email = SyncEmail(call)
        self.crypto = SyncCrypto(call)
        self.indeed = SyncIndeed(call)
        self.tripadvisor = SyncTripadvisor(call)
        self.googletravel = SyncGoogletravel(call)
        self.amazon = SyncAmazon(call)
        self.shopify = SyncShopify(call)
        self.walmart = SyncWalmart(call)
        self.aliexpress = SyncAliexpress(call)
        self.appstore = SyncAppstore(call)
        self.googleplay = SyncGoogleplay(call)
        self.airbnb = SyncAirbnb(call)
        self.rightmove = SyncRightmove(call)
        self.immoscout = SyncImmoscout(call)
        self.pinterest = SyncPinterest(call)
        self.x = SyncX(call)
        self.finance = SyncFinance(call)
        self.ads = SyncAds(call)
        self.suggest = SyncSuggest(call)


class AsyncEndpoints:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
    ) -> EndpointCatalog:
        body = None
        return await self._call("GET", "/v1/endpoints", body)


class AsyncWebSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        within: WebSearchWithin | None = None,
        limit: int | None = None,
    ) -> WebSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "within": within,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/web/search", body)


class AsyncWebNews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        topic: WebNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
    ) -> WebNewsResponse:
        body = _omit_none(
            {
                "query": query,
                "topic": topic,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "within": within,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/web/news", body)


class AsyncWeb:
    search: AsyncWebSearch
    news: AsyncWebNews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncWebSearch(call)
        self.news = AsyncWebNews(call)


class AsyncYoutubeSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        within: WebNewsWithin | None = None,
        sort: YoutubeSearchSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> YoutubeSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "within": within,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/youtube/search", body)


class AsyncYoutubeVideo:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video: str,
    ) -> YoutubeVideoResponse:
        body = _omit_none(
            {
                "video": video,
            }
        )
        return await self._call("POST", "/v1/youtube/video", body)


class AsyncYoutubeComments:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video: str,
        comment: str | None = None,
        sort: YoutubeCommentsSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> YoutubeCommentsResponse:
        body = _omit_none(
            {
                "video": video,
                "comment": comment,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/youtube/comments", body)


class AsyncYoutubeChannel:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        channel: str,
        tab: YoutubeChannelTab | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> YoutubeChannelResponse:
        body = _omit_none(
            {
                "channel": channel,
                "tab": tab,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/youtube/channel", body)


class AsyncYoutubePlaylist:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        playlist: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> YoutubePlaylistResponse:
        body = _omit_none(
            {
                "playlist": playlist,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/youtube/playlist", body)


class AsyncYoutube:
    search: AsyncYoutubeSearch
    video: AsyncYoutubeVideo
    comments: AsyncYoutubeComments
    channel: AsyncYoutubeChannel
    playlist: AsyncYoutubePlaylist

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncYoutubeSearch(call)
        self.video = AsyncYoutubeVideo(call)
        self.comments = AsyncYoutubeComments(call)
        self.channel = AsyncYoutubeChannel(call)
        self.playlist = AsyncYoutubePlaylist(call)


class AsyncTranscript:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
    ) -> TranscriptResponse:
        body = _omit_none(
            {
                "video": video,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return await self._call("POST", "/v1/transcript", body)


class AsyncRedditSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: RedditSearchType | None = None,
        subreddit: str | None = None,
        sort: RedditSearchSort | None = None,
        within: WebNewsWithin | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RedditSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "subreddit": subreddit,
                "sort": sort,
                "within": within,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/reddit/search", body)


class AsyncRedditPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post: str,
        sort: RedditPostSort | None = None,
    ) -> RedditPostResponse:
        body = _omit_none(
            {
                "post": post,
                "sort": sort,
            }
        )
        return await self._call("POST", "/v1/reddit/post", body)


class AsyncRedditSubreddit:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        subreddit: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RedditSubredditResponse:
        body = _omit_none(
            {
                "subreddit": subreddit,
                "sort": sort,
                "within": within,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/reddit/subreddit", body)


class AsyncRedditUser:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RedditUserResponse:
        body = _omit_none(
            {
                "profile": profile,
                "tab": tab,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/reddit/user", body)


class AsyncRedditDomain:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        domain: str,
        sort: RedditSubredditSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RedditDomainResponse:
        body = _omit_none(
            {
                "domain": domain,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/reddit/domain", body)


class AsyncReddit:
    search: AsyncRedditSearch
    post: AsyncRedditPost
    subreddit: AsyncRedditSubreddit
    user: AsyncRedditUser
    domain: AsyncRedditDomain

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncRedditSearch(call)
        self.post = AsyncRedditPost(call)
        self.subreddit = AsyncRedditSubreddit(call)
        self.user = AsyncRedditUser(call)
        self.domain = AsyncRedditDomain(call)


class AsyncMapsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        location: str,
        cursor: str | None = None,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
    ) -> MapsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "cursor": cursor,
                "country": country,
                "language": language,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/maps/search", body)


class AsyncMapsPlace:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        place: str,
        country: str | None = None,
        language: str | None = None,
    ) -> MapsPlaceResponse:
        body = _omit_none(
            {
                "place": place,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/maps/place", body)


class AsyncMapsReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        place: str,
        sort: MapsReviewsSort | None = None,
        cursor: str | None = None,
        language: str | None = None,
        limit: int | None = None,
    ) -> MapsReviewsResponse:
        body = _omit_none(
            {
                "place": place,
                "sort": sort,
                "cursor": cursor,
                "language": language,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/maps/reviews", body)


class AsyncMaps:
    search: AsyncMapsSearch
    place: AsyncMapsPlace
    reviews: AsyncMapsReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncMapsSearch(call)
        self.place = AsyncMapsPlace(call)
        self.reviews = AsyncMapsReviews(call)


class AsyncInstagramProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
    ) -> InstagramProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/instagram/profile", body)


class AsyncInstagramPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post: str,
    ) -> InstagramPostResponse:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return await self._call("POST", "/v1/instagram/post", body)


class AsyncInstagramSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: InstagramSearchType | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
    ) -> InstagramSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "within": within,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/instagram/search", body)


class AsyncInstagramComments:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post: str,
        comment: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> InstagramCommentsResponse:
        body = _omit_none(
            {
                "post": post,
                "comment": comment,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/instagram/comments", body)


class AsyncInstagram:
    profile: AsyncInstagramProfile
    post: AsyncInstagramPost
    search: AsyncInstagramSearch
    comments: AsyncInstagramComments

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncInstagramProfile(call)
        self.post = AsyncInstagramPost(call)
        self.search = AsyncInstagramSearch(call)
        self.comments = AsyncInstagramComments(call)


class AsyncTiktokProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
    ) -> TiktokProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/profile", body)


class AsyncTiktokVideo:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video: str,
    ) -> TiktokVideoResponse:
        body = _omit_none(
            {
                "video": video,
            }
        )
        return await self._call("POST", "/v1/tiktok/video", body)


class AsyncTiktokHashtag:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        hashtag: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TiktokHashtagResponse:
        body = _omit_none(
            {
                "hashtag": hashtag,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/tiktok/hashtag", body)


class AsyncTiktokComments:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video: str,
        comment: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TiktokCommentsResponse:
        body = _omit_none(
            {
                "video": video,
                "comment": comment,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/tiktok/comments", body)


class AsyncTiktokSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: TiktokSearchType | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TiktokSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/tiktok/search", body)


class AsyncTiktok:
    profile: AsyncTiktokProfile
    video: AsyncTiktokVideo
    hashtag: AsyncTiktokHashtag
    comments: AsyncTiktokComments
    search: AsyncTiktokSearch

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncTiktokProfile(call)
        self.video = AsyncTiktokVideo(call)
        self.hashtag = AsyncTiktokHashtag(call)
        self.comments = AsyncTiktokComments(call)
        self.search = AsyncTiktokSearch(call)


class AsyncBlueskyProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
    ) -> BlueskyProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/bluesky/profile", body)


class AsyncBlueskyPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post: str,
    ) -> BlueskyPostResponse:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return await self._call("POST", "/v1/bluesky/post", body)


class AsyncBlueskyFollowers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> BlueskyFollowersResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/bluesky/followers", body)


class AsyncBluesky:
    profile: AsyncBlueskyProfile
    post: AsyncBlueskyPost
    followers: AsyncBlueskyFollowers

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncBlueskyProfile(call)
        self.post = AsyncBlueskyPost(call)
        self.followers = AsyncBlueskyFollowers(call)


class AsyncThreadsProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
    ) -> ThreadsProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/threads/profile", body)


class AsyncThreadsPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post: str,
        cursor: str | None = None,
    ) -> ThreadsPostResponse:
        body = _omit_none(
            {
                "post": post,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/threads/post", body)


class AsyncThreadsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
    ) -> ThreadsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/threads/search", body)


class AsyncThreads:
    profile: AsyncThreadsProfile
    post: AsyncThreadsPost
    search: AsyncThreadsSearch

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncThreadsProfile(call)
        self.post = AsyncThreadsPost(call)
        self.search = AsyncThreadsSearch(call)


class AsyncTelegramPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        channel: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TelegramPostsResponse:
        body = _omit_none(
            {
                "channel": channel,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/telegram/posts", body)


class AsyncTelegramPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post: str,
    ) -> TelegramPostResponse:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return await self._call("POST", "/v1/telegram/post", body)


class AsyncTelegram:
    posts: AsyncTelegramPosts
    post: AsyncTelegramPost

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.posts = AsyncTelegramPosts(call)
        self.post = AsyncTelegramPost(call)


class AsyncMetaAdsPage:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> MetaAdsPageResponse:
        body = _omit_none(
            {
                "page": page,
                "country": country,
                "status": status,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/meta/ads/page", body)


class AsyncMetaAds:
    page: AsyncMetaAdsPage

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.page = AsyncMetaAdsPage(call)


class AsyncMeta:
    ads: AsyncMetaAds

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.ads = AsyncMetaAds(call)


class AsyncLinkedinJobsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> LinkedinJobsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "within": within,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/linkedin/jobs/search", body)


class AsyncLinkedinJobsJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        job: str,
    ) -> LinkedinJobsJobResponse:
        body = _omit_none(
            {
                "job": job,
            }
        )
        return await self._call("POST", "/v1/linkedin/jobs/job", body)


class AsyncLinkedinJobs:
    search: AsyncLinkedinJobsSearch
    job: AsyncLinkedinJobsJob

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncLinkedinJobsSearch(call)
        self.job = AsyncLinkedinJobsJob(call)


class AsyncLinkedinCompany:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        company: str,
    ) -> LinkedinCompanyResponse:
        body = _omit_none(
            {
                "company": company,
            }
        )
        return await self._call("POST", "/v1/linkedin/company", body)


class AsyncLinkedinProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
    ) -> LinkedinProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
            }
        )
        return await self._call("POST", "/v1/linkedin/profile", body)


class AsyncLinkedinPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str | None = None,
        company: str | None = None,
        limit: int | None = None,
    ) -> LinkedinPostsResponse:
        body = _omit_none(
            {
                "profile": profile,
                "company": company,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/linkedin/posts", body)


class AsyncLinkedin:
    jobs: AsyncLinkedinJobs
    company: AsyncLinkedinCompany
    profile: AsyncLinkedinProfile
    posts: AsyncLinkedinPosts

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.jobs = AsyncLinkedinJobs(call)
        self.company = AsyncLinkedinCompany(call)
        self.profile = AsyncLinkedinProfile(call)
        self.posts = AsyncLinkedinPosts(call)


class AsyncZillowSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        location: str,
        status: ZillowSearchStatus | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_bedrooms: int | None = None,
        max_bedrooms: int | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        sort: ZillowSearchSort | None = None,
        query: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ZillowSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minBedrooms": min_bedrooms,
                "maxBedrooms": max_bedrooms,
                "homeTypes": home_types,
                "sort": sort,
                "query": query,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/zillow/search", body)


class AsyncZillowProperty:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        property: str,
    ) -> ZillowPropertyResponse:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return await self._call("POST", "/v1/zillow/property", body)


class AsyncZillow:
    search: AsyncZillowSearch
    property: AsyncZillowProperty

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncZillowSearch(call)
        self.property = AsyncZillowProperty(call)


class AsyncUpworkSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        sort: UpworkSearchSort | None = None,
        job_type: UpworkSearchJobType | None = None,
        experience: UpworkSearchExperience | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> UpworkSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "jobType": job_type,
                "experience": experience,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/upwork/search", body)


class AsyncUpworkJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        job: str,
    ) -> UpworkJobResponse:
        body = _omit_none(
            {
                "job": job,
            }
        )
        return await self._call("POST", "/v1/upwork/job", body)


class AsyncUpwork:
    search: AsyncUpworkSearch
    job: AsyncUpworkJob

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncUpworkSearch(call)
        self.job = AsyncUpworkJob(call)


class AsyncGoogleTrendsRelated:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
    ) -> GoogleTrendsRelatedResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "within": within,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/google/trends/related", body)


class AsyncGoogleTrendsTrending:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        country: str | None = None,
        within: GoogleTrendsTrendingWithin | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        limit: int | None = None,
    ) -> GoogleTrendsTrendingResponse:
        body = _omit_none(
            {
                "country": country,
                "within": within,
                "category": category,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/google/trends/trending", body)


class AsyncGoogleTrends:
    related: AsyncGoogleTrendsRelated
    trending: AsyncGoogleTrendsTrending

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.related = AsyncGoogleTrendsRelated(call)
        self.trending = AsyncGoogleTrendsTrending(call)

    @overload
    async def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        within: WebNewsWithin | None = None,
        by: Literal["time"],
        limit: int | None = None,
    ) -> GoogleTrendsResponse: ...
    @overload
    async def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        within: WebNewsWithin | None = None,
        resolution: GoogleTrendsOption1Resolution | None = None,
        by: Literal["region"],
        limit: int | None = None,
    ) -> GoogleTrendsResponse: ...
    async def __call__(
        self,
        *,
        queries: list[str] | None = None,
        country: str | None = None,
        within: WebNewsWithin | None = None,
        by: Literal["time"] | Literal["region"] | None = None,
        limit: int | None = None,
        resolution: GoogleTrendsOption1Resolution | None = None,
    ) -> GoogleTrendsResponse:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "within": within,
                "by": by,
                "limit": limit,
                "resolution": resolution,
            }
        )
        return await self._call("POST", "/v1/google/trends", body)


class AsyncGoogle:
    trends: AsyncGoogleTrends

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.trends = AsyncGoogleTrends(call)


class AsyncSiteSeo:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        url: str,
    ) -> SiteSeoResponse:
        body = _omit_none(
            {
                "url": url,
            }
        )
        return await self._call("POST", "/v1/site/seo", body)


class AsyncSite:
    seo: AsyncSiteSeo

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.seo = AsyncSiteSeo(call)


class AsyncEmailVerify:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        email: str,
    ) -> EmailVerifyResponse:
        body = _omit_none(
            {
                "email": email,
            }
        )
        return await self._call("POST", "/v1/email/verify", body)


class AsyncEmailFind:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        domain: str,
        name: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
    ) -> EmailFindResponse:
        body = _omit_none(
            {
                "domain": domain,
                "name": name,
                "firstName": first_name,
                "lastName": last_name,
            }
        )
        return await self._call("POST", "/v1/email/find", body)


class AsyncEmail:
    verify: AsyncEmailVerify
    find: AsyncEmailFind

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.verify = AsyncEmailVerify(call)
        self.find = AsyncEmailFind(call)


class AsyncCryptoCoins:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        currency: str | None = None,
        category: str | None = None,
        coins: list[str] | None = None,
        sort: CryptoCoinsSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> CryptoCoinsResponse:
        body = _omit_none(
            {
                "currency": currency,
                "category": category,
                "coins": coins,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/coins", body)


class AsyncCryptoCoin:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        coin: str,
        platform: str | None = None,
        currency: str | None = None,
    ) -> CryptoCoinResponse:
        body = _omit_none(
            {
                "coin": coin,
                "platform": platform,
                "currency": currency,
            }
        )
        return await self._call("POST", "/v1/crypto/coin", body)


class AsyncCryptoHistory:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        coin: str,
        currency: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
    ) -> CryptoHistoryResponse:
        body = _omit_none(
            {
                "coin": coin,
                "currency": currency,
                "from": from_,
                "to": to,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/history", body)


class AsyncCryptoDexSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
    ) -> CryptoDexSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/dex/search", body)


class AsyncCryptoDexToken:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        chain: str | None = None,
        token: str,
    ) -> CryptoDexTokenResponse:
        body = _omit_none(
            {
                "chain": chain,
                "token": token,
            }
        )
        return await self._call("POST", "/v1/crypto/dex/token", body)


class AsyncCryptoDex:
    search: AsyncCryptoDexSearch
    token: AsyncCryptoDexToken

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncCryptoDexSearch(call)
        self.token = AsyncCryptoDexToken(call)


class AsyncCryptoWallet:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        chain: CryptoWalletChain,
        wallet: str,
        cursor: str | None = None,
    ) -> CryptoWalletResponse:
        body = _omit_none(
            {
                "chain": chain,
                "wallet": wallet,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/crypto/wallet", body)


class AsyncCrypto:
    coins: AsyncCryptoCoins
    coin: AsyncCryptoCoin
    history: AsyncCryptoHistory
    dex: AsyncCryptoDex
    wallet: AsyncCryptoWallet

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.coins = AsyncCryptoCoins(call)
        self.coin = AsyncCryptoCoin(call)
        self.history = AsyncCryptoHistory(call)
        self.dex = AsyncCryptoDex(call)
        self.wallet = AsyncCryptoWallet(call)


class AsyncIndeedSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        country: IndeedSearchCountry | None = None,
        remote: bool | None = None,
        within: IndeedSearchWithin | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> IndeedSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "country": country,
                "remote": remote,
                "within": within,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/indeed/search", body)


class AsyncIndeedJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        job: str,
        country: IndeedSearchCountry | None = None,
    ) -> IndeedJobResponse:
        body = _omit_none(
            {
                "job": job,
                "country": country,
            }
        )
        return await self._call("POST", "/v1/indeed/job", body)


class AsyncIndeed:
    search: AsyncIndeedSearch
    job: AsyncIndeedJob

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncIndeedSearch(call)
        self.job = AsyncIndeedJob(call)


class AsyncTripadvisorSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        limit: int | None = None,
    ) -> TripadvisorSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/tripadvisor/search", body)


class AsyncTripadvisorPlace:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        place: str,
    ) -> TripadvisorPlaceResponse:
        body = _omit_none(
            {
                "place": place,
            }
        )
        return await self._call("POST", "/v1/tripadvisor/place", body)


class AsyncTripadvisorReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        place: str,
        language: str | None = None,
        ratings: list[int] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TripadvisorReviewsResponse:
        body = _omit_none(
            {
                "place": place,
                "language": language,
                "ratings": ratings,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/tripadvisor/reviews", body)


class AsyncTripadvisor:
    search: AsyncTripadvisorSearch
    place: AsyncTripadvisorPlace
    reviews: AsyncTripadvisorReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncTripadvisorSearch(call)
        self.place = AsyncTripadvisorPlace(call)
        self.reviews = AsyncTripadvisorReviews(call)


class AsyncGoogletravelFlights:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        adults: int | None = None,
        cabin: GoogletravelFlightsCabin | None = None,
        limit: int | None = None,
    ) -> GoogletravelFlightsResponse:
        body = _omit_none(
            {
                "origin": origin,
                "destination": destination,
                "departDate": depart_date,
                "returnDate": return_date,
                "adults": adults,
                "cabin": cabin,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/googletravel/flights", body)


class AsyncGoogletravel:
    flights: AsyncGoogletravelFlights

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.flights = AsyncGoogletravelFlights(call)


class AsyncAmazonSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        category: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort: AmazonSearchSort | None = None,
        country: AmazonSearchCountry | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AmazonSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "category": category,
                "minPrice": min_price,
                "maxPrice": max_price,
                "sort": sort,
                "country": country,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/amazon/search", body)


class AsyncAmazonProduct:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        product: str,
        country: AmazonSearchCountry | None = None,
    ) -> AmazonProductResponse:
        body = _omit_none(
            {
                "product": product,
                "country": country,
            }
        )
        return await self._call("POST", "/v1/amazon/product", body)


class AsyncAmazonBestsellers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        category: str,
        country: AmazonSearchCountry | None = None,
        cursor: Literal["2"] | None = None,
        limit: int | None = None,
    ) -> AmazonBestsellersResponse:
        body = _omit_none(
            {
                "category": category,
                "country": country,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/amazon/bestsellers", body)


class AsyncAmazon:
    search: AsyncAmazonSearch
    product: AsyncAmazonProduct
    bestsellers: AsyncAmazonBestsellers

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncAmazonSearch(call)
        self.product = AsyncAmazonProduct(call)
        self.bestsellers = AsyncAmazonBestsellers(call)


class AsyncShopifyProducts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        store: str,
        collection: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ShopifyProductsResponse:
        body = _omit_none(
            {
                "store": store,
                "collection": collection,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/shopify/products", body)


class AsyncShopifyCollections:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        store: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ShopifyCollectionsResponse:
        body = _omit_none(
            {
                "store": store,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/shopify/collections", body)


class AsyncShopifyStore:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        store: str,
    ) -> ShopifyStoreResponse:
        body = _omit_none(
            {
                "store": store,
            }
        )
        return await self._call("POST", "/v1/shopify/store", body)


class AsyncShopify:
    products: AsyncShopifyProducts
    collections: AsyncShopifyCollections
    store: AsyncShopifyStore

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.products = AsyncShopifyProducts(call)
        self.collections = AsyncShopifyCollections(call)
        self.store = AsyncShopifyStore(call)


class AsyncWalmartSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        sort: WalmartSearchSort | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> WalmartSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "minPrice": min_price,
                "maxPrice": max_price,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/walmart/search", body)


class AsyncWalmartProduct:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        product: str,
    ) -> WalmartProductResponse:
        body = _omit_none(
            {
                "product": product,
            }
        )
        return await self._call("POST", "/v1/walmart/product", body)


class AsyncWalmart:
    search: AsyncWalmartSearch
    product: AsyncWalmartProduct

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncWalmartSearch(call)
        self.product = AsyncWalmartProduct(call)


class AsyncAliexpressSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        sort: AliexpressSearchSort | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AliexpressSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "minPrice": min_price,
                "maxPrice": max_price,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/aliexpress/search", body)


class AsyncAliexpressProduct:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        product: str,
    ) -> AliexpressProductResponse:
        body = _omit_none(
            {
                "product": product,
            }
        )
        return await self._call("POST", "/v1/aliexpress/product", body)


class AsyncAliexpress:
    search: AsyncAliexpressSearch
    product: AsyncAliexpressProduct

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncAliexpressSearch(call)
        self.product = AsyncAliexpressProduct(call)


class AsyncAppstoreApp:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
    ) -> AppstoreAppResponse:
        body = _omit_none(
            {
                "app": app,
                "country": country,
            }
        )
        return await self._call("POST", "/v1/appstore/app", body)


class AsyncAppstoreSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        device: AppstoreSearchDevice | None = None,
        limit: int | None = None,
    ) -> AppstoreSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "device": device,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/appstore/search", body)


class AsyncAppstoreReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AppstoreReviewsResponse:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/appstore/reviews", body)


class AsyncAppstoreTop:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        chart: AppstoreTopChart | None = None,
        device: AppstoreSearchDevice | None = None,
        genre: AppstoreTopGenre | None = None,
        country: str | None = None,
        limit: int | None = None,
    ) -> AppstoreTopResponse:
        body = _omit_none(
            {
                "chart": chart,
                "device": device,
                "genre": genre,
                "country": country,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/appstore/top", body)


class AsyncAppstore:
    app: AsyncAppstoreApp
    search: AsyncAppstoreSearch
    reviews: AsyncAppstoreReviews
    top: AsyncAppstoreTop

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.app = AsyncAppstoreApp(call)
        self.search = AsyncAppstoreSearch(call)
        self.reviews = AsyncAppstoreReviews(call)
        self.top = AsyncAppstoreTop(call)


class AsyncGoogleplayApp:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
    ) -> GoogleplayAppResponse:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/googleplay/app", body)


class AsyncGoogleplaySearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
    ) -> GoogleplaySearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/googleplay/search", body)


class AsyncGoogleplayReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        sort: GoogleplayReviewsSort | None = None,
        rating: int | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> GoogleplayReviewsResponse:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "language": language,
                "sort": sort,
                "rating": rating,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/googleplay/reviews", body)


class AsyncGoogleplay:
    app: AsyncGoogleplayApp
    search: AsyncGoogleplaySearch
    reviews: AsyncGoogleplayReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.app = AsyncGoogleplayApp(call)
        self.search = AsyncGoogleplaySearch(call)
        self.reviews = AsyncGoogleplayReviews(call)


class AsyncAirbnbSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        location: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AirbnbSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "checkIn": check_in,
                "checkOut": check_out,
                "adults": adults,
                "minPrice": min_price,
                "maxPrice": max_price,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/airbnb/search", body)


class AsyncAirbnbListing:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        listing: str,
    ) -> AirbnbListingResponse:
        body = _omit_none(
            {
                "listing": listing,
            }
        )
        return await self._call("POST", "/v1/airbnb/listing", body)


class AsyncAirbnbCalendar:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        listing: str,
        month: str | None = None,
        limit: int | None = None,
    ) -> AirbnbCalendarResponse:
        body = _omit_none(
            {
                "listing": listing,
                "month": month,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/airbnb/calendar", body)


class AsyncAirbnbReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        listing: str,
        sort: MapsReviewsSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> AirbnbReviewsResponse:
        body = _omit_none(
            {
                "listing": listing,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/airbnb/reviews", body)


class AsyncAirbnb:
    search: AsyncAirbnbSearch
    listing: AsyncAirbnbListing
    calendar: AsyncAirbnbCalendar
    reviews: AsyncAirbnbReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncAirbnbSearch(call)
        self.listing = AsyncAirbnbListing(call)
        self.calendar = AsyncAirbnbCalendar(call)
        self.reviews = AsyncAirbnbReviews(call)


class AsyncRightmoveSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        location: str,
        status: RightmoveSearchStatus | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_bedrooms: int | None = None,
        max_bedrooms: int | None = None,
        sort: RightmoveSearchSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> RightmoveSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minBedrooms": min_bedrooms,
                "maxBedrooms": max_bedrooms,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/rightmove/search", body)


class AsyncRightmoveProperty:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        property: str,
    ) -> RightmovePropertyResponse:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return await self._call("POST", "/v1/rightmove/property", body)


class AsyncRightmove:
    search: AsyncRightmoveSearch
    property: AsyncRightmoveProperty

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncRightmoveSearch(call)
        self.property = AsyncRightmoveProperty(call)


class AsyncImmoscoutSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        location: str,
        type: ImmoscoutSearchType | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_rooms: float | None = None,
        sort: ImmoscoutSearchSort | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ImmoscoutSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "type": type,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minRooms": min_rooms,
                "sort": sort,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/immoscout/search", body)


class AsyncImmoscoutListing:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        listing: str,
    ) -> ImmoscoutListingResponse:
        body = _omit_none(
            {
                "listing": listing,
            }
        )
        return await self._call("POST", "/v1/immoscout/listing", body)


class AsyncImmoscout:
    search: AsyncImmoscoutSearch
    listing: AsyncImmoscoutListing

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncImmoscoutSearch(call)
        self.listing = AsyncImmoscoutListing(call)


class AsyncPinterestSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> PinterestSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/pinterest/search", body)


class AsyncPinterestPin:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        pin: str,
    ) -> PinterestPinResponse:
        body = _omit_none(
            {
                "pin": pin,
            }
        )
        return await self._call("POST", "/v1/pinterest/pin", body)


class AsyncPinterestBoard:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        board: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> PinterestBoardResponse:
        body = _omit_none(
            {
                "board": board,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/pinterest/board", body)


class AsyncPinterestUser:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> PinterestUserResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/pinterest/user", body)


class AsyncPinterest:
    search: AsyncPinterestSearch
    pin: AsyncPinterestPin
    board: AsyncPinterestBoard
    user: AsyncPinterestUser

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncPinterestSearch(call)
        self.pin = AsyncPinterestPin(call)
        self.board = AsyncPinterestBoard(call)
        self.user = AsyncPinterestUser(call)


class AsyncXPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post: str,
    ) -> XPostResponse:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return await self._call("POST", "/v1/x/post", body)


class AsyncX:
    post: AsyncXPost

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.post = AsyncXPost(call)


class AsyncFinanceQuote:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        symbols: list[str],
        limit: int | None = None,
    ) -> FinanceQuoteResponse:
        body = _omit_none(
            {
                "symbols": symbols,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/finance/quote", body)


class AsyncFinanceHistory:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        symbol: str,
        from_: str | None = None,
        to: str | None = None,
        interval: FinanceHistoryInterval | None = None,
        limit: int | None = None,
    ) -> FinanceHistoryResponse:
        body = _omit_none(
            {
                "symbol": symbol,
                "from": from_,
                "to": to,
                "interval": interval,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/finance/history", body)


class AsyncFinanceSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
    ) -> FinanceSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/finance/search", body)


class AsyncFinanceStock:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        symbol: str,
    ) -> FinanceStockResponse:
        body = _omit_none(
            {
                "symbol": symbol,
            }
        )
        return await self._call("POST", "/v1/finance/stock", body)


class AsyncFinance:
    quote: AsyncFinanceQuote
    history: AsyncFinanceHistory
    search: AsyncFinanceSearch
    stock: AsyncFinanceStock

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.quote = AsyncFinanceQuote(call)
        self.history = AsyncFinanceHistory(call)
        self.search = AsyncFinanceSearch(call)
        self.stock = AsyncFinanceStock(call)


class AsyncAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        cursor: str | None = None,
        network: Literal["meta"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    async def __call__(
        self,
        *,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: AdsSearchOption1MediaType | None = None,
        cursor: str | None = None,
        network: Literal["google"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        cursor: str | None = None,
        network: Literal["tiktok"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        within: AdsSearchOption3Within | None = None,
        cursor: str | None = None,
        network: Literal["linkedin"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        cursor: str | None = None,
        network: Literal["microsoft"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    async def __call__(
        self,
        *,
        country: str,
        advertiser: str | None = None,
        cursor: str | None = None,
        network: Literal["pinterest"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        cursor: str | None = None,
        network: Literal["meta"]
        | Literal["google"]
        | Literal["tiktok"]
        | Literal["linkedin"]
        | Literal["microsoft"]
        | Literal["pinterest"]
        | None = None,
        limit: int | None = None,
        advertiser: str | None = None,
        domain: str | None = None,
        media_type: AdsSearchOption1MediaType | None = None,
        within: AdsSearchOption3Within | None = None,
    ) -> AdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "status": status,
                "cursor": cursor,
                "network": network,
                "limit": limit,
                "advertiser": advertiser,
                "domain": domain,
                "mediaType": media_type,
                "within": within,
            }
        )
        return await self._call("POST", "/v1/ads/search", body)


class AsyncAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    async def __call__(
        self,
        *,
        ad: str,
        network: Literal["meta"],
    ) -> AdsAdResponse: ...
    @overload
    async def __call__(
        self,
        *,
        advertiser: str | None = None,
        ad: str,
        network: Literal["google"],
    ) -> AdsAdResponse: ...
    @overload
    async def __call__(
        self,
        *,
        ad: str,
        network: Literal["tiktok"],
    ) -> AdsAdResponse: ...
    @overload
    async def __call__(
        self,
        *,
        ad: str,
        network: Literal["linkedin"],
    ) -> AdsAdResponse: ...
    @overload
    async def __call__(
        self,
        *,
        ad: str,
        network: Literal["microsoft"],
    ) -> AdsAdResponse: ...
    @overload
    async def __call__(
        self,
        *,
        ad: str,
        network: Literal["pinterest"],
    ) -> AdsAdResponse: ...
    async def __call__(
        self,
        *,
        ad: str | None = None,
        network: Literal["meta"]
        | Literal["google"]
        | Literal["tiktok"]
        | Literal["linkedin"]
        | Literal["microsoft"]
        | Literal["pinterest"]
        | None = None,
        advertiser: str | None = None,
    ) -> AdsAdResponse:
        body = _omit_none(
            {
                "ad": ad,
                "network": network,
                "advertiser": advertiser,
            }
        )
        return await self._call("POST", "/v1/ads/ad", body)


class AsyncAdsAdvertisers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        network: Literal["google"],
        limit: int | None = None,
    ) -> AdsAdvertisersResponse: ...
    @overload
    async def __call__(
        self,
        *,
        query: str,
        network: Literal["microsoft"],
        limit: int | None = None,
    ) -> AdsAdvertisersResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        country: str | None = None,
        network: Literal["google"] | Literal["microsoft"] | None = None,
        limit: int | None = None,
    ) -> AdsAdvertisersResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "network": network,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/ads/advertisers", body)


class AsyncAds:
    search: AsyncAdsSearch
    ad: AsyncAdsAd
    advertisers: AsyncAdsAdvertisers

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncAdsSearch(call)
        self.ad = AsyncAdsAd(call)
        self.advertisers = AsyncAdsAdvertisers(call)


class AsyncSuggest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        source: Literal["google"],
        limit: int | None = None,
    ) -> SuggestResponse: ...
    @overload
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        source: Literal["youtube"],
        limit: int | None = None,
    ) -> SuggestResponse: ...
    @overload
    async def __call__(
        self,
        *,
        query: str,
        country: SuggestOption2Country | None = None,
        source: Literal["amazon"],
        limit: int | None = None,
    ) -> SuggestResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        country: str | SuggestOption2Country | None = None,
        language: str | None = None,
        source: Literal["google"] | Literal["youtube"] | Literal["amazon"] | None = None,
        limit: int | None = None,
    ) -> SuggestResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "source": source,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/suggest", body)


class AsyncSurface:
    endpoints: AsyncEndpoints
    web: AsyncWeb
    youtube: AsyncYoutube
    transcript: AsyncTranscript
    reddit: AsyncReddit
    maps: AsyncMaps
    instagram: AsyncInstagram
    tiktok: AsyncTiktok
    bluesky: AsyncBluesky
    threads: AsyncThreads
    telegram: AsyncTelegram
    meta: AsyncMeta
    linkedin: AsyncLinkedin
    zillow: AsyncZillow
    upwork: AsyncUpwork
    google: AsyncGoogle
    site: AsyncSite
    email: AsyncEmail
    crypto: AsyncCrypto
    indeed: AsyncIndeed
    tripadvisor: AsyncTripadvisor
    googletravel: AsyncGoogletravel
    amazon: AsyncAmazon
    shopify: AsyncShopify
    walmart: AsyncWalmart
    aliexpress: AsyncAliexpress
    appstore: AsyncAppstore
    googleplay: AsyncGoogleplay
    airbnb: AsyncAirbnb
    rightmove: AsyncRightmove
    immoscout: AsyncImmoscout
    pinterest: AsyncPinterest
    x: AsyncX
    finance: AsyncFinance
    ads: AsyncAds
    suggest: AsyncSuggest

    def __init__(self, call: AsyncCall) -> None:
        self.endpoints = AsyncEndpoints(call)
        self.web = AsyncWeb(call)
        self.youtube = AsyncYoutube(call)
        self.transcript = AsyncTranscript(call)
        self.reddit = AsyncReddit(call)
        self.maps = AsyncMaps(call)
        self.instagram = AsyncInstagram(call)
        self.tiktok = AsyncTiktok(call)
        self.bluesky = AsyncBluesky(call)
        self.threads = AsyncThreads(call)
        self.telegram = AsyncTelegram(call)
        self.meta = AsyncMeta(call)
        self.linkedin = AsyncLinkedin(call)
        self.zillow = AsyncZillow(call)
        self.upwork = AsyncUpwork(call)
        self.google = AsyncGoogle(call)
        self.site = AsyncSite(call)
        self.email = AsyncEmail(call)
        self.crypto = AsyncCrypto(call)
        self.indeed = AsyncIndeed(call)
        self.tripadvisor = AsyncTripadvisor(call)
        self.googletravel = AsyncGoogletravel(call)
        self.amazon = AsyncAmazon(call)
        self.shopify = AsyncShopify(call)
        self.walmart = AsyncWalmart(call)
        self.aliexpress = AsyncAliexpress(call)
        self.appstore = AsyncAppstore(call)
        self.googleplay = AsyncGoogleplay(call)
        self.airbnb = AsyncAirbnb(call)
        self.rightmove = AsyncRightmove(call)
        self.immoscout = AsyncImmoscout(call)
        self.pinterest = AsyncPinterest(call)
        self.x = AsyncX(call)
        self.finance = AsyncFinance(call)
        self.ads = AsyncAds(call)
        self.suggest = AsyncSuggest(call)
