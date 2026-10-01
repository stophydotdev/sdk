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
    EndpointCatalog,
    GoogletravelFlightsCabin,
    GoogletravelFlightsResponse,
    ImmoscoutListingResponse,
    ImmoscoutSearchResponse,
    ImmoscoutSearchSort,
    ImmoscoutSearchType,
    InstagramCommentsResponse,
    InstagramPostResponse,
    InstagramProfileResponse,
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
    MetaAdsPageMediaType,
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
    TiktokCommentsResponse,
    TiktokHashtagResponse,
    TiktokProfileResponse,
    TiktokSearchResponse,
    TiktokSearchType,
    TiktokVideoResponse,
    TranscriptResponse,
    UpworkJobResponse,
    UpworkSearchExperience,
    UpworkSearchJobType,
    UpworkSearchResponse,
    UpworkSearchSort,
    WebSearchResponse,
    WebSearchWithin,
    YoutubeChannelResponse,
    YoutubeChannelTab,
    YoutubeCommentsResponse,
    YoutubeCommentsSort,
    YoutubePlaylistResponse,
    YoutubeSearchResponse,
    YoutubeSearchSort,
    YoutubeSearchType,
    YoutubeSearchWithin,
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


class SyncWeb:
    search: SyncWebSearch

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncWebSearch(call)


class SyncYoutubeSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        within: YoutubeSearchWithin | None = None,
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
        within: YoutubeSearchWithin | None = None,
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
        within: YoutubeSearchWithin | None = None,
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
        limit: int | None = None,
    ) -> InstagramProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
                "limit": limit,
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
    comments: SyncInstagramComments

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncInstagramProfile(call)
        self.post = SyncInstagramPost(call)
        self.comments = SyncInstagramComments(call)


class SyncTiktokProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TiktokProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
                "limit": limit,
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


class SyncMetaAdsPage:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        media_type: MetaAdsPageMediaType | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> MetaAdsPageResponse:
        body = _omit_none(
            {
                "page": page,
                "country": country,
                "status": status,
                "mediaType": media_type,
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
        media_type: MetaAdsPageMediaType | None = None,
        cursor: str | None = None,
        network: Literal["meta"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    def __call__(
        self,
        *,
        query: str | None = None,
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
        query: str | None = None,
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
        media_type: MetaAdsPageMediaType | AdsSearchOption1MediaType | None = None,
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
        within: AdsSearchOption3Within | None = None,
    ) -> AdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "status": status,
                "mediaType": media_type,
                "cursor": cursor,
                "network": network,
                "limit": limit,
                "advertiser": advertiser,
                "domain": domain,
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


class SyncSurface:
    endpoints: SyncEndpoints
    web: SyncWeb
    youtube: SyncYoutube
    transcript: SyncTranscript
    reddit: SyncReddit
    maps: SyncMaps
    instagram: SyncInstagram
    tiktok: SyncTiktok
    meta: SyncMeta
    linkedin: SyncLinkedin
    zillow: SyncZillow
    upwork: SyncUpwork
    googletravel: SyncGoogletravel
    airbnb: SyncAirbnb
    rightmove: SyncRightmove
    immoscout: SyncImmoscout
    pinterest: SyncPinterest
    ads: SyncAds

    def __init__(self, call: SyncCall) -> None:
        self.endpoints = SyncEndpoints(call)
        self.web = SyncWeb(call)
        self.youtube = SyncYoutube(call)
        self.transcript = SyncTranscript(call)
        self.reddit = SyncReddit(call)
        self.maps = SyncMaps(call)
        self.instagram = SyncInstagram(call)
        self.tiktok = SyncTiktok(call)
        self.meta = SyncMeta(call)
        self.linkedin = SyncLinkedin(call)
        self.zillow = SyncZillow(call)
        self.upwork = SyncUpwork(call)
        self.googletravel = SyncGoogletravel(call)
        self.airbnb = SyncAirbnb(call)
        self.rightmove = SyncRightmove(call)
        self.immoscout = SyncImmoscout(call)
        self.pinterest = SyncPinterest(call)
        self.ads = SyncAds(call)


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


class AsyncWeb:
    search: AsyncWebSearch

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncWebSearch(call)


class AsyncYoutubeSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        within: YoutubeSearchWithin | None = None,
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
        within: YoutubeSearchWithin | None = None,
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
        within: YoutubeSearchWithin | None = None,
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
        limit: int | None = None,
    ) -> InstagramProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
                "limit": limit,
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
    comments: AsyncInstagramComments

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncInstagramProfile(call)
        self.post = AsyncInstagramPost(call)
        self.comments = AsyncInstagramComments(call)


class AsyncTiktokProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile: str,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> TiktokProfileResponse:
        body = _omit_none(
            {
                "profile": profile,
                "cursor": cursor,
                "limit": limit,
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


class AsyncMetaAdsPage:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        page: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        media_type: MetaAdsPageMediaType | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> MetaAdsPageResponse:
        body = _omit_none(
            {
                "page": page,
                "country": country,
                "status": status,
                "mediaType": media_type,
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
        media_type: MetaAdsPageMediaType | None = None,
        cursor: str | None = None,
        network: Literal["meta"],
        limit: int | None = None,
    ) -> AdsSearchResponse: ...
    @overload
    async def __call__(
        self,
        *,
        query: str | None = None,
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
        query: str | None = None,
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
        media_type: MetaAdsPageMediaType | AdsSearchOption1MediaType | None = None,
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
        within: AdsSearchOption3Within | None = None,
    ) -> AdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "status": status,
                "mediaType": media_type,
                "cursor": cursor,
                "network": network,
                "limit": limit,
                "advertiser": advertiser,
                "domain": domain,
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


class AsyncSurface:
    endpoints: AsyncEndpoints
    web: AsyncWeb
    youtube: AsyncYoutube
    transcript: AsyncTranscript
    reddit: AsyncReddit
    maps: AsyncMaps
    instagram: AsyncInstagram
    tiktok: AsyncTiktok
    meta: AsyncMeta
    linkedin: AsyncLinkedin
    zillow: AsyncZillow
    upwork: AsyncUpwork
    googletravel: AsyncGoogletravel
    airbnb: AsyncAirbnb
    rightmove: AsyncRightmove
    immoscout: AsyncImmoscout
    pinterest: AsyncPinterest
    ads: AsyncAds

    def __init__(self, call: AsyncCall) -> None:
        self.endpoints = AsyncEndpoints(call)
        self.web = AsyncWeb(call)
        self.youtube = AsyncYoutube(call)
        self.transcript = AsyncTranscript(call)
        self.reddit = AsyncReddit(call)
        self.maps = AsyncMaps(call)
        self.instagram = AsyncInstagram(call)
        self.tiktok = AsyncTiktok(call)
        self.meta = AsyncMeta(call)
        self.linkedin = AsyncLinkedin(call)
        self.zillow = AsyncZillow(call)
        self.upwork = AsyncUpwork(call)
        self.googletravel = AsyncGoogletravel(call)
        self.airbnb = AsyncAirbnb(call)
        self.rightmove = AsyncRightmove(call)
        self.immoscout = AsyncImmoscout(call)
        self.pinterest = AsyncPinterest(call)
        self.ads = AsyncAds(call)
