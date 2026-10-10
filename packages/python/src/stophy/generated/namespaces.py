"""Generated from openapi.json by scripts/gen_python.py. Do not edit."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Protocol

from .models import (
    AirbnbListingResponse,
    AirbnbReviewsResponse,
    AirbnbSearchCurrency,
    AirbnbSearchResponse,
    AirbnbSearchRoomType,
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
    AppstoreTopGenre,
    AppstoreTopResponse,
    BookingHotelResponse,
    BookingHotelReviewsResponse,
    BookingHotelReviewsSort,
    BookingSearchResponse,
    BookingSearchSort,
    CareersJobResponse,
    CareersJobsResponse,
    EbayItemResponse,
    EbaySearchCondition,
    EbaySearchResponse,
    EbaySearchSort,
    EndpointCatalog,
    FacebookMarketplaceSearchResponse,
    FacebookMarketplaceSearchSort,
    FacebookPagePostsResponse,
    FacebookPageResponse,
    FacebookPostCommentsResponse,
    FacebookPostResponse,
    GoogleAdsAdResponse,
    GoogleAdsAdvertisersResponse,
    GoogleAdsSearchMediaType,
    GoogleAdsSearchPlatform,
    GoogleAdsSearchResponse,
    GoogleAiModeResponse,
    GoogleFlightsArrivalTime,
    GoogleFlightsCabin,
    GoogleFlightsDepartureTime,
    GoogleFlightsResponse,
    GoogleFlightsStops,
    GoogleHotelsAmenitiesItem,
    GoogleHotelsMinRating,
    GoogleHotelsPropertyTypesItem,
    GoogleHotelsResponse,
    GoogleHotelsSort,
    GoogleImagesResponse,
    GoogleImagesSize,
    GoogleImagesTime,
    GoogleImagesType,
    GoogleImagesUsageRights,
    GoogleJobsDatePosted,
    GoogleJobsJobType,
    GoogleJobsResponse,
    GoogleMapsPlaceResponse,
    GoogleMapsReviewsResponse,
    GoogleMapsReviewsSort,
    GoogleMapsSearchMinRating,
    GoogleMapsSearchResponse,
    GoogleNewsResponse,
    GoogleNewsSort,
    GoogleNewsTopic,
    GooglePatentsDateType,
    GooglePatentsLanguage,
    GooglePatentsLitigation,
    GooglePatentsResponse,
    GooglePatentsSort,
    GooglePatentsStatus,
    GooglePatentsType,
    GooglePlayAppResponse,
    GooglePlayReviewsResponse,
    GooglePlayReviewsSort,
    GooglePlaySearchResponse,
    GoogleScholarResponse,
    GoogleScholarType,
    GoogleSearchResponse,
    GoogleSearchTime,
    GoogleShoppingResponse,
    GoogleSuggestResponse,
    GoogleTrendsInterestResponse,
    GoogleTrendsRegionsResolution,
    GoogleTrendsRegionsResponse,
    GoogleTrendsRelatedCategory,
    GoogleTrendsRelatedResponse,
    GoogleTrendsRelatedSearchType,
    GoogleTrendsRelatedTime,
    GoogleTrendsTrendingCategory,
    GoogleTrendsTrendingResponse,
    GoogleTrendsTrendingSort,
    GoogleTrendsTrendingStatus,
    GoogleTrendsTrendingTime,
    IndeedJobResponse,
    IndeedSearchCountry,
    IndeedSearchDatePosted,
    IndeedSearchDistanceMiles,
    IndeedSearchEducation,
    IndeedSearchExperienceLevel,
    IndeedSearchJobType,
    IndeedSearchRemote,
    IndeedSearchResponse,
    InstagramCommentsResponse,
    InstagramPostResponse,
    InstagramProfileReelsResponse,
    InstagramProfileResponse,
    LinkedinAdsAdResponse,
    LinkedinAdsSearchResponse,
    LinkedinAdsSearchWithin,
    LinkedinCompanyResponse,
    LinkedinJobsJobResponse,
    LinkedinJobsSearchDatePosted,
    LinkedinJobsSearchResponse,
    LinkedinPostsResponse,
    LinkedinProfileResponse,
    MetaAdsAdResponse,
    MetaAdsPageMediaType,
    MetaAdsPagePlatformsItem,
    MetaAdsPageResponse,
    MetaAdsPageStatus,
    PinterestBoardResponse,
    PinterestPinResponse,
    PinterestProfileResponse,
    PinterestSearchResponse,
    PinterestSearchType,
    RedditDiscussionsResponse,
    RedditPostResponse,
    RedditPostSort,
    RedditSearchResponse,
    RedditSearchSort,
    RedditSearchTime,
    RedditSearchType,
    RedditSubredditResponse,
    RedditSubredditSort,
    RedditSubredditsResponse,
    RedditSubredditsSort,
    RedditUserResponse,
    RedditUserSort,
    RedditUserTab,
    ThreadsPostResponse,
    ThreadsProfilePostsResponse,
    ThreadsProfileResponse,
    TiktokAdsAdResponse,
    TiktokAdsSearchResponse,
    TiktokCommentsResponse,
    TiktokHashtagResponse,
    TiktokProfileResponse,
    TiktokSearchDatePosted,
    TiktokSearchResponse,
    TiktokSearchSort,
    TiktokSearchType,
    TiktokShopProductResponse,
    TiktokShopProductsResponse,
    TiktokShopReviewsResponse,
    TiktokShopSearchResponse,
    TiktokSoundResponse,
    TiktokVideoResponse,
    TripadvisorPlaceResponse,
    TripadvisorReviewsMonthsItem,
    TripadvisorReviewsResponse,
    TripadvisorReviewsSort,
    TripadvisorReviewsTravelerTypesItem,
    TripadvisorSearchResponse,
    TripadvisorSearchType,
    TrustpilotCompanyResponse,
    TrustpilotCompanyReviewsDatePublished,
    TrustpilotCompanyReviewsResponse,
    TrustpilotSearchResponse,
    UpworkJobResponse,
    UpworkSearchDuration,
    UpworkSearchExperienceLevel,
    UpworkSearchJobType,
    UpworkSearchResponse,
    UpworkSearchSort,
    UpworkSearchWorkload,
    XPostResponse,
    XProfileResponse,
    YoutubeChannelResponse,
    YoutubeChannelSort,
    YoutubeChannelTab,
    YoutubeCommentsResponse,
    YoutubeCommentsSort,
    YoutubePlaylistResponse,
    YoutubePostResponse,
    YoutubeSearchDuration,
    YoutubeSearchFeaturesItem,
    YoutubeSearchPrioritize,
    YoutubeSearchResponse,
    YoutubeSearchType,
    YoutubeSearchUploadDate,
    YoutubeSuggestCountry,
    YoutubeTranscriptResponse,
    YoutubeVideoResponse,
    ZillowPropertyResponse,
    ZillowSearchDaysOnZillow,
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


class SyncGoogleSearch:
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
        time: GoogleSearchTime | None = None,
        safe_search: bool | None = None,
        scrape_results: bool | None = None,
        scrape_limit: int | None = None,
        page: int | None = None,
    ) -> GoogleSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "time": time,
                "safeSearch": safe_search,
                "scrapeResults": scrape_results,
                "scrapeLimit": scrape_limit,
                "page": page,
            }
        )
        return self._call("POST", "/v1/google/search", body)


class SyncGoogleNews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        topic: GoogleNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        time: GoogleSearchTime | None = None,
        sort: GoogleNewsSort | None = None,
        page: int | None = None,
    ) -> GoogleNewsResponse:
        body = _omit_none(
            {
                "query": query,
                "topic": topic,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "time": time,
                "sort": sort,
                "page": page,
            }
        )
        return self._call("POST", "/v1/google/news", body)


class SyncGoogleImages:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        size: GoogleImagesSize | None = None,
        type: GoogleImagesType | None = None,
        time: GoogleImagesTime | None = None,
        usage_rights: GoogleImagesUsageRights | None = None,
        limit: int | None = None,
    ) -> GoogleImagesResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "size": size,
                "type": type,
                "time": time,
                "usageRights": usage_rights,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/google/images", body)


class SyncGoogleAiMode:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
    ) -> GoogleAiModeResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/google/aiMode", body)


class SyncGoogleShopping:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        filter: str | None = None,
        country: str | None = None,
        language: str | None = None,
        page: int | None = None,
    ) -> GoogleShoppingResponse:
        body = _omit_none(
            {
                "query": query,
                "filter": filter,
                "country": country,
                "language": language,
                "page": page,
            }
        )
        return self._call("POST", "/v1/google/shopping", body)


class SyncGoogleSuggest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
    ) -> GoogleSuggestResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/google/suggest", body)


class SyncGoogleAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: GoogleAdsSearchMediaType | None = None,
        platform: GoogleAdsSearchPlatform | None = None,
        shown_from: str | None = None,
        shown_to: str | None = None,
        cursor: str | None = None,
    ) -> GoogleAdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "domain": domain,
                "country": country,
                "mediaType": media_type,
                "platform": platform,
                "shownFrom": shown_from,
                "shownTo": shown_to,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/google/ads/search", body)


class SyncGoogleAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        ad_url: str | None = None,
        ad_id: str | None = None,
        advertiser_id: str | None = None,
    ) -> GoogleAdsAdResponse:
        body = _omit_none(
            {
                "adUrl": ad_url,
                "adId": ad_id,
                "advertiserId": advertiser_id,
            }
        )
        return self._call("POST", "/v1/google/ads/ad", body)


class SyncGoogleAdsAdvertisers:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        limit: int | None = None,
    ) -> GoogleAdsAdvertisersResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/google/ads/advertisers", body)


class SyncGoogleAds:
    search: SyncGoogleAdsSearch
    ad: SyncGoogleAdsAd
    advertisers: SyncGoogleAdsAdvertisers

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncGoogleAdsSearch(call)
        self.ad = SyncGoogleAdsAd(call)
        self.advertisers = SyncGoogleAdsAdvertisers(call)


class SyncGoogleScholar:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        cites_id: str | None = None,
        year_from: int | None = None,
        year_to: int | None = None,
        sort: GoogleNewsSort | None = None,
        type: GoogleScholarType | None = None,
        include_patents: bool | None = None,
        include_citations: bool | None = None,
        page: int | None = None,
    ) -> GoogleScholarResponse:
        body = _omit_none(
            {
                "query": query,
                "citesId": cites_id,
                "yearFrom": year_from,
                "yearTo": year_to,
                "sort": sort,
                "type": type,
                "includePatents": include_patents,
                "includeCitations": include_citations,
                "page": page,
            }
        )
        return self._call("POST", "/v1/google/scholar", body)


class SyncGoogleJobs:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        location: str | None = None,
        country: str | None = None,
        language: str | None = None,
        date_posted: GoogleJobsDatePosted | None = None,
        job_type: GoogleJobsJobType | None = None,
        remote: bool | None = None,
        cursor: str | None = None,
    ) -> GoogleJobsResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "country": country,
                "language": language,
                "datePosted": date_posted,
                "jobType": job_type,
                "remote": remote,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/google/jobs", body)


class SyncGooglePatents:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        inventor: str | None = None,
        assignee: str | None = None,
        office: str | None = None,
        language: GooglePatentsLanguage | None = None,
        date_type: GooglePatentsDateType | None = None,
        after: str | None = None,
        before: str | None = None,
        status: GooglePatentsStatus | None = None,
        type: GooglePatentsType | None = None,
        litigation: GooglePatentsLitigation | None = None,
        sort: GooglePatentsSort | None = None,
        page: int | None = None,
    ) -> GooglePatentsResponse:
        body = _omit_none(
            {
                "query": query,
                "inventor": inventor,
                "assignee": assignee,
                "office": office,
                "language": language,
                "dateType": date_type,
                "after": after,
                "before": before,
                "status": status,
                "type": type,
                "litigation": litigation,
                "sort": sort,
                "page": page,
            }
        )
        return self._call("POST", "/v1/google/patents", body)


class SyncGoogleMapsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        location: str,
        min_rating: GoogleMapsSearchMinRating | None = None,
        open_now: bool | None = None,
        country: str | None = None,
        language: str | None = None,
        page: int | None = None,
    ) -> GoogleMapsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "minRating": min_rating,
                "openNow": open_now,
                "country": country,
                "language": language,
                "page": page,
            }
        )
        return self._call("POST", "/v1/google/maps/search", body)


class SyncGoogleMapsPlace:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        place_url: str | None = None,
        place_id: str | None = None,
        country: str | None = None,
        language: str | None = None,
    ) -> GoogleMapsPlaceResponse:
        body = _omit_none(
            {
                "placeUrl": place_url,
                "placeId": place_id,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/google/maps/place", body)


class SyncGoogleMapsReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        place_url: str | None = None,
        place_id: str | None = None,
        sort: GoogleMapsReviewsSort | None = None,
        language: str | None = None,
        cursor: str | None = None,
    ) -> GoogleMapsReviewsResponse:
        body = _omit_none(
            {
                "placeUrl": place_url,
                "placeId": place_id,
                "sort": sort,
                "language": language,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/google/maps/reviews", body)


class SyncGoogleMaps:
    search: SyncGoogleMapsSearch
    place: SyncGoogleMapsPlace
    reviews: SyncGoogleMapsReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncGoogleMapsSearch(call)
        self.place = SyncGoogleMapsPlace(call)
        self.reviews = SyncGoogleMapsReviews(call)


class SyncGoogleTrendsRelated:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        time: GoogleTrendsRelatedTime | None = None,
        search_type: GoogleTrendsRelatedSearchType | None = None,
        category: GoogleTrendsRelatedCategory | None = None,
    ) -> GoogleTrendsRelatedResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "time": time,
                "searchType": search_type,
                "category": category,
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
        time: GoogleTrendsTrendingTime | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        status: GoogleTrendsTrendingStatus | None = None,
        sort: GoogleTrendsTrendingSort | None = None,
    ) -> GoogleTrendsTrendingResponse:
        body = _omit_none(
            {
                "country": country,
                "time": time,
                "category": category,
                "status": status,
                "sort": sort,
            }
        )
        return self._call("POST", "/v1/google/trends/trending", body)


class SyncGoogleTrendsInterest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        time: GoogleTrendsRelatedTime | None = None,
        search_type: GoogleTrendsRelatedSearchType | None = None,
        category: GoogleTrendsRelatedCategory | None = None,
    ) -> GoogleTrendsInterestResponse:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "time": time,
                "searchType": search_type,
                "category": category,
            }
        )
        return self._call("POST", "/v1/google/trends/interest", body)


class SyncGoogleTrendsRegions:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        time: GoogleTrendsRelatedTime | None = None,
        search_type: GoogleTrendsRelatedSearchType | None = None,
        category: GoogleTrendsRelatedCategory | None = None,
        resolution: GoogleTrendsRegionsResolution | None = None,
    ) -> GoogleTrendsRegionsResponse:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "time": time,
                "searchType": search_type,
                "category": category,
                "resolution": resolution,
            }
        )
        return self._call("POST", "/v1/google/trends/regions", body)


class SyncGoogleTrends:
    related: SyncGoogleTrendsRelated
    trending: SyncGoogleTrendsTrending
    interest: SyncGoogleTrendsInterest
    regions: SyncGoogleTrendsRegions

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.related = SyncGoogleTrendsRelated(call)
        self.trending = SyncGoogleTrendsTrending(call)
        self.interest = SyncGoogleTrendsInterest(call)
        self.regions = SyncGoogleTrendsRegions(call)


class SyncGoogleFlights:
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
        cabin: GoogleFlightsCabin | None = None,
        stops: GoogleFlightsStops | None = None,
        airlines: list[str] | None = None,
        carry_on_bags: int | None = None,
        checked_bags: int | None = None,
        max_price: int | None = None,
        departure_time: GoogleFlightsDepartureTime | None = None,
        arrival_time: GoogleFlightsArrivalTime | None = None,
        max_duration_hours: int | None = None,
    ) -> GoogleFlightsResponse:
        body = _omit_none(
            {
                "origin": origin,
                "destination": destination,
                "departDate": depart_date,
                "returnDate": return_date,
                "adults": adults,
                "cabin": cabin,
                "stops": stops,
                "airlines": airlines,
                "carryOnBags": carry_on_bags,
                "checkedBags": checked_bags,
                "maxPrice": max_price,
                "departureTime": departure_time,
                "arrivalTime": arrival_time,
                "maxDurationHours": max_duration_hours,
            }
        )
        return self._call("POST", "/v1/google/flights", body)


class SyncGoogleHotels:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        children_ages: list[int] | None = None,
        currency: str | None = None,
        min_price: int | None = None,
        max_price: int | None = None,
        min_rating: GoogleHotelsMinRating | None = None,
        hotel_class: list[int] | None = None,
        amenities: list[GoogleHotelsAmenitiesItem] | None = None,
        property_types: list[GoogleHotelsPropertyTypesItem] | None = None,
        free_cancellation: bool | None = None,
        special_offers: bool | None = None,
        sort: GoogleHotelsSort | None = None,
        cursor: str | None = None,
    ) -> GoogleHotelsResponse:
        body = _omit_none(
            {
                "query": query,
                "checkIn": check_in,
                "checkOut": check_out,
                "adults": adults,
                "childrenAges": children_ages,
                "currency": currency,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minRating": min_rating,
                "hotelClass": hotel_class,
                "amenities": amenities,
                "propertyTypes": property_types,
                "freeCancellation": free_cancellation,
                "specialOffers": special_offers,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/google/hotels", body)


class SyncGooglePlayApp:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        app_url: str | None = None,
        app_id: str | None = None,
        country: str | None = None,
        language: str | None = None,
    ) -> GooglePlayAppResponse:
        body = _omit_none(
            {
                "appUrl": app_url,
                "appId": app_id,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/google/play/app", body)


class SyncGooglePlaySearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
    ) -> GooglePlaySearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "limit": limit,
            }
        )
        return self._call("POST", "/v1/google/play/search", body)


class SyncGooglePlayReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        app_url: str | None = None,
        app_id: str | None = None,
        language: str | None = None,
        sort: GooglePlayReviewsSort | None = None,
        rating: int | None = None,
        cursor: str | None = None,
    ) -> GooglePlayReviewsResponse:
        body = _omit_none(
            {
                "appUrl": app_url,
                "appId": app_id,
                "language": language,
                "sort": sort,
                "rating": rating,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/google/play/reviews", body)


class SyncGooglePlay:
    app: SyncGooglePlayApp
    search: SyncGooglePlaySearch
    reviews: SyncGooglePlayReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.app = SyncGooglePlayApp(call)
        self.search = SyncGooglePlaySearch(call)
        self.reviews = SyncGooglePlayReviews(call)


class SyncGoogle:
    search: SyncGoogleSearch
    news: SyncGoogleNews
    images: SyncGoogleImages
    aiMode: SyncGoogleAiMode
    shopping: SyncGoogleShopping
    suggest: SyncGoogleSuggest
    ads: SyncGoogleAds
    scholar: SyncGoogleScholar
    jobs: SyncGoogleJobs
    patents: SyncGooglePatents
    maps: SyncGoogleMaps
    trends: SyncGoogleTrends
    flights: SyncGoogleFlights
    hotels: SyncGoogleHotels
    play: SyncGooglePlay

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncGoogleSearch(call)
        self.news = SyncGoogleNews(call)
        self.images = SyncGoogleImages(call)
        self.aiMode = SyncGoogleAiMode(call)
        self.shopping = SyncGoogleShopping(call)
        self.suggest = SyncGoogleSuggest(call)
        self.ads = SyncGoogleAds(call)
        self.scholar = SyncGoogleScholar(call)
        self.jobs = SyncGoogleJobs(call)
        self.patents = SyncGooglePatents(call)
        self.maps = SyncGoogleMaps(call)
        self.trends = SyncGoogleTrends(call)
        self.flights = SyncGoogleFlights(call)
        self.hotels = SyncGoogleHotels(call)
        self.play = SyncGooglePlay(call)


class SyncYoutubeSuggest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: YoutubeSuggestCountry | None = None,
        language: str | None = None,
    ) -> GoogleSuggestResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
            }
        )
        return self._call("POST", "/v1/youtube/suggest", body)


class SyncYoutubeSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        duration: YoutubeSearchDuration | None = None,
        upload_date: YoutubeSearchUploadDate | None = None,
        features: list[YoutubeSearchFeaturesItem] | None = None,
        prioritize: YoutubeSearchPrioritize | None = None,
        cursor: str | None = None,
    ) -> YoutubeSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "duration": duration,
                "uploadDate": upload_date,
                "features": features,
                "prioritize": prioritize,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/search", body)


class SyncYoutubeTranscript:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        language: str | None = None,
        include_timestamps: bool | None = None,
    ) -> YoutubeTranscriptResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return self._call("POST", "/v1/youtube/transcript", body)


class SyncYoutubeVideo:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
    ) -> YoutubeVideoResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
            }
        )
        return self._call("POST", "/v1/youtube/video", body)


class SyncYoutubeComments:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        comment: str | None = None,
        sort: YoutubeCommentsSort | None = None,
        cursor: str | None = None,
    ) -> YoutubeCommentsResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "comment": comment,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/comments", body)


class SyncYoutubeChannel:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        channel_url: str | None = None,
        channel_id: str | None = None,
        tab: YoutubeChannelTab | None = None,
        sort: YoutubeChannelSort | None = None,
        cursor: str | None = None,
    ) -> YoutubeChannelResponse:
        body = _omit_none(
            {
                "channelUrl": channel_url,
                "channelId": channel_id,
                "tab": tab,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/channel", body)


class SyncYoutubePost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
        sort: YoutubeCommentsSort | None = None,
        cursor: str | None = None,
    ) -> YoutubePostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/post", body)


class SyncYoutubePlaylist:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        playlist_url: str | None = None,
        playlist_id: str | None = None,
        cursor: str | None = None,
    ) -> YoutubePlaylistResponse:
        body = _omit_none(
            {
                "playlistUrl": playlist_url,
                "playlistId": playlist_id,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/youtube/playlist", body)


class SyncYoutube:
    suggest: SyncYoutubeSuggest
    search: SyncYoutubeSearch
    transcript: SyncYoutubeTranscript
    video: SyncYoutubeVideo
    comments: SyncYoutubeComments
    channel: SyncYoutubeChannel
    post: SyncYoutubePost
    playlist: SyncYoutubePlaylist

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.suggest = SyncYoutubeSuggest(call)
        self.search = SyncYoutubeSearch(call)
        self.transcript = SyncYoutubeTranscript(call)
        self.video = SyncYoutubeVideo(call)
        self.comments = SyncYoutubeComments(call)
        self.channel = SyncYoutubeChannel(call)
        self.post = SyncYoutubePost(call)
        self.playlist = SyncYoutubePlaylist(call)


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
        time: RedditSearchTime | None = None,
        cursor: str | None = None,
    ) -> RedditSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "subreddit": subreddit,
                "sort": sort,
                "time": time,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/search", body)


class SyncRedditPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
        comment: str | None = None,
        sort: RedditPostSort | None = None,
        cursor: str | None = None,
    ) -> RedditPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
                "comment": comment,
                "sort": sort,
                "cursor": cursor,
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
        time: RedditSearchTime | None = None,
        cursor: str | None = None,
    ) -> RedditSubredditResponse:
        body = _omit_none(
            {
                "subreddit": subreddit,
                "sort": sort,
                "time": time,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/subreddit", body)


class SyncRedditUser:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        time: RedditSearchTime | None = None,
        cursor: str | None = None,
    ) -> RedditUserResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "tab": tab,
                "sort": sort,
                "time": time,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/user", body)


class SyncRedditDiscussions:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
        cursor: str | None = None,
    ) -> RedditDiscussionsResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/discussions", body)


class SyncRedditSubreddits:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        sort: RedditSubredditsSort | None = None,
        cursor: str | None = None,
    ) -> RedditSubredditsResponse:
        body = _omit_none(
            {
                "sort": sort,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/reddit/subreddits", body)


class SyncReddit:
    search: SyncRedditSearch
    post: SyncRedditPost
    subreddit: SyncRedditSubreddit
    user: SyncRedditUser
    discussions: SyncRedditDiscussions
    subreddits: SyncRedditSubreddits

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncRedditSearch(call)
        self.post = SyncRedditPost(call)
        self.subreddit = SyncRedditSubreddit(call)
        self.user = SyncRedditUser(call)
        self.discussions = SyncRedditDiscussions(call)
        self.subreddits = SyncRedditSubreddits(call)


class SyncInstagramComments:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_code: str | None = None,
        cursor: str | None = None,
    ) -> InstagramCommentsResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postCode": post_code,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/instagram/comments", body)


class SyncInstagramPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_code: str | None = None,
    ) -> InstagramPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postCode": post_code,
            }
        )
        return self._call("POST", "/v1/instagram/post", body)


class SyncInstagramProfileReels:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> InstagramProfileReelsResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/instagram/profile/reels", body)


class SyncInstagramProfile:
    reels: SyncInstagramProfileReels

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.reels = SyncInstagramProfileReels(call)

    def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> InstagramProfileResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/instagram/profile", body)


class SyncInstagramTranscript:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        language: str | None = None,
        include_timestamps: bool | None = None,
    ) -> YoutubeTranscriptResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return self._call("POST", "/v1/instagram/transcript", body)


class SyncInstagram:
    comments: SyncInstagramComments
    post: SyncInstagramPost
    profile: SyncInstagramProfile
    transcript: SyncInstagramTranscript

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.comments = SyncInstagramComments(call)
        self.post = SyncInstagramPost(call)
        self.profile = SyncInstagramProfile(call)
        self.transcript = SyncInstagramTranscript(call)


class SyncTiktokProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> TiktokProfileResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
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
        video_url: str | None = None,
        video_id: str | None = None,
    ) -> TiktokVideoResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
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
    ) -> TiktokHashtagResponse:
        body = _omit_none(
            {
                "hashtag": hashtag,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/hashtag", body)


class SyncTiktokSound:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        audio_id: str,
        cursor: str | None = None,
    ) -> TiktokSoundResponse:
        body = _omit_none(
            {
                "audioId": audio_id,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/sound", body)


class SyncTiktokComments:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        comment: str | None = None,
        cursor: str | None = None,
    ) -> TiktokCommentsResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "comment": comment,
                "cursor": cursor,
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
        sort: TiktokSearchSort | None = None,
        date_posted: TiktokSearchDatePosted | None = None,
        cursor: str | None = None,
    ) -> TiktokSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "sort": sort,
                "datePosted": date_posted,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/search", body)


class SyncTiktokTranscript:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        language: str | None = None,
        include_timestamps: bool | None = None,
    ) -> YoutubeTranscriptResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return self._call("POST", "/v1/tiktok/transcript", body)


class SyncTiktokAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        cursor: str | None = None,
    ) -> TiktokAdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "country": country,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/ads/search", body)


class SyncTiktokAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        ad_url: str | None = None,
        ad_id: str | None = None,
    ) -> TiktokAdsAdResponse:
        body = _omit_none(
            {
                "adUrl": ad_url,
                "adId": ad_id,
            }
        )
        return self._call("POST", "/v1/tiktok/ads/ad", body)


class SyncTiktokAds:
    search: SyncTiktokAdsSearch
    ad: SyncTiktokAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncTiktokAdsSearch(call)
        self.ad = SyncTiktokAdsAd(call)


class SyncTiktokShopSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        cursor: str | None = None,
    ) -> TiktokShopSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/shop/search", body)


class SyncTiktokShopProducts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        shop_url: str | None = None,
        shop_id: str | None = None,
        cursor: str | None = None,
    ) -> TiktokShopProductsResponse:
        body = _omit_none(
            {
                "shopUrl": shop_url,
                "shopId": shop_id,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/tiktok/shop/products", body)


class SyncTiktokShopProduct:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        product_url: str | None = None,
        product_id: str | None = None,
    ) -> TiktokShopProductResponse:
        body = _omit_none(
            {
                "productUrl": product_url,
                "productId": product_id,
            }
        )
        return self._call("POST", "/v1/tiktok/shop/product", body)


class SyncTiktokShopReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        product_url: str | None = None,
        product_id: str | None = None,
    ) -> TiktokShopReviewsResponse:
        body = _omit_none(
            {
                "productUrl": product_url,
                "productId": product_id,
            }
        )
        return self._call("POST", "/v1/tiktok/shop/reviews", body)


class SyncTiktokShop:
    search: SyncTiktokShopSearch
    products: SyncTiktokShopProducts
    product: SyncTiktokShopProduct
    reviews: SyncTiktokShopReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncTiktokShopSearch(call)
        self.products = SyncTiktokShopProducts(call)
        self.product = SyncTiktokShopProduct(call)
        self.reviews = SyncTiktokShopReviews(call)


class SyncTiktok:
    profile: SyncTiktokProfile
    video: SyncTiktokVideo
    hashtag: SyncTiktokHashtag
    sound: SyncTiktokSound
    comments: SyncTiktokComments
    search: SyncTiktokSearch
    transcript: SyncTiktokTranscript
    ads: SyncTiktokAds
    shop: SyncTiktokShop

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncTiktokProfile(call)
        self.video = SyncTiktokVideo(call)
        self.hashtag = SyncTiktokHashtag(call)
        self.sound = SyncTiktokSound(call)
        self.comments = SyncTiktokComments(call)
        self.search = SyncTiktokSearch(call)
        self.transcript = SyncTiktokTranscript(call)
        self.ads = SyncTiktokAds(call)
        self.shop = SyncTiktokShop(call)


class SyncMetaAdsPage:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        advertiser: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        media_type: MetaAdsPageMediaType | None = None,
        platforms: list[MetaAdsPagePlatformsItem] | None = None,
        language: str | None = None,
        shown_from: str | None = None,
        shown_to: str | None = None,
        cursor: str | None = None,
    ) -> MetaAdsPageResponse:
        body = _omit_none(
            {
                "advertiser": advertiser,
                "country": country,
                "status": status,
                "mediaType": media_type,
                "platforms": platforms,
                "language": language,
                "shownFrom": shown_from,
                "shownTo": shown_to,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/meta/ads/page", body)


class SyncMetaAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        media_type: MetaAdsPageMediaType | None = None,
        platforms: list[MetaAdsPagePlatformsItem] | None = None,
        language: str | None = None,
        shown_from: str | None = None,
        shown_to: str | None = None,
        cursor: str | None = None,
    ) -> MetaAdsPageResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "status": status,
                "mediaType": media_type,
                "platforms": platforms,
                "language": language,
                "shownFrom": shown_from,
                "shownTo": shown_to,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/meta/ads/search", body)


class SyncMetaAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        ad_url: str | None = None,
        ad_id: str | None = None,
    ) -> MetaAdsAdResponse:
        body = _omit_none(
            {
                "adUrl": ad_url,
                "adId": ad_id,
            }
        )
        return self._call("POST", "/v1/meta/ads/ad", body)


class SyncMetaAds:
    page: SyncMetaAdsPage
    search: SyncMetaAdsSearch
    ad: SyncMetaAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.page = SyncMetaAdsPage(call)
        self.search = SyncMetaAdsSearch(call)
        self.ad = SyncMetaAdsAd(call)


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
        date_posted: LinkedinJobsSearchDatePosted | None = None,
        company: str | list[str] | None = None,
        easy_apply: bool | None = None,
        few_applicants: bool | None = None,
        page: int | None = None,
    ) -> LinkedinJobsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "datePosted": date_posted,
                "company": company,
                "easyApply": easy_apply,
                "fewApplicants": few_applicants,
                "page": page,
            }
        )
        return self._call("POST", "/v1/linkedin/jobs/search", body)


class SyncLinkedinJobsJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        job_url: str | None = None,
        job_id: str | None = None,
    ) -> LinkedinJobsJobResponse:
        body = _omit_none(
            {
                "jobUrl": job_url,
                "jobId": job_id,
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
        company_url: str | None = None,
        company_id: str | None = None,
    ) -> LinkedinCompanyResponse:
        body = _omit_none(
            {
                "companyUrl": company_url,
                "companyId": company_id,
            }
        )
        return self._call("POST", "/v1/linkedin/company", body)


class SyncLinkedinProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile_url: str | None = None,
        profile_id: str | None = None,
    ) -> LinkedinProfileResponse:
        body = _omit_none(
            {
                "profileUrl": profile_url,
                "profileId": profile_id,
            }
        )
        return self._call("POST", "/v1/linkedin/profile", body)


class SyncLinkedinPosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile_url: str | None = None,
        profile_id: str | None = None,
        company_url: str | None = None,
        company_id: str | None = None,
        cursor: str | None = None,
    ) -> LinkedinPostsResponse:
        body = _omit_none(
            {
                "profileUrl": profile_url,
                "profileId": profile_id,
                "companyUrl": company_url,
                "companyId": company_id,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/linkedin/posts", body)


class SyncLinkedinAdsSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        within: LinkedinAdsSearchWithin | None = None,
        cursor: str | None = None,
    ) -> LinkedinAdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "country": country,
                "within": within,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/linkedin/ads/search", body)


class SyncLinkedinAdsAd:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        ad_url: str | None = None,
        ad_id: str | None = None,
    ) -> LinkedinAdsAdResponse:
        body = _omit_none(
            {
                "adUrl": ad_url,
                "adId": ad_id,
            }
        )
        return self._call("POST", "/v1/linkedin/ads/ad", body)


class SyncLinkedinAds:
    search: SyncLinkedinAdsSearch
    ad: SyncLinkedinAdsAd

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncLinkedinAdsSearch(call)
        self.ad = SyncLinkedinAdsAd(call)


class SyncLinkedin:
    jobs: SyncLinkedinJobs
    company: SyncLinkedinCompany
    profile: SyncLinkedinProfile
    posts: SyncLinkedinPosts
    ads: SyncLinkedinAds

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.jobs = SyncLinkedinJobs(call)
        self.company = SyncLinkedinCompany(call)
        self.profile = SyncLinkedinProfile(call)
        self.posts = SyncLinkedinPosts(call)
        self.ads = SyncLinkedinAds(call)


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
        min_bathrooms: float | None = None,
        min_sqft: int | None = None,
        max_sqft: int | None = None,
        min_lot_size: int | None = None,
        max_lot_size: int | None = None,
        min_year_built: int | None = None,
        max_year_built: int | None = None,
        max_hoa: float | None = None,
        min_parking_spots: int | None = None,
        days_on_zillow: ZillowSearchDaysOnZillow | None = None,
        has_pool: bool | None = None,
        has_garage: bool | None = None,
        has_air_conditioning: bool | None = None,
        is_waterfront: bool | None = None,
        single_story: bool | None = None,
        open_house: bool | None = None,
        price_reduced: bool | None = None,
        has3d_tour: bool | None = None,
        pets_allowed: bool | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        sort: ZillowSearchSort | None = None,
        keywords: str | None = None,
        page: int | None = None,
    ) -> ZillowSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minBedrooms": min_bedrooms,
                "maxBedrooms": max_bedrooms,
                "minBathrooms": min_bathrooms,
                "minSqft": min_sqft,
                "maxSqft": max_sqft,
                "minLotSize": min_lot_size,
                "maxLotSize": max_lot_size,
                "minYearBuilt": min_year_built,
                "maxYearBuilt": max_year_built,
                "maxHoa": max_hoa,
                "minParkingSpots": min_parking_spots,
                "daysOnZillow": days_on_zillow,
                "hasPool": has_pool,
                "hasGarage": has_garage,
                "hasAirConditioning": has_air_conditioning,
                "isWaterfront": is_waterfront,
                "singleStory": single_story,
                "openHouse": open_house,
                "priceReduced": price_reduced,
                "has3dTour": has3d_tour,
                "petsAllowed": pets_allowed,
                "homeTypes": home_types,
                "sort": sort,
                "keywords": keywords,
                "page": page,
            }
        )
        return self._call("POST", "/v1/zillow/search", body)


class SyncZillowProperty:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        property_url: str | None = None,
        property_id: str | None = None,
    ) -> ZillowPropertyResponse:
        body = _omit_none(
            {
                "propertyUrl": property_url,
                "propertyId": property_id,
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
        experience_level: UpworkSearchExperienceLevel | None = None,
        workload: UpworkSearchWorkload | None = None,
        duration: UpworkSearchDuration | None = None,
        min_hourly_rate: int | None = None,
        max_hourly_rate: int | None = None,
        page: int | None = None,
    ) -> UpworkSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "jobType": job_type,
                "experienceLevel": experience_level,
                "workload": workload,
                "duration": duration,
                "minHourlyRate": min_hourly_rate,
                "maxHourlyRate": max_hourly_rate,
                "page": page,
            }
        )
        return self._call("POST", "/v1/upwork/search", body)


class SyncUpworkJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        job_url: str | None = None,
        job_id: str | None = None,
    ) -> UpworkJobResponse:
        body = _omit_none(
            {
                "jobUrl": job_url,
                "jobId": job_id,
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


class SyncIndeedSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        country: IndeedSearchCountry | None = None,
        distance_miles: IndeedSearchDistanceMiles | None = None,
        date_posted: IndeedSearchDatePosted | None = None,
        remote: IndeedSearchRemote | None = None,
        job_type: IndeedSearchJobType | None = None,
        experience_level: IndeedSearchExperienceLevel | None = None,
        education: IndeedSearchEducation | None = None,
        sort: GoogleNewsSort | None = None,
        cursor: str | None = None,
    ) -> IndeedSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "country": country,
                "distanceMiles": distance_miles,
                "datePosted": date_posted,
                "remote": remote,
                "jobType": job_type,
                "experienceLevel": experience_level,
                "education": education,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/indeed/search", body)


class SyncIndeedJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        job_url: str | None = None,
        job_id: str | None = None,
        country: IndeedSearchCountry | None = None,
    ) -> IndeedJobResponse:
        body = _omit_none(
            {
                "jobUrl": job_url,
                "jobId": job_id,
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


class SyncCareersJobs:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        board_url: str,
        cursor: str | None = None,
    ) -> CareersJobsResponse:
        body = _omit_none(
            {
                "boardUrl": board_url,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/careers/jobs", body)


class SyncCareersJob:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        job_url: str,
    ) -> CareersJobResponse:
        body = _omit_none(
            {
                "jobUrl": job_url,
            }
        )
        return self._call("POST", "/v1/careers/job", body)


class SyncCareers:
    jobs: SyncCareersJobs
    job: SyncCareersJob

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.jobs = SyncCareersJobs(call)
        self.job = SyncCareersJob(call)


class SyncTripadvisorSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        location: str | None = None,
    ) -> TripadvisorSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "location": location,
            }
        )
        return self._call("POST", "/v1/tripadvisor/search", body)


class SyncTripadvisorPlace:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        place_url: str | None = None,
        place_id: str | None = None,
    ) -> TripadvisorPlaceResponse:
        body = _omit_none(
            {
                "placeUrl": place_url,
                "placeId": place_id,
            }
        )
        return self._call("POST", "/v1/tripadvisor/place", body)


class SyncTripadvisorReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        place_url: str | None = None,
        place_id: str | None = None,
        language: str | None = None,
        ratings: list[int] | None = None,
        traveler_types: list[TripadvisorReviewsTravelerTypesItem] | None = None,
        months: list[TripadvisorReviewsMonthsItem] | None = None,
        sort: TripadvisorReviewsSort | None = None,
        page: int | None = None,
    ) -> TripadvisorReviewsResponse:
        body = _omit_none(
            {
                "placeUrl": place_url,
                "placeId": place_id,
                "language": language,
                "ratings": ratings,
                "travelerTypes": traveler_types,
                "months": months,
                "sort": sort,
                "page": page,
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


class SyncBookingSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        rooms: int | None = None,
        currency: str | None = None,
        sort: BookingSearchSort | None = None,
        cursor: str | None = None,
    ) -> BookingSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "checkIn": check_in,
                "checkOut": check_out,
                "adults": adults,
                "rooms": rooms,
                "currency": currency,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/booking/search", body)


class SyncBookingHotelReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        hotel_url: str | None = None,
        hotel_id: str | None = None,
        sort: BookingHotelReviewsSort | None = None,
        cursor: str | None = None,
    ) -> BookingHotelReviewsResponse:
        body = _omit_none(
            {
                "hotelUrl": hotel_url,
                "hotelId": hotel_id,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/booking/hotel/reviews", body)


class SyncBookingHotel:
    reviews: SyncBookingHotelReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.reviews = SyncBookingHotelReviews(call)

    def __call__(
        self,
        *,
        hotel_url: str | None = None,
        hotel_id: str | None = None,
    ) -> BookingHotelResponse:
        body = _omit_none(
            {
                "hotelUrl": hotel_url,
                "hotelId": hotel_id,
            }
        )
        return self._call("POST", "/v1/booking/hotel", body)


class SyncBooking:
    search: SyncBookingSearch
    hotel: SyncBookingHotel

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncBookingSearch(call)
        self.hotel = SyncBookingHotel(call)


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
        min_rating: Literal[4] | None = None,
        brand: str | None = None,
        sort: AmazonSearchSort | None = None,
        country: AmazonSearchCountry | None = None,
        page: int | None = None,
    ) -> AmazonSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "category": category,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minRating": min_rating,
                "brand": brand,
                "sort": sort,
                "country": country,
                "page": page,
            }
        )
        return self._call("POST", "/v1/amazon/search", body)


class SyncAmazonProduct:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        product_url: str | None = None,
        product_id: str | None = None,
        country: AmazonSearchCountry | None = None,
    ) -> AmazonProductResponse:
        body = _omit_none(
            {
                "productUrl": product_url,
                "productId": product_id,
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
        page: int | None = None,
    ) -> AmazonBestsellersResponse:
        body = _omit_none(
            {
                "category": category,
                "country": country,
                "page": page,
            }
        )
        return self._call("POST", "/v1/amazon/bestsellers", body)


class SyncAmazonSuggest:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        country: AmazonSuggestCountry | None = None,
    ) -> GoogleSuggestResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
            }
        )
        return self._call("POST", "/v1/amazon/suggest", body)


class SyncAmazon:
    search: SyncAmazonSearch
    product: SyncAmazonProduct
    bestsellers: SyncAmazonBestsellers
    suggest: SyncAmazonSuggest

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncAmazonSearch(call)
        self.product = SyncAmazonProduct(call)
        self.bestsellers = SyncAmazonBestsellers(call)
        self.suggest = SyncAmazonSuggest(call)


class SyncAppstoreApp:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        app_url: str | None = None,
        app_id: str | None = None,
        country: str | None = None,
    ) -> AppstoreAppResponse:
        body = _omit_none(
            {
                "appUrl": app_url,
                "appId": app_id,
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
        app_url: str | None = None,
        app_id: str | None = None,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        page: int | None = None,
    ) -> AppstoreReviewsResponse:
        body = _omit_none(
            {
                "appUrl": app_url,
                "appId": app_id,
                "country": country,
                "sort": sort,
                "page": page,
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


class SyncPinterestSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        cursor: str | None = None,
    ) -> PinterestSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/pinterest/search", body)


class SyncPinterestPin:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        pin_url: str | None = None,
        pin_id: str | None = None,
    ) -> PinterestPinResponse:
        body = _omit_none(
            {
                "pinUrl": pin_url,
                "pinId": pin_id,
            }
        )
        return self._call("POST", "/v1/pinterest/pin", body)


class SyncPinterestBoard:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        board_url: str,
        cursor: str | None = None,
    ) -> PinterestBoardResponse:
        body = _omit_none(
            {
                "boardUrl": board_url,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/pinterest/board", body)


class SyncPinterestProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> PinterestProfileResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/pinterest/profile", body)


class SyncPinterest:
    search: SyncPinterestSearch
    pin: SyncPinterestPin
    board: SyncPinterestBoard
    profile: SyncPinterestProfile

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncPinterestSearch(call)
        self.pin = SyncPinterestPin(call)
        self.board = SyncPinterestBoard(call)
        self.profile = SyncPinterestProfile(call)


class SyncXProfile:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        profile_url: str | None = None,
        username: str | None = None,
    ) -> XProfileResponse:
        body = _omit_none(
            {
                "profileUrl": profile_url,
                "username": username,
            }
        )
        return self._call("POST", "/v1/x/profile", body)


class SyncXPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
    ) -> XPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
            }
        )
        return self._call("POST", "/v1/x/post", body)


class SyncX:
    profile: SyncXProfile
    post: SyncXPost

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncXProfile(call)
        self.post = SyncXPost(call)


class SyncThreadsProfilePosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> ThreadsProfilePostsResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/threads/profile/posts", body)


class SyncThreadsProfile:
    posts: SyncThreadsProfilePosts

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.posts = SyncThreadsProfilePosts(call)

    def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
    ) -> ThreadsProfileResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
            }
        )
        return self._call("POST", "/v1/threads/profile", body)


class SyncThreadsPost:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_code: str | None = None,
        cursor: str | None = None,
    ) -> ThreadsPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postCode": post_code,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/threads/post", body)


class SyncThreads:
    profile: SyncThreadsProfile
    post: SyncThreadsPost

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.profile = SyncThreadsProfile(call)
        self.post = SyncThreadsPost(call)


class SyncTrustpilotCompanyReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        company_url: str | None = None,
        company_domain: str | None = None,
        ratings: list[int] | None = None,
        language: str | None = None,
        date_published: TrustpilotCompanyReviewsDatePublished | None = None,
        verified_only: bool | None = None,
        search: str | None = None,
        page: int | None = None,
    ) -> TrustpilotCompanyReviewsResponse:
        body = _omit_none(
            {
                "companyUrl": company_url,
                "companyDomain": company_domain,
                "ratings": ratings,
                "language": language,
                "datePublished": date_published,
                "verifiedOnly": verified_only,
                "search": search,
                "page": page,
            }
        )
        return self._call("POST", "/v1/trustpilot/company/reviews", body)


class SyncTrustpilotCompany:
    reviews: SyncTrustpilotCompanyReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.reviews = SyncTrustpilotCompanyReviews(call)

    def __call__(
        self,
        *,
        company_url: str | None = None,
        company_domain: str | None = None,
    ) -> TrustpilotCompanyResponse:
        body = _omit_none(
            {
                "companyUrl": company_url,
                "companyDomain": company_domain,
            }
        )
        return self._call("POST", "/v1/trustpilot/company", body)


class SyncTrustpilotSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        page: int | None = None,
    ) -> TrustpilotSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "page": page,
            }
        )
        return self._call("POST", "/v1/trustpilot/search", body)


class SyncTrustpilot:
    company: SyncTrustpilotCompany
    search: SyncTrustpilotSearch

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.company = SyncTrustpilotCompany(call)
        self.search = SyncTrustpilotSearch(call)


class SyncEbaySearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        condition: EbaySearchCondition | None = None,
        auctions_only: bool | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort: EbaySearchSort | None = None,
        page: int | None = None,
    ) -> EbaySearchResponse:
        body = _omit_none(
            {
                "query": query,
                "condition": condition,
                "auctionsOnly": auctions_only,
                "minPrice": min_price,
                "maxPrice": max_price,
                "sort": sort,
                "page": page,
            }
        )
        return self._call("POST", "/v1/ebay/search", body)


class SyncEbayItem:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        item_url: str | None = None,
        item_id: str | None = None,
    ) -> EbayItemResponse:
        body = _omit_none(
            {
                "itemUrl": item_url,
                "itemId": item_id,
            }
        )
        return self._call("POST", "/v1/ebay/item", body)


class SyncEbay:
    search: SyncEbaySearch
    item: SyncEbayItem

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncEbaySearch(call)
        self.item = SyncEbayItem(call)


class SyncAirbnbSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        location: str,
        check_in: str,
        check_out: str,
        guests: int | None = None,
        min_price: int | None = None,
        max_price: int | None = None,
        room_type: AirbnbSearchRoomType | None = None,
        currency: AirbnbSearchCurrency | None = None,
        cursor: str | None = None,
    ) -> AirbnbSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "checkIn": check_in,
                "checkOut": check_out,
                "guests": guests,
                "minPrice": min_price,
                "maxPrice": max_price,
                "roomType": room_type,
                "currency": currency,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/airbnb/search", body)


class SyncAirbnbListing:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        listing_url: str | None = None,
        listing_id: str | None = None,
        check_in: str | None = None,
        check_out: str | None = None,
        guests: int | None = None,
        currency: AirbnbSearchCurrency | None = None,
    ) -> AirbnbListingResponse:
        body = _omit_none(
            {
                "listingUrl": listing_url,
                "listingId": listing_id,
                "checkIn": check_in,
                "checkOut": check_out,
                "guests": guests,
                "currency": currency,
            }
        )
        return self._call("POST", "/v1/airbnb/listing", body)


class SyncAirbnbReviews:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        listing_url: str | None = None,
        listing_id: str | None = None,
        page: int | None = None,
    ) -> AirbnbReviewsResponse:
        body = _omit_none(
            {
                "listingUrl": listing_url,
                "listingId": listing_id,
                "page": page,
            }
        )
        return self._call("POST", "/v1/airbnb/reviews", body)


class SyncAirbnb:
    search: SyncAirbnbSearch
    listing: SyncAirbnbListing
    reviews: SyncAirbnbReviews

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncAirbnbSearch(call)
        self.listing = SyncAirbnbListing(call)
        self.reviews = SyncAirbnbReviews(call)


class SyncFacebookPagePosts:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        page_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> FacebookPagePostsResponse:
        body = _omit_none(
            {
                "pageUrl": page_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/facebook/page/posts", body)


class SyncFacebookPage:
    posts: SyncFacebookPagePosts

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.posts = SyncFacebookPagePosts(call)

    def __call__(
        self,
        *,
        page_url: str | None = None,
        username: str | None = None,
    ) -> FacebookPageResponse:
        body = _omit_none(
            {
                "pageUrl": page_url,
                "username": username,
            }
        )
        return self._call("POST", "/v1/facebook/page", body)


class SyncFacebookPostComments:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
        cursor: str | None = None,
    ) -> FacebookPostCommentsResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
                "cursor": cursor,
            }
        )
        return self._call("POST", "/v1/facebook/post/comments", body)


class SyncFacebookPost:
    comments: SyncFacebookPostComments

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.comments = SyncFacebookPostComments(call)

    def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
    ) -> FacebookPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
            }
        )
        return self._call("POST", "/v1/facebook/post", body)


class SyncFacebookMarketplaceSearch:
    def __init__(self, call: SyncCall) -> None:
        self._call = call

    def __call__(
        self,
        *,
        query: str,
        location: str,
        min_price: int | None = None,
        max_price: int | None = None,
        sort: FacebookMarketplaceSearchSort | None = None,
    ) -> FacebookMarketplaceSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "minPrice": min_price,
                "maxPrice": max_price,
                "sort": sort,
            }
        )
        return self._call("POST", "/v1/facebook/marketplace/search", body)


class SyncFacebookMarketplace:
    search: SyncFacebookMarketplaceSearch

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.search = SyncFacebookMarketplaceSearch(call)


class SyncFacebook:
    page: SyncFacebookPage
    post: SyncFacebookPost
    marketplace: SyncFacebookMarketplace

    def __init__(self, call: SyncCall) -> None:
        self._call = call
        self.page = SyncFacebookPage(call)
        self.post = SyncFacebookPost(call)
        self.marketplace = SyncFacebookMarketplace(call)


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
        time: GoogleSearchTime | None = None,
        safe_search: bool | None = None,
        scrape_results: bool | None = None,
        scrape_limit: int | None = None,
        page: int | None = None,
    ) -> GoogleSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "time": time,
                "safeSearch": safe_search,
                "scrapeResults": scrape_results,
                "scrapeLimit": scrape_limit,
                "page": page,
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
        topic: GoogleNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        time: GoogleSearchTime | None = None,
        sort: GoogleNewsSort | None = None,
        page: int | None = None,
    ) -> GoogleNewsResponse:
        body = _omit_none(
            {
                "query": query,
                "topic": topic,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "time": time,
                "sort": sort,
                "page": page,
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


class SyncSurface:
    endpoints: SyncEndpoints
    google: SyncGoogle
    youtube: SyncYoutube
    reddit: SyncReddit
    instagram: SyncInstagram
    tiktok: SyncTiktok
    meta: SyncMeta
    linkedin: SyncLinkedin
    zillow: SyncZillow
    upwork: SyncUpwork
    indeed: SyncIndeed
    careers: SyncCareers
    tripadvisor: SyncTripadvisor
    booking: SyncBooking
    amazon: SyncAmazon
    appstore: SyncAppstore
    pinterest: SyncPinterest
    x: SyncX
    threads: SyncThreads
    trustpilot: SyncTrustpilot
    ebay: SyncEbay
    airbnb: SyncAirbnb
    facebook: SyncFacebook
    web: SyncWeb

    def __init__(self, call: SyncCall) -> None:
        self.endpoints = SyncEndpoints(call)
        self.google = SyncGoogle(call)
        self.youtube = SyncYoutube(call)
        self.reddit = SyncReddit(call)
        self.instagram = SyncInstagram(call)
        self.tiktok = SyncTiktok(call)
        self.meta = SyncMeta(call)
        self.linkedin = SyncLinkedin(call)
        self.zillow = SyncZillow(call)
        self.upwork = SyncUpwork(call)
        self.indeed = SyncIndeed(call)
        self.careers = SyncCareers(call)
        self.tripadvisor = SyncTripadvisor(call)
        self.booking = SyncBooking(call)
        self.amazon = SyncAmazon(call)
        self.appstore = SyncAppstore(call)
        self.pinterest = SyncPinterest(call)
        self.x = SyncX(call)
        self.threads = SyncThreads(call)
        self.trustpilot = SyncTrustpilot(call)
        self.ebay = SyncEbay(call)
        self.airbnb = SyncAirbnb(call)
        self.facebook = SyncFacebook(call)
        self.web = SyncWeb(call)


class AsyncEndpoints:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
    ) -> EndpointCatalog:
        body = None
        return await self._call("GET", "/v1/endpoints", body)


class AsyncGoogleSearch:
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
        time: GoogleSearchTime | None = None,
        safe_search: bool | None = None,
        scrape_results: bool | None = None,
        scrape_limit: int | None = None,
        page: int | None = None,
    ) -> GoogleSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "time": time,
                "safeSearch": safe_search,
                "scrapeResults": scrape_results,
                "scrapeLimit": scrape_limit,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/google/search", body)


class AsyncGoogleNews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        topic: GoogleNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        time: GoogleSearchTime | None = None,
        sort: GoogleNewsSort | None = None,
        page: int | None = None,
    ) -> GoogleNewsResponse:
        body = _omit_none(
            {
                "query": query,
                "topic": topic,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "time": time,
                "sort": sort,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/google/news", body)


class AsyncGoogleImages:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        size: GoogleImagesSize | None = None,
        type: GoogleImagesType | None = None,
        time: GoogleImagesTime | None = None,
        usage_rights: GoogleImagesUsageRights | None = None,
        limit: int | None = None,
    ) -> GoogleImagesResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "size": size,
                "type": type,
                "time": time,
                "usageRights": usage_rights,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/google/images", body)


class AsyncGoogleAiMode:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
    ) -> GoogleAiModeResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/google/aiMode", body)


class AsyncGoogleShopping:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        filter: str | None = None,
        country: str | None = None,
        language: str | None = None,
        page: int | None = None,
    ) -> GoogleShoppingResponse:
        body = _omit_none(
            {
                "query": query,
                "filter": filter,
                "country": country,
                "language": language,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/google/shopping", body)


class AsyncGoogleSuggest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
    ) -> GoogleSuggestResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/google/suggest", body)


class AsyncGoogleAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        domain: str | None = None,
        country: str | None = None,
        media_type: GoogleAdsSearchMediaType | None = None,
        platform: GoogleAdsSearchPlatform | None = None,
        shown_from: str | None = None,
        shown_to: str | None = None,
        cursor: str | None = None,
    ) -> GoogleAdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "domain": domain,
                "country": country,
                "mediaType": media_type,
                "platform": platform,
                "shownFrom": shown_from,
                "shownTo": shown_to,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/google/ads/search", body)


class AsyncGoogleAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        ad_url: str | None = None,
        ad_id: str | None = None,
        advertiser_id: str | None = None,
    ) -> GoogleAdsAdResponse:
        body = _omit_none(
            {
                "adUrl": ad_url,
                "adId": ad_id,
                "advertiserId": advertiser_id,
            }
        )
        return await self._call("POST", "/v1/google/ads/ad", body)


class AsyncGoogleAdsAdvertisers:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        limit: int | None = None,
    ) -> GoogleAdsAdvertisersResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/google/ads/advertisers", body)


class AsyncGoogleAds:
    search: AsyncGoogleAdsSearch
    ad: AsyncGoogleAdsAd
    advertisers: AsyncGoogleAdsAdvertisers

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncGoogleAdsSearch(call)
        self.ad = AsyncGoogleAdsAd(call)
        self.advertisers = AsyncGoogleAdsAdvertisers(call)


class AsyncGoogleScholar:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        cites_id: str | None = None,
        year_from: int | None = None,
        year_to: int | None = None,
        sort: GoogleNewsSort | None = None,
        type: GoogleScholarType | None = None,
        include_patents: bool | None = None,
        include_citations: bool | None = None,
        page: int | None = None,
    ) -> GoogleScholarResponse:
        body = _omit_none(
            {
                "query": query,
                "citesId": cites_id,
                "yearFrom": year_from,
                "yearTo": year_to,
                "sort": sort,
                "type": type,
                "includePatents": include_patents,
                "includeCitations": include_citations,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/google/scholar", body)


class AsyncGoogleJobs:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        location: str | None = None,
        country: str | None = None,
        language: str | None = None,
        date_posted: GoogleJobsDatePosted | None = None,
        job_type: GoogleJobsJobType | None = None,
        remote: bool | None = None,
        cursor: str | None = None,
    ) -> GoogleJobsResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "country": country,
                "language": language,
                "datePosted": date_posted,
                "jobType": job_type,
                "remote": remote,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/google/jobs", body)


class AsyncGooglePatents:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        inventor: str | None = None,
        assignee: str | None = None,
        office: str | None = None,
        language: GooglePatentsLanguage | None = None,
        date_type: GooglePatentsDateType | None = None,
        after: str | None = None,
        before: str | None = None,
        status: GooglePatentsStatus | None = None,
        type: GooglePatentsType | None = None,
        litigation: GooglePatentsLitigation | None = None,
        sort: GooglePatentsSort | None = None,
        page: int | None = None,
    ) -> GooglePatentsResponse:
        body = _omit_none(
            {
                "query": query,
                "inventor": inventor,
                "assignee": assignee,
                "office": office,
                "language": language,
                "dateType": date_type,
                "after": after,
                "before": before,
                "status": status,
                "type": type,
                "litigation": litigation,
                "sort": sort,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/google/patents", body)


class AsyncGoogleMapsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        location: str,
        min_rating: GoogleMapsSearchMinRating | None = None,
        open_now: bool | None = None,
        country: str | None = None,
        language: str | None = None,
        page: int | None = None,
    ) -> GoogleMapsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "minRating": min_rating,
                "openNow": open_now,
                "country": country,
                "language": language,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/google/maps/search", body)


class AsyncGoogleMapsPlace:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        place_url: str | None = None,
        place_id: str | None = None,
        country: str | None = None,
        language: str | None = None,
    ) -> GoogleMapsPlaceResponse:
        body = _omit_none(
            {
                "placeUrl": place_url,
                "placeId": place_id,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/google/maps/place", body)


class AsyncGoogleMapsReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        place_url: str | None = None,
        place_id: str | None = None,
        sort: GoogleMapsReviewsSort | None = None,
        language: str | None = None,
        cursor: str | None = None,
    ) -> GoogleMapsReviewsResponse:
        body = _omit_none(
            {
                "placeUrl": place_url,
                "placeId": place_id,
                "sort": sort,
                "language": language,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/google/maps/reviews", body)


class AsyncGoogleMaps:
    search: AsyncGoogleMapsSearch
    place: AsyncGoogleMapsPlace
    reviews: AsyncGoogleMapsReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncGoogleMapsSearch(call)
        self.place = AsyncGoogleMapsPlace(call)
        self.reviews = AsyncGoogleMapsReviews(call)


class AsyncGoogleTrendsRelated:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        time: GoogleTrendsRelatedTime | None = None,
        search_type: GoogleTrendsRelatedSearchType | None = None,
        category: GoogleTrendsRelatedCategory | None = None,
    ) -> GoogleTrendsRelatedResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "time": time,
                "searchType": search_type,
                "category": category,
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
        time: GoogleTrendsTrendingTime | None = None,
        category: GoogleTrendsTrendingCategory | None = None,
        status: GoogleTrendsTrendingStatus | None = None,
        sort: GoogleTrendsTrendingSort | None = None,
    ) -> GoogleTrendsTrendingResponse:
        body = _omit_none(
            {
                "country": country,
                "time": time,
                "category": category,
                "status": status,
                "sort": sort,
            }
        )
        return await self._call("POST", "/v1/google/trends/trending", body)


class AsyncGoogleTrendsInterest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        time: GoogleTrendsRelatedTime | None = None,
        search_type: GoogleTrendsRelatedSearchType | None = None,
        category: GoogleTrendsRelatedCategory | None = None,
    ) -> GoogleTrendsInterestResponse:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "time": time,
                "searchType": search_type,
                "category": category,
            }
        )
        return await self._call("POST", "/v1/google/trends/interest", body)


class AsyncGoogleTrendsRegions:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        queries: list[str],
        country: str | None = None,
        time: GoogleTrendsRelatedTime | None = None,
        search_type: GoogleTrendsRelatedSearchType | None = None,
        category: GoogleTrendsRelatedCategory | None = None,
        resolution: GoogleTrendsRegionsResolution | None = None,
    ) -> GoogleTrendsRegionsResponse:
        body = _omit_none(
            {
                "queries": queries,
                "country": country,
                "time": time,
                "searchType": search_type,
                "category": category,
                "resolution": resolution,
            }
        )
        return await self._call("POST", "/v1/google/trends/regions", body)


class AsyncGoogleTrends:
    related: AsyncGoogleTrendsRelated
    trending: AsyncGoogleTrendsTrending
    interest: AsyncGoogleTrendsInterest
    regions: AsyncGoogleTrendsRegions

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.related = AsyncGoogleTrendsRelated(call)
        self.trending = AsyncGoogleTrendsTrending(call)
        self.interest = AsyncGoogleTrendsInterest(call)
        self.regions = AsyncGoogleTrendsRegions(call)


class AsyncGoogleFlights:
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
        cabin: GoogleFlightsCabin | None = None,
        stops: GoogleFlightsStops | None = None,
        airlines: list[str] | None = None,
        carry_on_bags: int | None = None,
        checked_bags: int | None = None,
        max_price: int | None = None,
        departure_time: GoogleFlightsDepartureTime | None = None,
        arrival_time: GoogleFlightsArrivalTime | None = None,
        max_duration_hours: int | None = None,
    ) -> GoogleFlightsResponse:
        body = _omit_none(
            {
                "origin": origin,
                "destination": destination,
                "departDate": depart_date,
                "returnDate": return_date,
                "adults": adults,
                "cabin": cabin,
                "stops": stops,
                "airlines": airlines,
                "carryOnBags": carry_on_bags,
                "checkedBags": checked_bags,
                "maxPrice": max_price,
                "departureTime": departure_time,
                "arrivalTime": arrival_time,
                "maxDurationHours": max_duration_hours,
            }
        )
        return await self._call("POST", "/v1/google/flights", body)


class AsyncGoogleHotels:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        children_ages: list[int] | None = None,
        currency: str | None = None,
        min_price: int | None = None,
        max_price: int | None = None,
        min_rating: GoogleHotelsMinRating | None = None,
        hotel_class: list[int] | None = None,
        amenities: list[GoogleHotelsAmenitiesItem] | None = None,
        property_types: list[GoogleHotelsPropertyTypesItem] | None = None,
        free_cancellation: bool | None = None,
        special_offers: bool | None = None,
        sort: GoogleHotelsSort | None = None,
        cursor: str | None = None,
    ) -> GoogleHotelsResponse:
        body = _omit_none(
            {
                "query": query,
                "checkIn": check_in,
                "checkOut": check_out,
                "adults": adults,
                "childrenAges": children_ages,
                "currency": currency,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minRating": min_rating,
                "hotelClass": hotel_class,
                "amenities": amenities,
                "propertyTypes": property_types,
                "freeCancellation": free_cancellation,
                "specialOffers": special_offers,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/google/hotels", body)


class AsyncGooglePlayApp:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        app_url: str | None = None,
        app_id: str | None = None,
        country: str | None = None,
        language: str | None = None,
    ) -> GooglePlayAppResponse:
        body = _omit_none(
            {
                "appUrl": app_url,
                "appId": app_id,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/google/play/app", body)


class AsyncGooglePlaySearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        language: str | None = None,
        limit: int | None = None,
    ) -> GooglePlaySearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "limit": limit,
            }
        )
        return await self._call("POST", "/v1/google/play/search", body)


class AsyncGooglePlayReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        app_url: str | None = None,
        app_id: str | None = None,
        language: str | None = None,
        sort: GooglePlayReviewsSort | None = None,
        rating: int | None = None,
        cursor: str | None = None,
    ) -> GooglePlayReviewsResponse:
        body = _omit_none(
            {
                "appUrl": app_url,
                "appId": app_id,
                "language": language,
                "sort": sort,
                "rating": rating,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/google/play/reviews", body)


class AsyncGooglePlay:
    app: AsyncGooglePlayApp
    search: AsyncGooglePlaySearch
    reviews: AsyncGooglePlayReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.app = AsyncGooglePlayApp(call)
        self.search = AsyncGooglePlaySearch(call)
        self.reviews = AsyncGooglePlayReviews(call)


class AsyncGoogle:
    search: AsyncGoogleSearch
    news: AsyncGoogleNews
    images: AsyncGoogleImages
    aiMode: AsyncGoogleAiMode
    shopping: AsyncGoogleShopping
    suggest: AsyncGoogleSuggest
    ads: AsyncGoogleAds
    scholar: AsyncGoogleScholar
    jobs: AsyncGoogleJobs
    patents: AsyncGooglePatents
    maps: AsyncGoogleMaps
    trends: AsyncGoogleTrends
    flights: AsyncGoogleFlights
    hotels: AsyncGoogleHotels
    play: AsyncGooglePlay

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncGoogleSearch(call)
        self.news = AsyncGoogleNews(call)
        self.images = AsyncGoogleImages(call)
        self.aiMode = AsyncGoogleAiMode(call)
        self.shopping = AsyncGoogleShopping(call)
        self.suggest = AsyncGoogleSuggest(call)
        self.ads = AsyncGoogleAds(call)
        self.scholar = AsyncGoogleScholar(call)
        self.jobs = AsyncGoogleJobs(call)
        self.patents = AsyncGooglePatents(call)
        self.maps = AsyncGoogleMaps(call)
        self.trends = AsyncGoogleTrends(call)
        self.flights = AsyncGoogleFlights(call)
        self.hotels = AsyncGoogleHotels(call)
        self.play = AsyncGooglePlay(call)


class AsyncYoutubeSuggest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: YoutubeSuggestCountry | None = None,
        language: str | None = None,
    ) -> GoogleSuggestResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
            }
        )
        return await self._call("POST", "/v1/youtube/suggest", body)


class AsyncYoutubeSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: YoutubeSearchType | None = None,
        duration: YoutubeSearchDuration | None = None,
        upload_date: YoutubeSearchUploadDate | None = None,
        features: list[YoutubeSearchFeaturesItem] | None = None,
        prioritize: YoutubeSearchPrioritize | None = None,
        cursor: str | None = None,
    ) -> YoutubeSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "duration": duration,
                "uploadDate": upload_date,
                "features": features,
                "prioritize": prioritize,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/search", body)


class AsyncYoutubeTranscript:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        language: str | None = None,
        include_timestamps: bool | None = None,
    ) -> YoutubeTranscriptResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return await self._call("POST", "/v1/youtube/transcript", body)


class AsyncYoutubeVideo:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
    ) -> YoutubeVideoResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
            }
        )
        return await self._call("POST", "/v1/youtube/video", body)


class AsyncYoutubeComments:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        comment: str | None = None,
        sort: YoutubeCommentsSort | None = None,
        cursor: str | None = None,
    ) -> YoutubeCommentsResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "comment": comment,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/comments", body)


class AsyncYoutubeChannel:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        channel_url: str | None = None,
        channel_id: str | None = None,
        tab: YoutubeChannelTab | None = None,
        sort: YoutubeChannelSort | None = None,
        cursor: str | None = None,
    ) -> YoutubeChannelResponse:
        body = _omit_none(
            {
                "channelUrl": channel_url,
                "channelId": channel_id,
                "tab": tab,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/channel", body)


class AsyncYoutubePost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
        sort: YoutubeCommentsSort | None = None,
        cursor: str | None = None,
    ) -> YoutubePostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/post", body)


class AsyncYoutubePlaylist:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        playlist_url: str | None = None,
        playlist_id: str | None = None,
        cursor: str | None = None,
    ) -> YoutubePlaylistResponse:
        body = _omit_none(
            {
                "playlistUrl": playlist_url,
                "playlistId": playlist_id,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/youtube/playlist", body)


class AsyncYoutube:
    suggest: AsyncYoutubeSuggest
    search: AsyncYoutubeSearch
    transcript: AsyncYoutubeTranscript
    video: AsyncYoutubeVideo
    comments: AsyncYoutubeComments
    channel: AsyncYoutubeChannel
    post: AsyncYoutubePost
    playlist: AsyncYoutubePlaylist

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.suggest = AsyncYoutubeSuggest(call)
        self.search = AsyncYoutubeSearch(call)
        self.transcript = AsyncYoutubeTranscript(call)
        self.video = AsyncYoutubeVideo(call)
        self.comments = AsyncYoutubeComments(call)
        self.channel = AsyncYoutubeChannel(call)
        self.post = AsyncYoutubePost(call)
        self.playlist = AsyncYoutubePlaylist(call)


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
        time: RedditSearchTime | None = None,
        cursor: str | None = None,
    ) -> RedditSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "subreddit": subreddit,
                "sort": sort,
                "time": time,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/search", body)


class AsyncRedditPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
        comment: str | None = None,
        sort: RedditPostSort | None = None,
        cursor: str | None = None,
    ) -> RedditPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
                "comment": comment,
                "sort": sort,
                "cursor": cursor,
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
        time: RedditSearchTime | None = None,
        cursor: str | None = None,
    ) -> RedditSubredditResponse:
        body = _omit_none(
            {
                "subreddit": subreddit,
                "sort": sort,
                "time": time,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/subreddit", body)


class AsyncRedditUser:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        tab: RedditUserTab | None = None,
        sort: RedditUserSort | None = None,
        time: RedditSearchTime | None = None,
        cursor: str | None = None,
    ) -> RedditUserResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "tab": tab,
                "sort": sort,
                "time": time,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/user", body)


class AsyncRedditDiscussions:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
        cursor: str | None = None,
    ) -> RedditDiscussionsResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/discussions", body)


class AsyncRedditSubreddits:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        sort: RedditSubredditsSort | None = None,
        cursor: str | None = None,
    ) -> RedditSubredditsResponse:
        body = _omit_none(
            {
                "sort": sort,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/reddit/subreddits", body)


class AsyncReddit:
    search: AsyncRedditSearch
    post: AsyncRedditPost
    subreddit: AsyncRedditSubreddit
    user: AsyncRedditUser
    discussions: AsyncRedditDiscussions
    subreddits: AsyncRedditSubreddits

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncRedditSearch(call)
        self.post = AsyncRedditPost(call)
        self.subreddit = AsyncRedditSubreddit(call)
        self.user = AsyncRedditUser(call)
        self.discussions = AsyncRedditDiscussions(call)
        self.subreddits = AsyncRedditSubreddits(call)


class AsyncInstagramComments:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_code: str | None = None,
        cursor: str | None = None,
    ) -> InstagramCommentsResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postCode": post_code,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/instagram/comments", body)


class AsyncInstagramPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_code: str | None = None,
    ) -> InstagramPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postCode": post_code,
            }
        )
        return await self._call("POST", "/v1/instagram/post", body)


class AsyncInstagramProfileReels:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> InstagramProfileReelsResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/instagram/profile/reels", body)


class AsyncInstagramProfile:
    reels: AsyncInstagramProfileReels

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.reels = AsyncInstagramProfileReels(call)

    async def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> InstagramProfileResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/instagram/profile", body)


class AsyncInstagramTranscript:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        language: str | None = None,
        include_timestamps: bool | None = None,
    ) -> YoutubeTranscriptResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return await self._call("POST", "/v1/instagram/transcript", body)


class AsyncInstagram:
    comments: AsyncInstagramComments
    post: AsyncInstagramPost
    profile: AsyncInstagramProfile
    transcript: AsyncInstagramTranscript

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.comments = AsyncInstagramComments(call)
        self.post = AsyncInstagramPost(call)
        self.profile = AsyncInstagramProfile(call)
        self.transcript = AsyncInstagramTranscript(call)


class AsyncTiktokProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> TiktokProfileResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
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
        video_url: str | None = None,
        video_id: str | None = None,
    ) -> TiktokVideoResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
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
    ) -> TiktokHashtagResponse:
        body = _omit_none(
            {
                "hashtag": hashtag,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/hashtag", body)


class AsyncTiktokSound:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        audio_id: str,
        cursor: str | None = None,
    ) -> TiktokSoundResponse:
        body = _omit_none(
            {
                "audioId": audio_id,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/sound", body)


class AsyncTiktokComments:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        comment: str | None = None,
        cursor: str | None = None,
    ) -> TiktokCommentsResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "comment": comment,
                "cursor": cursor,
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
        sort: TiktokSearchSort | None = None,
        date_posted: TiktokSearchDatePosted | None = None,
        cursor: str | None = None,
    ) -> TiktokSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "sort": sort,
                "datePosted": date_posted,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/search", body)


class AsyncTiktokTranscript:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        video_url: str | None = None,
        video_id: str | None = None,
        language: str | None = None,
        include_timestamps: bool | None = None,
    ) -> YoutubeTranscriptResponse:
        body = _omit_none(
            {
                "videoUrl": video_url,
                "videoId": video_id,
                "language": language,
                "includeTimestamps": include_timestamps,
            }
        )
        return await self._call("POST", "/v1/tiktok/transcript", body)


class AsyncTiktokAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        cursor: str | None = None,
    ) -> TiktokAdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "country": country,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/ads/search", body)


class AsyncTiktokAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        ad_url: str | None = None,
        ad_id: str | None = None,
    ) -> TiktokAdsAdResponse:
        body = _omit_none(
            {
                "adUrl": ad_url,
                "adId": ad_id,
            }
        )
        return await self._call("POST", "/v1/tiktok/ads/ad", body)


class AsyncTiktokAds:
    search: AsyncTiktokAdsSearch
    ad: AsyncTiktokAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncTiktokAdsSearch(call)
        self.ad = AsyncTiktokAdsAd(call)


class AsyncTiktokShopSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        cursor: str | None = None,
    ) -> TiktokShopSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/shop/search", body)


class AsyncTiktokShopProducts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        shop_url: str | None = None,
        shop_id: str | None = None,
        cursor: str | None = None,
    ) -> TiktokShopProductsResponse:
        body = _omit_none(
            {
                "shopUrl": shop_url,
                "shopId": shop_id,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/tiktok/shop/products", body)


class AsyncTiktokShopProduct:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        product_url: str | None = None,
        product_id: str | None = None,
    ) -> TiktokShopProductResponse:
        body = _omit_none(
            {
                "productUrl": product_url,
                "productId": product_id,
            }
        )
        return await self._call("POST", "/v1/tiktok/shop/product", body)


class AsyncTiktokShopReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        product_url: str | None = None,
        product_id: str | None = None,
    ) -> TiktokShopReviewsResponse:
        body = _omit_none(
            {
                "productUrl": product_url,
                "productId": product_id,
            }
        )
        return await self._call("POST", "/v1/tiktok/shop/reviews", body)


class AsyncTiktokShop:
    search: AsyncTiktokShopSearch
    products: AsyncTiktokShopProducts
    product: AsyncTiktokShopProduct
    reviews: AsyncTiktokShopReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncTiktokShopSearch(call)
        self.products = AsyncTiktokShopProducts(call)
        self.product = AsyncTiktokShopProduct(call)
        self.reviews = AsyncTiktokShopReviews(call)


class AsyncTiktok:
    profile: AsyncTiktokProfile
    video: AsyncTiktokVideo
    hashtag: AsyncTiktokHashtag
    sound: AsyncTiktokSound
    comments: AsyncTiktokComments
    search: AsyncTiktokSearch
    transcript: AsyncTiktokTranscript
    ads: AsyncTiktokAds
    shop: AsyncTiktokShop

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncTiktokProfile(call)
        self.video = AsyncTiktokVideo(call)
        self.hashtag = AsyncTiktokHashtag(call)
        self.sound = AsyncTiktokSound(call)
        self.comments = AsyncTiktokComments(call)
        self.search = AsyncTiktokSearch(call)
        self.transcript = AsyncTiktokTranscript(call)
        self.ads = AsyncTiktokAds(call)
        self.shop = AsyncTiktokShop(call)


class AsyncMetaAdsPage:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        advertiser: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        media_type: MetaAdsPageMediaType | None = None,
        platforms: list[MetaAdsPagePlatformsItem] | None = None,
        language: str | None = None,
        shown_from: str | None = None,
        shown_to: str | None = None,
        cursor: str | None = None,
    ) -> MetaAdsPageResponse:
        body = _omit_none(
            {
                "advertiser": advertiser,
                "country": country,
                "status": status,
                "mediaType": media_type,
                "platforms": platforms,
                "language": language,
                "shownFrom": shown_from,
                "shownTo": shown_to,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/meta/ads/page", body)


class AsyncMetaAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: str | None = None,
        status: MetaAdsPageStatus | None = None,
        media_type: MetaAdsPageMediaType | None = None,
        platforms: list[MetaAdsPagePlatformsItem] | None = None,
        language: str | None = None,
        shown_from: str | None = None,
        shown_to: str | None = None,
        cursor: str | None = None,
    ) -> MetaAdsPageResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "status": status,
                "mediaType": media_type,
                "platforms": platforms,
                "language": language,
                "shownFrom": shown_from,
                "shownTo": shown_to,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/meta/ads/search", body)


class AsyncMetaAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        ad_url: str | None = None,
        ad_id: str | None = None,
    ) -> MetaAdsAdResponse:
        body = _omit_none(
            {
                "adUrl": ad_url,
                "adId": ad_id,
            }
        )
        return await self._call("POST", "/v1/meta/ads/ad", body)


class AsyncMetaAds:
    page: AsyncMetaAdsPage
    search: AsyncMetaAdsSearch
    ad: AsyncMetaAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.page = AsyncMetaAdsPage(call)
        self.search = AsyncMetaAdsSearch(call)
        self.ad = AsyncMetaAdsAd(call)


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
        date_posted: LinkedinJobsSearchDatePosted | None = None,
        company: str | list[str] | None = None,
        easy_apply: bool | None = None,
        few_applicants: bool | None = None,
        page: int | None = None,
    ) -> LinkedinJobsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "datePosted": date_posted,
                "company": company,
                "easyApply": easy_apply,
                "fewApplicants": few_applicants,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/linkedin/jobs/search", body)


class AsyncLinkedinJobsJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        job_url: str | None = None,
        job_id: str | None = None,
    ) -> LinkedinJobsJobResponse:
        body = _omit_none(
            {
                "jobUrl": job_url,
                "jobId": job_id,
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
        company_url: str | None = None,
        company_id: str | None = None,
    ) -> LinkedinCompanyResponse:
        body = _omit_none(
            {
                "companyUrl": company_url,
                "companyId": company_id,
            }
        )
        return await self._call("POST", "/v1/linkedin/company", body)


class AsyncLinkedinProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile_url: str | None = None,
        profile_id: str | None = None,
    ) -> LinkedinProfileResponse:
        body = _omit_none(
            {
                "profileUrl": profile_url,
                "profileId": profile_id,
            }
        )
        return await self._call("POST", "/v1/linkedin/profile", body)


class AsyncLinkedinPosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile_url: str | None = None,
        profile_id: str | None = None,
        company_url: str | None = None,
        company_id: str | None = None,
        cursor: str | None = None,
    ) -> LinkedinPostsResponse:
        body = _omit_none(
            {
                "profileUrl": profile_url,
                "profileId": profile_id,
                "companyUrl": company_url,
                "companyId": company_id,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/linkedin/posts", body)


class AsyncLinkedinAdsSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        advertiser: str | None = None,
        country: str | None = None,
        within: LinkedinAdsSearchWithin | None = None,
        cursor: str | None = None,
    ) -> LinkedinAdsSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "advertiser": advertiser,
                "country": country,
                "within": within,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/linkedin/ads/search", body)


class AsyncLinkedinAdsAd:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        ad_url: str | None = None,
        ad_id: str | None = None,
    ) -> LinkedinAdsAdResponse:
        body = _omit_none(
            {
                "adUrl": ad_url,
                "adId": ad_id,
            }
        )
        return await self._call("POST", "/v1/linkedin/ads/ad", body)


class AsyncLinkedinAds:
    search: AsyncLinkedinAdsSearch
    ad: AsyncLinkedinAdsAd

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncLinkedinAdsSearch(call)
        self.ad = AsyncLinkedinAdsAd(call)


class AsyncLinkedin:
    jobs: AsyncLinkedinJobs
    company: AsyncLinkedinCompany
    profile: AsyncLinkedinProfile
    posts: AsyncLinkedinPosts
    ads: AsyncLinkedinAds

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.jobs = AsyncLinkedinJobs(call)
        self.company = AsyncLinkedinCompany(call)
        self.profile = AsyncLinkedinProfile(call)
        self.posts = AsyncLinkedinPosts(call)
        self.ads = AsyncLinkedinAds(call)


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
        min_bathrooms: float | None = None,
        min_sqft: int | None = None,
        max_sqft: int | None = None,
        min_lot_size: int | None = None,
        max_lot_size: int | None = None,
        min_year_built: int | None = None,
        max_year_built: int | None = None,
        max_hoa: float | None = None,
        min_parking_spots: int | None = None,
        days_on_zillow: ZillowSearchDaysOnZillow | None = None,
        has_pool: bool | None = None,
        has_garage: bool | None = None,
        has_air_conditioning: bool | None = None,
        is_waterfront: bool | None = None,
        single_story: bool | None = None,
        open_house: bool | None = None,
        price_reduced: bool | None = None,
        has3d_tour: bool | None = None,
        pets_allowed: bool | None = None,
        home_types: list[ZillowSearchHomeTypesItem] | None = None,
        sort: ZillowSearchSort | None = None,
        keywords: str | None = None,
        page: int | None = None,
    ) -> ZillowSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "status": status,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minBedrooms": min_bedrooms,
                "maxBedrooms": max_bedrooms,
                "minBathrooms": min_bathrooms,
                "minSqft": min_sqft,
                "maxSqft": max_sqft,
                "minLotSize": min_lot_size,
                "maxLotSize": max_lot_size,
                "minYearBuilt": min_year_built,
                "maxYearBuilt": max_year_built,
                "maxHoa": max_hoa,
                "minParkingSpots": min_parking_spots,
                "daysOnZillow": days_on_zillow,
                "hasPool": has_pool,
                "hasGarage": has_garage,
                "hasAirConditioning": has_air_conditioning,
                "isWaterfront": is_waterfront,
                "singleStory": single_story,
                "openHouse": open_house,
                "priceReduced": price_reduced,
                "has3dTour": has3d_tour,
                "petsAllowed": pets_allowed,
                "homeTypes": home_types,
                "sort": sort,
                "keywords": keywords,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/zillow/search", body)


class AsyncZillowProperty:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        property_url: str | None = None,
        property_id: str | None = None,
    ) -> ZillowPropertyResponse:
        body = _omit_none(
            {
                "propertyUrl": property_url,
                "propertyId": property_id,
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
        experience_level: UpworkSearchExperienceLevel | None = None,
        workload: UpworkSearchWorkload | None = None,
        duration: UpworkSearchDuration | None = None,
        min_hourly_rate: int | None = None,
        max_hourly_rate: int | None = None,
        page: int | None = None,
    ) -> UpworkSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "sort": sort,
                "jobType": job_type,
                "experienceLevel": experience_level,
                "workload": workload,
                "duration": duration,
                "minHourlyRate": min_hourly_rate,
                "maxHourlyRate": max_hourly_rate,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/upwork/search", body)


class AsyncUpworkJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        job_url: str | None = None,
        job_id: str | None = None,
    ) -> UpworkJobResponse:
        body = _omit_none(
            {
                "jobUrl": job_url,
                "jobId": job_id,
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


class AsyncIndeedSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str | None = None,
        location: str | None = None,
        country: IndeedSearchCountry | None = None,
        distance_miles: IndeedSearchDistanceMiles | None = None,
        date_posted: IndeedSearchDatePosted | None = None,
        remote: IndeedSearchRemote | None = None,
        job_type: IndeedSearchJobType | None = None,
        experience_level: IndeedSearchExperienceLevel | None = None,
        education: IndeedSearchEducation | None = None,
        sort: GoogleNewsSort | None = None,
        cursor: str | None = None,
    ) -> IndeedSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "country": country,
                "distanceMiles": distance_miles,
                "datePosted": date_posted,
                "remote": remote,
                "jobType": job_type,
                "experienceLevel": experience_level,
                "education": education,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/indeed/search", body)


class AsyncIndeedJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        job_url: str | None = None,
        job_id: str | None = None,
        country: IndeedSearchCountry | None = None,
    ) -> IndeedJobResponse:
        body = _omit_none(
            {
                "jobUrl": job_url,
                "jobId": job_id,
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


class AsyncCareersJobs:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        board_url: str,
        cursor: str | None = None,
    ) -> CareersJobsResponse:
        body = _omit_none(
            {
                "boardUrl": board_url,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/careers/jobs", body)


class AsyncCareersJob:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        job_url: str,
    ) -> CareersJobResponse:
        body = _omit_none(
            {
                "jobUrl": job_url,
            }
        )
        return await self._call("POST", "/v1/careers/job", body)


class AsyncCareers:
    jobs: AsyncCareersJobs
    job: AsyncCareersJob

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.jobs = AsyncCareersJobs(call)
        self.job = AsyncCareersJob(call)


class AsyncTripadvisorSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: TripadvisorSearchType | None = None,
        location: str | None = None,
    ) -> TripadvisorSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "location": location,
            }
        )
        return await self._call("POST", "/v1/tripadvisor/search", body)


class AsyncTripadvisorPlace:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        place_url: str | None = None,
        place_id: str | None = None,
    ) -> TripadvisorPlaceResponse:
        body = _omit_none(
            {
                "placeUrl": place_url,
                "placeId": place_id,
            }
        )
        return await self._call("POST", "/v1/tripadvisor/place", body)


class AsyncTripadvisorReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        place_url: str | None = None,
        place_id: str | None = None,
        language: str | None = None,
        ratings: list[int] | None = None,
        traveler_types: list[TripadvisorReviewsTravelerTypesItem] | None = None,
        months: list[TripadvisorReviewsMonthsItem] | None = None,
        sort: TripadvisorReviewsSort | None = None,
        page: int | None = None,
    ) -> TripadvisorReviewsResponse:
        body = _omit_none(
            {
                "placeUrl": place_url,
                "placeId": place_id,
                "language": language,
                "ratings": ratings,
                "travelerTypes": traveler_types,
                "months": months,
                "sort": sort,
                "page": page,
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


class AsyncBookingSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        check_in: str | None = None,
        check_out: str | None = None,
        adults: int | None = None,
        rooms: int | None = None,
        currency: str | None = None,
        sort: BookingSearchSort | None = None,
        cursor: str | None = None,
    ) -> BookingSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "checkIn": check_in,
                "checkOut": check_out,
                "adults": adults,
                "rooms": rooms,
                "currency": currency,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/booking/search", body)


class AsyncBookingHotelReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        hotel_url: str | None = None,
        hotel_id: str | None = None,
        sort: BookingHotelReviewsSort | None = None,
        cursor: str | None = None,
    ) -> BookingHotelReviewsResponse:
        body = _omit_none(
            {
                "hotelUrl": hotel_url,
                "hotelId": hotel_id,
                "sort": sort,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/booking/hotel/reviews", body)


class AsyncBookingHotel:
    reviews: AsyncBookingHotelReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.reviews = AsyncBookingHotelReviews(call)

    async def __call__(
        self,
        *,
        hotel_url: str | None = None,
        hotel_id: str | None = None,
    ) -> BookingHotelResponse:
        body = _omit_none(
            {
                "hotelUrl": hotel_url,
                "hotelId": hotel_id,
            }
        )
        return await self._call("POST", "/v1/booking/hotel", body)


class AsyncBooking:
    search: AsyncBookingSearch
    hotel: AsyncBookingHotel

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncBookingSearch(call)
        self.hotel = AsyncBookingHotel(call)


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
        min_rating: Literal[4] | None = None,
        brand: str | None = None,
        sort: AmazonSearchSort | None = None,
        country: AmazonSearchCountry | None = None,
        page: int | None = None,
    ) -> AmazonSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "category": category,
                "minPrice": min_price,
                "maxPrice": max_price,
                "minRating": min_rating,
                "brand": brand,
                "sort": sort,
                "country": country,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/amazon/search", body)


class AsyncAmazonProduct:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        product_url: str | None = None,
        product_id: str | None = None,
        country: AmazonSearchCountry | None = None,
    ) -> AmazonProductResponse:
        body = _omit_none(
            {
                "productUrl": product_url,
                "productId": product_id,
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
        page: int | None = None,
    ) -> AmazonBestsellersResponse:
        body = _omit_none(
            {
                "category": category,
                "country": country,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/amazon/bestsellers", body)


class AsyncAmazonSuggest:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        country: AmazonSuggestCountry | None = None,
    ) -> GoogleSuggestResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
            }
        )
        return await self._call("POST", "/v1/amazon/suggest", body)


class AsyncAmazon:
    search: AsyncAmazonSearch
    product: AsyncAmazonProduct
    bestsellers: AsyncAmazonBestsellers
    suggest: AsyncAmazonSuggest

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncAmazonSearch(call)
        self.product = AsyncAmazonProduct(call)
        self.bestsellers = AsyncAmazonBestsellers(call)
        self.suggest = AsyncAmazonSuggest(call)


class AsyncAppstoreApp:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        app_url: str | None = None,
        app_id: str | None = None,
        country: str | None = None,
    ) -> AppstoreAppResponse:
        body = _omit_none(
            {
                "appUrl": app_url,
                "appId": app_id,
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
        app_url: str | None = None,
        app_id: str | None = None,
        country: str | None = None,
        sort: AppstoreReviewsSort | None = None,
        page: int | None = None,
    ) -> AppstoreReviewsResponse:
        body = _omit_none(
            {
                "appUrl": app_url,
                "appId": app_id,
                "country": country,
                "sort": sort,
                "page": page,
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


class AsyncPinterestSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        type: PinterestSearchType | None = None,
        cursor: str | None = None,
    ) -> PinterestSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "type": type,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/pinterest/search", body)


class AsyncPinterestPin:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        pin_url: str | None = None,
        pin_id: str | None = None,
    ) -> PinterestPinResponse:
        body = _omit_none(
            {
                "pinUrl": pin_url,
                "pinId": pin_id,
            }
        )
        return await self._call("POST", "/v1/pinterest/pin", body)


class AsyncPinterestBoard:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        board_url: str,
        cursor: str | None = None,
    ) -> PinterestBoardResponse:
        body = _omit_none(
            {
                "boardUrl": board_url,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/pinterest/board", body)


class AsyncPinterestProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> PinterestProfileResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/pinterest/profile", body)


class AsyncPinterest:
    search: AsyncPinterestSearch
    pin: AsyncPinterestPin
    board: AsyncPinterestBoard
    profile: AsyncPinterestProfile

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncPinterestSearch(call)
        self.pin = AsyncPinterestPin(call)
        self.board = AsyncPinterestBoard(call)
        self.profile = AsyncPinterestProfile(call)


class AsyncXProfile:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        profile_url: str | None = None,
        username: str | None = None,
    ) -> XProfileResponse:
        body = _omit_none(
            {
                "profileUrl": profile_url,
                "username": username,
            }
        )
        return await self._call("POST", "/v1/x/profile", body)


class AsyncXPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
    ) -> XPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
            }
        )
        return await self._call("POST", "/v1/x/post", body)


class AsyncX:
    profile: AsyncXProfile
    post: AsyncXPost

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncXProfile(call)
        self.post = AsyncXPost(call)


class AsyncThreadsProfilePosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> ThreadsProfilePostsResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/threads/profile/posts", body)


class AsyncThreadsProfile:
    posts: AsyncThreadsProfilePosts

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.posts = AsyncThreadsProfilePosts(call)

    async def __call__(
        self,
        *,
        user_url: str | None = None,
        username: str | None = None,
    ) -> ThreadsProfileResponse:
        body = _omit_none(
            {
                "userUrl": user_url,
                "username": username,
            }
        )
        return await self._call("POST", "/v1/threads/profile", body)


class AsyncThreadsPost:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_code: str | None = None,
        cursor: str | None = None,
    ) -> ThreadsPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postCode": post_code,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/threads/post", body)


class AsyncThreads:
    profile: AsyncThreadsProfile
    post: AsyncThreadsPost

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.profile = AsyncThreadsProfile(call)
        self.post = AsyncThreadsPost(call)


class AsyncTrustpilotCompanyReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        company_url: str | None = None,
        company_domain: str | None = None,
        ratings: list[int] | None = None,
        language: str | None = None,
        date_published: TrustpilotCompanyReviewsDatePublished | None = None,
        verified_only: bool | None = None,
        search: str | None = None,
        page: int | None = None,
    ) -> TrustpilotCompanyReviewsResponse:
        body = _omit_none(
            {
                "companyUrl": company_url,
                "companyDomain": company_domain,
                "ratings": ratings,
                "language": language,
                "datePublished": date_published,
                "verifiedOnly": verified_only,
                "search": search,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/trustpilot/company/reviews", body)


class AsyncTrustpilotCompany:
    reviews: AsyncTrustpilotCompanyReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.reviews = AsyncTrustpilotCompanyReviews(call)

    async def __call__(
        self,
        *,
        company_url: str | None = None,
        company_domain: str | None = None,
    ) -> TrustpilotCompanyResponse:
        body = _omit_none(
            {
                "companyUrl": company_url,
                "companyDomain": company_domain,
            }
        )
        return await self._call("POST", "/v1/trustpilot/company", body)


class AsyncTrustpilotSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        page: int | None = None,
    ) -> TrustpilotSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/trustpilot/search", body)


class AsyncTrustpilot:
    company: AsyncTrustpilotCompany
    search: AsyncTrustpilotSearch

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.company = AsyncTrustpilotCompany(call)
        self.search = AsyncTrustpilotSearch(call)


class AsyncEbaySearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        condition: EbaySearchCondition | None = None,
        auctions_only: bool | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort: EbaySearchSort | None = None,
        page: int | None = None,
    ) -> EbaySearchResponse:
        body = _omit_none(
            {
                "query": query,
                "condition": condition,
                "auctionsOnly": auctions_only,
                "minPrice": min_price,
                "maxPrice": max_price,
                "sort": sort,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/ebay/search", body)


class AsyncEbayItem:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        item_url: str | None = None,
        item_id: str | None = None,
    ) -> EbayItemResponse:
        body = _omit_none(
            {
                "itemUrl": item_url,
                "itemId": item_id,
            }
        )
        return await self._call("POST", "/v1/ebay/item", body)


class AsyncEbay:
    search: AsyncEbaySearch
    item: AsyncEbayItem

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncEbaySearch(call)
        self.item = AsyncEbayItem(call)


class AsyncAirbnbSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        location: str,
        check_in: str,
        check_out: str,
        guests: int | None = None,
        min_price: int | None = None,
        max_price: int | None = None,
        room_type: AirbnbSearchRoomType | None = None,
        currency: AirbnbSearchCurrency | None = None,
        cursor: str | None = None,
    ) -> AirbnbSearchResponse:
        body = _omit_none(
            {
                "location": location,
                "checkIn": check_in,
                "checkOut": check_out,
                "guests": guests,
                "minPrice": min_price,
                "maxPrice": max_price,
                "roomType": room_type,
                "currency": currency,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/airbnb/search", body)


class AsyncAirbnbListing:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        listing_url: str | None = None,
        listing_id: str | None = None,
        check_in: str | None = None,
        check_out: str | None = None,
        guests: int | None = None,
        currency: AirbnbSearchCurrency | None = None,
    ) -> AirbnbListingResponse:
        body = _omit_none(
            {
                "listingUrl": listing_url,
                "listingId": listing_id,
                "checkIn": check_in,
                "checkOut": check_out,
                "guests": guests,
                "currency": currency,
            }
        )
        return await self._call("POST", "/v1/airbnb/listing", body)


class AsyncAirbnbReviews:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        listing_url: str | None = None,
        listing_id: str | None = None,
        page: int | None = None,
    ) -> AirbnbReviewsResponse:
        body = _omit_none(
            {
                "listingUrl": listing_url,
                "listingId": listing_id,
                "page": page,
            }
        )
        return await self._call("POST", "/v1/airbnb/reviews", body)


class AsyncAirbnb:
    search: AsyncAirbnbSearch
    listing: AsyncAirbnbListing
    reviews: AsyncAirbnbReviews

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncAirbnbSearch(call)
        self.listing = AsyncAirbnbListing(call)
        self.reviews = AsyncAirbnbReviews(call)


class AsyncFacebookPagePosts:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        page_url: str | None = None,
        username: str | None = None,
        cursor: str | None = None,
    ) -> FacebookPagePostsResponse:
        body = _omit_none(
            {
                "pageUrl": page_url,
                "username": username,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/facebook/page/posts", body)


class AsyncFacebookPage:
    posts: AsyncFacebookPagePosts

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.posts = AsyncFacebookPagePosts(call)

    async def __call__(
        self,
        *,
        page_url: str | None = None,
        username: str | None = None,
    ) -> FacebookPageResponse:
        body = _omit_none(
            {
                "pageUrl": page_url,
                "username": username,
            }
        )
        return await self._call("POST", "/v1/facebook/page", body)


class AsyncFacebookPostComments:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
        cursor: str | None = None,
    ) -> FacebookPostCommentsResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
                "cursor": cursor,
            }
        )
        return await self._call("POST", "/v1/facebook/post/comments", body)


class AsyncFacebookPost:
    comments: AsyncFacebookPostComments

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.comments = AsyncFacebookPostComments(call)

    async def __call__(
        self,
        *,
        post_url: str | None = None,
        post_id: str | None = None,
    ) -> FacebookPostResponse:
        body = _omit_none(
            {
                "postUrl": post_url,
                "postId": post_id,
            }
        )
        return await self._call("POST", "/v1/facebook/post", body)


class AsyncFacebookMarketplaceSearch:
    def __init__(self, call: AsyncCall) -> None:
        self._call = call

    async def __call__(
        self,
        *,
        query: str,
        location: str,
        min_price: int | None = None,
        max_price: int | None = None,
        sort: FacebookMarketplaceSearchSort | None = None,
    ) -> FacebookMarketplaceSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "location": location,
                "minPrice": min_price,
                "maxPrice": max_price,
                "sort": sort,
            }
        )
        return await self._call("POST", "/v1/facebook/marketplace/search", body)


class AsyncFacebookMarketplace:
    search: AsyncFacebookMarketplaceSearch

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.search = AsyncFacebookMarketplaceSearch(call)


class AsyncFacebook:
    page: AsyncFacebookPage
    post: AsyncFacebookPost
    marketplace: AsyncFacebookMarketplace

    def __init__(self, call: AsyncCall) -> None:
        self._call = call
        self.page = AsyncFacebookPage(call)
        self.post = AsyncFacebookPost(call)
        self.marketplace = AsyncFacebookMarketplace(call)


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
        time: GoogleSearchTime | None = None,
        safe_search: bool | None = None,
        scrape_results: bool | None = None,
        scrape_limit: int | None = None,
        page: int | None = None,
    ) -> GoogleSearchResponse:
        body = _omit_none(
            {
                "query": query,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "time": time,
                "safeSearch": safe_search,
                "scrapeResults": scrape_results,
                "scrapeLimit": scrape_limit,
                "page": page,
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
        topic: GoogleNewsTopic | None = None,
        country: str | None = None,
        language: str | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        time: GoogleSearchTime | None = None,
        sort: GoogleNewsSort | None = None,
        page: int | None = None,
    ) -> GoogleNewsResponse:
        body = _omit_none(
            {
                "query": query,
                "topic": topic,
                "country": country,
                "language": language,
                "includeDomains": include_domains,
                "excludeDomains": exclude_domains,
                "time": time,
                "sort": sort,
                "page": page,
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


class AsyncSurface:
    endpoints: AsyncEndpoints
    google: AsyncGoogle
    youtube: AsyncYoutube
    reddit: AsyncReddit
    instagram: AsyncInstagram
    tiktok: AsyncTiktok
    meta: AsyncMeta
    linkedin: AsyncLinkedin
    zillow: AsyncZillow
    upwork: AsyncUpwork
    indeed: AsyncIndeed
    careers: AsyncCareers
    tripadvisor: AsyncTripadvisor
    booking: AsyncBooking
    amazon: AsyncAmazon
    appstore: AsyncAppstore
    pinterest: AsyncPinterest
    x: AsyncX
    threads: AsyncThreads
    trustpilot: AsyncTrustpilot
    ebay: AsyncEbay
    airbnb: AsyncAirbnb
    facebook: AsyncFacebook
    web: AsyncWeb

    def __init__(self, call: AsyncCall) -> None:
        self.endpoints = AsyncEndpoints(call)
        self.google = AsyncGoogle(call)
        self.youtube = AsyncYoutube(call)
        self.reddit = AsyncReddit(call)
        self.instagram = AsyncInstagram(call)
        self.tiktok = AsyncTiktok(call)
        self.meta = AsyncMeta(call)
        self.linkedin = AsyncLinkedin(call)
        self.zillow = AsyncZillow(call)
        self.upwork = AsyncUpwork(call)
        self.indeed = AsyncIndeed(call)
        self.careers = AsyncCareers(call)
        self.tripadvisor = AsyncTripadvisor(call)
        self.booking = AsyncBooking(call)
        self.amazon = AsyncAmazon(call)
        self.appstore = AsyncAppstore(call)
        self.pinterest = AsyncPinterest(call)
        self.x = AsyncX(call)
        self.threads = AsyncThreads(call)
        self.trustpilot = AsyncTrustpilot(call)
        self.ebay = AsyncEbay(call)
        self.airbnb = AsyncAirbnb(call)
        self.facebook = AsyncFacebook(call)
        self.web = AsyncWeb(call)
