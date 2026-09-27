"""Generated from openapi.json by scripts/gen_python.py. Do not edit."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Protocol, overload

from .models import (
    AirbnbCalendarResponse,
    AirbnbListingResponse,
    AirbnbReviewsResponse,
    AirbnbSearchAmenitiesItem,
    AirbnbSearchBathrooms,
    AirbnbSearchBedrooms,
    AirbnbSearchResponse,
    AirbnbSearchRoomType,
    AliexpressProductResponse,
    AliexpressSearchResponse,
    AliexpressSearchSort,
    AmazonBestsellersResponse,
    AmazonProductResponse,
    AmazonSearchCountry,
    AmazonSearchResponse,
    AmazonSearchSort,
    AmazonSuggestCountry,
    AppstoreAppResponse,
    AppstoreReviewsResponse,
    AppstoreReviewsSort,
    AppstoreSearchDevice,
    AppstoreSearchResponse,
    AppstoreTopChart,
    AppstoreTopResponse,
    BlueskyFollowersResponse,
    BlueskyPostResponse,
    BlueskyPostsResponse,
    BlueskyPostsType,
    BlueskyProfileResponse,
    CryptoBinanceAnnouncementsCategory,
    CryptoBinanceAnnouncementsResponse,
    CryptoCategoriesResponse,
    CryptoCategoriesSort,
    CryptoCoinResponse,
    CryptoCoinsOrder,
    CryptoCoinsResponse,
    CryptoCoinsResponseDataCoinsItemSource,
    CryptoCoinsSort,
    CryptoDexNewResponse,
    CryptoDexNewType,
    CryptoDexSearchResponse,
    CryptoDexTokenResponse,
    CryptoHistoryResponse,
    CryptoHistoryWithin,
    CryptoMoversRankUpTo,
    CryptoMoversResponse,
    CryptoMoversWithin,
    CryptoNewResponse,
    CryptoPumpCoinResponse,
    CryptoPumpCoinsResponse,
    CryptoPumpCoinsSort,
    CryptoPumpTradesResponse,
    CryptoTokenHoldersChain,
    CryptoTokenHoldersResponse,
    CryptoTrendingResponse,
    CryptoWalletChain,
    CryptoWalletResponse,
    DomainDnsResponse,
    DomainDnsTypesItem,
    DomainTechResponse,
    DomainWhoisResponse,
    EmailCheckResponse,
    EndpointCatalog,
    FinanceHistoryInterval,
    FinanceHistoryResponse,
    FinanceHistoryWithin,
    FinanceProfileResponse,
    FinanceQuoteResponse,
    FinanceSearchResponse,
    GoogleAdsAdResponse,
    GoogleAdsAdvertisersResponse,
    GoogleAdsSearchMediaType,
    GoogleAdsSearchPlatform,
    GoogleAdsSearchResponse,
    GoogleplayAppResponse,
    GoogleplayReviewsResponse,
    GoogleplayReviewsSort,
    GoogleplaySearchResponse,
    GoogleSuggestExpand,
    GoogleSuggestResponse,
    GoogleSuggestVertical,
    GoogletravelFlightsCabin,
    GoogletravelFlightsResponse,
    GoogleTrendsInterestResponse,
    GoogleTrendsInterestVertical,
    GoogleTrendsRegionsResolution,
    GoogleTrendsRegionsResponse,
    GoogleTrendsRelatedResponse,
    GoogleTrendsTrendingCategory,
    GoogleTrendsTrendingResponse,
    GoogleTrendsTrendingWithin,
    ImmoscoutListingResponse,
    ImmoscoutSearchEquipmentItem,
    ImmoscoutSearchResponse,
    ImmoscoutSearchSort,
    ImmoscoutSearchType,
    IndeedJobResponse,
    IndeedSearchCountry,
    IndeedSearchJobType,
    IndeedSearchResponse,
    IndeedSearchSalary,
    IndeedSearchWithin,
    InstagramCommentsRepliesResponse,
    InstagramCommentsResponse,
    InstagramPostResponse,
    InstagramPostsResponse,
    InstagramPostsType,
    InstagramProfileResponse,
    InstagramSearchResponse,
    InstagramSearchType,
    InstagramTranscriptResponse,
    InstagramUrlResponse,
    KickChannelResponse,
    KickClipsResponse,
    KickVideosResponse,
    LinkedinAdsAdResponse,
    LinkedinAdsSearchResponse,
    LinkedinAdsSearchWithin,
    LinkedinJobsJobResponse,
    LinkedinJobsSearchExperienceItem,
    LinkedinJobsSearchJobTypesItem,
    LinkedinJobsSearchResponse,
    LinkedinJobsSearchSort,
    LinkedinJobsSearchWithin,
    LinkedinJobsSearchWorkplaceItem,
    MapsPlaceResponse,
    MapsReviewsResponse,
    MapsReviewsSort,
    MapsSearchCenter,
    MapsSearchResponse,
    MastodonPostResponse,
    MastodonPostsResponse,
    MastodonProfileResponse,
    MetaAdsAdResponse,
    MetaAdsSearchAdType,
    MetaAdsSearchMediaType,
    MetaAdsSearchPlatformsItem,
    MetaAdsSearchResponse,
    MetaAdsSearchStatus,
    MicrosoftAdsAdResponse,
    MicrosoftAdsAdvertisersResponse,
    MicrosoftAdsSearchResponse,
    PinterestAdsAdResponse,
    PinterestAdsSearchResponse,
    PinterestBoardResponse,
    PinterestPinResponse,
    PinterestSearchResponse,
    PinterestSearchType,
    PinterestUserResponse,
    QuoraQuestionResponse,
    RealtorPropertyResponse,
    RealtorSearchHomeTypesItem,
    RealtorSearchResponse,
    RealtorSearchSort,
    RealtorSearchStatus,
    RedditCommentsMoreResponse,
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
    RedfinPropertyResponse,
    RedfinSearchBathrooms,
    RedfinSearchHomeTypesItem,
    RedfinSearchResponse,
    RedfinSearchSoldWithin,
    RedfinSearchSort,
    RedfinSearchStatus,
    RightmovePropertyResponse,
    RightmoveSearchMustHaveItem,
    RightmoveSearchPropertyTypesItem,
    RightmoveSearchResponse,
    RightmoveSearchSort,
    RightmoveSearchStatus,
    RightmoveSearchWithin,
    ShopifyCollectionsResponse,
    ShopifyProductsResponse,
    ShopifyStoreResponse,
    SiteMapResponse,
    SiteSeoResponse,
    SnapchatAdsAdResponse,
    SnapchatAdsSearchResponse,
    SnapchatAdsSearchStatus,
    SnapchatProfileResponse,
    TelegramChannelResponse,
    TelegramPostResponse,
    TelegramPostsResponse,
    ThreadsPostResponse,
    ThreadsPostsResponse,
    ThreadsProfileResponse,
    ThreadsSearchResponse,
    TiktokAdsAdResponse,
    TiktokAdsSearchResponse,
    TiktokCommentsRepliesResponse,
    TiktokCommentsResponse,
    TiktokPostsResponse,
    TiktokProfileResponse,
    TiktokSearchResponse,
    TiktokSearchType,
    TiktokUrlResponse,
    TiktokVideoResponse,
    TripadvisorPlaceResponse,
    TripadvisorReviewsResponse,
    TripadvisorSearchResponse,
    TripadvisorSearchType,
    TumblrBlogResponse,
    TumblrPostResponse,
    TumblrPostsResponse,
    TumblrPostsType,
    TumblrSearchResponse,
    UpworkJobResponse,
    UpworkSearchClientHiresItem,
    UpworkSearchDurationItem,
    UpworkSearchExperienceItem,
    UpworkSearchHourlyRate,
    UpworkSearchJobType,
    UpworkSearchResponse,
    UpworkSearchSort,
    UpworkSearchWorkloadItem,
    WalmartProductResponse,
    WalmartSearchResponse,
    WalmartSearchSort,
    WebContactsResponse,
    WebNewsResponse,
    WebNewsTopic,
    WebNewsWithin,
    WebSearchResponse,
    WebSearchWithin,
    XTweetResponse,
    YoutubeChannelResponse,
    YoutubeChannelTab,
    YoutubeCommentsRepliesResponse,
    YoutubeCommentsResponse,
    YoutubeCommentsSort,
    YoutubePlaylistResponse,
    YoutubeSearchDuration,
    YoutubeSearchFeaturesItem,
    YoutubeSearchResponse,
    YoutubeSearchSort,
    YoutubeSearchType,
    YoutubeTranscriptResponse,
    YoutubeVideoResponse,
    ZillowPropertyResponse,
    ZillowSearchBounds,
    ZillowSearchFeaturesItem,
    ZillowSearchHoa,
    ZillowSearchHomeTypesItem,
    ZillowSearchListingTypesItem,
    ZillowSearchPrice,
    ZillowSearchResponse,
    ZillowSearchSort,
    ZillowSearchStatus,
    ZillowSearchWithin,
)


class SyncCall(Protocol):
    def __call__(
        self,
        method: str,
        path: str,
        body: Mapping[str, Any] | None,
        format: str | None,
    ) -> Any: ...


class AsyncCall(Protocol):
    async def __call__(
        self,
        method: str,
        path: str,
        body: Mapping[str, Any] | None,
        format: str | None,
    ) -> Any: ...


def _omit_none(values: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in values.items() if value is not None}


class SyncEndpoints:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        format: None = None,
    ) -> EndpointCatalog: ...
    def __call__(
        self,
        *,
        format: Literal["markdown"] | None = None,
    ) -> EndpointCatalog | str:
        body = None
        return self._call("GET", "/v1/endpoints", body, format)


class SyncWebSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebSearchWithin | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebSearchWithin | None = None,
        format: None = None,
    ) -> WebSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebSearchWithin | None = None,
        format: Literal["markdown"] | None = None,
    ) -> WebSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "from": from_,
                "to": to,
                "limit": limit,
                "within": within,
            }
        )
        return self._call("POST", "/v1/web/search", body, format)


class SyncWebNews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        topic: WebNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebNewsWithin | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        topic: WebNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebNewsWithin | None = None,
        format: None = None,
    ) -> WebNewsResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        topic: WebNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebNewsWithin | None = None,
        format: Literal["markdown"] | None = None,
    ) -> WebNewsResponse | str:
        body = _omit_none(
            {
                "query": query,
                "topic": topic,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "from": from_,
                "to": to,
                "limit": limit,
                "within": within,
            }
        )
        return self._call("POST", "/v1/web/news", body, format)


class SyncWebContacts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        max_pages: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        max_pages: int | None = None,
        format: None = None,
    ) -> WebContactsResponse: ...
    def __call__(
        self,
        *,
        url: str,
        max_pages: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> WebContactsResponse | str:
        body = _omit_none(
            {
                "url": url,
                "maxPages": max_pages,
            }
        )
        return self._call("POST", "/v1/web/contacts", body, format)


class SyncWeb:
    search: SyncWebSearch
    news: SyncWebNews
    contacts: SyncWebContacts

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncWebSearch(call)
        self.news = SyncWebNews(call)
        self.contacts = SyncWebContacts(call)


class SyncYoutubeSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        duration: YoutubeSearchDuration | None = None,
        within: WebNewsWithin | None = None,
        sort: YoutubeSearchSort | None = None,
        features: list[YoutubeSearchFeaturesItem] | None = None,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        duration: YoutubeSearchDuration | None = None,
        within: WebNewsWithin | None = None,
        sort: YoutubeSearchSort | None = None,
        features: list[YoutubeSearchFeaturesItem] | None = None,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> YoutubeSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        duration: YoutubeSearchDuration | None = None,
        within: WebNewsWithin | None = None,
        sort: YoutubeSearchSort | None = None,
        features: list[YoutubeSearchFeaturesItem] | None = None,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "duration": duration,
                "within": within,
                "sort": sort,
                "features": features,
                "country": country,
                "language": language,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/search", body, format)


class SyncYoutubeVideo:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        format: None = None,
    ) -> YoutubeVideoResponse: ...
    def __call__(
        self,
        *,
        video: str,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeVideoResponse | str:
        body = _omit_none(
            {
                "video": video,
            }
        )
        return self._call("POST", "/v1/youtube/video", body, format)


class SyncYoutubeTranscript:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: None = None,
    ) -> YoutubeTranscriptResponse: ...
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeTranscriptResponse | str:
        body = _omit_none(
            {
                "video": video,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return self._call("POST", "/v1/youtube/transcript", body, format)


class SyncYoutubeCommentsReplies:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str,
        format: None = None,
    ) -> YoutubeCommentsRepliesResponse: ...
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeCommentsRepliesResponse | str:
        body = _omit_none(
            {
                "video": video,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/comments/replies", body, format)


class SyncYoutubeComments:
    replies: SyncYoutubeCommentsReplies

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.replies = SyncYoutubeCommentsReplies(call)

    @overload
    def __call__(
        self,
        *,
        video: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> YoutubeCommentsResponse: ...
    def __call__(
        self,
        *,
        video: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeCommentsResponse | str:
        body = _omit_none(
            {
                "video": video,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/comments", body, format)


class SyncYoutubeChannel:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        tab: YoutubeChannelTab | None = None,
        query: str | None = None,
        include_about: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        tab: YoutubeChannelTab | None = None,
        query: str | None = None,
        include_about: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> YoutubeChannelResponse: ...
    def __call__(
        self,
        *,
        channel: str,
        tab: YoutubeChannelTab | None = None,
        query: str | None = None,
        include_about: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeChannelResponse | str:
        body = _omit_none(
            {
                "channel": channel,
                "tab": tab,
                "query": query,
                "includeAbout": include_about,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/channel", body, format)


class SyncYoutubePlaylist:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        playlist: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        playlist: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> YoutubePlaylistResponse: ...
    def __call__(
        self,
        *,
        playlist: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubePlaylistResponse | str:
        body = _omit_none(
            {
                "playlist": playlist,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/playlist", body, format)


class SyncYoutubeSuggest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: None = None,
    ) -> GoogleSuggestResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleSuggestResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "expand": expand,
            }
        )
        return self._call("POST", "/v1/youtube/suggest", body, format)


class SyncYoutube:
    search: SyncYoutubeSearch
    video: SyncYoutubeVideo
    transcript: SyncYoutubeTranscript
    comments: SyncYoutubeComments
    channel: SyncYoutubeChannel
    playlist: SyncYoutubePlaylist
    suggest: SyncYoutubeSuggest

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncYoutubeSearch(call)
        self.video = SyncYoutubeVideo(call)
        self.transcript = SyncYoutubeTranscript(call)
        self.comments = SyncYoutubeComments(call)
        self.channel = SyncYoutubeChannel(call)
        self.playlist = SyncYoutubePlaylist(call)
        self.suggest = SyncYoutubeSuggest(call)


class SyncRedditSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: RedditSearchType | None = None,
        subreddit: str | None = None,
        sort: RedditSearchSort | None = None,
        within: WebNewsWithin | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: RedditSearchType | None = None,
        subreddit: str | None = None,
        sort: RedditSearchSort | None = None,
        within: WebNewsWithin | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedditSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        type: RedditSearchType | None = None,
        subreddit: str | None = None,
        sort: RedditSearchSort | None = None,
        within: WebNewsWithin | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "subreddit": subreddit,
                "sort": sort,
                "within": within,
                "includeNsfw": include_nsfw,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/search", body, format)


class SyncRedditPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        sort: RedditPostSort | None = None,
        depth: int | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        sort: RedditPostSort | None = None,
        depth: int | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> RedditPostResponse: ...
    def __call__(
        self,
        *,
        post: str,
        sort: RedditPostSort | None = None,
        depth: int | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditPostResponse | str:
        body = _omit_none(
            {
                "post": post,
                "sort": sort,
                "depth": depth,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/reddit/post", body, format)


class SyncRedditCommentsMore:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        limit: int | None = None,
        cursor: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        limit: int | None = None,
        cursor: str,
        format: None = None,
    ) -> RedditCommentsMoreResponse: ...
    def __call__(
        self,
        *,
        limit: int | None = None,
        cursor: str,
        format: Literal["markdown"] | None = None,
    ) -> RedditCommentsMoreResponse | str:
        body = _omit_none(
            {
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/comments/more", body, format)


class SyncRedditComments:
    more: SyncRedditCommentsMore

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.more = SyncRedditCommentsMore(call)


class SyncRedditSubreddit:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        subreddit: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        subreddit: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedditSubredditResponse: ...
    def __call__(
        self,
        *,
        subreddit: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditSubredditResponse | str:
        body = _omit_none(
            {
                "subreddit": subreddit,
                "sort": sort,
                "within": within,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/subreddit", body, format)


class SyncRedditUser:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedditUserResponse: ...
    def __call__(
        self,
        *,
        user: str,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditUserResponse | str:
        body = _omit_none(
            {
                "user": user,
                "tab": tab,
                "sort": sort,
                "within": within,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/user", body, format)


class SyncRedditDomain:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        domain: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        domain: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedditDomainResponse: ...
    def __call__(
        self,
        *,
        domain: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditDomainResponse | str:
        body = _omit_none(
            {
                "domain": domain,
                "sort": sort,
                "within": within,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/domain", body, format)


class SyncReddit:
    search: SyncRedditSearch
    post: SyncRedditPost
    comments: SyncRedditComments
    subreddit: SyncRedditSubreddit
    user: SyncRedditUser
    domain: SyncRedditDomain

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncRedditSearch(call)
        self.post = SyncRedditPost(call)
        self.comments = SyncRedditComments(call)
        self.subreddit = SyncRedditSubreddit(call)
        self.user = SyncRedditUser(call)
        self.domain = SyncRedditDomain(call)


class SyncMapsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        near: str | None = None,
        center: MapsSearchCenter | None = None,
        radius_km: float | None = None,
        limit: int | None = None,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        near: str | None = None,
        center: MapsSearchCenter | None = None,
        radius_km: float | None = None,
        limit: int | None = None,
        country: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> MapsSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        near: str | None = None,
        center: MapsSearchCenter | None = None,
        radius_km: float | None = None,
        limit: int | None = None,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MapsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "near": near,
                "center": center,
                "radiusKm": radius_km,
                "limit": limit,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/maps/search", body, format)


class SyncMapsPlace:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        place: str,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        place: str,
        country: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> MapsPlaceResponse: ...
    def __call__(
        self,
        *,
        place: str,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MapsPlaceResponse | str:
        body = _omit_none(
            {
                "place": place,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/maps/place", body, format)


class SyncMapsReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        place: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        place: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> MapsReviewsResponse: ...
    def __call__(
        self,
        *,
        place: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MapsReviewsResponse | str:
        body = _omit_none(
            {
                "place": place,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
                "from": from_,
                "language": language,
            }
        )
        return self._call("POST", "/v1/maps/reviews", body, format)


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

    @overload
    def __call__(
        self,
        *,
        user: str,
        include_posts: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        include_posts: bool | None = None,
        format: None = None,
    ) -> InstagramProfileResponse: ...
    def __call__(
        self,
        *,
        user: str,
        include_posts: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
                "includePosts": include_posts,
            }
        )
        return self._call("POST", "/v1/instagram/profile", body, format)


class SyncInstagramPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        type: InstagramPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_views: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        type: InstagramPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_views: bool | None = None,
        format: None = None,
    ) -> InstagramPostsResponse: ...
    def __call__(
        self,
        *,
        user: str,
        type: InstagramPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_views: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "type": type,
                "limit": limit,
                "cursor": cursor,
                "from": from_,
                "to": to,
                "includeViews": include_views,
            }
        )
        return self._call("POST", "/v1/instagram/posts", body, format)


class SyncInstagramPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        include_comments: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        include_comments: bool | None = None,
        format: None = None,
    ) -> InstagramPostResponse: ...
    def __call__(
        self,
        *,
        post: str,
        include_comments: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramPostResponse | str:
        body = _omit_none(
            {
                "post": post,
                "includeComments": include_comments,
            }
        )
        return self._call("POST", "/v1/instagram/post", body, format)


class SyncInstagramUrl:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        format: None = None,
    ) -> InstagramUrlResponse: ...
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"] | None = None,
    ) -> InstagramUrlResponse | str:
        body = _omit_none(
            {
                "url": url,
            }
        )
        return self._call("POST", "/v1/instagram/url", body, format)


class SyncInstagramSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: InstagramSearchType | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: InstagramSearchType | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> InstagramSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        type: InstagramSearchType | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "within": within,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/instagram/search", body, format)


class SyncInstagramTranscript:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> InstagramTranscriptResponse: ...
    def __call__(
        self,
        *,
        post: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramTranscriptResponse | str:
        body = _omit_none(
            {
                "post": post,
                "language": language,
                "includeTimestamps": include_timestamps,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/instagram/transcript", body, format)


class SyncInstagramCommentsReplies:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> InstagramCommentsRepliesResponse: ...
    def __call__(
        self,
        *,
        post: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramCommentsRepliesResponse | str:
        body = _omit_none(
            {
                "post": post,
                "comment": comment,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/instagram/comments/replies", body, format)


class SyncInstagramComments:
    replies: SyncInstagramCommentsReplies

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.replies = SyncInstagramCommentsReplies(call)

    @overload
    def __call__(
        self,
        *,
        post: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> InstagramCommentsResponse: ...
    def __call__(
        self,
        *,
        post: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramCommentsResponse | str:
        body = _omit_none(
            {
                "post": post,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/instagram/comments", body, format)


class SyncInstagram:
    profile: SyncInstagramProfile
    posts: SyncInstagramPosts
    post: SyncInstagramPost
    url: SyncInstagramUrl
    search: SyncInstagramSearch
    transcript: SyncInstagramTranscript
    comments: SyncInstagramComments

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncInstagramProfile(call)
        self.posts = SyncInstagramPosts(call)
        self.post = SyncInstagramPost(call)
        self.url = SyncInstagramUrl(call)
        self.search = SyncInstagramSearch(call)
        self.transcript = SyncInstagramTranscript(call)
        self.comments = SyncInstagramComments(call)


class SyncTiktokProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> TiktokProfileResponse: ...
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> TiktokProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return self._call("POST", "/v1/tiktok/profile", body, format)


class SyncTiktokVideo:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        format: None = None,
    ) -> TiktokVideoResponse: ...
    def __call__(
        self,
        *,
        video: str,
        format: Literal["markdown"] | None = None,
    ) -> TiktokVideoResponse | str:
        body = _omit_none(
            {
                "video": video,
            }
        )
        return self._call("POST", "/v1/tiktok/video", body, format)


class SyncTiktokUrl:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        format: None = None,
    ) -> TiktokUrlResponse: ...
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"] | None = None,
    ) -> TiktokUrlResponse | str:
        body = _omit_none(
            {
                "url": url,
            }
        )
        return self._call("POST", "/v1/tiktok/url", body, format)


class SyncTiktokTranscript:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: None = None,
    ) -> YoutubeTranscriptResponse: ...
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeTranscriptResponse | str:
        body = _omit_none(
            {
                "video": video,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return self._call("POST", "/v1/tiktok/transcript", body, format)


class SyncTiktokPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokPostsResponse: ...
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/posts", body, format)


class SyncTiktokCommentsReplies:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokCommentsRepliesResponse: ...
    def __call__(
        self,
        *,
        video: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokCommentsRepliesResponse | str:
        body = _omit_none(
            {
                "video": video,
                "comment": comment,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/comments/replies", body, format)


class SyncTiktokComments:
    replies: SyncTiktokCommentsReplies

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.replies = SyncTiktokCommentsReplies(call)

    @overload
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokCommentsResponse: ...
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokCommentsResponse | str:
        body = _omit_none(
            {
                "video": video,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/comments", body, format)


class SyncTiktokSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: TiktokSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: TiktokSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        type: TiktokSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/search", body, format)


class SyncTiktokAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokAdsSearchResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokAdsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "country": country,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/ads/search", body, format)


class SyncTiktokAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> TiktokAdsAdResponse: ...
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> TiktokAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return self._call("POST", "/v1/tiktok/ads/ad", body, format)


class SyncTiktokAds:
    search: SyncTiktokAdsSearch
    ad: SyncTiktokAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncTiktokAdsSearch(call)
        self.ad = SyncTiktokAdsAd(call)


class SyncTiktok:
    profile: SyncTiktokProfile
    video: SyncTiktokVideo
    url: SyncTiktokUrl
    transcript: SyncTiktokTranscript
    posts: SyncTiktokPosts
    comments: SyncTiktokComments
    search: SyncTiktokSearch
    ads: SyncTiktokAds

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncTiktokProfile(call)
        self.video = SyncTiktokVideo(call)
        self.url = SyncTiktokUrl(call)
        self.transcript = SyncTiktokTranscript(call)
        self.posts = SyncTiktokPosts(call)
        self.comments = SyncTiktokComments(call)
        self.search = SyncTiktokSearch(call)
        self.ads = SyncTiktokAds(call)


class SyncBlueskyProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> BlueskyProfileResponse: ...
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> BlueskyProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return self._call("POST", "/v1/bluesky/profile", body, format)


class SyncBlueskyPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        type: BlueskyPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        type: BlueskyPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> BlueskyPostsResponse: ...
    def __call__(
        self,
        *,
        user: str,
        type: BlueskyPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> BlueskyPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "type": type,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/bluesky/posts", body, format)


class SyncBlueskyPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        depth: int | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        depth: int | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> BlueskyPostResponse: ...
    def __call__(
        self,
        *,
        post: str,
        depth: int | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> BlueskyPostResponse | str:
        body = _omit_none(
            {
                "post": post,
                "depth": depth,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/bluesky/post", body, format)


class SyncBlueskyFollowers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> BlueskyFollowersResponse: ...
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> BlueskyFollowersResponse | str:
        body = _omit_none(
            {
                "user": user,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/bluesky/followers", body, format)


class SyncBluesky:
    profile: SyncBlueskyProfile
    posts: SyncBlueskyPosts
    post: SyncBlueskyPost
    followers: SyncBlueskyFollowers

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncBlueskyProfile(call)
        self.posts = SyncBlueskyPosts(call)
        self.post = SyncBlueskyPost(call)
        self.followers = SyncBlueskyFollowers(call)


class SyncMastodonProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> MastodonProfileResponse: ...
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> MastodonProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return self._call("POST", "/v1/mastodon/profile", body, format)


class SyncMastodonPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        exclude_replies: bool | None = None,
        exclude_reposts: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        exclude_replies: bool | None = None,
        exclude_reposts: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MastodonPostsResponse: ...
    def __call__(
        self,
        *,
        user: str,
        exclude_replies: bool | None = None,
        exclude_reposts: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MastodonPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "excludeReplies": exclude_replies,
                "excludeReposts": exclude_reposts,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/mastodon/posts", body, format)


class SyncMastodonPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        format: None = None,
    ) -> MastodonPostResponse: ...
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"] | None = None,
    ) -> MastodonPostResponse | str:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return self._call("POST", "/v1/mastodon/post", body, format)


class SyncMastodonHashtag:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        hashtag: str,
        instance: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        hashtag: str,
        instance: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MastodonPostsResponse: ...
    def __call__(
        self,
        *,
        hashtag: str,
        instance: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MastodonPostsResponse | str:
        body = _omit_none(
            {
                "hashtag": hashtag,
                "instance": instance,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/mastodon/hashtag", body, format)


class SyncMastodon:
    profile: SyncMastodonProfile
    posts: SyncMastodonPosts
    post: SyncMastodonPost
    hashtag: SyncMastodonHashtag

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncMastodonProfile(call)
        self.posts = SyncMastodonPosts(call)
        self.post = SyncMastodonPost(call)
        self.hashtag = SyncMastodonHashtag(call)


class SyncThreadsProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> ThreadsProfileResponse: ...
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> ThreadsProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return self._call("POST", "/v1/threads/profile", body, format)


class SyncThreadsPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ThreadsPostsResponse: ...
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ThreadsPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/threads/posts", body, format)


class SyncThreadsPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        cursor: str | None = None,
        format: None = None,
    ) -> ThreadsPostResponse: ...
    def __call__(
        self,
        *,
        post: str,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ThreadsPostResponse | str:
        body = _omit_none(
            {
                "post": post,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/threads/post", body, format)


class SyncThreadsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: None = None,
    ) -> ThreadsSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ThreadsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/threads/search", body, format)


class SyncThreads:
    profile: SyncThreadsProfile
    posts: SyncThreadsPosts
    post: SyncThreadsPost
    search: SyncThreadsSearch

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncThreadsProfile(call)
        self.posts = SyncThreadsPosts(call)
        self.post = SyncThreadsPost(call)
        self.search = SyncThreadsSearch(call)


class SyncTelegramChannel:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        format: None = None,
    ) -> TelegramChannelResponse: ...
    def __call__(
        self,
        *,
        channel: str,
        format: Literal["markdown"] | None = None,
    ) -> TelegramChannelResponse | str:
        body = _omit_none(
            {
                "channel": channel,
            }
        )
        return self._call("POST", "/v1/telegram/channel", body, format)


class SyncTelegramPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TelegramPostsResponse: ...
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TelegramPostsResponse | str:
        body = _omit_none(
            {
                "channel": channel,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/telegram/posts", body, format)


class SyncTelegramPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        format: None = None,
    ) -> TelegramPostResponse: ...
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"] | None = None,
    ) -> TelegramPostResponse | str:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return self._call("POST", "/v1/telegram/post", body, format)


class SyncTelegram:
    channel: SyncTelegramChannel
    posts: SyncTelegramPosts
    post: SyncTelegramPost

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.channel = SyncTelegramChannel(call)
        self.posts = SyncTelegramPosts(call)
        self.post = SyncTelegramPost(call)


class SyncMetaAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MetaAdsSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MetaAdsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "adType": ad_type,
                "status": status,
                "mediaType": media_type,
                "platforms": platforms,
                "from": from_,
                "to": to,
                "language": language,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/meta/ads/search", body, format)


class SyncMetaAdsPage:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MetaAdsSearchResponse: ...
    def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MetaAdsSearchResponse | str:
        body = _omit_none(
            {
                "page": page,
                "country": country,
                "adType": ad_type,
                "status": status,
                "mediaType": media_type,
                "platforms": platforms,
                "from": from_,
                "to": to,
                "language": language,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/meta/ads/page", body, format)


class SyncMetaAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> MetaAdsAdResponse: ...
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> MetaAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return self._call("POST", "/v1/meta/ads/ad", body, format)


class SyncMetaAds:
    search: SyncMetaAdsSearch
    page: SyncMetaAdsPage
    ad: SyncMetaAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncMetaAdsSearch(call)
        self.page = SyncMetaAdsPage(call)
        self.ad = SyncMetaAdsAd(call)


class SyncMeta:
    ads: SyncMetaAds

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.ads = SyncMetaAds(call)


class SyncLinkedinJobsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        geo_id: str | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        job_types: list[LinkedinJobsSearchJobTypesItem] | None = None,
        experience: list[LinkedinJobsSearchExperienceItem] | None = None,
        workplace: list[LinkedinJobsSearchWorkplaceItem] | None = None,
        company_ids: list[str] | None = None,
        easy_apply: bool | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        geo_id: str | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        job_types: list[LinkedinJobsSearchJobTypesItem] | None = None,
        experience: list[LinkedinJobsSearchExperienceItem] | None = None,
        workplace: list[LinkedinJobsSearchWorkplaceItem] | None = None,
        company_ids: list[str] | None = None,
        easy_apply: bool | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> LinkedinJobsSearchResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        geo_id: str | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        job_types: list[LinkedinJobsSearchJobTypesItem] | None = None,
        experience: list[LinkedinJobsSearchExperienceItem] | None = None,
        workplace: list[LinkedinJobsSearchWorkplaceItem] | None = None,
        company_ids: list[str] | None = None,
        easy_apply: bool | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> LinkedinJobsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "geoId": geo_id,
                "within": within,
                "jobTypes": job_types,
                "experience": experience,
                "workplace": workplace,
                "companyIds": company_ids,
                "easyApply": easy_apply,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/linkedin/jobs/search", body, format)


class SyncLinkedinJobsJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        job: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        job: str,
        format: None = None,
    ) -> LinkedinJobsJobResponse: ...
    def __call__(
        self,
        *,
        job: str,
        format: Literal["markdown"] | None = None,
    ) -> LinkedinJobsJobResponse | str:
        body = _omit_none(
            {
                "job": job,
            }
        )
        return self._call("POST", "/v1/linkedin/jobs/job", body, format)


class SyncLinkedinJobs:
    search: SyncLinkedinJobsSearch
    job: SyncLinkedinJobsJob

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncLinkedinJobsSearch(call)
        self.job = SyncLinkedinJobsJob(call)


class SyncLinkedinAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        paid_by: str | None = None,
        countries: list[str] | None = None,
        within: LinkedinAdsSearchWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        paid_by: str | None = None,
        countries: list[str] | None = None,
        within: LinkedinAdsSearchWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> LinkedinAdsSearchResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        paid_by: str | None = None,
        countries: list[str] | None = None,
        within: LinkedinAdsSearchWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> LinkedinAdsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "paidBy": paid_by,
                "countries": countries,
                "within": within,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/linkedin/ads/search", body, format)


class SyncLinkedinAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> LinkedinAdsAdResponse: ...
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> LinkedinAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return self._call("POST", "/v1/linkedin/ads/ad", body, format)


class SyncLinkedinAds:
    search: SyncLinkedinAdsSearch
    ad: SyncLinkedinAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncLinkedinAdsSearch(call)
        self.ad = SyncLinkedinAdsAd(call)


class SyncLinkedin:
    jobs: SyncLinkedinJobs
    ads: SyncLinkedinAds

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.jobs = SyncLinkedinJobs(call)
        self.ads = SyncLinkedinAds(call)


class SyncZillowSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        location: str | None = None,
        bounds: ZillowSearchBounds | None = None,
        status: ZillowSearchStatus | None = None,
        sort: ZillowSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        listing_types: list[ZillowSearchListingTypesItem] | None = None,
        within: ZillowSearchWithin | None = None,
        query: str | None = None,
        features: list[ZillowSearchFeaturesItem] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str | None = None,
        bounds: ZillowSearchBounds | None = None,
        status: ZillowSearchStatus | None = None,
        sort: ZillowSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        listing_types: list[ZillowSearchListingTypesItem] | None = None,
        within: ZillowSearchWithin | None = None,
        query: str | None = None,
        features: list[ZillowSearchFeaturesItem] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ZillowSearchResponse: ...
    def __call__(
        self,
        *,
        location: str | None = None,
        bounds: ZillowSearchBounds | None = None,
        status: ZillowSearchStatus | None = None,
        sort: ZillowSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        listing_types: list[ZillowSearchListingTypesItem] | None = None,
        within: ZillowSearchWithin | None = None,
        query: str | None = None,
        features: list[ZillowSearchFeaturesItem] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ZillowSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "bounds": bounds,
                "status": status,
                "sort": sort,
                "price": price,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "sqft": sqft,
                "lotSqft": lot_sqft,
                "yearBuilt": year_built,
                "hoa": hoa,
                "homeTypes": home_types,
                "listingTypes": listing_types,
                "within": within,
                "query": query,
                "features": features,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/zillow/search", body, format)


class SyncZillowProperty:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        property: str,
        format: None = None,
    ) -> ZillowPropertyResponse: ...
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"] | None = None,
    ) -> ZillowPropertyResponse | str:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return self._call("POST", "/v1/zillow/property", body, format)


class SyncZillow:
    search: SyncZillowSearch
    property: SyncZillowProperty

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncZillowSearch(call)
        self.property = SyncZillowProperty(call)


class SyncGoogleAdsAdvertisers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> GoogleAdsAdvertisersResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleAdsAdvertisersResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/google/ads/advertisers", body, format)


class SyncGoogleAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: GoogleAdsSearchMediaType | None = None,
        platform: GoogleAdsSearchPlatform | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: GoogleAdsSearchMediaType | None = None,
        platform: GoogleAdsSearchPlatform | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> GoogleAdsSearchResponse: ...
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: GoogleAdsSearchMediaType | None = None,
        platform: GoogleAdsSearchPlatform | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleAdsSearchResponse | str:
        body = _omit_none(
            {
                "advertiser": advertiser,
                "domain": domain,
                "country": country,
                "mediaType": media_type,
                "platform": platform,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/google/ads/search", body, format)


class SyncGoogleAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        ad: str,
        format: None = None,
    ) -> GoogleAdsAdResponse: ...
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> GoogleAdsAdResponse | str:
        body = _omit_none(
            {
                "advertiser": advertiser,
                "ad": ad,
            }
        )
        return self._call("POST", "/v1/google/ads/ad", body, format)


class SyncGoogleAds:
    advertisers: SyncGoogleAdsAdvertisers
    search: SyncGoogleAdsSearch
    ad: SyncGoogleAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.advertisers = SyncGoogleAdsAdvertisers(call)
        self.search = SyncGoogleAdsSearch(call)
        self.ad = SyncGoogleAdsAd(call)


class SyncGoogleSuggest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        vertical: GoogleSuggestVertical | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        vertical: GoogleSuggestVertical | None = None,
        format: None = None,
    ) -> GoogleSuggestResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        vertical: GoogleSuggestVertical | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleSuggestResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "expand": expand,
                "vertical": vertical,
            }
        )
        return self._call("POST", "/v1/google/suggest", body, format)


class SyncGoogleTrendsInterest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: None = None,
    ) -> GoogleTrendsInterestResponse: ...
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleTrendsInterestResponse | str:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "subdivision": subdivision,
                "within": within,
                "from": from_,
                "to": to,
                "category": category,
                "vertical": vertical,
                "language": language,
            }
        )
        return self._call("POST", "/v1/google/trends/interest", body, format)


class SyncGoogleTrendsRegions:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        resolution: GoogleTrendsRegionsResolution | None = None,
        include_low_volume: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        resolution: GoogleTrendsRegionsResolution | None = None,
        include_low_volume: bool | None = None,
        format: None = None,
    ) -> GoogleTrendsRegionsResponse: ...
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        resolution: GoogleTrendsRegionsResolution | None = None,
        include_low_volume: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleTrendsRegionsResponse | str:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "subdivision": subdivision,
                "within": within,
                "from": from_,
                "to": to,
                "category": category,
                "vertical": vertical,
                "language": language,
                "resolution": resolution,
                "includeLowVolume": include_low_volume,
            }
        )
        return self._call("POST", "/v1/google/trends/regions", body, format)


class SyncGoogleTrendsRelated:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: None = None,
    ) -> GoogleTrendsRelatedResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleTrendsRelatedResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "subdivision": subdivision,
                "within": within,
                "from": from_,
                "to": to,
                "category": category,
                "vertical": vertical,
                "language": language,
            }
        )
        return self._call("POST", "/v1/google/trends/related", body, format)


class SyncGoogleTrendsTrending:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        country: str | None = None,
        subdivision: str | None = None,
        within: GoogleTrendsTrendingWithin | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        active: bool | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        country: str | None = None,
        subdivision: str | None = None,
        within: GoogleTrendsTrendingWithin | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        active: bool | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> GoogleTrendsTrendingResponse: ...
    def __call__(
        self,
        *,
        country: str | None = None,
        subdivision: str | None = None,
        within: GoogleTrendsTrendingWithin | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        active: bool | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleTrendsTrendingResponse | str:
        body = _omit_none(
            {
                "country": country,
                "subdivision": subdivision,
                "within": within,
                "category": category,
                "active": active,
                "language": language,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/google/trends/trending", body, format)


class SyncGoogleTrends:
    interest: SyncGoogleTrendsInterest
    regions: SyncGoogleTrendsRegions
    related: SyncGoogleTrendsRelated
    trending: SyncGoogleTrendsTrending

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.interest = SyncGoogleTrendsInterest(call)
        self.regions = SyncGoogleTrendsRegions(call)
        self.related = SyncGoogleTrendsRelated(call)
        self.trending = SyncGoogleTrendsTrending(call)


class SyncGoogle:
    ads: SyncGoogleAds
    suggest: SyncGoogleSuggest
    trends: SyncGoogleTrends

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.ads = SyncGoogleAds(call)
        self.suggest = SyncGoogleSuggest(call)
        self.trends = SyncGoogleTrends(call)


class SyncUpworkSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        sort: UpworkSearchSort | None = None,
        job_type: UpworkSearchJobType | None = None,
        experience: list[UpworkSearchExperienceItem] | None = None,
        duration: list[UpworkSearchDurationItem] | None = None,
        workload: list[UpworkSearchWorkloadItem] | None = None,
        client_hires: list[UpworkSearchClientHiresItem] | None = None,
        hourly_rate: UpworkSearchHourlyRate | None = None,
        contract_to_hire: bool | None = None,
        locations: list[str] | None = None,
        timezones: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        sort: UpworkSearchSort | None = None,
        job_type: UpworkSearchJobType | None = None,
        experience: list[UpworkSearchExperienceItem] | None = None,
        duration: list[UpworkSearchDurationItem] | None = None,
        workload: list[UpworkSearchWorkloadItem] | None = None,
        client_hires: list[UpworkSearchClientHiresItem] | None = None,
        hourly_rate: UpworkSearchHourlyRate | None = None,
        contract_to_hire: bool | None = None,
        locations: list[str] | None = None,
        timezones: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> UpworkSearchResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        sort: UpworkSearchSort | None = None,
        job_type: UpworkSearchJobType | None = None,
        experience: list[UpworkSearchExperienceItem] | None = None,
        duration: list[UpworkSearchDurationItem] | None = None,
        workload: list[UpworkSearchWorkloadItem] | None = None,
        client_hires: list[UpworkSearchClientHiresItem] | None = None,
        hourly_rate: UpworkSearchHourlyRate | None = None,
        contract_to_hire: bool | None = None,
        locations: list[str] | None = None,
        timezones: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> UpworkSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "jobType": job_type,
                "experience": experience,
                "duration": duration,
                "workload": workload,
                "clientHires": client_hires,
                "hourlyRate": hourly_rate,
                "contractToHire": contract_to_hire,
                "locations": locations,
                "timezones": timezones,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/upwork/search", body, format)


class SyncUpworkJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        job: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        job: str,
        format: None = None,
    ) -> UpworkJobResponse: ...
    def __call__(
        self,
        *,
        job: str,
        format: Literal["markdown"] | None = None,
    ) -> UpworkJobResponse | str:
        body = _omit_none(
            {
                "job": job,
            }
        )
        return self._call("POST", "/v1/upwork/job", body, format)


class SyncUpwork:
    search: SyncUpworkSearch
    job: SyncUpworkJob

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncUpworkSearch(call)
        self.job = SyncUpworkJob(call)


class SyncAmazonSuggest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: AmazonSuggestCountry | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: AmazonSuggestCountry | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: None = None,
    ) -> GoogleSuggestResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: AmazonSuggestCountry | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleSuggestResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "expand": expand,
            }
        )
        return self._call("POST", "/v1/amazon/suggest", body, format)


class SyncAmazonSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        category: str | None = None,
        price: ZillowSearchPrice | None = None,
        sort: AmazonSearchSort | None = None,
        prime: bool | None = None,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        category: str | None = None,
        price: ZillowSearchPrice | None = None,
        sort: AmazonSearchSort | None = None,
        prime: bool | None = None,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AmazonSearchResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        category: str | None = None,
        price: ZillowSearchPrice | None = None,
        sort: AmazonSearchSort | None = None,
        prime: bool | None = None,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AmazonSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "category": category,
                "price": price,
                "sort": sort,
                "prime": prime,
                "country": country,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/amazon/search", body, format)


class SyncAmazonProduct:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        product: str,
        country: AmazonSearchCountry | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        product: str,
        country: AmazonSearchCountry | None = None,
        format: None = None,
    ) -> AmazonProductResponse: ...
    def __call__(
        self,
        *,
        product: str,
        country: AmazonSearchCountry | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AmazonProductResponse | str:
        body = _omit_none(
            {
                "product": product,
                "country": country,
            }
        )
        return self._call("POST", "/v1/amazon/product", body, format)


class SyncAmazonBestsellers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        category: str,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        category: str,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AmazonBestsellersResponse: ...
    def __call__(
        self,
        *,
        category: str,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AmazonBestsellersResponse | str:
        body = _omit_none(
            {
                "category": category,
                "country": country,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/amazon/bestsellers", body, format)


class SyncAmazon:
    suggest: SyncAmazonSuggest
    search: SyncAmazonSearch
    product: SyncAmazonProduct
    bestsellers: SyncAmazonBestsellers

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.suggest = SyncAmazonSuggest(call)
        self.search = SyncAmazonSearch(call)
        self.product = SyncAmazonProduct(call)
        self.bestsellers = SyncAmazonBestsellers(call)


class SyncSiteMap:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> SiteMapResponse: ...
    def __call__(
        self,
        *,
        url: str,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> SiteMapResponse | str:
        body = _omit_none(
            {
                "url": url,
                "include": include,
                "exclude": exclude,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/site/map", body, format)


class SyncSiteSeo:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        check_links: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        check_links: int | None = None,
        format: None = None,
    ) -> SiteSeoResponse: ...
    def __call__(
        self,
        *,
        url: str,
        check_links: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> SiteSeoResponse | str:
        body = _omit_none(
            {
                "url": url,
                "checkLinks": check_links,
            }
        )
        return self._call("POST", "/v1/site/seo", body, format)


class SyncSite:
    map: SyncSiteMap
    seo: SyncSiteSeo

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.map = SyncSiteMap(call)
        self.seo = SyncSiteSeo(call)


class SyncDomainWhois:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        domain: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        domain: str,
        format: None = None,
    ) -> DomainWhoisResponse: ...
    def __call__(
        self,
        *,
        domain: str,
        format: Literal["markdown"] | None = None,
    ) -> DomainWhoisResponse | str:
        body = _omit_none(
            {
                "domain": domain,
            }
        )
        return self._call("POST", "/v1/domain/whois", body, format)


class SyncDomainDns:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        domain: str,
        types: list[DomainDnsTypesItem] | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        domain: str,
        types: list[DomainDnsTypesItem] | None = None,
        format: None = None,
    ) -> DomainDnsResponse: ...
    def __call__(
        self,
        *,
        domain: str,
        types: list[DomainDnsTypesItem] | None = None,
        format: Literal["markdown"] | None = None,
    ) -> DomainDnsResponse | str:
        body = _omit_none(
            {
                "domain": domain,
                "types": types,
            }
        )
        return self._call("POST", "/v1/domain/dns", body, format)


class SyncDomainTech:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        format: None = None,
    ) -> DomainTechResponse: ...
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"] | None = None,
    ) -> DomainTechResponse | str:
        body = _omit_none(
            {
                "url": url,
            }
        )
        return self._call("POST", "/v1/domain/tech", body, format)


class SyncDomain:
    whois: SyncDomainWhois
    dns: SyncDomainDns
    tech: SyncDomainTech

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.whois = SyncDomainWhois(call)
        self.dns = SyncDomainDns(call)
        self.tech = SyncDomainTech(call)


class SyncEmailCheck:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        emails: list[str],
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        emails: list[str],
        format: None = None,
    ) -> EmailCheckResponse: ...
    def __call__(
        self,
        *,
        emails: list[str],
        format: Literal["markdown"] | None = None,
    ) -> EmailCheckResponse | str:
        body = _omit_none(
            {
                "emails": emails,
            }
        )
        return self._call("POST", "/v1/email/check", body, format)


class SyncEmail:
    check: SyncEmailCheck

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.check = SyncEmailCheck(call)


class SyncCryptoCoins:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        currency: str | None = None,
        category: str | None = None,
        coins: list[str] | None = None,
        sort: CryptoCoinsSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        currency: str | None = None,
        category: str | None = None,
        coins: list[str] | None = None,
        sort: CryptoCoinsSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoCoinsResponse: ...
    def __call__(
        self,
        *,
        currency: str | None = None,
        category: str | None = None,
        coins: list[str] | None = None,
        sort: CryptoCoinsSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoCoinsResponse | str:
        body = _omit_none(
            {
                "currency": currency,
                "category": category,
                "coins": coins,
                "sort": sort,
                "order": order,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/crypto/coins", body, format)


class SyncCryptoCoin:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        coin: str,
        source: CryptoCoinsResponseDataCoinsItemSource | None = None,
        platform: str | None = None,
        currency: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        coin: str,
        source: CryptoCoinsResponseDataCoinsItemSource | None = None,
        platform: str | None = None,
        currency: str | None = None,
        format: None = None,
    ) -> CryptoCoinResponse: ...
    def __call__(
        self,
        *,
        coin: str,
        source: CryptoCoinsResponseDataCoinsItemSource | None = None,
        platform: str | None = None,
        currency: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoCoinResponse | str:
        body = _omit_none(
            {
                "coin": coin,
                "source": source,
                "platform": platform,
                "currency": currency,
            }
        )
        return self._call("POST", "/v1/crypto/coin", body, format)


class SyncCryptoHistory:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        coin: str,
        currency: str | None = None,
        within: CryptoHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_candles: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        coin: str,
        currency: str | None = None,
        within: CryptoHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_candles: bool | None = None,
        format: None = None,
    ) -> CryptoHistoryResponse: ...
    def __call__(
        self,
        *,
        coin: str,
        currency: str | None = None,
        within: CryptoHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_candles: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoHistoryResponse | str:
        body = _omit_none(
            {
                "coin": coin,
                "currency": currency,
                "within": within,
                "from": from_,
                "to": to,
                "includeCandles": include_candles,
            }
        )
        return self._call("POST", "/v1/crypto/history", body, format)


class SyncCryptoTrending:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        format: None = None,
    ) -> CryptoTrendingResponse: ...
    def __call__(
        self,
        *,
        format: Literal["markdown"] | None = None,
    ) -> CryptoTrendingResponse | str:
        body = {}
        return self._call("POST", "/v1/crypto/trending", body, format)


class SyncCryptoCategories:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        sort: CryptoCategoriesSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        sort: CryptoCategoriesSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoCategoriesResponse: ...
    def __call__(
        self,
        *,
        sort: CryptoCategoriesSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoCategoriesResponse | str:
        body = _omit_none(
            {
                "sort": sort,
                "order": order,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/categories", body, format)


class SyncCryptoMovers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        within: CryptoMoversWithin | None = None,
        rank_up_to: CryptoMoversRankUpTo | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        within: CryptoMoversWithin | None = None,
        rank_up_to: CryptoMoversRankUpTo | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoMoversResponse: ...
    def __call__(
        self,
        *,
        within: CryptoMoversWithin | None = None,
        rank_up_to: CryptoMoversRankUpTo | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoMoversResponse | str:
        body = _omit_none(
            {
                "within": within,
                "rankUpTo": rank_up_to,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/movers", body, format)


class SyncCryptoNew:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoNewResponse: ...
    def __call__(
        self,
        *,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoNewResponse | str:
        body = _omit_none(
            {
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/new", body, format)


class SyncCryptoDexSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoDexSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoDexSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/dex/search", body, format)


class SyncCryptoDexPairs:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chain: str | None = None,
        pair: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chain: str | None = None,
        pair: str,
        format: None = None,
    ) -> CryptoDexSearchResponse: ...
    def __call__(
        self,
        *,
        chain: str | None = None,
        pair: str,
        format: Literal["markdown"] | None = None,
    ) -> CryptoDexSearchResponse | str:
        body = _omit_none(
            {
                "chain": chain,
                "pair": pair,
            }
        )
        return self._call("POST", "/v1/crypto/dex/pairs", body, format)


class SyncCryptoDexToken:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chain: str | None = None,
        token: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chain: str | None = None,
        token: str,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoDexTokenResponse: ...
    def __call__(
        self,
        *,
        chain: str | None = None,
        token: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoDexTokenResponse | str:
        body = _omit_none(
            {
                "chain": chain,
                "token": token,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/dex/token", body, format)


class SyncCryptoDexNew:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        type: CryptoDexNewType | None = None,
        chain: str | None = None,
        include_pairs: bool | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        type: CryptoDexNewType | None = None,
        chain: str | None = None,
        include_pairs: bool | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoDexNewResponse: ...
    def __call__(
        self,
        *,
        type: CryptoDexNewType | None = None,
        chain: str | None = None,
        include_pairs: bool | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoDexNewResponse | str:
        body = _omit_none(
            {
                "type": type,
                "chain": chain,
                "includePairs": include_pairs,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/crypto/dex/new", body, format)


class SyncCryptoDex:
    search: SyncCryptoDexSearch
    pairs: SyncCryptoDexPairs
    token: SyncCryptoDexToken
    new: SyncCryptoDexNew

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncCryptoDexSearch(call)
        self.pairs = SyncCryptoDexPairs(call)
        self.token = SyncCryptoDexToken(call)
        self.new = SyncCryptoDexNew(call)


class SyncCryptoPumpCoins:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        sort: CryptoPumpCoinsSort | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        sort: CryptoPumpCoinsSort | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoPumpCoinsResponse: ...
    def __call__(
        self,
        *,
        sort: CryptoPumpCoinsSort | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoPumpCoinsResponse | str:
        body = _omit_none(
            {
                "sort": sort,
                "includeNsfw": include_nsfw,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/crypto/pump/coins", body, format)


class SyncCryptoPumpCoin:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        coin: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        coin: str,
        format: None = None,
    ) -> CryptoPumpCoinResponse: ...
    def __call__(
        self,
        *,
        coin: str,
        format: Literal["markdown"] | None = None,
    ) -> CryptoPumpCoinResponse | str:
        body = _omit_none(
            {
                "coin": coin,
            }
        )
        return self._call("POST", "/v1/crypto/pump/coin", body, format)


class SyncCryptoPumpTrades:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        coin: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        coin: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoPumpTradesResponse: ...
    def __call__(
        self,
        *,
        coin: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoPumpTradesResponse | str:
        body = _omit_none(
            {
                "coin": coin,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/crypto/pump/trades", body, format)


class SyncCryptoPump:
    coins: SyncCryptoPumpCoins
    coin: SyncCryptoPumpCoin
    trades: SyncCryptoPumpTrades

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.coins = SyncCryptoPumpCoins(call)
        self.coin = SyncCryptoPumpCoin(call)
        self.trades = SyncCryptoPumpTrades(call)


class SyncCryptoWallet:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chain: CryptoWalletChain,
        wallet: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chain: CryptoWalletChain,
        wallet: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoWalletResponse: ...
    def __call__(
        self,
        *,
        chain: CryptoWalletChain,
        wallet: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoWalletResponse | str:
        body = _omit_none(
            {
                "chain": chain,
                "wallet": wallet,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/crypto/wallet", body, format)


class SyncCryptoTokenHolders:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chain: CryptoTokenHoldersChain,
        token: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chain: CryptoTokenHoldersChain,
        token: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoTokenHoldersResponse: ...
    def __call__(
        self,
        *,
        chain: CryptoTokenHoldersChain,
        token: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoTokenHoldersResponse | str:
        body = _omit_none(
            {
                "chain": chain,
                "token": token,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/crypto/token/holders", body, format)


class SyncCryptoToken:
    holders: SyncCryptoTokenHolders

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.holders = SyncCryptoTokenHolders(call)


class SyncCryptoBinanceAnnouncements:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        category: CryptoBinanceAnnouncementsCategory | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        category: CryptoBinanceAnnouncementsCategory | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoBinanceAnnouncementsResponse: ...
    def __call__(
        self,
        *,
        category: CryptoBinanceAnnouncementsCategory | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoBinanceAnnouncementsResponse | str:
        body = _omit_none(
            {
                "category": category,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/crypto/binance/announcements", body, format)


class SyncCryptoBinance:
    announcements: SyncCryptoBinanceAnnouncements

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.announcements = SyncCryptoBinanceAnnouncements(call)


class SyncCrypto:
    coins: SyncCryptoCoins
    coin: SyncCryptoCoin
    history: SyncCryptoHistory
    trending: SyncCryptoTrending
    categories: SyncCryptoCategories
    movers: SyncCryptoMovers
    new: SyncCryptoNew
    dex: SyncCryptoDex
    pump: SyncCryptoPump
    wallet: SyncCryptoWallet
    token: SyncCryptoToken
    binance: SyncCryptoBinance

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.coins = SyncCryptoCoins(call)
        self.coin = SyncCryptoCoin(call)
        self.history = SyncCryptoHistory(call)
        self.trending = SyncCryptoTrending(call)
        self.categories = SyncCryptoCategories(call)
        self.movers = SyncCryptoMovers(call)
        self.new = SyncCryptoNew(call)
        self.dex = SyncCryptoDex(call)
        self.pump = SyncCryptoPump(call)
        self.wallet = SyncCryptoWallet(call)
        self.token = SyncCryptoToken(call)
        self.binance = SyncCryptoBinance(call)


class SyncIndeedSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        radius_km: float | None = None,
        country: IndeedSearchCountry | None = None,
        job_type: IndeedSearchJobType | None = None,
        remote: bool | None = None,
        within: IndeedSearchWithin | None = None,
        salary: IndeedSearchSalary | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        radius_km: float | None = None,
        country: IndeedSearchCountry | None = None,
        job_type: IndeedSearchJobType | None = None,
        remote: bool | None = None,
        within: IndeedSearchWithin | None = None,
        salary: IndeedSearchSalary | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> IndeedSearchResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        radius_km: float | None = None,
        country: IndeedSearchCountry | None = None,
        job_type: IndeedSearchJobType | None = None,
        remote: bool | None = None,
        within: IndeedSearchWithin | None = None,
        salary: IndeedSearchSalary | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> IndeedSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "radiusKm": radius_km,
                "country": country,
                "jobType": job_type,
                "remote": remote,
                "within": within,
                "salary": salary,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/indeed/search", body, format)


class SyncIndeedJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        job: str,
        country: IndeedSearchCountry | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        job: str,
        country: IndeedSearchCountry | None = None,
        format: None = None,
    ) -> IndeedJobResponse: ...
    def __call__(
        self,
        *,
        job: str,
        country: IndeedSearchCountry | None = None,
        format: Literal["markdown"] | None = None,
    ) -> IndeedJobResponse | str:
        body = _omit_none(
            {
                "job": job,
                "country": country,
            }
        )
        return self._call("POST", "/v1/indeed/job", body, format)


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

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> TripadvisorSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TripadvisorSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/tripadvisor/search", body, format)


class SyncTripadvisorPlace:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        place: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        place: str,
        format: None = None,
    ) -> TripadvisorPlaceResponse: ...
    def __call__(
        self,
        *,
        place: str,
        format: Literal["markdown"] | None = None,
    ) -> TripadvisorPlaceResponse | str:
        body = _omit_none(
            {
                "place": place,
            }
        )
        return self._call("POST", "/v1/tripadvisor/place", body, format)


class SyncTripadvisorReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        place: str,
        language: str | None = None,
        ratings: list[int] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        place: str,
        language: str | None = None,
        ratings: list[int] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TripadvisorReviewsResponse: ...
    def __call__(
        self,
        *,
        place: str,
        language: str | None = None,
        ratings: list[int] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TripadvisorReviewsResponse | str:
        body = _omit_none(
            {
                "place": place,
                "language": language,
                "ratings": ratings,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tripadvisor/reviews", body, format)


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

    @overload
    def __call__(
        self,
        *,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        cabin: GoogletravelFlightsCabin | None = None,
        max_stops: int | None = None,
        currency: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        cabin: GoogletravelFlightsCabin | None = None,
        max_stops: int | None = None,
        currency: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> GoogletravelFlightsResponse: ...
    def __call__(
        self,
        *,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        cabin: GoogletravelFlightsCabin | None = None,
        max_stops: int | None = None,
        currency: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogletravelFlightsResponse | str:
        body = _omit_none(
            {
                "origin": origin,
                "destination": destination,
                "departDate": depart_date,
                "returnDate": return_date,
                "adults": adults,
                "children": children,
                "cabin": cabin,
                "maxStops": max_stops,
                "currency": currency,
                "language": language,
            }
        )
        return self._call("POST", "/v1/googletravel/flights", body, format)


class SyncGoogletravel:
    flights: SyncGoogletravelFlights

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.flights = SyncGoogletravelFlights(call)


class SyncShopifyProducts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        store: str,
        collection: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        store: str,
        collection: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ShopifyProductsResponse: ...
    def __call__(
        self,
        *,
        store: str,
        collection: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ShopifyProductsResponse | str:
        body = _omit_none(
            {
                "store": store,
                "collection": collection,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/shopify/products", body, format)


class SyncShopifyCollections:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        store: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        store: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ShopifyCollectionsResponse: ...
    def __call__(
        self,
        *,
        store: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ShopifyCollectionsResponse | str:
        body = _omit_none(
            {
                "store": store,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/shopify/collections", body, format)


class SyncShopifyStore:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        store: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        store: str,
        format: None = None,
    ) -> ShopifyStoreResponse: ...
    def __call__(
        self,
        *,
        store: str,
        format: Literal["markdown"] | None = None,
    ) -> ShopifyStoreResponse | str:
        body = _omit_none(
            {
                "store": store,
            }
        )
        return self._call("POST", "/v1/shopify/store", body, format)


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

    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: WalmartSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: WalmartSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> WalmartSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        sort: WalmartSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> WalmartSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "price": price,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/walmart/search", body, format)


class SyncWalmartProduct:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        product: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        product: str,
        format: None = None,
    ) -> WalmartProductResponse: ...
    def __call__(
        self,
        *,
        product: str,
        format: Literal["markdown"] | None = None,
    ) -> WalmartProductResponse | str:
        body = _omit_none(
            {
                "product": product,
            }
        )
        return self._call("POST", "/v1/walmart/product", body, format)


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

    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: AliexpressSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: AliexpressSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AliexpressSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        sort: AliexpressSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AliexpressSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "price": price,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/aliexpress/search", body, format)


class SyncAliexpressProduct:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        product: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        product: str,
        format: None = None,
    ) -> AliexpressProductResponse: ...
    def __call__(
        self,
        *,
        product: str,
        format: Literal["markdown"] | None = None,
    ) -> AliexpressProductResponse | str:
        body = _omit_none(
            {
                "product": product,
            }
        )
        return self._call("POST", "/v1/aliexpress/product", body, format)


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

    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        format: None = None,
    ) -> AppstoreAppResponse: ...
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AppstoreAppResponse | str:
        body = _omit_none(
            {
                "app": app,
                "country": country,
            }
        )
        return self._call("POST", "/v1/appstore/app", body, format)


class SyncAppstoreSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        device: AppstoreSearchDevice | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        device: AppstoreSearchDevice | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> AppstoreSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        device: AppstoreSearchDevice | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AppstoreSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "device": device,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/appstore/search", body, format)


class SyncAppstoreReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AppstoreReviewsResponse: ...
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AppstoreReviewsResponse | str:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/appstore/reviews", body, format)


class SyncAppstoreTop:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chart: AppstoreTopChart | None = None,
        device: AppstoreSearchDevice | None = None,
        genre: int | None = None,
        country: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chart: AppstoreTopChart | None = None,
        device: AppstoreSearchDevice | None = None,
        genre: int | None = None,
        country: str | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> AppstoreTopResponse: ...
    def __call__(
        self,
        *,
        chart: AppstoreTopChart | None = None,
        device: AppstoreSearchDevice | None = None,
        genre: int | None = None,
        country: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AppstoreTopResponse | str:
        body = _omit_none(
            {
                "chart": chart,
                "device": device,
                "genre": genre,
                "country": country,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/appstore/top", body, format)


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

    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> GoogleplayAppResponse: ...
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleplayAppResponse | str:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/googleplay/app", body, format)


class SyncGoogleplaySearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> GoogleplaySearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleplaySearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/googleplay/search", body, format)


class SyncGoogleplayReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        sort: GoogleplayReviewsSort | None = None,
        rating: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        sort: GoogleplayReviewsSort | None = None,
        rating: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> GoogleplayReviewsResponse: ...
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        sort: GoogleplayReviewsSort | None = None,
        rating: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleplayReviewsResponse | str:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "language": language,
                "sort": sort,
                "rating": rating,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/googleplay/reviews", body, format)


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

    @overload
    def __call__(
        self,
        *,
        location: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        infants: int | None = None,
        pets: int | None = None,
        price: ZillowSearchPrice | None = None,
        currency: str | None = None,
        room_type: AirbnbSearchRoomType | None = None,
        bedrooms: AirbnbSearchBedrooms | None = None,
        bathrooms: AirbnbSearchBathrooms | None = None,
        amenities: list[AirbnbSearchAmenitiesItem] | None = None,
        superhost: bool | None = None,
        instant_book: bool | None = None,
        guest_favorite: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        infants: int | None = None,
        pets: int | None = None,
        price: ZillowSearchPrice | None = None,
        currency: str | None = None,
        room_type: AirbnbSearchRoomType | None = None,
        bedrooms: AirbnbSearchBedrooms | None = None,
        bathrooms: AirbnbSearchBathrooms | None = None,
        amenities: list[AirbnbSearchAmenitiesItem] | None = None,
        superhost: bool | None = None,
        instant_book: bool | None = None,
        guest_favorite: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AirbnbSearchResponse: ...
    def __call__(
        self,
        *,
        location: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        infants: int | None = None,
        pets: int | None = None,
        price: ZillowSearchPrice | None = None,
        currency: str | None = None,
        room_type: AirbnbSearchRoomType | None = None,
        bedrooms: AirbnbSearchBedrooms | None = None,
        bathrooms: AirbnbSearchBathrooms | None = None,
        amenities: list[AirbnbSearchAmenitiesItem] | None = None,
        superhost: bool | None = None,
        instant_book: bool | None = None,
        guest_favorite: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AirbnbSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "checkIn": check_in,
                "checkOut": check_out,
                "adults": adults,
                "children": children,
                "infants": infants,
                "pets": pets,
                "price": price,
                "currency": currency,
                "roomType": room_type,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "amenities": amenities,
                "superhost": superhost,
                "instantBook": instant_book,
                "guestFavorite": guest_favorite,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/airbnb/search", body, format)


class SyncAirbnbListing:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        listing: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        listing: str,
        format: None = None,
    ) -> AirbnbListingResponse: ...
    def __call__(
        self,
        *,
        listing: str,
        format: Literal["markdown"] | None = None,
    ) -> AirbnbListingResponse | str:
        body = _omit_none(
            {
                "listing": listing,
            }
        )
        return self._call("POST", "/v1/airbnb/listing", body, format)


class SyncAirbnbCalendar:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        listing: str,
        month: str | None = None,
        months: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        listing: str,
        month: str | None = None,
        months: int | None = None,
        format: None = None,
    ) -> AirbnbCalendarResponse: ...
    def __call__(
        self,
        *,
        listing: str,
        month: str | None = None,
        months: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AirbnbCalendarResponse | str:
        body = _omit_none(
            {
                "listing": listing,
                "month": month,
                "months": months,
            }
        )
        return self._call("POST", "/v1/airbnb/calendar", body, format)


class SyncAirbnbReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        listing: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        listing: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AirbnbReviewsResponse: ...
    def __call__(
        self,
        *,
        listing: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AirbnbReviewsResponse | str:
        body = _omit_none(
            {
                "listing": listing,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/airbnb/reviews", body, format)


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


class SyncRedfinSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RedfinSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RedfinSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: RedfinSearchBathrooms | None = None,
        home_types: list[RedfinSearchHomeTypesItem] | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        days_on_market: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RedfinSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RedfinSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: RedfinSearchBathrooms | None = None,
        home_types: list[RedfinSearchHomeTypesItem] | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        days_on_market: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedfinSearchResponse: ...
    def __call__(
        self,
        *,
        location: str,
        status: RedfinSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RedfinSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: RedfinSearchBathrooms | None = None,
        home_types: list[RedfinSearchHomeTypesItem] | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        days_on_market: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedfinSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "soldWithin": sold_within,
                "sort": sort,
                "price": price,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "homeTypes": home_types,
                "sqft": sqft,
                "lotSqft": lot_sqft,
                "yearBuilt": year_built,
                "daysOnMarket": days_on_market,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/redfin/search", body, format)


class SyncRedfinProperty:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        property: str,
        format: None = None,
    ) -> RedfinPropertyResponse: ...
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"] | None = None,
    ) -> RedfinPropertyResponse | str:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return self._call("POST", "/v1/redfin/property", body, format)


class SyncRedfin:
    search: SyncRedfinSearch
    property: SyncRedfinProperty

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncRedfinSearch(call)
        self.property = SyncRedfinProperty(call)


class SyncRealtorSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RealtorSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RealtorSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[RealtorSearchHomeTypesItem] | None = None,
        new_construction: bool | None = None,
        foreclosure: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RealtorSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RealtorSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[RealtorSearchHomeTypesItem] | None = None,
        new_construction: bool | None = None,
        foreclosure: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RealtorSearchResponse: ...
    def __call__(
        self,
        *,
        location: str,
        status: RealtorSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RealtorSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[RealtorSearchHomeTypesItem] | None = None,
        new_construction: bool | None = None,
        foreclosure: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RealtorSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "soldWithin": sold_within,
                "sort": sort,
                "price": price,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "sqft": sqft,
                "lotSqft": lot_sqft,
                "yearBuilt": year_built,
                "hoa": hoa,
                "homeTypes": home_types,
                "newConstruction": new_construction,
                "foreclosure": foreclosure,
                "queries": queries,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/realtor/search", body, format)


class SyncRealtorProperty:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        property: str,
        format: None = None,
    ) -> RealtorPropertyResponse: ...
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"] | None = None,
    ) -> RealtorPropertyResponse | str:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return self._call("POST", "/v1/realtor/property", body, format)


class SyncRealtor:
    search: SyncRealtorSearch
    property: SyncRealtorProperty

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncRealtorSearch(call)
        self.property = SyncRealtorProperty(call)


class SyncRightmoveSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RightmoveSearchStatus | None = None,
        sort: RightmoveSearchSort | None = None,
        radius_km: float | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        property_types: list[RightmoveSearchPropertyTypesItem] | None = None,
        must_have: list[RightmoveSearchMustHaveItem] | None = None,
        within: RightmoveSearchWithin | None = None,
        include_under_offer: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RightmoveSearchStatus | None = None,
        sort: RightmoveSearchSort | None = None,
        radius_km: float | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        property_types: list[RightmoveSearchPropertyTypesItem] | None = None,
        must_have: list[RightmoveSearchMustHaveItem] | None = None,
        within: RightmoveSearchWithin | None = None,
        include_under_offer: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RightmoveSearchResponse: ...
    def __call__(
        self,
        *,
        location: str,
        status: RightmoveSearchStatus | None = None,
        sort: RightmoveSearchSort | None = None,
        radius_km: float | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        property_types: list[RightmoveSearchPropertyTypesItem] | None = None,
        must_have: list[RightmoveSearchMustHaveItem] | None = None,
        within: RightmoveSearchWithin | None = None,
        include_under_offer: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RightmoveSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "sort": sort,
                "radiusKm": radius_km,
                "price": price,
                "bedrooms": bedrooms,
                "propertyTypes": property_types,
                "mustHave": must_have,
                "within": within,
                "includeUnderOffer": include_under_offer,
                "queries": queries,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/rightmove/search", body, format)


class SyncRightmoveProperty:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        property: str,
        format: None = None,
    ) -> RightmovePropertyResponse: ...
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"] | None = None,
    ) -> RightmovePropertyResponse | str:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return self._call("POST", "/v1/rightmove/property", body, format)


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

    @overload
    def __call__(
        self,
        *,
        location: str,
        type: ImmoscoutSearchType | None = None,
        sort: ImmoscoutSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        rooms: ZillowSearchPrice | None = None,
        living_space: ZillowSearchPrice | None = None,
        equipment: list[ImmoscoutSearchEquipmentItem] | None = None,
        new_construction: bool | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        type: ImmoscoutSearchType | None = None,
        sort: ImmoscoutSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        rooms: ZillowSearchPrice | None = None,
        living_space: ZillowSearchPrice | None = None,
        equipment: list[ImmoscoutSearchEquipmentItem] | None = None,
        new_construction: bool | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ImmoscoutSearchResponse: ...
    def __call__(
        self,
        *,
        location: str,
        type: ImmoscoutSearchType | None = None,
        sort: ImmoscoutSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        rooms: ZillowSearchPrice | None = None,
        living_space: ZillowSearchPrice | None = None,
        equipment: list[ImmoscoutSearchEquipmentItem] | None = None,
        new_construction: bool | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ImmoscoutSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "type": type,
                "sort": sort,
                "price": price,
                "rooms": rooms,
                "livingSpace": living_space,
                "equipment": equipment,
                "newConstruction": new_construction,
                "query": query,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/immoscout/search", body, format)


class SyncImmoscoutListing:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        listing: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        listing: str,
        format: None = None,
    ) -> ImmoscoutListingResponse: ...
    def __call__(
        self,
        *,
        listing: str,
        format: Literal["markdown"] | None = None,
    ) -> ImmoscoutListingResponse | str:
        body = _omit_none(
            {
                "listing": listing,
            }
        )
        return self._call("POST", "/v1/immoscout/listing", body, format)


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

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> PinterestSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> PinterestSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/pinterest/search", body, format)


class SyncPinterestPin:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        pin: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        pin: str,
        format: None = None,
    ) -> PinterestPinResponse: ...
    def __call__(
        self,
        *,
        pin: str,
        format: Literal["markdown"] | None = None,
    ) -> PinterestPinResponse | str:
        body = _omit_none(
            {
                "pin": pin,
            }
        )
        return self._call("POST", "/v1/pinterest/pin", body, format)


class SyncPinterestBoard:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        board: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        board: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> PinterestBoardResponse: ...
    def __call__(
        self,
        *,
        board: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> PinterestBoardResponse | str:
        body = _omit_none(
            {
                "board": board,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/pinterest/board", body, format)


class SyncPinterestUser:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> PinterestUserResponse: ...
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> PinterestUserResponse | str:
        body = _omit_none(
            {
                "user": user,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/pinterest/user", body, format)


class SyncPinterestAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        country: str,
        advertiser: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        country: str,
        advertiser: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> PinterestAdsSearchResponse: ...
    def __call__(
        self,
        *,
        country: str,
        advertiser: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> PinterestAdsSearchResponse | str:
        body = _omit_none(
            {
                "country": country,
                "advertiser": advertiser,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/pinterest/ads/search", body, format)


class SyncPinterestAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> PinterestAdsAdResponse: ...
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> PinterestAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return self._call("POST", "/v1/pinterest/ads/ad", body, format)


class SyncPinterestAds:
    search: SyncPinterestAdsSearch
    ad: SyncPinterestAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncPinterestAdsSearch(call)
        self.ad = SyncPinterestAdsAd(call)


class SyncPinterest:
    search: SyncPinterestSearch
    pin: SyncPinterestPin
    board: SyncPinterestBoard
    user: SyncPinterestUser
    ads: SyncPinterestAds

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncPinterestSearch(call)
        self.pin = SyncPinterestPin(call)
        self.board = SyncPinterestBoard(call)
        self.user = SyncPinterestUser(call)
        self.ads = SyncPinterestAds(call)


class SyncXTweet:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        tweet: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        tweet: str,
        format: None = None,
    ) -> XTweetResponse: ...
    def __call__(
        self,
        *,
        tweet: str,
        format: Literal["markdown"] | None = None,
    ) -> XTweetResponse | str:
        body = _omit_none(
            {
                "tweet": tweet,
            }
        )
        return self._call("POST", "/v1/x/tweet", body, format)


class SyncX:
    tweet: SyncXTweet

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.tweet = SyncXTweet(call)


class SyncKickChannel:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        format: None = None,
    ) -> KickChannelResponse: ...
    def __call__(
        self,
        *,
        channel: str,
        format: Literal["markdown"] | None = None,
    ) -> KickChannelResponse | str:
        body = _omit_none(
            {
                "channel": channel,
            }
        )
        return self._call("POST", "/v1/kick/channel", body, format)


class SyncKickVideos:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        format: None = None,
    ) -> KickVideosResponse: ...
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> KickVideosResponse | str:
        body = _omit_none(
            {
                "channel": channel,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/kick/videos", body, format)


class SyncKickClips:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        sort: YoutubeCommentsSort | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        sort: YoutubeCommentsSort | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> KickClipsResponse: ...
    def __call__(
        self,
        *,
        channel: str,
        sort: YoutubeCommentsSort | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> KickClipsResponse | str:
        body = _omit_none(
            {
                "channel": channel,
                "sort": sort,
                "within": within,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/kick/clips", body, format)


class SyncKick:
    channel: SyncKickChannel
    videos: SyncKickVideos
    clips: SyncKickClips

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.channel = SyncKickChannel(call)
        self.videos = SyncKickVideos(call)
        self.clips = SyncKickClips(call)


class SyncFinanceQuote:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        symbols: list[str],
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        symbols: list[str],
        format: None = None,
    ) -> FinanceQuoteResponse: ...
    def __call__(
        self,
        *,
        symbols: list[str],
        format: Literal["markdown"] | None = None,
    ) -> FinanceQuoteResponse | str:
        body = _omit_none(
            {
                "symbols": symbols,
            }
        )
        return self._call("POST", "/v1/finance/quote", body, format)


class SyncFinanceHistory:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        symbol: str,
        within: FinanceHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        interval: FinanceHistoryInterval | None = None,
        include_extended_hours: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        symbol: str,
        within: FinanceHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        interval: FinanceHistoryInterval | None = None,
        include_extended_hours: bool | None = None,
        format: None = None,
    ) -> FinanceHistoryResponse: ...
    def __call__(
        self,
        *,
        symbol: str,
        within: FinanceHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        interval: FinanceHistoryInterval | None = None,
        include_extended_hours: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> FinanceHistoryResponse | str:
        body = _omit_none(
            {
                "symbol": symbol,
                "within": within,
                "from": from_,
                "to": to,
                "interval": interval,
                "includeExtendedHours": include_extended_hours,
            }
        )
        return self._call("POST", "/v1/finance/history", body, format)


class SyncFinanceSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        quotes_limit: int | None = None,
        news_limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        quotes_limit: int | None = None,
        news_limit: int | None = None,
        format: None = None,
    ) -> FinanceSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        quotes_limit: int | None = None,
        news_limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> FinanceSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "quotesLimit": quotes_limit,
                "newsLimit": news_limit,
            }
        )
        return self._call("POST", "/v1/finance/search", body, format)


class SyncFinanceProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        symbol: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        symbol: str,
        format: None = None,
    ) -> FinanceProfileResponse: ...
    def __call__(
        self,
        *,
        symbol: str,
        format: Literal["markdown"] | None = None,
    ) -> FinanceProfileResponse | str:
        body = _omit_none(
            {
                "symbol": symbol,
            }
        )
        return self._call("POST", "/v1/finance/profile", body, format)


class SyncFinance:
    quote: SyncFinanceQuote
    history: SyncFinanceHistory
    search: SyncFinanceSearch
    profile: SyncFinanceProfile

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.quote = SyncFinanceQuote(call)
        self.history = SyncFinanceHistory(call)
        self.search = SyncFinanceSearch(call)
        self.profile = SyncFinanceProfile(call)


class SyncMicrosoftAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        countries: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        countries: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MicrosoftAdsSearchResponse: ...
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        countries: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MicrosoftAdsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "countries": countries,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/microsoft/ads/search", body, format)


class SyncMicrosoftAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> MicrosoftAdsAdResponse: ...
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> MicrosoftAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return self._call("POST", "/v1/microsoft/ads/ad", body, format)


class SyncMicrosoftAdsAdvertisers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: None = None,
    ) -> MicrosoftAdsAdvertisersResponse: ...
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MicrosoftAdsAdvertisersResponse | str:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/microsoft/ads/advertisers", body, format)


class SyncMicrosoftAds:
    search: SyncMicrosoftAdsSearch
    ad: SyncMicrosoftAdsAd
    advertisers: SyncMicrosoftAdsAdvertisers

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncMicrosoftAdsSearch(call)
        self.ad = SyncMicrosoftAdsAd(call)
        self.advertisers = SyncMicrosoftAdsAdvertisers(call)


class SyncMicrosoft:
    ads: SyncMicrosoftAds

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.ads = SyncMicrosoftAds(call)


class SyncSnapchatProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> SnapchatProfileResponse: ...
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> SnapchatProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return self._call("POST", "/v1/snapchat/profile", body, format)


class SyncSnapchatAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        advertiser: str,
        countries: list[str] | None = None,
        status: SnapchatAdsSearchStatus | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        advertiser: str,
        countries: list[str] | None = None,
        status: SnapchatAdsSearchStatus | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> SnapchatAdsSearchResponse: ...
    def __call__(
        self,
        *,
        advertiser: str,
        countries: list[str] | None = None,
        status: SnapchatAdsSearchStatus | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> SnapchatAdsSearchResponse | str:
        body = _omit_none(
            {
                "advertiser": advertiser,
                "countries": countries,
                "status": status,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/snapchat/ads/search", body, format)


class SyncSnapchatAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> SnapchatAdsAdResponse: ...
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> SnapchatAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return self._call("POST", "/v1/snapchat/ads/ad", body, format)


class SyncSnapchatAds:
    search: SyncSnapchatAdsSearch
    ad: SyncSnapchatAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncSnapchatAdsSearch(call)
        self.ad = SyncSnapchatAdsAd(call)


class SyncSnapchat:
    profile: SyncSnapchatProfile
    ads: SyncSnapchatAds

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncSnapchatProfile(call)
        self.ads = SyncSnapchatAds(call)


class SyncTumblrBlog:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        blog: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        blog: str,
        format: None = None,
    ) -> TumblrBlogResponse: ...
    def __call__(
        self,
        *,
        blog: str,
        format: Literal["markdown"] | None = None,
    ) -> TumblrBlogResponse | str:
        body = _omit_none(
            {
                "blog": blog,
            }
        )
        return self._call("POST", "/v1/tumblr/blog", body, format)


class SyncTumblrPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        blog: str,
        tag: str | None = None,
        type: TumblrPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        blog: str,
        tag: str | None = None,
        type: TumblrPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TumblrPostsResponse: ...
    def __call__(
        self,
        *,
        blog: str,
        tag: str | None = None,
        type: TumblrPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TumblrPostsResponse | str:
        body = _omit_none(
            {
                "blog": blog,
                "tag": tag,
                "type": type,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tumblr/posts", body, format)


class SyncTumblrPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        format: None = None,
    ) -> TumblrPostResponse: ...
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"] | None = None,
    ) -> TumblrPostResponse | str:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return self._call("POST", "/v1/tumblr/post", body, format)


class SyncTumblrSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TumblrSearchResponse: ...
    def __call__(
        self,
        *,
        query: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TumblrSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tumblr/search", body, format)


class SyncTumblr:
    blog: SyncTumblrBlog
    posts: SyncTumblrPosts
    post: SyncTumblrPost
    search: SyncTumblrSearch

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.blog = SyncTumblrBlog(call)
        self.posts = SyncTumblrPosts(call)
        self.post = SyncTumblrPost(call)
        self.search = SyncTumblrSearch(call)


class SyncQuoraQuestion:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        question: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        question: str,
        format: None = None,
    ) -> QuoraQuestionResponse: ...
    def __call__(
        self,
        *,
        question: str,
        format: Literal["markdown"] | None = None,
    ) -> QuoraQuestionResponse | str:
        body = _omit_none(
            {
                "question": question,
            }
        )
        return self._call("POST", "/v1/quora/question", body, format)


class SyncQuora:
    question: SyncQuoraQuestion

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.question = SyncQuoraQuestion(call)


class SyncSurface:
    endpoints: SyncEndpoints
    web: SyncWeb
    youtube: SyncYoutube
    reddit: SyncReddit
    maps: SyncMaps
    instagram: SyncInstagram
    tiktok: SyncTiktok
    bluesky: SyncBluesky
    mastodon: SyncMastodon
    threads: SyncThreads
    telegram: SyncTelegram
    meta: SyncMeta
    linkedin: SyncLinkedin
    zillow: SyncZillow
    google: SyncGoogle
    upwork: SyncUpwork
    amazon: SyncAmazon
    site: SyncSite
    domain: SyncDomain
    email: SyncEmail
    crypto: SyncCrypto
    indeed: SyncIndeed
    tripadvisor: SyncTripadvisor
    googletravel: SyncGoogletravel
    shopify: SyncShopify
    walmart: SyncWalmart
    aliexpress: SyncAliexpress
    appstore: SyncAppstore
    googleplay: SyncGoogleplay
    airbnb: SyncAirbnb
    redfin: SyncRedfin
    realtor: SyncRealtor
    rightmove: SyncRightmove
    immoscout: SyncImmoscout
    pinterest: SyncPinterest
    x: SyncX
    kick: SyncKick
    finance: SyncFinance
    microsoft: SyncMicrosoft
    snapchat: SyncSnapchat
    tumblr: SyncTumblr
    quora: SyncQuora

    def __init__(self, call: SyncCall) -> None:
        self.endpoints = SyncEndpoints(call)
        self.web = SyncWeb(call)
        self.youtube = SyncYoutube(call)
        self.reddit = SyncReddit(call)
        self.maps = SyncMaps(call)
        self.instagram = SyncInstagram(call)
        self.tiktok = SyncTiktok(call)
        self.bluesky = SyncBluesky(call)
        self.mastodon = SyncMastodon(call)
        self.threads = SyncThreads(call)
        self.telegram = SyncTelegram(call)
        self.meta = SyncMeta(call)
        self.linkedin = SyncLinkedin(call)
        self.zillow = SyncZillow(call)
        self.google = SyncGoogle(call)
        self.upwork = SyncUpwork(call)
        self.amazon = SyncAmazon(call)
        self.site = SyncSite(call)
        self.domain = SyncDomain(call)
        self.email = SyncEmail(call)
        self.crypto = SyncCrypto(call)
        self.indeed = SyncIndeed(call)
        self.tripadvisor = SyncTripadvisor(call)
        self.googletravel = SyncGoogletravel(call)
        self.shopify = SyncShopify(call)
        self.walmart = SyncWalmart(call)
        self.aliexpress = SyncAliexpress(call)
        self.appstore = SyncAppstore(call)
        self.googleplay = SyncGoogleplay(call)
        self.airbnb = SyncAirbnb(call)
        self.redfin = SyncRedfin(call)
        self.realtor = SyncRealtor(call)
        self.rightmove = SyncRightmove(call)
        self.immoscout = SyncImmoscout(call)
        self.pinterest = SyncPinterest(call)
        self.x = SyncX(call)
        self.kick = SyncKick(call)
        self.finance = SyncFinance(call)
        self.microsoft = SyncMicrosoft(call)
        self.snapchat = SyncSnapchat(call)
        self.tumblr = SyncTumblr(call)
        self.quora = SyncQuora(call)


class AsyncEndpoints:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        format: None = None,
    ) -> EndpointCatalog: ...
    async def __call__(
        self,
        *,
        format: Literal["markdown"] | None = None,
    ) -> EndpointCatalog | str:
        body = None
        return await self._call("GET", "/v1/endpoints", body, format)


class AsyncWebSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebSearchWithin | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebSearchWithin | None = None,
        format: None = None,
    ) -> WebSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebSearchWithin | None = None,
        format: Literal["markdown"] | None = None,
    ) -> WebSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "from": from_,
                "to": to,
                "limit": limit,
                "within": within,
            }
        )
        return await self._call("POST", "/v1/web/search", body, format)


class AsyncWebNews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        topic: WebNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebNewsWithin | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        topic: WebNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebNewsWithin | None = None,
        format: None = None,
    ) -> WebNewsResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        topic: WebNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        within: WebNewsWithin | None = None,
        format: Literal["markdown"] | None = None,
    ) -> WebNewsResponse | str:
        body = _omit_none(
            {
                "query": query,
                "topic": topic,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "from": from_,
                "to": to,
                "limit": limit,
                "within": within,
            }
        )
        return await self._call("POST", "/v1/web/news", body, format)


class AsyncWebContacts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        max_pages: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        max_pages: int | None = None,
        format: None = None,
    ) -> WebContactsResponse: ...
    async def __call__(
        self,
        *,
        url: str,
        max_pages: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> WebContactsResponse | str:
        body = _omit_none(
            {
                "url": url,
                "maxPages": max_pages,
            }
        )
        return await self._call("POST", "/v1/web/contacts", body, format)


class AsyncWeb:
    search: AsyncWebSearch
    news: AsyncWebNews
    contacts: AsyncWebContacts

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncWebSearch(call)
        self.news = AsyncWebNews(call)
        self.contacts = AsyncWebContacts(call)


class AsyncYoutubeSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        duration: YoutubeSearchDuration | None = None,
        within: WebNewsWithin | None = None,
        sort: YoutubeSearchSort | None = None,
        features: list[YoutubeSearchFeaturesItem] | None = None,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        duration: YoutubeSearchDuration | None = None,
        within: WebNewsWithin | None = None,
        sort: YoutubeSearchSort | None = None,
        features: list[YoutubeSearchFeaturesItem] | None = None,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> YoutubeSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        duration: YoutubeSearchDuration | None = None,
        within: WebNewsWithin | None = None,
        sort: YoutubeSearchSort | None = None,
        features: list[YoutubeSearchFeaturesItem] | None = None,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "duration": duration,
                "within": within,
                "sort": sort,
                "features": features,
                "country": country,
                "language": language,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/search", body, format)


class AsyncYoutubeVideo:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        format: None = None,
    ) -> YoutubeVideoResponse: ...
    async def __call__(
        self,
        *,
        video: str,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeVideoResponse | str:
        body = _omit_none(
            {
                "video": video,
            }
        )
        return await self._call("POST", "/v1/youtube/video", body, format)


class AsyncYoutubeTranscript:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: None = None,
    ) -> YoutubeTranscriptResponse: ...
    async def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeTranscriptResponse | str:
        body = _omit_none(
            {
                "video": video,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return await self._call("POST", "/v1/youtube/transcript", body, format)


class AsyncYoutubeCommentsReplies:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str,
        format: None = None,
    ) -> YoutubeCommentsRepliesResponse: ...
    async def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeCommentsRepliesResponse | str:
        body = _omit_none(
            {
                "video": video,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/comments/replies", body, format)


class AsyncYoutubeComments:
    replies: AsyncYoutubeCommentsReplies

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.replies = AsyncYoutubeCommentsReplies(call)

    @overload
    def __call__(
        self,
        *,
        video: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> YoutubeCommentsResponse: ...
    async def __call__(
        self,
        *,
        video: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeCommentsResponse | str:
        body = _omit_none(
            {
                "video": video,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/comments", body, format)


class AsyncYoutubeChannel:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        tab: YoutubeChannelTab | None = None,
        query: str | None = None,
        include_about: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        tab: YoutubeChannelTab | None = None,
        query: str | None = None,
        include_about: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> YoutubeChannelResponse: ...
    async def __call__(
        self,
        *,
        channel: str,
        tab: YoutubeChannelTab | None = None,
        query: str | None = None,
        include_about: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeChannelResponse | str:
        body = _omit_none(
            {
                "channel": channel,
                "tab": tab,
                "query": query,
                "includeAbout": include_about,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/channel", body, format)


class AsyncYoutubePlaylist:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        playlist: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        playlist: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> YoutubePlaylistResponse: ...
    async def __call__(
        self,
        *,
        playlist: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubePlaylistResponse | str:
        body = _omit_none(
            {
                "playlist": playlist,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/playlist", body, format)


class AsyncYoutubeSuggest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: None = None,
    ) -> GoogleSuggestResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleSuggestResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "expand": expand,
            }
        )
        return await self._call("POST", "/v1/youtube/suggest", body, format)


class AsyncYoutube:
    search: AsyncYoutubeSearch
    video: AsyncYoutubeVideo
    transcript: AsyncYoutubeTranscript
    comments: AsyncYoutubeComments
    channel: AsyncYoutubeChannel
    playlist: AsyncYoutubePlaylist
    suggest: AsyncYoutubeSuggest

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncYoutubeSearch(call)
        self.video = AsyncYoutubeVideo(call)
        self.transcript = AsyncYoutubeTranscript(call)
        self.comments = AsyncYoutubeComments(call)
        self.channel = AsyncYoutubeChannel(call)
        self.playlist = AsyncYoutubePlaylist(call)
        self.suggest = AsyncYoutubeSuggest(call)


class AsyncRedditSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: RedditSearchType | None = None,
        subreddit: str | None = None,
        sort: RedditSearchSort | None = None,
        within: WebNewsWithin | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: RedditSearchType | None = None,
        subreddit: str | None = None,
        sort: RedditSearchSort | None = None,
        within: WebNewsWithin | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedditSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        type: RedditSearchType | None = None,
        subreddit: str | None = None,
        sort: RedditSearchSort | None = None,
        within: WebNewsWithin | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "subreddit": subreddit,
                "sort": sort,
                "within": within,
                "includeNsfw": include_nsfw,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/search", body, format)


class AsyncRedditPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        sort: RedditPostSort | None = None,
        depth: int | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        sort: RedditPostSort | None = None,
        depth: int | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> RedditPostResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        sort: RedditPostSort | None = None,
        depth: int | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditPostResponse | str:
        body = _omit_none(
            {
                "post": post,
                "sort": sort,
                "depth": depth,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/reddit/post", body, format)


class AsyncRedditCommentsMore:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        limit: int | None = None,
        cursor: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        limit: int | None = None,
        cursor: str,
        format: None = None,
    ) -> RedditCommentsMoreResponse: ...
    async def __call__(
        self,
        *,
        limit: int | None = None,
        cursor: str,
        format: Literal["markdown"] | None = None,
    ) -> RedditCommentsMoreResponse | str:
        body = _omit_none(
            {
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/comments/more", body, format)


class AsyncRedditComments:
    more: AsyncRedditCommentsMore

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.more = AsyncRedditCommentsMore(call)


class AsyncRedditSubreddit:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        subreddit: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        subreddit: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedditSubredditResponse: ...
    async def __call__(
        self,
        *,
        subreddit: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditSubredditResponse | str:
        body = _omit_none(
            {
                "subreddit": subreddit,
                "sort": sort,
                "within": within,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/subreddit", body, format)


class AsyncRedditUser:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedditUserResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditUserResponse | str:
        body = _omit_none(
            {
                "user": user,
                "tab": tab,
                "sort": sort,
                "within": within,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/user", body, format)


class AsyncRedditDomain:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        domain: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        domain: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedditDomainResponse: ...
    async def __call__(
        self,
        *,
        domain: str,
        sort: RedditSubredditSort | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedditDomainResponse | str:
        body = _omit_none(
            {
                "domain": domain,
                "sort": sort,
                "within": within,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/domain", body, format)


class AsyncReddit:
    search: AsyncRedditSearch
    post: AsyncRedditPost
    comments: AsyncRedditComments
    subreddit: AsyncRedditSubreddit
    user: AsyncRedditUser
    domain: AsyncRedditDomain

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncRedditSearch(call)
        self.post = AsyncRedditPost(call)
        self.comments = AsyncRedditComments(call)
        self.subreddit = AsyncRedditSubreddit(call)
        self.user = AsyncRedditUser(call)
        self.domain = AsyncRedditDomain(call)


class AsyncMapsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        near: str | None = None,
        center: MapsSearchCenter | None = None,
        radius_km: float | None = None,
        limit: int | None = None,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        near: str | None = None,
        center: MapsSearchCenter | None = None,
        radius_km: float | None = None,
        limit: int | None = None,
        country: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> MapsSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        near: str | None = None,
        center: MapsSearchCenter | None = None,
        radius_km: float | None = None,
        limit: int | None = None,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MapsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "near": near,
                "center": center,
                "radiusKm": radius_km,
                "limit": limit,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/maps/search", body, format)


class AsyncMapsPlace:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        place: str,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        place: str,
        country: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> MapsPlaceResponse: ...
    async def __call__(
        self,
        *,
        place: str,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MapsPlaceResponse | str:
        body = _omit_none(
            {
                "place": place,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/maps/place", body, format)


class AsyncMapsReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        place: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        place: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> MapsReviewsResponse: ...
    async def __call__(
        self,
        *,
        place: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MapsReviewsResponse | str:
        body = _omit_none(
            {
                "place": place,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
                "from": from_,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/maps/reviews", body, format)


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

    @overload
    def __call__(
        self,
        *,
        user: str,
        include_posts: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        include_posts: bool | None = None,
        format: None = None,
    ) -> InstagramProfileResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        include_posts: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
                "includePosts": include_posts,
            }
        )
        return await self._call("POST", "/v1/instagram/profile", body, format)


class AsyncInstagramPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        type: InstagramPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_views: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        type: InstagramPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_views: bool | None = None,
        format: None = None,
    ) -> InstagramPostsResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        type: InstagramPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_views: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "type": type,
                "limit": limit,
                "cursor": cursor,
                "from": from_,
                "to": to,
                "includeViews": include_views,
            }
        )
        return await self._call("POST", "/v1/instagram/posts", body, format)


class AsyncInstagramPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        include_comments: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        include_comments: bool | None = None,
        format: None = None,
    ) -> InstagramPostResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        include_comments: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramPostResponse | str:
        body = _omit_none(
            {
                "post": post,
                "includeComments": include_comments,
            }
        )
        return await self._call("POST", "/v1/instagram/post", body, format)


class AsyncInstagramUrl:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        format: None = None,
    ) -> InstagramUrlResponse: ...
    async def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"] | None = None,
    ) -> InstagramUrlResponse | str:
        body = _omit_none(
            {
                "url": url,
            }
        )
        return await self._call("POST", "/v1/instagram/url", body, format)


class AsyncInstagramSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: InstagramSearchType | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: InstagramSearchType | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> InstagramSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        type: InstagramSearchType | None = None,
        within: WebNewsWithin | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "within": within,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/instagram/search", body, format)


class AsyncInstagramTranscript:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> InstagramTranscriptResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramTranscriptResponse | str:
        body = _omit_none(
            {
                "post": post,
                "language": language,
                "includeTimestamps": include_timestamps,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/instagram/transcript", body, format)


class AsyncInstagramCommentsReplies:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> InstagramCommentsRepliesResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramCommentsRepliesResponse | str:
        body = _omit_none(
            {
                "post": post,
                "comment": comment,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/instagram/comments/replies", body, format)


class AsyncInstagramComments:
    replies: AsyncInstagramCommentsReplies

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.replies = AsyncInstagramCommentsReplies(call)

    @overload
    def __call__(
        self,
        *,
        post: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> InstagramCommentsResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> InstagramCommentsResponse | str:
        body = _omit_none(
            {
                "post": post,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/instagram/comments", body, format)


class AsyncInstagram:
    profile: AsyncInstagramProfile
    posts: AsyncInstagramPosts
    post: AsyncInstagramPost
    url: AsyncInstagramUrl
    search: AsyncInstagramSearch
    transcript: AsyncInstagramTranscript
    comments: AsyncInstagramComments

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncInstagramProfile(call)
        self.posts = AsyncInstagramPosts(call)
        self.post = AsyncInstagramPost(call)
        self.url = AsyncInstagramUrl(call)
        self.search = AsyncInstagramSearch(call)
        self.transcript = AsyncInstagramTranscript(call)
        self.comments = AsyncInstagramComments(call)


class AsyncTiktokProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> TiktokProfileResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> TiktokProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return await self._call("POST", "/v1/tiktok/profile", body, format)


class AsyncTiktokVideo:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        format: None = None,
    ) -> TiktokVideoResponse: ...
    async def __call__(
        self,
        *,
        video: str,
        format: Literal["markdown"] | None = None,
    ) -> TiktokVideoResponse | str:
        body = _omit_none(
            {
                "video": video,
            }
        )
        return await self._call("POST", "/v1/tiktok/video", body, format)


class AsyncTiktokUrl:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        format: None = None,
    ) -> TiktokUrlResponse: ...
    async def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"] | None = None,
    ) -> TiktokUrlResponse | str:
        body = _omit_none(
            {
                "url": url,
            }
        )
        return await self._call("POST", "/v1/tiktok/url", body, format)


class AsyncTiktokTranscript:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: None = None,
    ) -> YoutubeTranscriptResponse: ...
    async def __call__(
        self,
        *,
        video: str,
        language: str | None = None,
        include_timestamps: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> YoutubeTranscriptResponse | str:
        body = _omit_none(
            {
                "video": video,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return await self._call("POST", "/v1/tiktok/transcript", body, format)


class AsyncTiktokPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokPostsResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/posts", body, format)


class AsyncTiktokCommentsReplies:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        video: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokCommentsRepliesResponse: ...
    async def __call__(
        self,
        *,
        video: str,
        comment: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokCommentsRepliesResponse | str:
        body = _omit_none(
            {
                "video": video,
                "comment": comment,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/comments/replies", body, format)


class AsyncTiktokComments:
    replies: AsyncTiktokCommentsReplies

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.replies = AsyncTiktokCommentsReplies(call)

    @overload
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokCommentsResponse: ...
    async def __call__(
        self,
        *,
        video: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokCommentsResponse | str:
        body = _omit_none(
            {
                "video": video,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/comments", body, format)


class AsyncTiktokSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: TiktokSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: TiktokSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        type: TiktokSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/search", body, format)


class AsyncTiktokAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TiktokAdsSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TiktokAdsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "country": country,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/ads/search", body, format)


class AsyncTiktokAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> TiktokAdsAdResponse: ...
    async def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> TiktokAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return await self._call("POST", "/v1/tiktok/ads/ad", body, format)


class AsyncTiktokAds:
    search: AsyncTiktokAdsSearch
    ad: AsyncTiktokAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncTiktokAdsSearch(call)
        self.ad = AsyncTiktokAdsAd(call)


class AsyncTiktok:
    profile: AsyncTiktokProfile
    video: AsyncTiktokVideo
    url: AsyncTiktokUrl
    transcript: AsyncTiktokTranscript
    posts: AsyncTiktokPosts
    comments: AsyncTiktokComments
    search: AsyncTiktokSearch
    ads: AsyncTiktokAds

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncTiktokProfile(call)
        self.video = AsyncTiktokVideo(call)
        self.url = AsyncTiktokUrl(call)
        self.transcript = AsyncTiktokTranscript(call)
        self.posts = AsyncTiktokPosts(call)
        self.comments = AsyncTiktokComments(call)
        self.search = AsyncTiktokSearch(call)
        self.ads = AsyncTiktokAds(call)


class AsyncBlueskyProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> BlueskyProfileResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> BlueskyProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return await self._call("POST", "/v1/bluesky/profile", body, format)


class AsyncBlueskyPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        type: BlueskyPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        type: BlueskyPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> BlueskyPostsResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        type: BlueskyPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> BlueskyPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "type": type,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/bluesky/posts", body, format)


class AsyncBlueskyPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        depth: int | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        depth: int | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> BlueskyPostResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        depth: int | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> BlueskyPostResponse | str:
        body = _omit_none(
            {
                "post": post,
                "depth": depth,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/bluesky/post", body, format)


class AsyncBlueskyFollowers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> BlueskyFollowersResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> BlueskyFollowersResponse | str:
        body = _omit_none(
            {
                "user": user,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/bluesky/followers", body, format)


class AsyncBluesky:
    profile: AsyncBlueskyProfile
    posts: AsyncBlueskyPosts
    post: AsyncBlueskyPost
    followers: AsyncBlueskyFollowers

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncBlueskyProfile(call)
        self.posts = AsyncBlueskyPosts(call)
        self.post = AsyncBlueskyPost(call)
        self.followers = AsyncBlueskyFollowers(call)


class AsyncMastodonProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> MastodonProfileResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> MastodonProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return await self._call("POST", "/v1/mastodon/profile", body, format)


class AsyncMastodonPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        exclude_replies: bool | None = None,
        exclude_reposts: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        exclude_replies: bool | None = None,
        exclude_reposts: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MastodonPostsResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        exclude_replies: bool | None = None,
        exclude_reposts: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MastodonPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "excludeReplies": exclude_replies,
                "excludeReposts": exclude_reposts,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/mastodon/posts", body, format)


class AsyncMastodonPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        format: None = None,
    ) -> MastodonPostResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"] | None = None,
    ) -> MastodonPostResponse | str:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return await self._call("POST", "/v1/mastodon/post", body, format)


class AsyncMastodonHashtag:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        hashtag: str,
        instance: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        hashtag: str,
        instance: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MastodonPostsResponse: ...
    async def __call__(
        self,
        *,
        hashtag: str,
        instance: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MastodonPostsResponse | str:
        body = _omit_none(
            {
                "hashtag": hashtag,
                "instance": instance,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/mastodon/hashtag", body, format)


class AsyncMastodon:
    profile: AsyncMastodonProfile
    posts: AsyncMastodonPosts
    post: AsyncMastodonPost
    hashtag: AsyncMastodonHashtag

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncMastodonProfile(call)
        self.posts = AsyncMastodonPosts(call)
        self.post = AsyncMastodonPost(call)
        self.hashtag = AsyncMastodonHashtag(call)


class AsyncThreadsProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> ThreadsProfileResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> ThreadsProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return await self._call("POST", "/v1/threads/profile", body, format)


class AsyncThreadsPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ThreadsPostsResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ThreadsPostsResponse | str:
        body = _omit_none(
            {
                "user": user,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/threads/posts", body, format)


class AsyncThreadsPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        cursor: str | None = None,
        format: None = None,
    ) -> ThreadsPostResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ThreadsPostResponse | str:
        body = _omit_none(
            {
                "post": post,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/threads/post", body, format)


class AsyncThreadsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: None = None,
    ) -> ThreadsSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ThreadsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/threads/search", body, format)


class AsyncThreads:
    profile: AsyncThreadsProfile
    posts: AsyncThreadsPosts
    post: AsyncThreadsPost
    search: AsyncThreadsSearch

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncThreadsProfile(call)
        self.posts = AsyncThreadsPosts(call)
        self.post = AsyncThreadsPost(call)
        self.search = AsyncThreadsSearch(call)


class AsyncTelegramChannel:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        format: None = None,
    ) -> TelegramChannelResponse: ...
    async def __call__(
        self,
        *,
        channel: str,
        format: Literal["markdown"] | None = None,
    ) -> TelegramChannelResponse | str:
        body = _omit_none(
            {
                "channel": channel,
            }
        )
        return await self._call("POST", "/v1/telegram/channel", body, format)


class AsyncTelegramPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TelegramPostsResponse: ...
    async def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TelegramPostsResponse | str:
        body = _omit_none(
            {
                "channel": channel,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/telegram/posts", body, format)


class AsyncTelegramPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        format: None = None,
    ) -> TelegramPostResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"] | None = None,
    ) -> TelegramPostResponse | str:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return await self._call("POST", "/v1/telegram/post", body, format)


class AsyncTelegram:
    channel: AsyncTelegramChannel
    posts: AsyncTelegramPosts
    post: AsyncTelegramPost

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.channel = AsyncTelegramChannel(call)
        self.posts = AsyncTelegramPosts(call)
        self.post = AsyncTelegramPost(call)


class AsyncMetaAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MetaAdsSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MetaAdsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "adType": ad_type,
                "status": status,
                "mediaType": media_type,
                "platforms": platforms,
                "from": from_,
                "to": to,
                "language": language,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/meta/ads/search", body, format)


class AsyncMetaAdsPage:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MetaAdsSearchResponse: ...
    async def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        ad_type: MetaAdsSearchAdType | None = None,
        status: MetaAdsSearchStatus | None = None,
        media_type: MetaAdsSearchMediaType | None = None,
        platforms: list[MetaAdsSearchPlatformsItem] | None = None,
        from_: str | None = None,
        to: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MetaAdsSearchResponse | str:
        body = _omit_none(
            {
                "page": page,
                "country": country,
                "adType": ad_type,
                "status": status,
                "mediaType": media_type,
                "platforms": platforms,
                "from": from_,
                "to": to,
                "language": language,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/meta/ads/page", body, format)


class AsyncMetaAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> MetaAdsAdResponse: ...
    async def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> MetaAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return await self._call("POST", "/v1/meta/ads/ad", body, format)


class AsyncMetaAds:
    search: AsyncMetaAdsSearch
    page: AsyncMetaAdsPage
    ad: AsyncMetaAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncMetaAdsSearch(call)
        self.page = AsyncMetaAdsPage(call)
        self.ad = AsyncMetaAdsAd(call)


class AsyncMeta:
    ads: AsyncMetaAds

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.ads = AsyncMetaAds(call)


class AsyncLinkedinJobsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        geo_id: str | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        job_types: list[LinkedinJobsSearchJobTypesItem] | None = None,
        experience: list[LinkedinJobsSearchExperienceItem] | None = None,
        workplace: list[LinkedinJobsSearchWorkplaceItem] | None = None,
        company_ids: list[str] | None = None,
        easy_apply: bool | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        geo_id: str | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        job_types: list[LinkedinJobsSearchJobTypesItem] | None = None,
        experience: list[LinkedinJobsSearchExperienceItem] | None = None,
        workplace: list[LinkedinJobsSearchWorkplaceItem] | None = None,
        company_ids: list[str] | None = None,
        easy_apply: bool | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> LinkedinJobsSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        geo_id: str | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        job_types: list[LinkedinJobsSearchJobTypesItem] | None = None,
        experience: list[LinkedinJobsSearchExperienceItem] | None = None,
        workplace: list[LinkedinJobsSearchWorkplaceItem] | None = None,
        company_ids: list[str] | None = None,
        easy_apply: bool | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> LinkedinJobsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "geoId": geo_id,
                "within": within,
                "jobTypes": job_types,
                "experience": experience,
                "workplace": workplace,
                "companyIds": company_ids,
                "easyApply": easy_apply,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/linkedin/jobs/search", body, format)


class AsyncLinkedinJobsJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        job: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        job: str,
        format: None = None,
    ) -> LinkedinJobsJobResponse: ...
    async def __call__(
        self,
        *,
        job: str,
        format: Literal["markdown"] | None = None,
    ) -> LinkedinJobsJobResponse | str:
        body = _omit_none(
            {
                "job": job,
            }
        )
        return await self._call("POST", "/v1/linkedin/jobs/job", body, format)


class AsyncLinkedinJobs:
    search: AsyncLinkedinJobsSearch
    job: AsyncLinkedinJobsJob

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncLinkedinJobsSearch(call)
        self.job = AsyncLinkedinJobsJob(call)


class AsyncLinkedinAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        paid_by: str | None = None,
        countries: list[str] | None = None,
        within: LinkedinAdsSearchWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        paid_by: str | None = None,
        countries: list[str] | None = None,
        within: LinkedinAdsSearchWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> LinkedinAdsSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        paid_by: str | None = None,
        countries: list[str] | None = None,
        within: LinkedinAdsSearchWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> LinkedinAdsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "paidBy": paid_by,
                "countries": countries,
                "within": within,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/linkedin/ads/search", body, format)


class AsyncLinkedinAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> LinkedinAdsAdResponse: ...
    async def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> LinkedinAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return await self._call("POST", "/v1/linkedin/ads/ad", body, format)


class AsyncLinkedinAds:
    search: AsyncLinkedinAdsSearch
    ad: AsyncLinkedinAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncLinkedinAdsSearch(call)
        self.ad = AsyncLinkedinAdsAd(call)


class AsyncLinkedin:
    jobs: AsyncLinkedinJobs
    ads: AsyncLinkedinAds

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.jobs = AsyncLinkedinJobs(call)
        self.ads = AsyncLinkedinAds(call)


class AsyncZillowSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        location: str | None = None,
        bounds: ZillowSearchBounds | None = None,
        status: ZillowSearchStatus | None = None,
        sort: ZillowSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        listing_types: list[ZillowSearchListingTypesItem] | None = None,
        within: ZillowSearchWithin | None = None,
        query: str | None = None,
        features: list[ZillowSearchFeaturesItem] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str | None = None,
        bounds: ZillowSearchBounds | None = None,
        status: ZillowSearchStatus | None = None,
        sort: ZillowSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        listing_types: list[ZillowSearchListingTypesItem] | None = None,
        within: ZillowSearchWithin | None = None,
        query: str | None = None,
        features: list[ZillowSearchFeaturesItem] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ZillowSearchResponse: ...
    async def __call__(
        self,
        *,
        location: str | None = None,
        bounds: ZillowSearchBounds | None = None,
        status: ZillowSearchStatus | None = None,
        sort: ZillowSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        listing_types: list[ZillowSearchListingTypesItem] | None = None,
        within: ZillowSearchWithin | None = None,
        query: str | None = None,
        features: list[ZillowSearchFeaturesItem] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ZillowSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "bounds": bounds,
                "status": status,
                "sort": sort,
                "price": price,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "sqft": sqft,
                "lotSqft": lot_sqft,
                "yearBuilt": year_built,
                "hoa": hoa,
                "homeTypes": home_types,
                "listingTypes": listing_types,
                "within": within,
                "query": query,
                "features": features,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/zillow/search", body, format)


class AsyncZillowProperty:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        property: str,
        format: None = None,
    ) -> ZillowPropertyResponse: ...
    async def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"] | None = None,
    ) -> ZillowPropertyResponse | str:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return await self._call("POST", "/v1/zillow/property", body, format)


class AsyncZillow:
    search: AsyncZillowSearch
    property: AsyncZillowProperty

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncZillowSearch(call)
        self.property = AsyncZillowProperty(call)


class AsyncGoogleAdsAdvertisers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> GoogleAdsAdvertisersResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleAdsAdvertisersResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/google/ads/advertisers", body, format)


class AsyncGoogleAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: GoogleAdsSearchMediaType | None = None,
        platform: GoogleAdsSearchPlatform | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: GoogleAdsSearchMediaType | None = None,
        platform: GoogleAdsSearchPlatform | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> GoogleAdsSearchResponse: ...
    async def __call__(
        self,
        *,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: GoogleAdsSearchMediaType | None = None,
        platform: GoogleAdsSearchPlatform | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleAdsSearchResponse | str:
        body = _omit_none(
            {
                "advertiser": advertiser,
                "domain": domain,
                "country": country,
                "mediaType": media_type,
                "platform": platform,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/google/ads/search", body, format)


class AsyncGoogleAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        advertiser: str | None = None,
        ad: str,
        format: None = None,
    ) -> GoogleAdsAdResponse: ...
    async def __call__(
        self,
        *,
        advertiser: str | None = None,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> GoogleAdsAdResponse | str:
        body = _omit_none(
            {
                "advertiser": advertiser,
                "ad": ad,
            }
        )
        return await self._call("POST", "/v1/google/ads/ad", body, format)


class AsyncGoogleAds:
    advertisers: AsyncGoogleAdsAdvertisers
    search: AsyncGoogleAdsSearch
    ad: AsyncGoogleAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.advertisers = AsyncGoogleAdsAdvertisers(call)
        self.search = AsyncGoogleAdsSearch(call)
        self.ad = AsyncGoogleAdsAd(call)


class AsyncGoogleSuggest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        vertical: GoogleSuggestVertical | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        vertical: GoogleSuggestVertical | None = None,
        format: None = None,
    ) -> GoogleSuggestResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        expand: GoogleSuggestExpand | None = None,
        vertical: GoogleSuggestVertical | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleSuggestResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "expand": expand,
                "vertical": vertical,
            }
        )
        return await self._call("POST", "/v1/google/suggest", body, format)


class AsyncGoogleTrendsInterest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: None = None,
    ) -> GoogleTrendsInterestResponse: ...
    async def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleTrendsInterestResponse | str:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "subdivision": subdivision,
                "within": within,
                "from": from_,
                "to": to,
                "category": category,
                "vertical": vertical,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/google/trends/interest", body, format)


class AsyncGoogleTrendsRegions:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        resolution: GoogleTrendsRegionsResolution | None = None,
        include_low_volume: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        resolution: GoogleTrendsRegionsResolution | None = None,
        include_low_volume: bool | None = None,
        format: None = None,
    ) -> GoogleTrendsRegionsResponse: ...
    async def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        resolution: GoogleTrendsRegionsResolution | None = None,
        include_low_volume: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleTrendsRegionsResponse | str:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "subdivision": subdivision,
                "within": within,
                "from": from_,
                "to": to,
                "category": category,
                "vertical": vertical,
                "language": language,
                "resolution": resolution,
                "includeLowVolume": include_low_volume,
            }
        )
        return await self._call("POST", "/v1/google/trends/regions", body, format)


class AsyncGoogleTrendsRelated:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: None = None,
    ) -> GoogleTrendsRelatedResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        subdivision: str | None = None,
        within: WebNewsWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        category: int | None = None,
        vertical: GoogleTrendsInterestVertical | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleTrendsRelatedResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "subdivision": subdivision,
                "within": within,
                "from": from_,
                "to": to,
                "category": category,
                "vertical": vertical,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/google/trends/related", body, format)


class AsyncGoogleTrendsTrending:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        country: str | None = None,
        subdivision: str | None = None,
        within: GoogleTrendsTrendingWithin | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        active: bool | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        country: str | None = None,
        subdivision: str | None = None,
        within: GoogleTrendsTrendingWithin | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        active: bool | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> GoogleTrendsTrendingResponse: ...
    async def __call__(
        self,
        *,
        country: str | None = None,
        subdivision: str | None = None,
        within: GoogleTrendsTrendingWithin | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        active: bool | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleTrendsTrendingResponse | str:
        body = _omit_none(
            {
                "country": country,
                "subdivision": subdivision,
                "within": within,
                "category": category,
                "active": active,
                "language": language,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/google/trends/trending", body, format)


class AsyncGoogleTrends:
    interest: AsyncGoogleTrendsInterest
    regions: AsyncGoogleTrendsRegions
    related: AsyncGoogleTrendsRelated
    trending: AsyncGoogleTrendsTrending

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.interest = AsyncGoogleTrendsInterest(call)
        self.regions = AsyncGoogleTrendsRegions(call)
        self.related = AsyncGoogleTrendsRelated(call)
        self.trending = AsyncGoogleTrendsTrending(call)


class AsyncGoogle:
    ads: AsyncGoogleAds
    suggest: AsyncGoogleSuggest
    trends: AsyncGoogleTrends

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.ads = AsyncGoogleAds(call)
        self.suggest = AsyncGoogleSuggest(call)
        self.trends = AsyncGoogleTrends(call)


class AsyncUpworkSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        sort: UpworkSearchSort | None = None,
        job_type: UpworkSearchJobType | None = None,
        experience: list[UpworkSearchExperienceItem] | None = None,
        duration: list[UpworkSearchDurationItem] | None = None,
        workload: list[UpworkSearchWorkloadItem] | None = None,
        client_hires: list[UpworkSearchClientHiresItem] | None = None,
        hourly_rate: UpworkSearchHourlyRate | None = None,
        contract_to_hire: bool | None = None,
        locations: list[str] | None = None,
        timezones: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        sort: UpworkSearchSort | None = None,
        job_type: UpworkSearchJobType | None = None,
        experience: list[UpworkSearchExperienceItem] | None = None,
        duration: list[UpworkSearchDurationItem] | None = None,
        workload: list[UpworkSearchWorkloadItem] | None = None,
        client_hires: list[UpworkSearchClientHiresItem] | None = None,
        hourly_rate: UpworkSearchHourlyRate | None = None,
        contract_to_hire: bool | None = None,
        locations: list[str] | None = None,
        timezones: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> UpworkSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        sort: UpworkSearchSort | None = None,
        job_type: UpworkSearchJobType | None = None,
        experience: list[UpworkSearchExperienceItem] | None = None,
        duration: list[UpworkSearchDurationItem] | None = None,
        workload: list[UpworkSearchWorkloadItem] | None = None,
        client_hires: list[UpworkSearchClientHiresItem] | None = None,
        hourly_rate: UpworkSearchHourlyRate | None = None,
        contract_to_hire: bool | None = None,
        locations: list[str] | None = None,
        timezones: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> UpworkSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "jobType": job_type,
                "experience": experience,
                "duration": duration,
                "workload": workload,
                "clientHires": client_hires,
                "hourlyRate": hourly_rate,
                "contractToHire": contract_to_hire,
                "locations": locations,
                "timezones": timezones,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/upwork/search", body, format)


class AsyncUpworkJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        job: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        job: str,
        format: None = None,
    ) -> UpworkJobResponse: ...
    async def __call__(
        self,
        *,
        job: str,
        format: Literal["markdown"] | None = None,
    ) -> UpworkJobResponse | str:
        body = _omit_none(
            {
                "job": job,
            }
        )
        return await self._call("POST", "/v1/upwork/job", body, format)


class AsyncUpwork:
    search: AsyncUpworkSearch
    job: AsyncUpworkJob

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncUpworkSearch(call)
        self.job = AsyncUpworkJob(call)


class AsyncAmazonSuggest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: AmazonSuggestCountry | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: AmazonSuggestCountry | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: None = None,
    ) -> GoogleSuggestResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: AmazonSuggestCountry | None = None,
        expand: GoogleSuggestExpand | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleSuggestResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "expand": expand,
            }
        )
        return await self._call("POST", "/v1/amazon/suggest", body, format)


class AsyncAmazonSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        category: str | None = None,
        price: ZillowSearchPrice | None = None,
        sort: AmazonSearchSort | None = None,
        prime: bool | None = None,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        category: str | None = None,
        price: ZillowSearchPrice | None = None,
        sort: AmazonSearchSort | None = None,
        prime: bool | None = None,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AmazonSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        category: str | None = None,
        price: ZillowSearchPrice | None = None,
        sort: AmazonSearchSort | None = None,
        prime: bool | None = None,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AmazonSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "category": category,
                "price": price,
                "sort": sort,
                "prime": prime,
                "country": country,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/amazon/search", body, format)


class AsyncAmazonProduct:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        product: str,
        country: AmazonSearchCountry | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        product: str,
        country: AmazonSearchCountry | None = None,
        format: None = None,
    ) -> AmazonProductResponse: ...
    async def __call__(
        self,
        *,
        product: str,
        country: AmazonSearchCountry | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AmazonProductResponse | str:
        body = _omit_none(
            {
                "product": product,
                "country": country,
            }
        )
        return await self._call("POST", "/v1/amazon/product", body, format)


class AsyncAmazonBestsellers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        category: str,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        category: str,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AmazonBestsellersResponse: ...
    async def __call__(
        self,
        *,
        category: str,
        country: AmazonSearchCountry | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AmazonBestsellersResponse | str:
        body = _omit_none(
            {
                "category": category,
                "country": country,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/amazon/bestsellers", body, format)


class AsyncAmazon:
    suggest: AsyncAmazonSuggest
    search: AsyncAmazonSearch
    product: AsyncAmazonProduct
    bestsellers: AsyncAmazonBestsellers

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.suggest = AsyncAmazonSuggest(call)
        self.search = AsyncAmazonSearch(call)
        self.product = AsyncAmazonProduct(call)
        self.bestsellers = AsyncAmazonBestsellers(call)


class AsyncSiteMap:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> SiteMapResponse: ...
    async def __call__(
        self,
        *,
        url: str,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> SiteMapResponse | str:
        body = _omit_none(
            {
                "url": url,
                "include": include,
                "exclude": exclude,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/site/map", body, format)


class AsyncSiteSeo:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        check_links: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        check_links: int | None = None,
        format: None = None,
    ) -> SiteSeoResponse: ...
    async def __call__(
        self,
        *,
        url: str,
        check_links: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> SiteSeoResponse | str:
        body = _omit_none(
            {
                "url": url,
                "checkLinks": check_links,
            }
        )
        return await self._call("POST", "/v1/site/seo", body, format)


class AsyncSite:
    map: AsyncSiteMap
    seo: AsyncSiteSeo

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.map = AsyncSiteMap(call)
        self.seo = AsyncSiteSeo(call)


class AsyncDomainWhois:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        domain: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        domain: str,
        format: None = None,
    ) -> DomainWhoisResponse: ...
    async def __call__(
        self,
        *,
        domain: str,
        format: Literal["markdown"] | None = None,
    ) -> DomainWhoisResponse | str:
        body = _omit_none(
            {
                "domain": domain,
            }
        )
        return await self._call("POST", "/v1/domain/whois", body, format)


class AsyncDomainDns:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        domain: str,
        types: list[DomainDnsTypesItem] | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        domain: str,
        types: list[DomainDnsTypesItem] | None = None,
        format: None = None,
    ) -> DomainDnsResponse: ...
    async def __call__(
        self,
        *,
        domain: str,
        types: list[DomainDnsTypesItem] | None = None,
        format: Literal["markdown"] | None = None,
    ) -> DomainDnsResponse | str:
        body = _omit_none(
            {
                "domain": domain,
                "types": types,
            }
        )
        return await self._call("POST", "/v1/domain/dns", body, format)


class AsyncDomainTech:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        url: str,
        format: None = None,
    ) -> DomainTechResponse: ...
    async def __call__(
        self,
        *,
        url: str,
        format: Literal["markdown"] | None = None,
    ) -> DomainTechResponse | str:
        body = _omit_none(
            {
                "url": url,
            }
        )
        return await self._call("POST", "/v1/domain/tech", body, format)


class AsyncDomain:
    whois: AsyncDomainWhois
    dns: AsyncDomainDns
    tech: AsyncDomainTech

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.whois = AsyncDomainWhois(call)
        self.dns = AsyncDomainDns(call)
        self.tech = AsyncDomainTech(call)


class AsyncEmailCheck:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        emails: list[str],
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        emails: list[str],
        format: None = None,
    ) -> EmailCheckResponse: ...
    async def __call__(
        self,
        *,
        emails: list[str],
        format: Literal["markdown"] | None = None,
    ) -> EmailCheckResponse | str:
        body = _omit_none(
            {
                "emails": emails,
            }
        )
        return await self._call("POST", "/v1/email/check", body, format)


class AsyncEmail:
    check: AsyncEmailCheck

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.check = AsyncEmailCheck(call)


class AsyncCryptoCoins:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        currency: str | None = None,
        category: str | None = None,
        coins: list[str] | None = None,
        sort: CryptoCoinsSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        currency: str | None = None,
        category: str | None = None,
        coins: list[str] | None = None,
        sort: CryptoCoinsSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoCoinsResponse: ...
    async def __call__(
        self,
        *,
        currency: str | None = None,
        category: str | None = None,
        coins: list[str] | None = None,
        sort: CryptoCoinsSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoCoinsResponse | str:
        body = _omit_none(
            {
                "currency": currency,
                "category": category,
                "coins": coins,
                "sort": sort,
                "order": order,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/crypto/coins", body, format)


class AsyncCryptoCoin:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        coin: str,
        source: CryptoCoinsResponseDataCoinsItemSource | None = None,
        platform: str | None = None,
        currency: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        coin: str,
        source: CryptoCoinsResponseDataCoinsItemSource | None = None,
        platform: str | None = None,
        currency: str | None = None,
        format: None = None,
    ) -> CryptoCoinResponse: ...
    async def __call__(
        self,
        *,
        coin: str,
        source: CryptoCoinsResponseDataCoinsItemSource | None = None,
        platform: str | None = None,
        currency: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoCoinResponse | str:
        body = _omit_none(
            {
                "coin": coin,
                "source": source,
                "platform": platform,
                "currency": currency,
            }
        )
        return await self._call("POST", "/v1/crypto/coin", body, format)


class AsyncCryptoHistory:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        coin: str,
        currency: str | None = None,
        within: CryptoHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_candles: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        coin: str,
        currency: str | None = None,
        within: CryptoHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_candles: bool | None = None,
        format: None = None,
    ) -> CryptoHistoryResponse: ...
    async def __call__(
        self,
        *,
        coin: str,
        currency: str | None = None,
        within: CryptoHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        include_candles: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoHistoryResponse | str:
        body = _omit_none(
            {
                "coin": coin,
                "currency": currency,
                "within": within,
                "from": from_,
                "to": to,
                "includeCandles": include_candles,
            }
        )
        return await self._call("POST", "/v1/crypto/history", body, format)


class AsyncCryptoTrending:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        format: None = None,
    ) -> CryptoTrendingResponse: ...
    async def __call__(
        self,
        *,
        format: Literal["markdown"] | None = None,
    ) -> CryptoTrendingResponse | str:
        body = {}
        return await self._call("POST", "/v1/crypto/trending", body, format)


class AsyncCryptoCategories:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        sort: CryptoCategoriesSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        sort: CryptoCategoriesSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoCategoriesResponse: ...
    async def __call__(
        self,
        *,
        sort: CryptoCategoriesSort | None = None,
        order: CryptoCoinsOrder | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoCategoriesResponse | str:
        body = _omit_none(
            {
                "sort": sort,
                "order": order,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/categories", body, format)


class AsyncCryptoMovers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        within: CryptoMoversWithin | None = None,
        rank_up_to: CryptoMoversRankUpTo | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        within: CryptoMoversWithin | None = None,
        rank_up_to: CryptoMoversRankUpTo | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoMoversResponse: ...
    async def __call__(
        self,
        *,
        within: CryptoMoversWithin | None = None,
        rank_up_to: CryptoMoversRankUpTo | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoMoversResponse | str:
        body = _omit_none(
            {
                "within": within,
                "rankUpTo": rank_up_to,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/movers", body, format)


class AsyncCryptoNew:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoNewResponse: ...
    async def __call__(
        self,
        *,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoNewResponse | str:
        body = _omit_none(
            {
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/new", body, format)


class AsyncCryptoDexSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoDexSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoDexSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/dex/search", body, format)


class AsyncCryptoDexPairs:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chain: str | None = None,
        pair: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chain: str | None = None,
        pair: str,
        format: None = None,
    ) -> CryptoDexSearchResponse: ...
    async def __call__(
        self,
        *,
        chain: str | None = None,
        pair: str,
        format: Literal["markdown"] | None = None,
    ) -> CryptoDexSearchResponse | str:
        body = _omit_none(
            {
                "chain": chain,
                "pair": pair,
            }
        )
        return await self._call("POST", "/v1/crypto/dex/pairs", body, format)


class AsyncCryptoDexToken:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chain: str | None = None,
        token: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chain: str | None = None,
        token: str,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoDexTokenResponse: ...
    async def __call__(
        self,
        *,
        chain: str | None = None,
        token: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoDexTokenResponse | str:
        body = _omit_none(
            {
                "chain": chain,
                "token": token,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/dex/token", body, format)


class AsyncCryptoDexNew:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        type: CryptoDexNewType | None = None,
        chain: str | None = None,
        include_pairs: bool | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        type: CryptoDexNewType | None = None,
        chain: str | None = None,
        include_pairs: bool | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> CryptoDexNewResponse: ...
    async def __call__(
        self,
        *,
        type: CryptoDexNewType | None = None,
        chain: str | None = None,
        include_pairs: bool | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoDexNewResponse | str:
        body = _omit_none(
            {
                "type": type,
                "chain": chain,
                "includePairs": include_pairs,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/crypto/dex/new", body, format)


class AsyncCryptoDex:
    search: AsyncCryptoDexSearch
    pairs: AsyncCryptoDexPairs
    token: AsyncCryptoDexToken
    new: AsyncCryptoDexNew

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncCryptoDexSearch(call)
        self.pairs = AsyncCryptoDexPairs(call)
        self.token = AsyncCryptoDexToken(call)
        self.new = AsyncCryptoDexNew(call)


class AsyncCryptoPumpCoins:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        sort: CryptoPumpCoinsSort | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        sort: CryptoPumpCoinsSort | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoPumpCoinsResponse: ...
    async def __call__(
        self,
        *,
        sort: CryptoPumpCoinsSort | None = None,
        include_nsfw: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoPumpCoinsResponse | str:
        body = _omit_none(
            {
                "sort": sort,
                "includeNsfw": include_nsfw,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/crypto/pump/coins", body, format)


class AsyncCryptoPumpCoin:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        coin: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        coin: str,
        format: None = None,
    ) -> CryptoPumpCoinResponse: ...
    async def __call__(
        self,
        *,
        coin: str,
        format: Literal["markdown"] | None = None,
    ) -> CryptoPumpCoinResponse | str:
        body = _omit_none(
            {
                "coin": coin,
            }
        )
        return await self._call("POST", "/v1/crypto/pump/coin", body, format)


class AsyncCryptoPumpTrades:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        coin: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        coin: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoPumpTradesResponse: ...
    async def __call__(
        self,
        *,
        coin: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoPumpTradesResponse | str:
        body = _omit_none(
            {
                "coin": coin,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/crypto/pump/trades", body, format)


class AsyncCryptoPump:
    coins: AsyncCryptoPumpCoins
    coin: AsyncCryptoPumpCoin
    trades: AsyncCryptoPumpTrades

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.coins = AsyncCryptoPumpCoins(call)
        self.coin = AsyncCryptoPumpCoin(call)
        self.trades = AsyncCryptoPumpTrades(call)


class AsyncCryptoWallet:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chain: CryptoWalletChain,
        wallet: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chain: CryptoWalletChain,
        wallet: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoWalletResponse: ...
    async def __call__(
        self,
        *,
        chain: CryptoWalletChain,
        wallet: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoWalletResponse | str:
        body = _omit_none(
            {
                "chain": chain,
                "wallet": wallet,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/crypto/wallet", body, format)


class AsyncCryptoTokenHolders:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chain: CryptoTokenHoldersChain,
        token: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chain: CryptoTokenHoldersChain,
        token: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoTokenHoldersResponse: ...
    async def __call__(
        self,
        *,
        chain: CryptoTokenHoldersChain,
        token: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoTokenHoldersResponse | str:
        body = _omit_none(
            {
                "chain": chain,
                "token": token,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/crypto/token/holders", body, format)


class AsyncCryptoToken:
    holders: AsyncCryptoTokenHolders

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.holders = AsyncCryptoTokenHolders(call)


class AsyncCryptoBinanceAnnouncements:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        category: CryptoBinanceAnnouncementsCategory | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        category: CryptoBinanceAnnouncementsCategory | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> CryptoBinanceAnnouncementsResponse: ...
    async def __call__(
        self,
        *,
        category: CryptoBinanceAnnouncementsCategory | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> CryptoBinanceAnnouncementsResponse | str:
        body = _omit_none(
            {
                "category": category,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/crypto/binance/announcements", body, format)


class AsyncCryptoBinance:
    announcements: AsyncCryptoBinanceAnnouncements

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.announcements = AsyncCryptoBinanceAnnouncements(call)


class AsyncCrypto:
    coins: AsyncCryptoCoins
    coin: AsyncCryptoCoin
    history: AsyncCryptoHistory
    trending: AsyncCryptoTrending
    categories: AsyncCryptoCategories
    movers: AsyncCryptoMovers
    new: AsyncCryptoNew
    dex: AsyncCryptoDex
    pump: AsyncCryptoPump
    wallet: AsyncCryptoWallet
    token: AsyncCryptoToken
    binance: AsyncCryptoBinance

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.coins = AsyncCryptoCoins(call)
        self.coin = AsyncCryptoCoin(call)
        self.history = AsyncCryptoHistory(call)
        self.trending = AsyncCryptoTrending(call)
        self.categories = AsyncCryptoCategories(call)
        self.movers = AsyncCryptoMovers(call)
        self.new = AsyncCryptoNew(call)
        self.dex = AsyncCryptoDex(call)
        self.pump = AsyncCryptoPump(call)
        self.wallet = AsyncCryptoWallet(call)
        self.token = AsyncCryptoToken(call)
        self.binance = AsyncCryptoBinance(call)


class AsyncIndeedSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        radius_km: float | None = None,
        country: IndeedSearchCountry | None = None,
        job_type: IndeedSearchJobType | None = None,
        remote: bool | None = None,
        within: IndeedSearchWithin | None = None,
        salary: IndeedSearchSalary | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        radius_km: float | None = None,
        country: IndeedSearchCountry | None = None,
        job_type: IndeedSearchJobType | None = None,
        remote: bool | None = None,
        within: IndeedSearchWithin | None = None,
        salary: IndeedSearchSalary | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> IndeedSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        radius_km: float | None = None,
        country: IndeedSearchCountry | None = None,
        job_type: IndeedSearchJobType | None = None,
        remote: bool | None = None,
        within: IndeedSearchWithin | None = None,
        salary: IndeedSearchSalary | None = None,
        sort: LinkedinJobsSearchSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> IndeedSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "radiusKm": radius_km,
                "country": country,
                "jobType": job_type,
                "remote": remote,
                "within": within,
                "salary": salary,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/indeed/search", body, format)


class AsyncIndeedJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        job: str,
        country: IndeedSearchCountry | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        job: str,
        country: IndeedSearchCountry | None = None,
        format: None = None,
    ) -> IndeedJobResponse: ...
    async def __call__(
        self,
        *,
        job: str,
        country: IndeedSearchCountry | None = None,
        format: Literal["markdown"] | None = None,
    ) -> IndeedJobResponse | str:
        body = _omit_none(
            {
                "job": job,
                "country": country,
            }
        )
        return await self._call("POST", "/v1/indeed/job", body, format)


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

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> TripadvisorSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TripadvisorSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/tripadvisor/search", body, format)


class AsyncTripadvisorPlace:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        place: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        place: str,
        format: None = None,
    ) -> TripadvisorPlaceResponse: ...
    async def __call__(
        self,
        *,
        place: str,
        format: Literal["markdown"] | None = None,
    ) -> TripadvisorPlaceResponse | str:
        body = _omit_none(
            {
                "place": place,
            }
        )
        return await self._call("POST", "/v1/tripadvisor/place", body, format)


class AsyncTripadvisorReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        place: str,
        language: str | None = None,
        ratings: list[int] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        place: str,
        language: str | None = None,
        ratings: list[int] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TripadvisorReviewsResponse: ...
    async def __call__(
        self,
        *,
        place: str,
        language: str | None = None,
        ratings: list[int] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TripadvisorReviewsResponse | str:
        body = _omit_none(
            {
                "place": place,
                "language": language,
                "ratings": ratings,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tripadvisor/reviews", body, format)


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

    @overload
    def __call__(
        self,
        *,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        cabin: GoogletravelFlightsCabin | None = None,
        max_stops: int | None = None,
        currency: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        cabin: GoogletravelFlightsCabin | None = None,
        max_stops: int | None = None,
        currency: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> GoogletravelFlightsResponse: ...
    async def __call__(
        self,
        *,
        origin: str,
        destination: str,
        depart_date: str,
        return_date: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        cabin: GoogletravelFlightsCabin | None = None,
        max_stops: int | None = None,
        currency: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogletravelFlightsResponse | str:
        body = _omit_none(
            {
                "origin": origin,
                "destination": destination,
                "departDate": depart_date,
                "returnDate": return_date,
                "adults": adults,
                "children": children,
                "cabin": cabin,
                "maxStops": max_stops,
                "currency": currency,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/googletravel/flights", body, format)


class AsyncGoogletravel:
    flights: AsyncGoogletravelFlights

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.flights = AsyncGoogletravelFlights(call)


class AsyncShopifyProducts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        store: str,
        collection: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        store: str,
        collection: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ShopifyProductsResponse: ...
    async def __call__(
        self,
        *,
        store: str,
        collection: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ShopifyProductsResponse | str:
        body = _omit_none(
            {
                "store": store,
                "collection": collection,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/shopify/products", body, format)


class AsyncShopifyCollections:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        store: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        store: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ShopifyCollectionsResponse: ...
    async def __call__(
        self,
        *,
        store: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ShopifyCollectionsResponse | str:
        body = _omit_none(
            {
                "store": store,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/shopify/collections", body, format)


class AsyncShopifyStore:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        store: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        store: str,
        format: None = None,
    ) -> ShopifyStoreResponse: ...
    async def __call__(
        self,
        *,
        store: str,
        format: Literal["markdown"] | None = None,
    ) -> ShopifyStoreResponse | str:
        body = _omit_none(
            {
                "store": store,
            }
        )
        return await self._call("POST", "/v1/shopify/store", body, format)


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

    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: WalmartSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: WalmartSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> WalmartSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        sort: WalmartSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> WalmartSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "price": price,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/walmart/search", body, format)


class AsyncWalmartProduct:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        product: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        product: str,
        format: None = None,
    ) -> WalmartProductResponse: ...
    async def __call__(
        self,
        *,
        product: str,
        format: Literal["markdown"] | None = None,
    ) -> WalmartProductResponse | str:
        body = _omit_none(
            {
                "product": product,
            }
        )
        return await self._call("POST", "/v1/walmart/product", body, format)


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

    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: AliexpressSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: AliexpressSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AliexpressSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        sort: AliexpressSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AliexpressSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "price": price,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/aliexpress/search", body, format)


class AsyncAliexpressProduct:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        product: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        product: str,
        format: None = None,
    ) -> AliexpressProductResponse: ...
    async def __call__(
        self,
        *,
        product: str,
        format: Literal["markdown"] | None = None,
    ) -> AliexpressProductResponse | str:
        body = _omit_none(
            {
                "product": product,
            }
        )
        return await self._call("POST", "/v1/aliexpress/product", body, format)


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

    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        format: None = None,
    ) -> AppstoreAppResponse: ...
    async def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AppstoreAppResponse | str:
        body = _omit_none(
            {
                "app": app,
                "country": country,
            }
        )
        return await self._call("POST", "/v1/appstore/app", body, format)


class AsyncAppstoreSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        device: AppstoreSearchDevice | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        device: AppstoreSearchDevice | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> AppstoreSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        device: AppstoreSearchDevice | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AppstoreSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "device": device,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/appstore/search", body, format)


class AsyncAppstoreReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AppstoreReviewsResponse: ...
    async def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AppstoreReviewsResponse | str:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/appstore/reviews", body, format)


class AsyncAppstoreTop:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        chart: AppstoreTopChart | None = None,
        device: AppstoreSearchDevice | None = None,
        genre: int | None = None,
        country: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        chart: AppstoreTopChart | None = None,
        device: AppstoreSearchDevice | None = None,
        genre: int | None = None,
        country: str | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> AppstoreTopResponse: ...
    async def __call__(
        self,
        *,
        chart: AppstoreTopChart | None = None,
        device: AppstoreSearchDevice | None = None,
        genre: int | None = None,
        country: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AppstoreTopResponse | str:
        body = _omit_none(
            {
                "chart": chart,
                "device": device,
                "genre": genre,
                "country": country,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/appstore/top", body, format)


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

    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        format: None = None,
    ) -> GoogleplayAppResponse: ...
    async def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleplayAppResponse | str:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/googleplay/app", body, format)


class AsyncGoogleplaySearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: None = None,
    ) -> GoogleplaySearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleplaySearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/googleplay/search", body, format)


class AsyncGoogleplayReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        sort: GoogleplayReviewsSort | None = None,
        rating: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        sort: GoogleplayReviewsSort | None = None,
        rating: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> GoogleplayReviewsResponse: ...
    async def __call__(
        self,
        *,
        app: str,
        country: str | None = None,
        language: str | None = None,
        sort: GoogleplayReviewsSort | None = None,
        rating: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> GoogleplayReviewsResponse | str:
        body = _omit_none(
            {
                "app": app,
                "country": country,
                "language": language,
                "sort": sort,
                "rating": rating,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/googleplay/reviews", body, format)


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

    @overload
    def __call__(
        self,
        *,
        location: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        infants: int | None = None,
        pets: int | None = None,
        price: ZillowSearchPrice | None = None,
        currency: str | None = None,
        room_type: AirbnbSearchRoomType | None = None,
        bedrooms: AirbnbSearchBedrooms | None = None,
        bathrooms: AirbnbSearchBathrooms | None = None,
        amenities: list[AirbnbSearchAmenitiesItem] | None = None,
        superhost: bool | None = None,
        instant_book: bool | None = None,
        guest_favorite: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        infants: int | None = None,
        pets: int | None = None,
        price: ZillowSearchPrice | None = None,
        currency: str | None = None,
        room_type: AirbnbSearchRoomType | None = None,
        bedrooms: AirbnbSearchBedrooms | None = None,
        bathrooms: AirbnbSearchBathrooms | None = None,
        amenities: list[AirbnbSearchAmenitiesItem] | None = None,
        superhost: bool | None = None,
        instant_book: bool | None = None,
        guest_favorite: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AirbnbSearchResponse: ...
    async def __call__(
        self,
        *,
        location: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        children: int | None = None,
        infants: int | None = None,
        pets: int | None = None,
        price: ZillowSearchPrice | None = None,
        currency: str | None = None,
        room_type: AirbnbSearchRoomType | None = None,
        bedrooms: AirbnbSearchBedrooms | None = None,
        bathrooms: AirbnbSearchBathrooms | None = None,
        amenities: list[AirbnbSearchAmenitiesItem] | None = None,
        superhost: bool | None = None,
        instant_book: bool | None = None,
        guest_favorite: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AirbnbSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "checkIn": check_in,
                "checkOut": check_out,
                "adults": adults,
                "children": children,
                "infants": infants,
                "pets": pets,
                "price": price,
                "currency": currency,
                "roomType": room_type,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "amenities": amenities,
                "superhost": superhost,
                "instantBook": instant_book,
                "guestFavorite": guest_favorite,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/airbnb/search", body, format)


class AsyncAirbnbListing:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        listing: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        listing: str,
        format: None = None,
    ) -> AirbnbListingResponse: ...
    async def __call__(
        self,
        *,
        listing: str,
        format: Literal["markdown"] | None = None,
    ) -> AirbnbListingResponse | str:
        body = _omit_none(
            {
                "listing": listing,
            }
        )
        return await self._call("POST", "/v1/airbnb/listing", body, format)


class AsyncAirbnbCalendar:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        listing: str,
        month: str | None = None,
        months: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        listing: str,
        month: str | None = None,
        months: int | None = None,
        format: None = None,
    ) -> AirbnbCalendarResponse: ...
    async def __call__(
        self,
        *,
        listing: str,
        month: str | None = None,
        months: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AirbnbCalendarResponse | str:
        body = _omit_none(
            {
                "listing": listing,
                "month": month,
                "months": months,
            }
        )
        return await self._call("POST", "/v1/airbnb/calendar", body, format)


class AsyncAirbnbReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        listing: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        listing: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> AirbnbReviewsResponse: ...
    async def __call__(
        self,
        *,
        listing: str,
        sort: MapsReviewsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> AirbnbReviewsResponse | str:
        body = _omit_none(
            {
                "listing": listing,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/airbnb/reviews", body, format)


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


class AsyncRedfinSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RedfinSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RedfinSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: RedfinSearchBathrooms | None = None,
        home_types: list[RedfinSearchHomeTypesItem] | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        days_on_market: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RedfinSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RedfinSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: RedfinSearchBathrooms | None = None,
        home_types: list[RedfinSearchHomeTypesItem] | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        days_on_market: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RedfinSearchResponse: ...
    async def __call__(
        self,
        *,
        location: str,
        status: RedfinSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RedfinSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: RedfinSearchBathrooms | None = None,
        home_types: list[RedfinSearchHomeTypesItem] | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        days_on_market: ZillowSearchPrice | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RedfinSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "soldWithin": sold_within,
                "sort": sort,
                "price": price,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "homeTypes": home_types,
                "sqft": sqft,
                "lotSqft": lot_sqft,
                "yearBuilt": year_built,
                "daysOnMarket": days_on_market,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/redfin/search", body, format)


class AsyncRedfinProperty:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        property: str,
        format: None = None,
    ) -> RedfinPropertyResponse: ...
    async def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"] | None = None,
    ) -> RedfinPropertyResponse | str:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return await self._call("POST", "/v1/redfin/property", body, format)


class AsyncRedfin:
    search: AsyncRedfinSearch
    property: AsyncRedfinProperty

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncRedfinSearch(call)
        self.property = AsyncRedfinProperty(call)


class AsyncRealtorSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RealtorSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RealtorSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[RealtorSearchHomeTypesItem] | None = None,
        new_construction: bool | None = None,
        foreclosure: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RealtorSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RealtorSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[RealtorSearchHomeTypesItem] | None = None,
        new_construction: bool | None = None,
        foreclosure: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RealtorSearchResponse: ...
    async def __call__(
        self,
        *,
        location: str,
        status: RealtorSearchStatus | None = None,
        sold_within: RedfinSearchSoldWithin | None = None,
        sort: RealtorSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        bathrooms: ZillowSearchPrice | None = None,
        sqft: ZillowSearchPrice | None = None,
        lot_sqft: ZillowSearchPrice | None = None,
        year_built: ZillowSearchPrice | None = None,
        hoa: ZillowSearchHoa | None = None,
        home_types: list[RealtorSearchHomeTypesItem] | None = None,
        new_construction: bool | None = None,
        foreclosure: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RealtorSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "soldWithin": sold_within,
                "sort": sort,
                "price": price,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "sqft": sqft,
                "lotSqft": lot_sqft,
                "yearBuilt": year_built,
                "hoa": hoa,
                "homeTypes": home_types,
                "newConstruction": new_construction,
                "foreclosure": foreclosure,
                "queries": queries,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/realtor/search", body, format)


class AsyncRealtorProperty:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        property: str,
        format: None = None,
    ) -> RealtorPropertyResponse: ...
    async def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"] | None = None,
    ) -> RealtorPropertyResponse | str:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return await self._call("POST", "/v1/realtor/property", body, format)


class AsyncRealtor:
    search: AsyncRealtorSearch
    property: AsyncRealtorProperty

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncRealtorSearch(call)
        self.property = AsyncRealtorProperty(call)


class AsyncRightmoveSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RightmoveSearchStatus | None = None,
        sort: RightmoveSearchSort | None = None,
        radius_km: float | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        property_types: list[RightmoveSearchPropertyTypesItem] | None = None,
        must_have: list[RightmoveSearchMustHaveItem] | None = None,
        within: RightmoveSearchWithin | None = None,
        include_under_offer: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        status: RightmoveSearchStatus | None = None,
        sort: RightmoveSearchSort | None = None,
        radius_km: float | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        property_types: list[RightmoveSearchPropertyTypesItem] | None = None,
        must_have: list[RightmoveSearchMustHaveItem] | None = None,
        within: RightmoveSearchWithin | None = None,
        include_under_offer: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> RightmoveSearchResponse: ...
    async def __call__(
        self,
        *,
        location: str,
        status: RightmoveSearchStatus | None = None,
        sort: RightmoveSearchSort | None = None,
        radius_km: float | None = None,
        price: ZillowSearchPrice | None = None,
        bedrooms: ZillowSearchPrice | None = None,
        property_types: list[RightmoveSearchPropertyTypesItem] | None = None,
        must_have: list[RightmoveSearchMustHaveItem] | None = None,
        within: RightmoveSearchWithin | None = None,
        include_under_offer: bool | None = None,
        queries: list[str] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> RightmoveSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "sort": sort,
                "radiusKm": radius_km,
                "price": price,
                "bedrooms": bedrooms,
                "propertyTypes": property_types,
                "mustHave": must_have,
                "within": within,
                "includeUnderOffer": include_under_offer,
                "queries": queries,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/rightmove/search", body, format)


class AsyncRightmoveProperty:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        property: str,
        format: None = None,
    ) -> RightmovePropertyResponse: ...
    async def __call__(
        self,
        *,
        property: str,
        format: Literal["markdown"] | None = None,
    ) -> RightmovePropertyResponse | str:
        body = _omit_none(
            {
                "property": property,
            }
        )
        return await self._call("POST", "/v1/rightmove/property", body, format)


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

    @overload
    def __call__(
        self,
        *,
        location: str,
        type: ImmoscoutSearchType | None = None,
        sort: ImmoscoutSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        rooms: ZillowSearchPrice | None = None,
        living_space: ZillowSearchPrice | None = None,
        equipment: list[ImmoscoutSearchEquipmentItem] | None = None,
        new_construction: bool | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        location: str,
        type: ImmoscoutSearchType | None = None,
        sort: ImmoscoutSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        rooms: ZillowSearchPrice | None = None,
        living_space: ZillowSearchPrice | None = None,
        equipment: list[ImmoscoutSearchEquipmentItem] | None = None,
        new_construction: bool | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> ImmoscoutSearchResponse: ...
    async def __call__(
        self,
        *,
        location: str,
        type: ImmoscoutSearchType | None = None,
        sort: ImmoscoutSearchSort | None = None,
        price: ZillowSearchPrice | None = None,
        rooms: ZillowSearchPrice | None = None,
        living_space: ZillowSearchPrice | None = None,
        equipment: list[ImmoscoutSearchEquipmentItem] | None = None,
        new_construction: bool | None = None,
        query: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> ImmoscoutSearchResponse | str:
        body = _omit_none(
            {
                "location": location,
                "type": type,
                "sort": sort,
                "price": price,
                "rooms": rooms,
                "livingSpace": living_space,
                "equipment": equipment,
                "newConstruction": new_construction,
                "query": query,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/immoscout/search", body, format)


class AsyncImmoscoutListing:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        listing: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        listing: str,
        format: None = None,
    ) -> ImmoscoutListingResponse: ...
    async def __call__(
        self,
        *,
        listing: str,
        format: Literal["markdown"] | None = None,
    ) -> ImmoscoutListingResponse | str:
        body = _omit_none(
            {
                "listing": listing,
            }
        )
        return await self._call("POST", "/v1/immoscout/listing", body, format)


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

    @overload
    def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> PinterestSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> PinterestSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/pinterest/search", body, format)


class AsyncPinterestPin:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        pin: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        pin: str,
        format: None = None,
    ) -> PinterestPinResponse: ...
    async def __call__(
        self,
        *,
        pin: str,
        format: Literal["markdown"] | None = None,
    ) -> PinterestPinResponse | str:
        body = _omit_none(
            {
                "pin": pin,
            }
        )
        return await self._call("POST", "/v1/pinterest/pin", body, format)


class AsyncPinterestBoard:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        board: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        board: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> PinterestBoardResponse: ...
    async def __call__(
        self,
        *,
        board: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> PinterestBoardResponse | str:
        body = _omit_none(
            {
                "board": board,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/pinterest/board", body, format)


class AsyncPinterestUser:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> PinterestUserResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> PinterestUserResponse | str:
        body = _omit_none(
            {
                "user": user,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/pinterest/user", body, format)


class AsyncPinterestAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        country: str,
        advertiser: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        country: str,
        advertiser: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> PinterestAdsSearchResponse: ...
    async def __call__(
        self,
        *,
        country: str,
        advertiser: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> PinterestAdsSearchResponse | str:
        body = _omit_none(
            {
                "country": country,
                "advertiser": advertiser,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/pinterest/ads/search", body, format)


class AsyncPinterestAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> PinterestAdsAdResponse: ...
    async def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> PinterestAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return await self._call("POST", "/v1/pinterest/ads/ad", body, format)


class AsyncPinterestAds:
    search: AsyncPinterestAdsSearch
    ad: AsyncPinterestAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncPinterestAdsSearch(call)
        self.ad = AsyncPinterestAdsAd(call)


class AsyncPinterest:
    search: AsyncPinterestSearch
    pin: AsyncPinterestPin
    board: AsyncPinterestBoard
    user: AsyncPinterestUser
    ads: AsyncPinterestAds

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncPinterestSearch(call)
        self.pin = AsyncPinterestPin(call)
        self.board = AsyncPinterestBoard(call)
        self.user = AsyncPinterestUser(call)
        self.ads = AsyncPinterestAds(call)


class AsyncXTweet:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        tweet: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        tweet: str,
        format: None = None,
    ) -> XTweetResponse: ...
    async def __call__(
        self,
        *,
        tweet: str,
        format: Literal["markdown"] | None = None,
    ) -> XTweetResponse | str:
        body = _omit_none(
            {
                "tweet": tweet,
            }
        )
        return await self._call("POST", "/v1/x/tweet", body, format)


class AsyncX:
    tweet: AsyncXTweet

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.tweet = AsyncXTweet(call)


class AsyncKickChannel:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        format: None = None,
    ) -> KickChannelResponse: ...
    async def __call__(
        self,
        *,
        channel: str,
        format: Literal["markdown"] | None = None,
    ) -> KickChannelResponse | str:
        body = _omit_none(
            {
                "channel": channel,
            }
        )
        return await self._call("POST", "/v1/kick/channel", body, format)


class AsyncKickVideos:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        format: None = None,
    ) -> KickVideosResponse: ...
    async def __call__(
        self,
        *,
        channel: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> KickVideosResponse | str:
        body = _omit_none(
            {
                "channel": channel,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/kick/videos", body, format)


class AsyncKickClips:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        channel: str,
        sort: YoutubeCommentsSort | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        channel: str,
        sort: YoutubeCommentsSort | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> KickClipsResponse: ...
    async def __call__(
        self,
        *,
        channel: str,
        sort: YoutubeCommentsSort | None = None,
        within: LinkedinJobsSearchWithin | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> KickClipsResponse | str:
        body = _omit_none(
            {
                "channel": channel,
                "sort": sort,
                "within": within,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/kick/clips", body, format)


class AsyncKick:
    channel: AsyncKickChannel
    videos: AsyncKickVideos
    clips: AsyncKickClips

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.channel = AsyncKickChannel(call)
        self.videos = AsyncKickVideos(call)
        self.clips = AsyncKickClips(call)


class AsyncFinanceQuote:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        symbols: list[str],
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        symbols: list[str],
        format: None = None,
    ) -> FinanceQuoteResponse: ...
    async def __call__(
        self,
        *,
        symbols: list[str],
        format: Literal["markdown"] | None = None,
    ) -> FinanceQuoteResponse | str:
        body = _omit_none(
            {
                "symbols": symbols,
            }
        )
        return await self._call("POST", "/v1/finance/quote", body, format)


class AsyncFinanceHistory:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        symbol: str,
        within: FinanceHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        interval: FinanceHistoryInterval | None = None,
        include_extended_hours: bool | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        symbol: str,
        within: FinanceHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        interval: FinanceHistoryInterval | None = None,
        include_extended_hours: bool | None = None,
        format: None = None,
    ) -> FinanceHistoryResponse: ...
    async def __call__(
        self,
        *,
        symbol: str,
        within: FinanceHistoryWithin | None = None,
        from_: str | None = None,
        to: str | None = None,
        interval: FinanceHistoryInterval | None = None,
        include_extended_hours: bool | None = None,
        format: Literal["markdown"] | None = None,
    ) -> FinanceHistoryResponse | str:
        body = _omit_none(
            {
                "symbol": symbol,
                "within": within,
                "from": from_,
                "to": to,
                "interval": interval,
                "includeExtendedHours": include_extended_hours,
            }
        )
        return await self._call("POST", "/v1/finance/history", body, format)


class AsyncFinanceSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        quotes_limit: int | None = None,
        news_limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        quotes_limit: int | None = None,
        news_limit: int | None = None,
        format: None = None,
    ) -> FinanceSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        quotes_limit: int | None = None,
        news_limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> FinanceSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "quotesLimit": quotes_limit,
                "newsLimit": news_limit,
            }
        )
        return await self._call("POST", "/v1/finance/search", body, format)


class AsyncFinanceProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        symbol: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        symbol: str,
        format: None = None,
    ) -> FinanceProfileResponse: ...
    async def __call__(
        self,
        *,
        symbol: str,
        format: Literal["markdown"] | None = None,
    ) -> FinanceProfileResponse | str:
        body = _omit_none(
            {
                "symbol": symbol,
            }
        )
        return await self._call("POST", "/v1/finance/profile", body, format)


class AsyncFinance:
    quote: AsyncFinanceQuote
    history: AsyncFinanceHistory
    search: AsyncFinanceSearch
    profile: AsyncFinanceProfile

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.quote = AsyncFinanceQuote(call)
        self.history = AsyncFinanceHistory(call)
        self.search = AsyncFinanceSearch(call)
        self.profile = AsyncFinanceProfile(call)


class AsyncMicrosoftAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        countries: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        countries: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> MicrosoftAdsSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        countries: list[str] | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MicrosoftAdsSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "countries": countries,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/microsoft/ads/search", body, format)


class AsyncMicrosoftAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> MicrosoftAdsAdResponse: ...
    async def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> MicrosoftAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return await self._call("POST", "/v1/microsoft/ads/ad", body, format)


class AsyncMicrosoftAdsAdvertisers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: None = None,
    ) -> MicrosoftAdsAdvertisersResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        limit: int | None = None,
        format: Literal["markdown"] | None = None,
    ) -> MicrosoftAdsAdvertisersResponse | str:
        body = _omit_none(
            {
                "query": query,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/microsoft/ads/advertisers", body, format)


class AsyncMicrosoftAds:
    search: AsyncMicrosoftAdsSearch
    ad: AsyncMicrosoftAdsAd
    advertisers: AsyncMicrosoftAdsAdvertisers

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncMicrosoftAdsSearch(call)
        self.ad = AsyncMicrosoftAdsAd(call)
        self.advertisers = AsyncMicrosoftAdsAdvertisers(call)


class AsyncMicrosoft:
    ads: AsyncMicrosoftAds

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.ads = AsyncMicrosoftAds(call)


class AsyncSnapchatProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        user: str,
        format: None = None,
    ) -> SnapchatProfileResponse: ...
    async def __call__(
        self,
        *,
        user: str,
        format: Literal["markdown"] | None = None,
    ) -> SnapchatProfileResponse | str:
        body = _omit_none(
            {
                "user": user,
            }
        )
        return await self._call("POST", "/v1/snapchat/profile", body, format)


class AsyncSnapchatAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        advertiser: str,
        countries: list[str] | None = None,
        status: SnapchatAdsSearchStatus | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        advertiser: str,
        countries: list[str] | None = None,
        status: SnapchatAdsSearchStatus | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> SnapchatAdsSearchResponse: ...
    async def __call__(
        self,
        *,
        advertiser: str,
        countries: list[str] | None = None,
        status: SnapchatAdsSearchStatus | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> SnapchatAdsSearchResponse | str:
        body = _omit_none(
            {
                "advertiser": advertiser,
                "countries": countries,
                "status": status,
                "from": from_,
                "to": to,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/snapchat/ads/search", body, format)


class AsyncSnapchatAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        ad: str,
        format: None = None,
    ) -> SnapchatAdsAdResponse: ...
    async def __call__(
        self,
        *,
        ad: str,
        format: Literal["markdown"] | None = None,
    ) -> SnapchatAdsAdResponse | str:
        body = _omit_none(
            {
                "ad": ad,
            }
        )
        return await self._call("POST", "/v1/snapchat/ads/ad", body, format)


class AsyncSnapchatAds:
    search: AsyncSnapchatAdsSearch
    ad: AsyncSnapchatAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncSnapchatAdsSearch(call)
        self.ad = AsyncSnapchatAdsAd(call)


class AsyncSnapchat:
    profile: AsyncSnapchatProfile
    ads: AsyncSnapchatAds

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncSnapchatProfile(call)
        self.ads = AsyncSnapchatAds(call)


class AsyncTumblrBlog:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        blog: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        blog: str,
        format: None = None,
    ) -> TumblrBlogResponse: ...
    async def __call__(
        self,
        *,
        blog: str,
        format: Literal["markdown"] | None = None,
    ) -> TumblrBlogResponse | str:
        body = _omit_none(
            {
                "blog": blog,
            }
        )
        return await self._call("POST", "/v1/tumblr/blog", body, format)


class AsyncTumblrPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        blog: str,
        tag: str | None = None,
        type: TumblrPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        blog: str,
        tag: str | None = None,
        type: TumblrPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TumblrPostsResponse: ...
    async def __call__(
        self,
        *,
        blog: str,
        tag: str | None = None,
        type: TumblrPostsType | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TumblrPostsResponse | str:
        body = _omit_none(
            {
                "blog": blog,
                "tag": tag,
                "type": type,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tumblr/posts", body, format)


class AsyncTumblrPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        post: str,
        format: None = None,
    ) -> TumblrPostResponse: ...
    async def __call__(
        self,
        *,
        post: str,
        format: Literal["markdown"] | None = None,
    ) -> TumblrPostResponse | str:
        body = _omit_none(
            {
                "post": post,
            }
        )
        return await self._call("POST", "/v1/tumblr/post", body, format)


class AsyncTumblrSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        query: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: None = None,
    ) -> TumblrSearchResponse: ...
    async def __call__(
        self,
        *,
        query: str,
        sort: YoutubeCommentsSort | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        format: Literal["markdown"] | None = None,
    ) -> TumblrSearchResponse | str:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "limit": limit,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tumblr/search", body, format)


class AsyncTumblr:
    blog: AsyncTumblrBlog
    posts: AsyncTumblrPosts
    post: AsyncTumblrPost
    search: AsyncTumblrSearch

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.blog = AsyncTumblrBlog(call)
        self.posts = AsyncTumblrPosts(call)
        self.post = AsyncTumblrPost(call)
        self.search = AsyncTumblrSearch(call)


class AsyncQuoraQuestion:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    @overload
    def __call__(
        self,
        *,
        question: str,
        format: Literal["markdown"],
    ) -> str: ...
    @overload
    def __call__(
        self,
        *,
        question: str,
        format: None = None,
    ) -> QuoraQuestionResponse: ...
    async def __call__(
        self,
        *,
        question: str,
        format: Literal["markdown"] | None = None,
    ) -> QuoraQuestionResponse | str:
        body = _omit_none(
            {
                "question": question,
            }
        )
        return await self._call("POST", "/v1/quora/question", body, format)


class AsyncQuora:
    question: AsyncQuoraQuestion

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.question = AsyncQuoraQuestion(call)


class AsyncSurface:
    endpoints: AsyncEndpoints
    web: AsyncWeb
    youtube: AsyncYoutube
    reddit: AsyncReddit
    maps: AsyncMaps
    instagram: AsyncInstagram
    tiktok: AsyncTiktok
    bluesky: AsyncBluesky
    mastodon: AsyncMastodon
    threads: AsyncThreads
    telegram: AsyncTelegram
    meta: AsyncMeta
    linkedin: AsyncLinkedin
    zillow: AsyncZillow
    google: AsyncGoogle
    upwork: AsyncUpwork
    amazon: AsyncAmazon
    site: AsyncSite
    domain: AsyncDomain
    email: AsyncEmail
    crypto: AsyncCrypto
    indeed: AsyncIndeed
    tripadvisor: AsyncTripadvisor
    googletravel: AsyncGoogletravel
    shopify: AsyncShopify
    walmart: AsyncWalmart
    aliexpress: AsyncAliexpress
    appstore: AsyncAppstore
    googleplay: AsyncGoogleplay
    airbnb: AsyncAirbnb
    redfin: AsyncRedfin
    realtor: AsyncRealtor
    rightmove: AsyncRightmove
    immoscout: AsyncImmoscout
    pinterest: AsyncPinterest
    x: AsyncX
    kick: AsyncKick
    finance: AsyncFinance
    microsoft: AsyncMicrosoft
    snapchat: AsyncSnapchat
    tumblr: AsyncTumblr
    quora: AsyncQuora

    def __init__(self, call: AsyncCall) -> None:
        self.endpoints = AsyncEndpoints(call)
        self.web = AsyncWeb(call)
        self.youtube = AsyncYoutube(call)
        self.reddit = AsyncReddit(call)
        self.maps = AsyncMaps(call)
        self.instagram = AsyncInstagram(call)
        self.tiktok = AsyncTiktok(call)
        self.bluesky = AsyncBluesky(call)
        self.mastodon = AsyncMastodon(call)
        self.threads = AsyncThreads(call)
        self.telegram = AsyncTelegram(call)
        self.meta = AsyncMeta(call)
        self.linkedin = AsyncLinkedin(call)
        self.zillow = AsyncZillow(call)
        self.google = AsyncGoogle(call)
        self.upwork = AsyncUpwork(call)
        self.amazon = AsyncAmazon(call)
        self.site = AsyncSite(call)
        self.domain = AsyncDomain(call)
        self.email = AsyncEmail(call)
        self.crypto = AsyncCrypto(call)
        self.indeed = AsyncIndeed(call)
        self.tripadvisor = AsyncTripadvisor(call)
        self.googletravel = AsyncGoogletravel(call)
        self.shopify = AsyncShopify(call)
        self.walmart = AsyncWalmart(call)
        self.aliexpress = AsyncAliexpress(call)
        self.appstore = AsyncAppstore(call)
        self.googleplay = AsyncGoogleplay(call)
        self.airbnb = AsyncAirbnb(call)
        self.redfin = AsyncRedfin(call)
        self.realtor = AsyncRealtor(call)
        self.rightmove = AsyncRightmove(call)
        self.immoscout = AsyncImmoscout(call)
        self.pinterest = AsyncPinterest(call)
        self.x = AsyncX(call)
        self.kick = AsyncKick(call)
        self.finance = AsyncFinance(call)
        self.microsoft = AsyncMicrosoft(call)
        self.snapchat = AsyncSnapchat(call)
        self.tumblr = AsyncTumblr(call)
        self.quora = AsyncQuora(call)
