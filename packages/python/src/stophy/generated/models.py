"""Generated from openapi.json by scripts/gen_python.py. Do not edit."""

from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

WebSearchWithin = Literal[
    "day",
    "week",
    "month",
    "year",
    "all",
]

WebNewsTopic = Literal[
    "world",
    "nation",
    "business",
    "technology",
    "entertainment",
    "sports",
    "science",
    "health",
]

WebNewsWithin = Literal[
    "hour",
    "day",
    "week",
    "month",
    "year",
    "all",
]

WebContactsResponseDataSocialsItemPlatform = Literal[
    "facebook",
    "instagram",
    "x",
    "linkedin",
    "youtube",
    "tiktok",
    "pinterest",
    "github",
    "threads",
]

YoutubeSearchType = Literal[
    "videos",
    "all",
    "channels",
    "playlists",
    "shorts",
]

YoutubeSearchSort = Literal[
    "relevance",
    "top",
]

YoutubeCommentsSort = Literal[
    "top",
    "newest",
]

YoutubeChannelTab = Literal[
    "videos",
    "shorts",
    "live",
    "playlists",
    "posts",
]

RedditSearchType = Literal[
    "posts",
    "subreddits",
    "users",
]

RedditSearchSort = Literal[
    "relevance",
    "hot",
    "top",
    "newest",
    "mostComments",
]

RedditPostSort = Literal[
    "best",
    "top",
    "newest",
]

RedditSubredditSort = Literal[
    "hot",
    "newest",
    "top",
]

RedditUserTab = Literal[
    "overview",
    "posts",
    "comments",
]

RedditUserSort = Literal[
    "newest",
    "hot",
    "top",
]

MapsReviewsSort = Literal[
    "relevance",
    "newest",
    "highest",
    "lowest",
]

InstagramProfileResponseDataPostsItemType = Literal[
    "photo",
    "video",
    "reel",
    "carousel",
]

InstagramSearchType = Literal[
    "all",
    "posts",
    "reels",
]

TiktokProfileResponseDataPostsItemType = Literal[
    "video",
    "photo",
]

TiktokSearchType = Literal[
    "videos",
    "users",
]

ThreadsProfileResponseDataPostsItemType = Literal[
    "text",
    "photo",
    "video",
    "carousel",
]

TelegramPostsResponseDataChannelType = Literal[
    "channel",
    "group",
]

TelegramPostsResponseDataResultsItemMediaItemType = Literal[
    "photo",
    "video",
    "roundVideo",
    "sticker",
    "voice",
    "audio",
    "document",
    "poll",
]

MetaAdsPageStatus = Literal[
    "active",
    "inactive",
    "all",
]

LinkedinJobsSearchWithin = Literal[
    "day",
    "week",
    "month",
    "all",
]

LinkedinJobsSearchWorkplacesItem = Literal[
    "onsite",
    "remote",
    "hybrid",
]

LinkedinJobsSearchExperiencesItem = Literal[
    "internship",
    "entry",
    "associate",
    "midSenior",
    "director",
    "executive",
]

ZillowSearchStatus = Literal[
    "forSale",
    "forRent",
    "sold",
]

ZillowSearchHomeTypesItem = Literal[
    "house",
    "townhouse",
    "multiFamily",
    "condo",
    "land",
    "apartment",
    "manufactured",
]

ZillowSearchSort = Literal[
    "relevance",
    "newest",
    "priceHigh",
    "priceLow",
]

ZillowSearchResponseDataResultsItemStatus = Literal[
    "forSale",
    "forRent",
    "sold",
    "other",
]

UpworkSearchSort = Literal[
    "newest",
    "relevance",
]

UpworkSearchJobType = Literal[
    "hourly",
    "fixed",
]

UpworkSearchExperience = Literal[
    "entry",
    "intermediate",
    "expert",
]

GoogleTrendsTrendingWithin = Literal[
    "fourHours",
    "day",
    "twoDays",
    "week",
]

GoogleTrendsTrendingCategory = Literal[
    "autos",
    "beautyFashion",
    "business",
    "entertainment",
    "foodDrink",
    "games",
    "health",
    "hobbies",
    "jobsEducation",
    "lawGovernment",
    "other",
    "petsAnimals",
    "politics",
    "science",
    "shopping",
    "sports",
    "technology",
    "travel",
    "climate",
]

EmailCheckResponseDataEmailsItemStatus = Literal[
    "ok",
    "risky",
    "invalid",
]

EmailFindResponseDataStatus = Literal[
    "ok",
    "risky",
    "invalid",
    "unknown",
]

CryptoCoinsSort = Literal[
    "marketCap",
    "volume",
]

CryptoWalletChain = Literal[
    "ethereum",
    "base",
    "arbitrum",
    "optimism",
    "polygon",
    "gnosis",
    "bitcoin",
    "solana",
]

CryptoWalletResponseDataTransactionsItemStatus = Literal[
    "success",
    "failed",
    "pending",
]

IndeedSearchCountry = Literal[
    "us",
    "gb",
    "ca",
    "au",
    "nz",
    "ie",
    "in",
    "sg",
    "my",
    "ph",
    "za",
    "ng",
    "ae",
    "sa",
    "qa",
    "kw",
    "bh",
    "om",
    "pk",
    "hk",
    "jp",
    "kr",
    "tw",
    "cn",
    "id",
    "th",
    "vn",
    "de",
    "at",
    "ch",
    "fr",
    "be",
    "nl",
    "lu",
    "es",
    "pt",
    "it",
    "gr",
    "mt",
    "cy",
    "pl",
    "cz",
    "sk",
    "hu",
    "ro",
    "bg",
    "hr",
    "si",
    "ee",
    "lv",
    "lt",
    "fi",
    "se",
    "no",
    "dk",
    "ua",
    "tr",
    "il",
    "eg",
    "ma",
    "mx",
    "br",
    "ar",
    "cl",
    "co",
    "pe",
    "ec",
    "uy",
    "ve",
    "cr",
    "pa",
]

IndeedSearchWithin = Literal[
    "day",
    "week",
    "month",
]

IndeedSearchResponseDataResultsItemSalaryPeriod = Literal[
    "hour",
    "day",
    "week",
    "month",
    "year",
]

IndeedSearchResponseDataResultsItemJobTypesItem = Literal[
    "fullTime",
    "partTime",
    "contract",
    "internship",
]

TripadvisorSearchType = Literal[
    "all",
    "hotels",
    "restaurants",
    "attractions",
    "geos",
]

GoogletravelFlightsCabin = Literal[
    "economy",
    "premiumEconomy",
    "business",
    "first",
]

AmazonSearchSort = Literal[
    "relevance",
    "priceLow",
    "priceHigh",
    "mostReviewed",
    "newest",
    "bestSelling",
]

AmazonSearchCountry = Literal[
    "us",
    "gb",
    "de",
    "fr",
    "it",
    "es",
    "ca",
    "jp",
    "in",
    "au",
    "mx",
    "br",
    "nl",
    "se",
    "pl",
    "sg",
    "ae",
    "sa",
    "tr",
    "be",
    "eg",
]

WalmartSearchSort = Literal[
    "relevance",
    "priceLow",
    "priceHigh",
    "bestSelling",
    "highest",
    "newest",
]

AliexpressSearchSort = Literal[
    "relevance",
    "bestSelling",
    "priceLow",
    "priceHigh",
]

AppstoreSearchDevice = Literal[
    "iphone",
    "ipad",
    "mac",
]

AppstoreReviewsSort = Literal[
    "newest",
    "helpful",
    "highest",
    "lowest",
]

AppstoreTopChart = Literal[
    "free",
    "paid",
    "grossing",
]

AppstoreTopGenre = Literal[
    "business",
    "weather",
    "utilities",
    "travel",
    "sports",
    "socialNetworking",
    "reference",
    "productivity",
    "photoVideo",
    "news",
    "navigation",
    "music",
    "lifestyle",
    "healthFitness",
    "games",
    "finance",
    "entertainment",
    "education",
    "books",
    "medical",
    "foodDrink",
    "shopping",
    "developerTools",
    "graphicsDesign",
]

GoogleplayReviewsSort = Literal[
    "newest",
    "relevance",
    "highest",
]

RightmoveSearchStatus = Literal[
    "forSale",
    "forRent",
]

RightmoveSearchSort = Literal[
    "newest",
    "oldest",
    "priceHigh",
    "priceLow",
]

ImmoscoutSearchType = Literal[
    "apartmentRent",
    "apartmentBuy",
    "houseRent",
    "houseBuy",
    "land",
    "flatShare",
    "shortTerm",
]

ImmoscoutSearchSort = Literal[
    "newest",
    "priceLow",
    "priceHigh",
    "largest",
]

PinterestSearchType = Literal[
    "pins",
    "videos",
]

XPostResponseDataMediaItemType = Literal[
    "photo",
    "video",
    "gif",
]

FinanceHistoryInterval = Literal[
    "minute",
    "fiveMinutes",
    "fifteenMinutes",
    "hour",
    "day",
    "week",
    "month",
]

AdsSearchOption1MediaType = Literal[
    "text",
    "image",
    "video",
]

AdsSearchOption3Within = Literal[
    "month",
    "year",
    "all",
]

AdsSearchResponseDataOption1ResultsItemFormat = Literal[
    "text",
    "image",
    "video",
    "unknown",
]

SuggestOption2Country = Literal[
    "us",
    "ca",
    "mx",
    "br",
    "gb",
    "de",
    "fr",
    "it",
    "es",
    "nl",
    "be",
    "se",
    "pl",
    "tr",
    "ae",
    "sa",
    "eg",
    "in",
    "jp",
    "au",
    "sg",
]

GoogleTrendsOption1Resolution = Literal[
    "country",
    "region",
    "metro",
]

LinkedinProfileResponseDataRolesItem = TypedDict(
    "LinkedinProfileResponseDataRolesItem",
    {
        "title": NotRequired[str],
        "company": NotRequired[str],
        "companyUrl": NotRequired[str],
        "from": NotRequired[str],
        "to": NotRequired[str],
        "isCurrent": bool,
    },
)

LinkedinProfileResponseDataEducationItem = TypedDict(
    "LinkedinProfileResponseDataEducationItem",
    {
        "school": NotRequired[str],
        "degree": NotRequired[str],
        "schoolUrl": NotRequired[str],
        "from": NotRequired[str],
        "to": NotRequired[str],
    },
)

CryptoWalletResponseDataTransactionsItem = TypedDict(
    "CryptoWalletResponseDataTransactionsItem",
    {
        "transactionId": NotRequired[str],
        "createdAt": NotRequired[str],
        "block": NotRequired[int],
        "from": NotRequired[str],
        "to": NotRequired[str],
        "value": NotRequired[str],
        "fee": NotRequired[str],
        "status": CryptoWalletResponseDataTransactionsItemStatus,
        "method": NotRequired[str],
    },
)


class EndpointCatalogSourcesItem(TypedDict):
    id: str
    name: str
    summary: str


class EndpointCatalogEndpointsItem(TypedDict):
    id: str
    title: str
    summary: str
    bestWhen: str | None
    method: Literal["POST"]
    path: str
    credits: int
    keyless: bool
    cacheTtlSeconds: int
    input: NotRequired[dict[str, Any]]
    example: dict[str, Any] | None


class EndpointCatalog(TypedDict):
    sources: list[EndpointCatalogSourcesItem]
    endpoints: list[EndpointCatalogEndpointsItem]


class WebSearchResponseDataResultsItem(TypedDict):
    title: str
    url: str
    description: NotRequired[str]
    domain: NotRequired[str]
    position: int


class WebSearchResponseData(TypedDict):
    results: list[WebSearchResponseDataResultsItem]


class WebSearchResponse(TypedDict):
    success: Literal[True]
    data: WebSearchResponseData
    creditsUsed: int
    requestId: str


class WebNewsResponseDataResultsItem(TypedDict):
    title: str
    url: str
    publisherName: NotRequired[str]
    publisherUrl: NotRequired[str]
    publishedAt: NotRequired[str]
    domain: NotRequired[str]
    position: int


class WebNewsResponseData(TypedDict):
    results: list[WebNewsResponseDataResultsItem]


class WebNewsResponse(TypedDict):
    success: Literal[True]
    data: WebNewsResponseData
    creditsUsed: int
    requestId: str


class WebContactsResponseDataSocialsItem(TypedDict):
    platform: WebContactsResponseDataSocialsItemPlatform
    url: str


class WebContactsResponseData(TypedDict):
    emails: list[str]
    phones: list[str]
    socials: list[WebContactsResponseDataSocialsItem]
    pages: list[str]


class WebContactsResponse(TypedDict):
    success: Literal[True]
    data: WebContactsResponseData
    creditsUsed: int
    requestId: str


class YoutubeSearchResponseDataResultsItemOption0(TypedDict):
    type: Literal["video"]
    videoId: NotRequired[str]
    videoUrl: str
    title: NotRequired[str]
    channelId: NotRequired[str]
    channelName: NotRequired[str]
    channelUrl: NotRequired[str]
    channelUsername: NotRequired[str]
    durationSeconds: NotRequired[int]
    views: NotRequired[int]
    thumbnailUrl: NotRequired[str]
    isShort: bool
    isLive: bool
    publishedAt: NotRequired[str]


class YoutubeSearchResponseDataResultsItemOption1(TypedDict):
    type: Literal["channel"]
    channelId: NotRequired[str]
    channelUrl: str
    channelName: NotRequired[str]
    channelUsername: NotRequired[str]
    description: NotRequired[str]
    subscribers: NotRequired[int]
    thumbnailUrl: NotRequired[str]


class YoutubeSearchResponseDataResultsItemOption2(TypedDict):
    type: Literal["playlist"]
    playlistId: NotRequired[str]
    playlistUrl: str
    title: NotRequired[str]
    channelId: NotRequired[str]
    channelName: NotRequired[str]
    channelUrl: NotRequired[str]
    channelUsername: NotRequired[str]
    videos: NotRequired[int]
    thumbnailUrl: NotRequired[str]


class YoutubeSearchResponseData(TypedDict):
    results: list[
        YoutubeSearchResponseDataResultsItemOption0
        | YoutubeSearchResponseDataResultsItemOption1
        | YoutubeSearchResponseDataResultsItemOption2
    ]
    cursor: NotRequired[str]


class YoutubeSearchResponse(TypedDict):
    success: Literal[True]
    data: YoutubeSearchResponseData
    creditsUsed: int
    requestId: str


class YoutubeVideoResponseData(TypedDict):
    videoId: NotRequired[str]
    videoUrl: str
    title: NotRequired[str]
    channelId: NotRequired[str]
    channelName: NotRequired[str]
    channelUrl: NotRequired[str]
    channelUsername: NotRequired[str]
    durationSeconds: NotRequired[int]
    views: NotRequired[int]
    thumbnailUrl: NotRequired[str]
    isShort: bool
    isLive: bool
    publishedAt: NotRequired[str]
    description: NotRequired[str]
    likes: NotRequired[int]
    category: NotRequired[str]
    tags: list[str]


class YoutubeVideoResponse(TypedDict):
    success: Literal[True]
    data: YoutubeVideoResponseData
    creditsUsed: int
    requestId: str


class TranscriptResponseDataSegmentsItem(TypedDict):
    startSeconds: float
    endSeconds: float
    text: NotRequired[str]


class TranscriptResponseData(TypedDict):
    videoId: NotRequired[str]
    videoUrl: str
    language: NotRequired[str]
    isAutoGenerated: bool
    durationSeconds: NotRequired[float]
    text: NotRequired[str]
    segments: NotRequired[list[TranscriptResponseDataSegmentsItem]]


class TranscriptResponse(TypedDict):
    success: Literal[True]
    data: TranscriptResponseData
    creditsUsed: int
    requestId: str


class YoutubeCommentsResponseDataResultsItem(TypedDict):
    commentId: NotRequired[str]
    commentUrl: str
    text: NotRequired[str]
    authorId: NotRequired[str]
    authorName: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: NotRequired[str]
    likes: int
    replies: int
    publishedAt: NotRequired[str]
    isPinned: bool
    isHearted: bool
    isChannelOwner: bool
    repliesCursor: NotRequired[str]


class YoutubeCommentsResponseData(TypedDict):
    results: list[YoutubeCommentsResponseDataResultsItem]
    cursor: NotRequired[str]


class YoutubeCommentsResponse(TypedDict):
    success: Literal[True]
    data: YoutubeCommentsResponseData
    creditsUsed: int
    requestId: str


class YoutubeChannelResponseDataResultsItemOption2(TypedDict):
    type: Literal["post"]
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    comments: NotRequired[int]
    imageUrls: NotRequired[list[str]]
    videoId: NotRequired[str]
    videoTitle: NotRequired[str]
    pollChoices: NotRequired[list[str]]
    pollTotalVotes: NotRequired[int]


class YoutubeChannelResponseData(TypedDict):
    channelId: NotRequired[str]
    channelUrl: NotRequired[str]
    channelName: NotRequired[str]
    channelUsername: NotRequired[str]
    description: NotRequired[str]
    subscribers: NotRequired[int]
    videos: NotRequired[int]
    avatarUrl: NotRequired[str]
    bannerUrl: NotRequired[str]
    country: NotRequired[str]
    joinedDate: NotRequired[str]
    totalViews: NotRequired[int]
    results: list[
        YoutubeSearchResponseDataResultsItemOption0
        | YoutubeSearchResponseDataResultsItemOption2
        | YoutubeChannelResponseDataResultsItemOption2
    ]
    cursor: NotRequired[str]


class YoutubeChannelResponse(TypedDict):
    success: Literal[True]
    data: YoutubeChannelResponseData
    creditsUsed: int
    requestId: str


class YoutubePlaylistResponseData(TypedDict):
    playlistId: NotRequired[str]
    playlistUrl: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    channelId: NotRequired[str]
    channelName: NotRequired[str]
    channelUrl: NotRequired[str]
    channelUsername: NotRequired[str]
    videos: NotRequired[int]
    views: NotRequired[int]
    thumbnailUrl: NotRequired[str]
    results: list[YoutubeSearchResponseDataResultsItemOption0]
    cursor: NotRequired[str]


class YoutubePlaylistResponse(TypedDict):
    success: Literal[True]
    data: YoutubePlaylistResponseData
    creditsUsed: int
    requestId: str


class RedditSearchResponseDataResultsItemOption0PollOptionsItem(TypedDict):
    text: NotRequired[str]
    votes: NotRequired[int]


class RedditSearchResponseDataResultsItemOption0(TypedDict):
    type: Literal["post"]
    postId: NotRequired[str]
    postUrl: str
    title: NotRequired[str]
    text: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: NotRequired[str]
    subreddit: NotRequired[str]
    score: int
    upvotePercent: NotRequired[float]
    comments: int
    publishedAt: NotRequired[str]
    flair: NotRequired[str]
    linkUrl: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    isNsfw: bool
    isVideo: bool
    isPinned: bool
    imageUrls: NotRequired[list[str]]
    videoUrl: NotRequired[str]
    videoHlsUrl: NotRequired[str]
    videoDurationSeconds: NotRequired[float]
    pollOptions: NotRequired[list[RedditSearchResponseDataResultsItemOption0PollOptionsItem]]
    pollTotalVotes: NotRequired[int]
    pollEndsAt: NotRequired[str]
    repostOfUrl: NotRequired[str]


class RedditSearchResponseDataResultsItemOption1(TypedDict):
    type: Literal["subreddit"]
    subredditId: NotRequired[str]
    subredditName: NotRequired[str]
    subredditUrl: str
    title: NotRequired[str]
    description: NotRequired[str]
    members: NotRequired[int]
    createdAt: NotRequired[str]
    avatarUrl: NotRequired[str]
    isNsfw: bool


class RedditSearchResponseDataResultsItemOption2(TypedDict):
    type: Literal["user"]
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: str
    postKarma: NotRequired[int]
    commentKarma: NotRequired[int]
    createdAt: NotRequired[str]
    avatarUrl: NotRequired[str]
    isVerified: bool


class RedditSearchResponseData(TypedDict):
    results: list[
        RedditSearchResponseDataResultsItemOption0
        | RedditSearchResponseDataResultsItemOption1
        | RedditSearchResponseDataResultsItemOption2
    ]
    cursor: NotRequired[str]


class RedditSearchResponse(TypedDict):
    success: Literal[True]
    data: RedditSearchResponseData
    creditsUsed: int
    requestId: str


class RedditPostResponseDataCommentsItem(TypedDict):
    commentId: NotRequired[str]
    commentUrl: str
    parentId: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: NotRequired[str]
    text: NotRequired[str]
    score: int
    publishedAt: NotRequired[str]
    depth: int
    isSubmitter: bool
    isPinned: bool


class RedditPostResponseData(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    title: NotRequired[str]
    text: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: NotRequired[str]
    subreddit: NotRequired[str]
    score: int
    upvotePercent: NotRequired[float]
    publishedAt: NotRequired[str]
    flair: NotRequired[str]
    linkUrl: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    isNsfw: bool
    isVideo: bool
    isPinned: bool
    imageUrls: list[str]
    videoUrl: NotRequired[str]
    videoHlsUrl: NotRequired[str]
    videoDurationSeconds: NotRequired[float]
    pollOptions: list[RedditSearchResponseDataResultsItemOption0PollOptionsItem]
    pollTotalVotes: NotRequired[int]
    pollEndsAt: NotRequired[str]
    repostOfUrl: NotRequired[str]
    commentCount: int
    comments: list[RedditPostResponseDataCommentsItem]


class RedditPostResponse(TypedDict):
    success: Literal[True]
    data: RedditPostResponseData
    creditsUsed: int
    requestId: str


class RedditSubredditResponseDataRulesItem(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]


class RedditSubredditResponseData(TypedDict):
    subredditId: NotRequired[str]
    subredditName: NotRequired[str]
    subredditUrl: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    members: NotRequired[int]
    createdAt: NotRequired[str]
    avatarUrl: NotRequired[str]
    isNsfw: NotRequired[bool]
    rules: NotRequired[list[RedditSubredditResponseDataRulesItem]]
    results: list[RedditSearchResponseDataResultsItemOption0]
    cursor: NotRequired[str]


class RedditSubredditResponse(TypedDict):
    success: Literal[True]
    data: RedditSubredditResponseData
    creditsUsed: int
    requestId: str


class RedditUserResponseDataResultsItemOption1(TypedDict):
    type: Literal["comment"]
    commentId: NotRequired[str]
    commentUrl: str
    text: NotRequired[str]
    score: int
    publishedAt: NotRequired[str]
    subreddit: NotRequired[str]
    postId: NotRequired[str]
    postTitle: NotRequired[str]


class RedditUserResponseData(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: NotRequired[str]
    postKarma: NotRequired[int]
    commentKarma: NotRequired[int]
    createdAt: NotRequired[str]
    avatarUrl: NotRequired[str]
    isVerified: NotRequired[bool]
    results: list[
        RedditSearchResponseDataResultsItemOption0 | RedditUserResponseDataResultsItemOption1
    ]
    cursor: NotRequired[str]


class RedditUserResponse(TypedDict):
    success: Literal[True]
    data: RedditUserResponseData
    creditsUsed: int
    requestId: str


class RedditDomainResponseData(TypedDict):
    results: list[RedditSearchResponseDataResultsItemOption0]
    cursor: NotRequired[str]


class RedditDomainResponse(TypedDict):
    success: Literal[True]
    data: RedditDomainResponseData
    creditsUsed: int
    requestId: str


class MapsSearchResponseDataResultsItem(TypedDict):
    placeId: NotRequired[str]
    googlePlaceId: NotRequired[str]
    placeUrl: str
    name: NotRequired[str]
    categories: NotRequired[list[str]]
    address: NotRequired[str]
    latitude: float
    longitude: float
    rating: NotRequired[float]
    photos: NotRequired[int]
    phone: NotRequired[str]
    website: NotRequired[str]
    description: NotRequired[str]
    hoursToday: NotRequired[str]
    openStatus: NotRequired[str]
    timezone: NotRequired[str]
    plusCode: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    reservationUrl: NotRequired[str]
    attributes: NotRequired[list[str]]


class MapsSearchResponseData(TypedDict):
    results: list[MapsSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class MapsSearchResponse(TypedDict):
    success: Literal[True]
    data: MapsSearchResponseData
    creditsUsed: int
    requestId: str


class MapsPlaceResponseData(TypedDict):
    placeId: NotRequired[str]
    googlePlaceId: NotRequired[str]
    placeUrl: str
    name: NotRequired[str]
    categories: list[str]
    address: NotRequired[str]
    latitude: float
    longitude: float
    rating: NotRequired[float]
    photos: NotRequired[int]
    phone: NotRequired[str]
    website: NotRequired[str]
    description: NotRequired[str]
    hoursToday: NotRequired[str]
    openStatus: NotRequired[str]
    timezone: NotRequired[str]
    plusCode: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    reservationUrl: NotRequired[str]
    attributes: list[str]


class MapsPlaceResponse(TypedDict):
    success: Literal[True]
    data: MapsPlaceResponseData
    creditsUsed: int
    requestId: str


class MapsReviewsResponseDataResultsItemDetailsItem(TypedDict):
    label: NotRequired[str]
    value: NotRequired[str]
    rating: NotRequired[float]


class MapsReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    reviewUrl: NotRequired[str]
    rating: int
    text: NotRequired[str]
    language: NotRequired[str]
    publishedAt: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorReviews: NotRequired[int]
    authorPhotos: NotRequired[int]
    authorIsLocalGuide: bool
    imageUrls: NotRequired[list[str]]
    details: NotRequired[list[MapsReviewsResponseDataResultsItemDetailsItem]]
    ownerReplyText: NotRequired[str]
    ownerReplyAt: NotRequired[str]


class MapsReviewsResponseData(TypedDict):
    results: list[MapsReviewsResponseDataResultsItem]
    cursor: NotRequired[str]


class MapsReviewsResponse(TypedDict):
    success: Literal[True]
    data: MapsReviewsResponseData
    creditsUsed: int
    requestId: str


class InstagramProfileResponseDataPostsItem(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    type: InstagramProfileResponseDataPostsItemType
    text: NotRequired[str]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    comments: NotRequired[int]
    views: NotRequired[int]
    thumbnailUrl: NotRequired[str]
    imageUrls: NotRequired[list[str]]
    videoUrls: NotRequired[list[str]]
    imageDescription: NotRequired[str]
    isPinned: bool
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: bool
    taggedUsers: NotRequired[list[str]]
    coauthors: NotRequired[list[str]]
    audioTitle: NotRequired[str]
    audioArtist: NotRequired[str]
    audioIsOriginal: NotRequired[bool]
    isPaidPartnership: bool
    sponsors: NotRequired[list[str]]


class InstagramProfileResponseData(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: NotRequired[str]
    name: NotRequired[str]
    bio: NotRequired[str]
    bioLinkUrls: NotRequired[list[str]]
    pronouns: NotRequired[list[str]]
    isVerified: NotRequired[bool]
    isPrivate: NotRequired[bool]
    followers: NotRequired[int]
    following: NotRequired[int]
    postCount: NotRequired[int]
    avatarUrl: NotRequired[str]
    postsAnalyzed: NotRequired[int]
    averageLikes: NotRequired[float]
    averageComments: NotRequired[float]
    engagementRate: NotRequired[float]
    postsPerWeek: NotRequired[float]
    lastPostAt: NotRequired[str]
    posts: list[InstagramProfileResponseDataPostsItem]
    cursor: NotRequired[str]


class InstagramProfileResponse(TypedDict):
    success: Literal[True]
    data: InstagramProfileResponseData
    creditsUsed: int
    requestId: str


class InstagramPostResponseDataCommentsItem(TypedDict):
    commentId: NotRequired[str]
    commentUrl: str
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: bool
    text: NotRequired[str]
    likes: int
    replies: int
    publishedAt: NotRequired[str]


class InstagramPostResponseData(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    type: InstagramProfileResponseDataPostsItemType
    text: NotRequired[str]
    hashtags: list[str]
    mentions: list[str]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    views: NotRequired[int]
    thumbnailUrl: NotRequired[str]
    imageUrls: list[str]
    videoUrls: list[str]
    imageDescription: NotRequired[str]
    isPinned: bool
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: bool
    taggedUsers: list[str]
    coauthors: list[str]
    audioTitle: NotRequired[str]
    audioArtist: NotRequired[str]
    audioIsOriginal: NotRequired[bool]
    isPaidPartnership: bool
    sponsors: list[str]
    commentCount: NotRequired[int]
    comments: list[InstagramPostResponseDataCommentsItem]


class InstagramPostResponse(TypedDict):
    success: Literal[True]
    data: InstagramPostResponseData
    creditsUsed: int
    requestId: str


class InstagramSearchResponseData(TypedDict):
    results: list[InstagramProfileResponseDataPostsItem]


class InstagramSearchResponse(TypedDict):
    success: Literal[True]
    data: InstagramSearchResponseData
    creditsUsed: int
    requestId: str


class InstagramCommentsResponseData(TypedDict):
    results: list[InstagramPostResponseDataCommentsItem]
    cursor: NotRequired[str]


class InstagramCommentsResponse(TypedDict):
    success: Literal[True]
    data: InstagramCommentsResponseData
    creditsUsed: int
    requestId: str


class TiktokProfileResponseDataPostsItem(TypedDict):
    videoId: NotRequired[str]
    videoUrl: str
    type: TiktokProfileResponseDataPostsItemType
    text: NotRequired[str]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    publishedAt: NotRequired[str]
    durationSeconds: NotRequired[float]
    thumbnailUrl: NotRequired[str]
    imageUrls: NotRequired[list[str]]
    views: NotRequired[int]
    likes: NotRequired[int]
    comments: NotRequired[int]
    shares: NotRequired[int]
    saves: NotRequired[int]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: str
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: bool
    audioId: NotRequired[str]
    audioTitle: NotRequired[str]
    audioArtist: NotRequired[str]
    audioIsOriginal: NotRequired[bool]
    isAd: bool
    isAiGenerated: bool


class TiktokProfileResponseData(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: NotRequired[str]
    name: NotRequired[str]
    bio: NotRequired[str]
    bioLinkUrl: NotRequired[str]
    avatarUrl: NotRequired[str]
    isVerified: NotRequired[bool]
    isPrivate: NotRequired[bool]
    isOrganization: NotRequired[bool]
    language: NotRequired[str]
    createdAt: NotRequired[str]
    followers: NotRequired[int]
    following: NotRequired[int]
    likes: NotRequired[int]
    videos: NotRequired[int]
    posts: list[TiktokProfileResponseDataPostsItem]
    cursor: NotRequired[str]


class TiktokProfileResponse(TypedDict):
    success: Literal[True]
    data: TiktokProfileResponseData
    creditsUsed: int
    requestId: str


class TiktokVideoResponseData(TypedDict):
    videoId: NotRequired[str]
    videoUrl: str
    type: TiktokProfileResponseDataPostsItemType
    text: NotRequired[str]
    hashtags: list[str]
    mentions: list[str]
    publishedAt: NotRequired[str]
    durationSeconds: NotRequired[float]
    thumbnailUrl: NotRequired[str]
    imageUrls: list[str]
    views: NotRequired[int]
    likes: NotRequired[int]
    comments: NotRequired[int]
    shares: NotRequired[int]
    saves: NotRequired[int]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: str
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: bool
    audioId: NotRequired[str]
    audioTitle: NotRequired[str]
    audioArtist: NotRequired[str]
    audioIsOriginal: NotRequired[bool]
    country: NotRequired[str]
    isAd: bool
    isAiGenerated: bool


class TiktokVideoResponse(TypedDict):
    success: Literal[True]
    data: TiktokVideoResponseData
    creditsUsed: int
    requestId: str


class TiktokHashtagResponseData(TypedDict):
    results: list[TiktokProfileResponseDataPostsItem]
    cursor: NotRequired[str]


class TiktokHashtagResponse(TypedDict):
    success: Literal[True]
    data: TiktokHashtagResponseData
    creditsUsed: int
    requestId: str


class TiktokCommentsResponseDataResultsItem(TypedDict):
    commentId: NotRequired[str]
    text: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: str
    authorAvatarUrl: NotRequired[str]
    likes: int
    replies: int
    publishedAt: NotRequired[str]


class TiktokCommentsResponseData(TypedDict):
    results: list[TiktokCommentsResponseDataResultsItem]
    cursor: NotRequired[str]


class TiktokCommentsResponse(TypedDict):
    success: Literal[True]
    data: TiktokCommentsResponseData
    creditsUsed: int
    requestId: str


class TiktokSearchResponseDataResultsItemOption1(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: str
    name: NotRequired[str]
    bio: NotRequired[str]
    avatarUrl: NotRequired[str]
    isVerified: bool
    followers: NotRequired[int]
    likes: NotRequired[int]


class TiktokSearchResponseData(TypedDict):
    results: list[TiktokProfileResponseDataPostsItem | TiktokSearchResponseDataResultsItemOption1]
    cursor: NotRequired[str]


class TiktokSearchResponse(TypedDict):
    success: Literal[True]
    data: TiktokSearchResponseData
    creditsUsed: int
    requestId: str


class BlueskyProfileResponseDataPostsItem(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    language: NotRequired[str]
    publishedAt: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    likes: int
    reposts: int
    replies: int
    quotes: int
    replyToId: NotRequired[str]
    repostedByUsername: NotRequired[str]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    links: NotRequired[list[str]]
    imageUrls: NotRequired[list[str]]
    videoUrl: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    quotedUrl: NotRequired[str]
    quotedText: NotRequired[str]


class BlueskyProfileResponseData(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: NotRequired[str]
    name: NotRequired[str]
    bio: NotRequired[str]
    avatarUrl: NotRequired[str]
    createdAt: NotRequired[str]
    bannerUrl: NotRequired[str]
    followers: NotRequired[int]
    following: NotRequired[int]
    postCount: NotRequired[int]
    isVerified: NotRequired[bool]
    pinnedPostId: NotRequired[str]
    posts: list[BlueskyProfileResponseDataPostsItem]
    cursor: NotRequired[str]


class BlueskyProfileResponse(TypedDict):
    success: Literal[True]
    data: BlueskyProfileResponseData
    creditsUsed: int
    requestId: str


class BlueskyPostResponseDataRepliesItem(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    language: NotRequired[str]
    publishedAt: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    likes: int
    reposts: int
    replies: int
    quotes: int
    replyToId: NotRequired[str]
    repostedByUsername: NotRequired[str]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    links: NotRequired[list[str]]
    imageUrls: NotRequired[list[str]]
    videoUrl: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    quotedUrl: NotRequired[str]
    quotedText: NotRequired[str]
    depth: int


class BlueskyPostResponseData(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    language: NotRequired[str]
    publishedAt: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    likes: int
    reposts: int
    quotes: int
    replyToId: NotRequired[str]
    repostedByUsername: NotRequired[str]
    hashtags: list[str]
    mentions: list[str]
    links: list[str]
    imageUrls: list[str]
    videoUrl: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    quotedUrl: NotRequired[str]
    quotedText: NotRequired[str]
    replyCount: int
    replies: list[BlueskyPostResponseDataRepliesItem]


class BlueskyPostResponse(TypedDict):
    success: Literal[True]
    data: BlueskyPostResponseData
    creditsUsed: int
    requestId: str


class BlueskyFollowersResponseDataResultsItem(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: str
    name: NotRequired[str]
    bio: NotRequired[str]
    avatarUrl: NotRequired[str]
    createdAt: NotRequired[str]


class BlueskyFollowersResponseData(TypedDict):
    results: list[BlueskyFollowersResponseDataResultsItem]
    cursor: NotRequired[str]


class BlueskyFollowersResponse(TypedDict):
    success: Literal[True]
    data: BlueskyFollowersResponseData
    creditsUsed: int
    requestId: str


class ThreadsProfileResponseDataPostsItem(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    type: ThreadsProfileResponseDataPostsItemType
    text: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    reposts: NotRequired[int]
    quotes: NotRequired[int]
    shares: NotRequired[int]
    imageUrls: NotRequired[list[str]]
    videoUrls: NotRequired[list[str]]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    isReply: bool
    replyToUrl: NotRequired[str]
    isPinned: bool
    quotedUrl: NotRequired[str]
    quotedText: NotRequired[str]
    repostOfUrl: NotRequired[str]


class ThreadsProfileResponseData(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: str
    name: NotRequired[str]
    bio: NotRequired[str]
    bioLinkUrls: list[str]
    isVerified: bool
    isPrivate: bool
    followers: NotRequired[int]
    avatarUrl: NotRequired[str]
    posts: list[ThreadsProfileResponseDataPostsItem]
    cursor: NotRequired[str]


class ThreadsProfileResponse(TypedDict):
    success: Literal[True]
    data: ThreadsProfileResponseData
    creditsUsed: int
    requestId: str


class ThreadsPostResponseData(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    type: ThreadsProfileResponseDataPostsItemType
    text: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    reposts: NotRequired[int]
    quotes: NotRequired[int]
    shares: NotRequired[int]
    imageUrls: list[str]
    videoUrls: list[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    isReply: bool
    replyToUrl: NotRequired[str]
    isPinned: bool
    quotedUrl: NotRequired[str]
    quotedText: NotRequired[str]
    repostOfUrl: NotRequired[str]
    replyCount: NotRequired[int]
    thread: list[ThreadsProfileResponseDataPostsItem]
    replies: list[ThreadsProfileResponseDataPostsItem]
    cursor: NotRequired[str]


class ThreadsPostResponse(TypedDict):
    success: Literal[True]
    data: ThreadsPostResponseData
    creditsUsed: int
    requestId: str


class ThreadsSearchResponseData(TypedDict):
    results: list[ThreadsProfileResponseDataPostsItem]


class ThreadsSearchResponse(TypedDict):
    success: Literal[True]
    data: ThreadsSearchResponseData
    creditsUsed: int
    requestId: str


class TelegramPostsResponseDataResultsItemMediaItem(TypedDict):
    type: TelegramPostsResponseDataResultsItemMediaItemType
    url: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    durationSeconds: NotRequired[int]


class TelegramPostsResponseDataResultsItemReactionsItem(TypedDict):
    emoji: NotRequired[str]
    customEmojiId: NotRequired[str]
    isPaid: bool
    count: int


class TelegramPostsResponseDataResultsItem(TypedDict):
    postId: NotRequired[str]
    channelUsername: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    links: NotRequired[list[str]]
    publishedAt: NotRequired[str]
    isEdited: bool
    views: NotRequired[int]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    repostOfUrl: NotRequired[str]
    repostOfAuthorName: NotRequired[str]
    replyToUrl: NotRequired[str]
    media: NotRequired[list[TelegramPostsResponseDataResultsItemMediaItem]]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    linkSiteName: NotRequired[str]
    reactions: NotRequired[list[TelegramPostsResponseDataResultsItemReactionsItem]]


class TelegramPostsResponseData(TypedDict):
    channelId: NotRequired[str]
    channelUsername: NotRequired[str]
    channelUrl: NotRequired[str]
    channelType: NotRequired[TelegramPostsResponseDataChannelType]
    channelName: NotRequired[str]
    description: NotRequired[str]
    avatarUrl: NotRequired[str]
    isVerified: NotRequired[bool]
    subscribers: NotRequired[int]
    photos: NotRequired[int]
    videos: NotRequired[int]
    files: NotRequired[int]
    links: NotRequired[int]
    results: list[TelegramPostsResponseDataResultsItem]
    cursor: NotRequired[str]


class TelegramPostsResponse(TypedDict):
    success: Literal[True]
    data: TelegramPostsResponseData
    creditsUsed: int
    requestId: str


class TelegramPostResponseData(TypedDict):
    postId: NotRequired[str]
    channelUsername: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    links: list[str]
    publishedAt: NotRequired[str]
    isEdited: bool
    views: NotRequired[int]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    repostOfUrl: NotRequired[str]
    repostOfAuthorName: NotRequired[str]
    replyToUrl: NotRequired[str]
    media: list[TelegramPostsResponseDataResultsItemMediaItem]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    linkSiteName: NotRequired[str]
    reactions: list[TelegramPostsResponseDataResultsItemReactionsItem]


class TelegramPostResponse(TypedDict):
    success: Literal[True]
    data: TelegramPostResponseData
    creditsUsed: int
    requestId: str


class MetaAdsPageResponseDataResultsItemCardsItem(TypedDict):
    text: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    ctaText: NotRequired[str]
    imageUrl: NotRequired[str]
    videoUrl: NotRequired[str]


class MetaAdsPageResponseDataResultsItem(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    pageId: NotRequired[str]
    pageName: NotRequired[str]
    pageUrl: NotRequired[str]
    pageAvatarUrl: NotRequired[str]
    pageCategories: NotRequired[list[str]]
    pageLikes: NotRequired[int]
    isActive: bool
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    platforms: NotRequired[list[str]]
    format: NotRequired[str]
    text: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    linkDescription: NotRequired[str]
    ctaText: NotRequired[str]
    imageUrls: NotRequired[list[str]]
    videoUrls: NotRequired[list[str]]
    cards: NotRequired[list[MetaAdsPageResponseDataResultsItemCardsItem]]
    versions: int
    categories: NotRequired[list[str]]
    paidBy: NotRequired[str]
    spendMin: NotRequired[int]
    spendMax: NotRequired[int]
    spendCurrency: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    reachMin: NotRequired[int]
    reachMax: NotRequired[int]
    countries: NotRequired[list[str]]


class MetaAdsPageResponseData(TypedDict):
    results: list[MetaAdsPageResponseDataResultsItem]
    cursor: NotRequired[str]


class MetaAdsPageResponse(TypedDict):
    success: Literal[True]
    data: MetaAdsPageResponseData
    creditsUsed: int
    requestId: str


class LinkedinJobsSearchResponseDataResultsItem(TypedDict):
    jobId: NotRequired[str]
    jobUrl: str
    title: NotRequired[str]
    companyName: NotRequired[str]
    companyUrl: NotRequired[str]
    companyAvatarUrl: NotRequired[str]
    location: NotRequired[str]
    publishedAt: NotRequired[str]
    salaryText: NotRequired[str]
    isEasyApply: NotRequired[bool]
    insight: NotRequired[str]


class LinkedinJobsSearchResponseData(TypedDict):
    results: list[LinkedinJobsSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class LinkedinJobsSearchResponse(TypedDict):
    success: Literal[True]
    data: LinkedinJobsSearchResponseData
    creditsUsed: int
    requestId: str


class LinkedinJobsJobResponseData(TypedDict):
    jobId: NotRequired[str]
    jobUrl: str
    title: NotRequired[str]
    companyName: NotRequired[str]
    companyUrl: NotRequired[str]
    companyAvatarUrl: NotRequired[str]
    location: NotRequired[str]
    publishedAt: NotRequired[str]
    salaryText: NotRequired[str]
    isEasyApply: NotRequired[bool]
    applicants: NotRequired[int]
    applyUrl: NotRequired[str]
    seniority: NotRequired[str]
    employmentType: NotRequired[str]
    jobFunction: NotRequired[str]
    industries: NotRequired[str]
    description: NotRequired[str]


class LinkedinJobsJobResponse(TypedDict):
    success: Literal[True]
    data: LinkedinJobsJobResponseData
    creditsUsed: int
    requestId: str


class LinkedinCompanyResponseData(TypedDict):
    companyId: NotRequired[str]
    companyUrl: str
    name: NotRequired[str]
    industry: NotRequired[str]
    size: NotRequired[str]
    employees: NotRequired[int]
    headquarters: NotRequired[str]
    website: NotRequired[str]
    followers: NotRequired[int]
    description: NotRequired[str]
    specialties: list[str]
    founded: NotRequired[str]


class LinkedinCompanyResponse(TypedDict):
    success: Literal[True]
    data: LinkedinCompanyResponseData
    creditsUsed: int
    requestId: str


class LinkedinProfileResponseData(TypedDict):
    profileId: NotRequired[str]
    profileUrl: str
    name: NotRequired[str]
    headline: NotRequired[str]
    location: NotRequired[str]
    about: NotRequired[str]
    followers: NotRequired[int]
    roles: list[LinkedinProfileResponseDataRolesItem]
    education: list[LinkedinProfileResponseDataEducationItem]


class LinkedinProfileResponse(TypedDict):
    success: Literal[True]
    data: LinkedinProfileResponseData
    creditsUsed: int
    requestId: str


class LinkedinPostsResponseDataResultsItem(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]


class LinkedinPostsResponseData(TypedDict):
    results: list[LinkedinPostsResponseDataResultsItem]


class LinkedinPostsResponse(TypedDict):
    success: Literal[True]
    data: LinkedinPostsResponseData
    creditsUsed: int
    requestId: str


class ZillowSearchResponseDataResultsItemUnitsItem(TypedDict):
    bedrooms: NotRequired[float]
    price: NotRequired[float]


class ZillowSearchResponseDataResultsItem(TypedDict):
    propertyId: NotRequired[str]
    propertyUrl: str
    status: ZillowSearchResponseDataResultsItemStatus
    statusText: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: Literal["USD"]
    addressFull: NotRequired[str]
    addressStreet: NotRequired[str]
    addressCity: NotRequired[str]
    addressRegion: NotRequired[str]
    addressPostalCode: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    bedrooms: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    homeType: NotRequired[str]
    daysOnZillow: NotRequired[int]
    lastSoldAt: NotRequired[str]
    zestimate: NotRequired[float]
    rentZestimate: NotRequired[float]
    brokerName: NotRequired[str]
    imageUrl: NotRequired[str]
    buildingName: NotRequired[str]
    buildingMinRent: NotRequired[float]
    buildingMaxRent: NotRequired[float]
    buildingAvailableUnits: NotRequired[int]
    units: NotRequired[list[ZillowSearchResponseDataResultsItemUnitsItem]]


class ZillowSearchResponseData(TypedDict):
    results: list[ZillowSearchResponseDataResultsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class ZillowSearchResponse(TypedDict):
    success: Literal[True]
    data: ZillowSearchResponseData
    creditsUsed: int
    requestId: str


class ZillowPropertyResponseDataPriceHistoryItem(TypedDict):
    date: str
    price: NotRequired[float]
    event: NotRequired[str]


class ZillowPropertyResponseDataFactsItem(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]


class ZillowPropertyResponseData(TypedDict):
    propertyId: NotRequired[str]
    propertyUrl: str
    status: NotRequired[str]
    homeType: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: Literal["USD"]
    zestimate: NotRequired[float]
    rentZestimate: NotRequired[float]
    lastSoldPrice: NotRequired[float]
    lastSoldAt: NotRequired[str]
    addressFull: NotRequired[str]
    addressStreet: NotRequired[str]
    addressCity: NotRequired[str]
    addressRegion: NotRequired[str]
    addressPostalCode: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    bedrooms: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    lotSize: NotRequired[float]
    lotSizeUnit: NotRequired[str]
    yearBuilt: NotRequired[int]
    description: NotRequired[str]
    imageUrls: list[str]
    priceHistory: list[ZillowPropertyResponseDataPriceHistoryItem]
    daysOnZillow: NotRequired[int]
    views: NotRequired[int]
    saves: NotRequired[int]
    monthlyHoa: NotRequired[float]
    propertyTaxRate: NotRequired[float]
    mlsId: NotRequired[str]
    mlsName: NotRequired[str]
    brokerName: NotRequired[str]
    brokerPhone: NotRequired[str]
    agentName: NotRequired[str]
    agentPhone: NotRequired[str]
    agentEmail: NotRequired[str]
    facts: list[ZillowPropertyResponseDataFactsItem]


class ZillowPropertyResponse(TypedDict):
    success: Literal[True]
    data: ZillowPropertyResponseData
    creditsUsed: int
    requestId: str


class UpworkSearchResponseDataResultsItem(TypedDict):
    jobId: NotRequired[str]
    jobUrl: str
    title: NotRequired[str]
    description: NotRequired[str]
    skills: NotRequired[list[str]]
    type: NotRequired[UpworkSearchJobType]
    experience: NotRequired[UpworkSearchExperience]
    hourlyRateMin: NotRequired[float]
    hourlyRateMax: NotRequired[float]
    fixedBudget: NotRequired[float]
    budgetCurrency: NotRequired[str]
    durationWeeks: NotRequired[int]
    publishedAt: NotRequired[str]


class UpworkSearchResponseData(TypedDict):
    results: list[UpworkSearchResponseDataResultsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class UpworkSearchResponse(TypedDict):
    success: Literal[True]
    data: UpworkSearchResponseData
    creditsUsed: int
    requestId: str


class UpworkJobResponseData(TypedDict):
    jobId: NotRequired[str]
    jobUrl: str
    title: NotRequired[str]
    description: NotRequired[str]
    skills: list[str]
    type: NotRequired[UpworkSearchJobType]
    experience: NotRequired[UpworkSearchExperience]
    hourlyRateMin: NotRequired[float]
    hourlyRateMax: NotRequired[float]
    fixedBudget: NotRequired[float]
    budgetCurrency: NotRequired[str]
    durationWeeks: NotRequired[int]
    publishedAt: NotRequired[str]
    createdAt: NotRequired[str]
    status: NotRequired[str]
    category: NotRequired[str]
    categoryGroup: NotRequired[str]
    durationText: NotRequired[str]
    applicants: NotRequired[int]
    hired: NotRequired[int]
    interviewing: NotRequired[int]
    invitesSent: NotRequired[int]
    unansweredInvites: NotRequired[int]
    positions: NotRequired[int]
    lastClientActivityAt: NotRequired[str]
    clientCity: NotRequired[str]
    clientCountry: NotRequired[str]
    clientTimezone: NotRequired[str]
    clientTotalSpent: NotRequired[float]
    clientHires: NotRequired[int]
    clientJobsWithHires: NotRequired[int]
    clientActiveContracts: NotRequired[int]
    clientReviews: NotRequired[int]
    clientRating: NotRequired[float]
    clientOpenJobs: NotRequired[int]
    clientPostedJobs: NotRequired[int]
    clientJoinedAt: NotRequired[str]
    clientIndustry: NotRequired[str]
    clientCompanySize: NotRequired[str]


class UpworkJobResponse(TypedDict):
    success: Literal[True]
    data: UpworkJobResponseData
    creditsUsed: int
    requestId: str


class GoogleTrendsRelatedResponseDataResultsItem(TypedDict):
    query: NotRequired[str]
    value: float


class GoogleTrendsRelatedResponseData(TypedDict):
    results: list[GoogleTrendsRelatedResponseDataResultsItem]


class GoogleTrendsRelatedResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsRelatedResponseData
    creditsUsed: int
    requestId: str


class GoogleTrendsTrendingResponseDataResultsItem(TypedDict):
    query: NotRequired[str]
    volume: NotRequired[float]
    increasePercent: NotRequired[float]
    startedAt: str
    endedAt: NotRequired[str]
    isActive: bool
    related: NotRequired[list[str]]
    categories: NotRequired[list[GoogleTrendsTrendingCategory]]
    url: str


class GoogleTrendsTrendingResponseData(TypedDict):
    results: list[GoogleTrendsTrendingResponseDataResultsItem]


class GoogleTrendsTrendingResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsTrendingResponseData
    creditsUsed: int
    requestId: str


class SiteSeoResponseDataOutlineItem(TypedDict):
    level: int
    text: NotRequired[str]


class SiteSeoResponseDataHreflangItem(TypedDict):
    language: NotRequired[str]
    url: str


class SiteSeoResponseDataLinksCheckedItem(TypedDict):
    url: str
    status: NotRequired[int]


class SiteSeoResponseData(TypedDict):
    title: NotRequired[str]
    titleLength: int
    description: NotRequired[str]
    descriptionLength: int
    language: NotRequired[str]
    hasViewport: bool
    canonicalUrl: NotRequired[str]
    canonicalIsSelf: bool
    robotsMeta: NotRequired[str]
    isNoindex: bool
    isNofollow: bool
    isAllowedByRobotsTxt: NotRequired[bool]
    h1: list[str]
    h2: list[str]
    outline: list[SiteSeoResponseDataOutlineItem]
    hreflang: list[SiteSeoResponseDataHreflangItem]
    ogTitle: NotRequired[str]
    ogDescription: NotRequired[str]
    ogImage: NotRequired[str]
    ogUrl: NotRequired[str]
    ogType: NotRequired[str]
    ogSiteName: NotRequired[str]
    twitterCard: NotRequired[str]
    twitterTitle: NotRequired[str]
    twitterDescription: NotRequired[str]
    twitterImage: NotRequired[str]
    twitterSite: NotRequired[str]
    jsonLdBlocks: int
    jsonLdInvalid: int
    jsonLdTypes: list[str]
    imagesTotal: int
    imagesMissingAlt: int
    imagesEmptyAlt: int
    imagesMissingAltExamples: list[str]
    linksInternal: int
    linksExternal: int
    linksNofollow: int
    linksChecked: list[SiteSeoResponseDataLinksCheckedItem]
    linksBroken: list[SiteSeoResponseDataLinksCheckedItem]
    words: int
    issues: list[str]


class SiteSeoResponse(TypedDict):
    success: Literal[True]
    data: SiteSeoResponseData
    creditsUsed: int
    requestId: str


class EmailCheckResponseDataEmailsItem(TypedDict):
    email: NotRequired[str]
    status: EmailCheckResponseDataEmailsItemStatus
    reasons: NotRequired[list[str]]
    isValidSyntax: bool
    domain: NotRequired[str]
    mx: NotRequired[list[str]]
    isDisposable: bool
    isRole: bool
    isFree: bool


class EmailCheckResponseData(TypedDict):
    emails: list[EmailCheckResponseDataEmailsItem]


class EmailCheckResponse(TypedDict):
    success: Literal[True]
    data: EmailCheckResponseData
    creditsUsed: int
    requestId: str


class EmailFindResponseData(TypedDict):
    email: NotRequired[str]
    status: EmailFindResponseDataStatus
    domain: NotRequired[str]
    isCatchAll: NotRequired[bool]
    pattern: NotRequired[str]


class EmailFindResponse(TypedDict):
    success: Literal[True]
    data: EmailFindResponseData
    creditsUsed: int
    requestId: str


class CryptoCoinsResponseDataResultsItem(TypedDict):
    coinId: NotRequired[str]
    symbol: NotRequired[str]
    name: NotRequired[str]
    coinUrl: str
    imageUrl: NotRequired[str]
    rank: NotRequired[int]
    priceCurrency: NotRequired[str]
    price: NotRequired[float]
    marketCap: NotRequired[float]
    fullyDilutedValue: NotRequired[float]
    volume24h: NotRequired[float]
    high24h: NotRequired[float]
    low24h: NotRequired[float]
    change1h: NotRequired[float]
    change24h: NotRequired[float]
    change7d: NotRequired[float]
    change30d: NotRequired[float]
    circulatingSupply: NotRequired[float]
    totalSupply: NotRequired[float]
    maxSupply: NotRequired[float]
    ath: NotRequired[float]
    athAt: NotRequired[str]
    atl: NotRequired[float]
    atlAt: NotRequired[str]
    updatedAt: NotRequired[str]


class CryptoCoinsResponseData(TypedDict):
    results: list[CryptoCoinsResponseDataResultsItem]
    cursor: NotRequired[str]


class CryptoCoinsResponse(TypedDict):
    success: Literal[True]
    data: CryptoCoinsResponseData
    creditsUsed: int
    requestId: str


class CryptoCoinResponseDataSocialsItem(TypedDict):
    type: NotRequired[str]
    url: str


class CryptoCoinResponseDataContractsItem(TypedDict):
    chain: NotRequired[str]
    address: NotRequired[str]
    decimals: NotRequired[int]


class CryptoCoinResponseData(TypedDict):
    coinId: NotRequired[str]
    symbol: NotRequired[str]
    name: NotRequired[str]
    coinUrl: str
    imageUrl: NotRequired[str]
    rank: NotRequired[int]
    priceCurrency: NotRequired[str]
    price: NotRequired[float]
    marketCap: NotRequired[float]
    fullyDilutedValue: NotRequired[float]
    volume24h: NotRequired[float]
    high24h: NotRequired[float]
    low24h: NotRequired[float]
    change1h: NotRequired[float]
    change24h: NotRequired[float]
    change7d: NotRequired[float]
    change30d: NotRequired[float]
    circulatingSupply: NotRequired[float]
    totalSupply: NotRequired[float]
    maxSupply: NotRequired[float]
    ath: NotRequired[float]
    athAt: NotRequired[str]
    atl: NotRequired[float]
    atlAt: NotRequired[str]
    chains: list[str]
    addedAt: NotRequired[str]
    updatedAt: NotRequired[str]
    description: NotRequired[str]
    categories: list[str]
    change1y: NotRequired[float]
    websites: list[str]
    whitepaperUrl: NotRequired[str]
    explorers: list[str]
    socials: list[CryptoCoinResponseDataSocialsItem]
    contracts: list[CryptoCoinResponseDataContractsItem]
    launchedAt: NotRequired[str]
    watchlists: NotRequired[int]


class CryptoCoinResponse(TypedDict):
    success: Literal[True]
    data: CryptoCoinResponseData
    creditsUsed: int
    requestId: str


class CryptoHistoryResponseDataResultsItem(TypedDict):
    recordedAt: str
    price: NotRequired[float]
    marketCap: NotRequired[float]
    volume: NotRequired[float]


class CryptoHistoryResponseData(TypedDict):
    results: list[CryptoHistoryResponseDataResultsItem]


class CryptoHistoryResponse(TypedDict):
    success: Literal[True]
    data: CryptoHistoryResponseData
    creditsUsed: int
    requestId: str


class CryptoDexSearchResponseDataResultsItem(TypedDict):
    pairId: NotRequired[str]
    chain: NotRequired[str]
    dex: NotRequired[str]
    pairUrl: str
    labels: NotRequired[list[str]]
    baseTokenAddress: NotRequired[str]
    baseTokenName: NotRequired[str]
    baseTokenSymbol: NotRequired[str]
    quoteTokenAddress: NotRequired[str]
    quoteTokenName: NotRequired[str]
    quoteTokenSymbol: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    priceNative: NotRequired[float]
    buys5m: int
    sells5m: int
    buys1h: int
    sells1h: int
    buys6h: int
    sells6h: int
    buys24h: int
    sells24h: int
    volume5m: NotRequired[float]
    volume1h: NotRequired[float]
    volume6h: NotRequired[float]
    volume24h: NotRequired[float]
    priceChange5m: NotRequired[float]
    priceChange1h: NotRequired[float]
    priceChange6h: NotRequired[float]
    priceChange24h: NotRequired[float]
    liquidityUsd: NotRequired[float]
    liquidityBase: NotRequired[float]
    liquidityQuote: NotRequired[float]
    fullyDilutedValue: NotRequired[float]
    marketCap: NotRequired[float]
    createdAt: NotRequired[str]
    imageUrl: NotRequired[str]
    websites: NotRequired[list[str]]
    socials: NotRequired[list[CryptoCoinResponseDataSocialsItem]]
    boosts: NotRequired[int]


class CryptoDexSearchResponseData(TypedDict):
    results: list[CryptoDexSearchResponseDataResultsItem]


class CryptoDexSearchResponse(TypedDict):
    success: Literal[True]
    data: CryptoDexSearchResponseData
    creditsUsed: int
    requestId: str


class CryptoDexTokenResponseData(TypedDict):
    tokenAddress: NotRequired[str]
    chain: NotRequired[str]
    name: NotRequired[str]
    symbol: NotRequired[str]
    tokenUrl: str
    imageUrl: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    marketCap: NotRequired[float]
    fullyDilutedValue: NotRequired[float]
    liquidity: float
    volume24h: float
    websites: list[str]
    socials: list[CryptoCoinResponseDataSocialsItem]
    pairs: list[CryptoDexSearchResponseDataResultsItem]


class CryptoDexTokenResponse(TypedDict):
    success: Literal[True]
    data: CryptoDexTokenResponseData
    creditsUsed: int
    requestId: str


class CryptoWalletResponseDataTokensItem(TypedDict):
    address: NotRequired[str]
    symbol: NotRequired[str]
    name: NotRequired[str]
    decimals: NotRequired[int]
    amount: NotRequired[str]
    value: NotRequired[float]
    valueCurrency: NotRequired[str]


class CryptoWalletResponseData(TypedDict):
    symbol: NotRequired[str]
    balance: NotRequired[str]
    balanceValue: NotRequired[float]
    valueCurrency: NotRequired[str]
    tokens: list[CryptoWalletResponseDataTokensItem]
    transactions: list[CryptoWalletResponseDataTransactionsItem]
    cursor: NotRequired[str]


class CryptoWalletResponse(TypedDict):
    success: Literal[True]
    data: CryptoWalletResponseData
    creditsUsed: int
    requestId: str


class IndeedSearchResponseDataResultsItem(TypedDict):
    jobId: NotRequired[str]
    jobUrl: str
    title: NotRequired[str]
    companyName: NotRequired[str]
    companyUrl: NotRequired[str]
    companyAvatarUrl: NotRequired[str]
    companyWebsite: NotRequired[str]
    companyIndustry: NotRequired[str]
    companyEmployeesText: NotRequired[str]
    companyRevenueText: NotRequired[str]
    companyDescription: NotRequired[str]
    addressFull: NotRequired[str]
    addressCity: NotRequired[str]
    addressRegion: NotRequired[str]
    addressPostalCode: NotRequired[str]
    addressCountry: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    salaryMin: NotRequired[float]
    salaryMax: NotRequired[float]
    salaryPeriod: NotRequired[IndeedSearchResponseDataResultsItemSalaryPeriod]
    salaryCurrency: NotRequired[str]
    salaryIsEstimate: bool
    jobTypes: NotRequired[list[IndeedSearchResponseDataResultsItemJobTypesItem]]
    isRemote: bool
    attributes: NotRequired[list[str]]
    publishedAt: NotRequired[str]
    indexedAt: NotRequired[str]
    applyUrl: NotRequired[str]
    isEasyApply: bool
    isUrgent: bool
    source: NotRequired[str]
    description: NotRequired[str]


class IndeedSearchResponseData(TypedDict):
    results: list[IndeedSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class IndeedSearchResponse(TypedDict):
    success: Literal[True]
    data: IndeedSearchResponseData
    creditsUsed: int
    requestId: str


class IndeedJobResponseData(TypedDict):
    jobId: NotRequired[str]
    jobUrl: str
    title: NotRequired[str]
    companyName: NotRequired[str]
    companyUrl: NotRequired[str]
    companyAvatarUrl: NotRequired[str]
    companyWebsite: NotRequired[str]
    companyIndustry: NotRequired[str]
    companyEmployeesText: NotRequired[str]
    companyRevenueText: NotRequired[str]
    companyDescription: NotRequired[str]
    addressFull: NotRequired[str]
    addressCity: NotRequired[str]
    addressRegion: NotRequired[str]
    addressPostalCode: NotRequired[str]
    addressCountry: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    salaryMin: NotRequired[float]
    salaryMax: NotRequired[float]
    salaryPeriod: NotRequired[IndeedSearchResponseDataResultsItemSalaryPeriod]
    salaryCurrency: NotRequired[str]
    salaryIsEstimate: bool
    jobTypes: list[IndeedSearchResponseDataResultsItemJobTypesItem]
    isRemote: bool
    attributes: list[str]
    publishedAt: NotRequired[str]
    indexedAt: NotRequired[str]
    applyUrl: NotRequired[str]
    isEasyApply: bool
    isUrgent: bool
    source: NotRequired[str]
    description: NotRequired[str]
    descriptionHtml: NotRequired[str]
    isExpired: bool
    language: NotRequired[str]


class IndeedJobResponse(TypedDict):
    success: Literal[True]
    data: IndeedJobResponseData
    creditsUsed: int
    requestId: str


class TripadvisorSearchResponseDataResultsItem(TypedDict):
    placeId: NotRequired[str]
    placeUrl: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    address: NotRequired[str]
    parent: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    imageUrl: NotRequired[str]


class TripadvisorSearchResponseData(TypedDict):
    results: list[TripadvisorSearchResponseDataResultsItem]


class TripadvisorSearchResponse(TypedDict):
    success: Literal[True]
    data: TripadvisorSearchResponseData
    creditsUsed: int
    requestId: str


class TripadvisorPlaceResponseDataParentsItem(TypedDict):
    placeId: NotRequired[str]
    name: NotRequired[str]


class TripadvisorPlaceResponseDataHoursItem(TypedDict):
    days: NotRequired[str]
    times: NotRequired[list[str]]


class TripadvisorPlaceResponseData(TypedDict):
    placeId: NotRequired[str]
    placeUrl: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    subtypes: list[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    rankingText: NotRequired[str]
    rankingPosition: NotRequired[int]
    rankingOf: NotRequired[int]
    rankingGeo: NotRequired[str]
    priceLevel: NotRequired[str]
    priceRangeText: NotRequired[str]
    hotelClass: NotRequired[float]
    description: NotRequired[str]
    addressFull: NotRequired[str]
    addressStreet: NotRequired[str]
    addressCity: NotRequired[str]
    addressRegion: NotRequired[str]
    addressCountry: NotRequired[str]
    addressPostalCode: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    phone: NotRequired[str]
    website: NotRequired[str]
    email: NotRequired[str]
    neighborhoods: list[str]
    parents: list[TripadvisorPlaceResponseDataParentsItem]
    cuisines: list[str]
    hours: list[TripadvisorPlaceResponseDataHoursItem]
    tags: list[str]
    imageUrl: NotRequired[str]
    timezone: NotRequired[str]
    isClosed: bool


class TripadvisorPlaceResponse(TypedDict):
    success: Literal[True]
    data: TripadvisorPlaceResponseData
    creditsUsed: int
    requestId: str


class TripadvisorReviewsResponseDataResultsItemSubRatingsItem(TypedDict):
    name: NotRequired[str]
    rating: float


class TripadvisorReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    reviewUrl: NotRequired[str]
    rating: NotRequired[float]
    title: NotRequired[str]
    text: NotRequired[str]
    language: NotRequired[str]
    createdDate: NotRequired[str]
    publishedDate: NotRequired[str]
    stayDate: NotRequired[str]
    tripType: NotRequired[str]
    helpful: int
    subRatings: NotRequired[list[TripadvisorReviewsResponseDataResultsItemSubRatingsItem]]
    authorName: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAddress: NotRequired[str]
    authorContributions: NotRequired[int]
    ownerReplyText: NotRequired[str]
    ownerReplyDate: NotRequired[str]
    ownerReplyAuthor: NotRequired[str]


class TripadvisorReviewsResponseData(TypedDict):
    placeId: NotRequired[str]
    placeName: NotRequired[str]
    placeType: NotRequired[str]
    placeUrl: NotRequired[str]
    total: NotRequired[int]
    results: list[TripadvisorReviewsResponseDataResultsItem]
    cursor: NotRequired[str]


class TripadvisorReviewsResponse(TypedDict):
    success: Literal[True]
    data: TripadvisorReviewsResponseData
    creditsUsed: int
    requestId: str


class GoogletravelFlightsResponseDataResultsItemLegsItem(TypedDict):
    flightNumber: NotRequired[str]
    airline: NotRequired[str]
    originCode: NotRequired[str]
    originName: NotRequired[str]
    destinationCode: NotRequired[str]
    destinationName: NotRequired[str]
    departureLocalTime: NotRequired[str]
    arrivalLocalTime: NotRequired[str]
    durationSeconds: NotRequired[int]
    aircraft: NotRequired[str]
    legroom: NotRequired[str]


class GoogletravelFlightsResponseDataResultsItemLayoversItem(TypedDict):
    airport: NotRequired[str]
    name: NotRequired[str]
    city: NotRequired[str]
    durationSeconds: NotRequired[int]


class GoogletravelFlightsResponseDataResultsItem(TypedDict):
    isBest: bool
    price: NotRequired[float]
    priceCurrency: Literal["USD"]
    airlines: NotRequired[list[str]]
    stops: int
    durationSeconds: NotRequired[int]
    departureLocalTime: NotRequired[str]
    arrivalLocalTime: NotRequired[str]
    legs: NotRequired[list[GoogletravelFlightsResponseDataResultsItemLegsItem]]
    layovers: NotRequired[list[GoogletravelFlightsResponseDataResultsItemLayoversItem]]
    emissionsGrams: NotRequired[int]
    typicalEmissionsGrams: NotRequired[int]


class GoogletravelFlightsResponseData(TypedDict):
    results: list[GoogletravelFlightsResponseDataResultsItem]


class GoogletravelFlightsResponse(TypedDict):
    success: Literal[True]
    data: GoogletravelFlightsResponseData
    creditsUsed: int
    requestId: str


class AmazonSearchResponseDataResultsItem(TypedDict):
    productId: NotRequired[str]
    productUrl: str
    title: NotRequired[str]
    imageUrl: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    boughtPastMonth: NotRequired[int]
    isSponsored: bool


class AmazonSearchResponseData(TypedDict):
    results: list[AmazonSearchResponseDataResultsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AmazonSearchResponse(TypedDict):
    success: Literal[True]
    data: AmazonSearchResponseData
    creditsUsed: int
    requestId: str


class AmazonProductResponseDataVariantsItem(TypedDict):
    productId: NotRequired[str]
    options: NotRequired[str]


class AmazonProductResponseDataBestSellersRankItem(TypedDict):
    rank: int
    category: NotRequired[str]


class AmazonProductResponseDataTopReviewsItem(TypedDict):
    reviewId: NotRequired[str]
    authorName: NotRequired[str]
    rating: NotRequired[float]
    title: NotRequired[str]
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    isVerified: bool
    variant: NotRequired[str]
    helpfulVotes: NotRequired[int]
    imageUrls: NotRequired[list[str]]


class AmazonProductResponseData(TypedDict):
    productId: NotRequired[str]
    productUrl: str
    title: NotRequired[str]
    brand: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    availability: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    bullets: list[str]
    description: NotRequired[str]
    imageUrls: list[str]
    variants: list[AmazonProductResponseDataVariantsItem]
    sellerName: NotRequired[str]
    sellerId: NotRequired[str]
    sellerShipsFrom: NotRequired[str]
    categories: list[str]
    bestSellersRank: list[AmazonProductResponseDataBestSellersRankItem]
    specs: list[ZillowPropertyResponseDataFactsItem]
    topReviews: list[AmazonProductResponseDataTopReviewsItem]


class AmazonProductResponse(TypedDict):
    success: Literal[True]
    data: AmazonProductResponseData
    creditsUsed: int
    requestId: str


class AmazonBestsellersResponseDataResultsItem(TypedDict):
    rank: int
    productId: NotRequired[str]
    productUrl: str
    title: NotRequired[str]
    imageUrl: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]


class AmazonBestsellersResponseData(TypedDict):
    category: NotRequired[str]
    results: list[AmazonBestsellersResponseDataResultsItem]
    cursor: NotRequired[str]


class AmazonBestsellersResponse(TypedDict):
    success: Literal[True]
    data: AmazonBestsellersResponseData
    creditsUsed: int
    requestId: str


class ShopifyProductsResponseDataResultsItemOptionsItem(TypedDict):
    name: NotRequired[str]
    values: NotRequired[list[str]]


class ShopifyProductsResponseDataResultsItemVariantsItem(TypedDict):
    variantId: NotRequired[str]
    title: NotRequired[str]
    sku: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    isAvailable: bool
    options: NotRequired[list[str]]
    weightGrams: NotRequired[float]


class ShopifyProductsResponseDataResultsItem(TypedDict):
    productId: NotRequired[str]
    slug: NotRequired[str]
    productUrl: str
    title: NotRequired[str]
    vendor: NotRequired[str]
    productType: NotRequired[str]
    tags: NotRequired[list[str]]
    description: NotRequired[str]
    price: NotRequired[float]
    maxPrice: NotRequired[float]
    originalPrice: NotRequired[float]
    isAvailable: bool
    options: NotRequired[list[ShopifyProductsResponseDataResultsItemOptionsItem]]
    variants: NotRequired[list[ShopifyProductsResponseDataResultsItemVariantsItem]]
    imageUrls: NotRequired[list[str]]
    publishedAt: NotRequired[str]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]


class ShopifyProductsResponseData(TypedDict):
    results: list[ShopifyProductsResponseDataResultsItem]
    cursor: NotRequired[str]


class ShopifyProductsResponse(TypedDict):
    success: Literal[True]
    data: ShopifyProductsResponseData
    creditsUsed: int
    requestId: str


class ShopifyCollectionsResponseDataResultsItem(TypedDict):
    collectionId: NotRequired[str]
    slug: NotRequired[str]
    collectionUrl: str
    title: NotRequired[str]
    description: NotRequired[str]
    imageUrl: NotRequired[str]
    products: NotRequired[int]
    publishedAt: NotRequired[str]
    updatedAt: NotRequired[str]


class ShopifyCollectionsResponseData(TypedDict):
    results: list[ShopifyCollectionsResponseDataResultsItem]
    cursor: NotRequired[str]


class ShopifyCollectionsResponse(TypedDict):
    success: Literal[True]
    data: ShopifyCollectionsResponseData
    creditsUsed: int
    requestId: str


class ShopifyStoreResponseData(TypedDict):
    storeId: NotRequired[str]
    storeUrl: str
    isShopify: bool
    name: NotRequired[str]
    description: NotRequired[str]
    myshopifyDomain: NotRequired[str]
    domain: NotRequired[str]
    currency: NotRequired[str]
    addressCity: NotRequired[str]
    addressRegion: NotRequired[str]
    addressCountry: NotRequired[str]
    shipsTo: list[str]
    products: NotRequired[int]
    collections: NotRequired[int]


class ShopifyStoreResponse(TypedDict):
    success: Literal[True]
    data: ShopifyStoreResponseData
    creditsUsed: int
    requestId: str


class WalmartSearchResponseDataResultsItem(TypedDict):
    productId: NotRequired[str]
    productUrl: str
    title: NotRequired[str]
    imageUrl: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    sellerName: NotRequired[str]
    availability: NotRequired[str]
    isSponsored: bool


class WalmartSearchResponseData(TypedDict):
    results: list[WalmartSearchResponseDataResultsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class WalmartSearchResponse(TypedDict):
    success: Literal[True]
    data: WalmartSearchResponseData
    creditsUsed: int
    requestId: str


class WalmartProductResponseDataTopReviewsItem(TypedDict):
    reviewId: NotRequired[str]
    authorName: NotRequired[str]
    rating: NotRequired[float]
    title: NotRequired[str]
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    helpful: NotRequired[int]


class WalmartProductResponseData(TypedDict):
    productId: NotRequired[str]
    productUrl: str
    title: NotRequired[str]
    brand: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    availability: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    sellerName: NotRequired[str]
    sellerId: NotRequired[str]
    categories: list[str]
    imageUrls: list[str]
    description: NotRequired[str]
    highlights: NotRequired[str]
    specs: list[ZillowPropertyResponseDataFactsItem]
    variants: list[ShopifyProductsResponseDataResultsItemOptionsItem]
    upc: NotRequired[str]
    model: NotRequired[str]
    topReviews: list[WalmartProductResponseDataTopReviewsItem]


class WalmartProductResponse(TypedDict):
    success: Literal[True]
    data: WalmartProductResponseData
    creditsUsed: int
    requestId: str


class AliexpressSearchResponseDataResultsItem(TypedDict):
    productId: NotRequired[str]
    productUrl: str
    title: NotRequired[str]
    imageUrl: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    rating: NotRequired[float]
    sold: NotRequired[int]
    isSponsored: bool


class AliexpressSearchResponseData(TypedDict):
    results: list[AliexpressSearchResponseDataResultsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AliexpressSearchResponse(TypedDict):
    success: Literal[True]
    data: AliexpressSearchResponseData
    creditsUsed: int
    requestId: str


class AliexpressProductResponseDataSkusItem(TypedDict):
    skuId: NotRequired[str]
    attributes: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    stock: NotRequired[int]
    isAvailable: bool


class AliexpressProductResponseData(TypedDict):
    productId: NotRequired[str]
    productUrl: str
    title: NotRequired[str]
    imageUrls: list[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    sold: NotRequired[int]
    storeName: NotRequired[str]
    storeId: NotRequired[str]
    sellerId: NotRequired[str]
    storePositivePercent: NotRequired[float]
    options: list[ShopifyProductsResponseDataResultsItemOptionsItem]
    skus: list[AliexpressProductResponseDataSkusItem]
    specs: list[ZillowPropertyResponseDataFactsItem]
    categoryId: NotRequired[str]


class AliexpressProductResponse(TypedDict):
    success: Literal[True]
    data: AliexpressProductResponseData
    creditsUsed: int
    requestId: str


class AppstoreAppResponseData(TypedDict):
    appId: NotRequired[str]
    appUrl: str
    bundleId: NotRequired[str]
    name: NotRequired[str]
    subtitle: NotRequired[str]
    developerId: NotRequired[str]
    developerName: NotRequired[str]
    developerUrl: NotRequired[str]
    seller: NotRequired[str]
    website: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    priceText: NotRequired[str]
    hasInAppPurchases: NotRequired[bool]
    genres: list[str]
    primaryGenreId: NotRequired[str]
    primaryGenre: NotRequired[str]
    contentRating: NotRequired[str]
    description: NotRequired[str]
    releaseNotes: NotRequired[str]
    version: NotRequired[str]
    releasedAt: NotRequired[str]
    updatedAt: NotRequired[str]
    minimumOsVersion: NotRequired[str]
    sizeBytes: NotRequired[int]
    languages: list[str]
    rating: NotRequired[float]
    ratings: NotRequired[int]
    ratingsOne: NotRequired[int]
    ratingsTwo: NotRequired[int]
    ratingsThree: NotRequired[int]
    ratingsFour: NotRequired[int]
    ratingsFive: NotRequired[int]
    chartName: NotRequired[str]
    chartGenre: NotRequired[str]
    chartPosition: NotRequired[int]
    iconUrl: NotRequired[str]
    screenshotUrls: list[str]
    ipadScreenshotUrls: list[str]


class AppstoreAppResponse(TypedDict):
    success: Literal[True]
    data: AppstoreAppResponseData
    creditsUsed: int
    requestId: str


class AppstoreSearchResponseDataResultsItem(TypedDict):
    appId: NotRequired[str]
    appUrl: str
    bundleId: NotRequired[str]
    name: NotRequired[str]
    developerId: NotRequired[str]
    developerName: NotRequired[str]
    developerUrl: NotRequired[str]
    seller: NotRequired[str]
    website: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    priceText: NotRequired[str]
    genres: NotRequired[list[str]]
    primaryGenreId: NotRequired[str]
    primaryGenre: NotRequired[str]
    contentRating: NotRequired[str]
    description: NotRequired[str]
    releaseNotes: NotRequired[str]
    version: NotRequired[str]
    releasedAt: NotRequired[str]
    updatedAt: NotRequired[str]
    minimumOsVersion: NotRequired[str]
    sizeBytes: NotRequired[int]
    languages: NotRequired[list[str]]
    rating: NotRequired[float]
    ratings: NotRequired[int]
    iconUrl: NotRequired[str]
    screenshotUrls: NotRequired[list[str]]
    ipadScreenshotUrls: NotRequired[list[str]]


class AppstoreSearchResponseData(TypedDict):
    results: list[AppstoreSearchResponseDataResultsItem]


class AppstoreSearchResponse(TypedDict):
    success: Literal[True]
    data: AppstoreSearchResponseData
    creditsUsed: int
    requestId: str


class AppstoreReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    rating: int
    title: NotRequired[str]
    text: NotRequired[str]
    authorName: NotRequired[str]
    publishedAt: NotRequired[str]
    isEdited: bool


class AppstoreReviewsResponseData(TypedDict):
    results: list[AppstoreReviewsResponseDataResultsItem]
    cursor: NotRequired[str]


class AppstoreReviewsResponse(TypedDict):
    success: Literal[True]
    data: AppstoreReviewsResponseData
    creditsUsed: int
    requestId: str


class AppstoreTopResponseDataResultsItem(TypedDict):
    rank: int
    appId: NotRequired[str]
    appUrl: str
    bundleId: NotRequired[str]
    name: NotRequired[str]
    developerId: NotRequired[str]
    developerName: NotRequired[str]
    developerUrl: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    genreId: NotRequired[str]
    genre: NotRequired[str]
    releasedAt: NotRequired[str]
    summary: NotRequired[str]
    iconUrl: NotRequired[str]


class AppstoreTopResponseData(TypedDict):
    results: list[AppstoreTopResponseDataResultsItem]


class AppstoreTopResponse(TypedDict):
    success: Literal[True]
    data: AppstoreTopResponseData
    creditsUsed: int
    requestId: str


class GoogleplayAppResponseData(TypedDict):
    appId: NotRequired[str]
    appUrl: str
    name: NotRequired[str]
    summary: NotRequired[str]
    description: NotRequired[str]
    developerId: NotRequired[str]
    developerName: NotRequired[str]
    developerEmail: NotRequired[str]
    developerWebsite: NotRequired[str]
    developerAddress: NotRequired[str]
    privacyPolicyUrl: NotRequired[str]
    genreId: NotRequired[str]
    genre: NotRequired[str]
    contentRating: NotRequired[str]
    installsText: NotRequired[str]
    installsMin: NotRequired[int]
    installsExact: NotRequired[int]
    rating: NotRequired[float]
    ratings: NotRequired[int]
    reviews: NotRequired[int]
    ratingsOne: NotRequired[int]
    ratingsTwo: NotRequired[int]
    ratingsThree: NotRequired[int]
    ratingsFour: NotRequired[int]
    ratingsFive: NotRequired[int]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    hasInAppPurchases: bool
    inAppPriceText: NotRequired[str]
    hasAds: bool
    version: NotRequired[str]
    recentChanges: NotRequired[str]
    releasedAt: NotRequired[str]
    updatedAt: NotRequired[str]
    iconUrl: NotRequired[str]
    bannerUrl: NotRequired[str]
    screenshotUrls: list[str]


class GoogleplayAppResponse(TypedDict):
    success: Literal[True]
    data: GoogleplayAppResponseData
    creditsUsed: int
    requestId: str


class GoogleplaySearchResponseDataResultsItem(TypedDict):
    appId: NotRequired[str]
    appUrl: str
    name: NotRequired[str]
    developerName: NotRequired[str]
    summary: NotRequired[str]
    genre: NotRequired[str]
    installsText: NotRequired[str]
    installsMin: NotRequired[int]
    rating: NotRequired[float]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    iconUrl: NotRequired[str]


class GoogleplaySearchResponseData(TypedDict):
    results: list[GoogleplaySearchResponseDataResultsItem]


class GoogleplaySearchResponse(TypedDict):
    success: Literal[True]
    data: GoogleplaySearchResponseData
    creditsUsed: int
    requestId: str


class GoogleplayReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    reviewUrl: str
    rating: int
    text: NotRequired[str]
    authorName: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    publishedAt: NotRequired[str]
    likes: int
    appVersion: NotRequired[str]
    ownerReplyText: NotRequired[str]
    ownerReplyAt: NotRequired[str]


class GoogleplayReviewsResponseData(TypedDict):
    results: list[GoogleplayReviewsResponseDataResultsItem]
    cursor: NotRequired[str]


class GoogleplayReviewsResponse(TypedDict):
    success: Literal[True]
    data: GoogleplayReviewsResponseData
    creditsUsed: int
    requestId: str


class AirbnbSearchResponseDataResultsItem(TypedDict):
    listingId: NotRequired[str]
    listingUrl: str
    name: NotRequired[str]
    title: NotRequired[str]
    subtitle: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    priceText: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    bedrooms: NotRequired[float]
    beds: NotRequired[float]
    bathrooms: NotRequired[float]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    badges: NotRequired[list[str]]
    imageUrls: NotRequired[list[str]]


class AirbnbSearchResponseData(TypedDict):
    results: list[AirbnbSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class AirbnbSearchResponse(TypedDict):
    success: Literal[True]
    data: AirbnbSearchResponseData
    creditsUsed: int
    requestId: str


class AirbnbListingResponseDataRatingCategoriesItem(TypedDict):
    category: NotRequired[str]
    rating: float


class AirbnbListingResponseDataRatingDistributionItem(TypedDict):
    stars: NotRequired[str]
    percent: float


class AirbnbListingResponseDataAmenitiesItem(TypedDict):
    group: NotRequired[str]
    name: NotRequired[str]
    isAvailable: bool


class AirbnbListingResponseData(TypedDict):
    listingId: NotRequired[str]
    listingUrl: str
    name: NotRequired[str]
    headline: NotRequired[str]
    description: NotRequired[str]
    propertyType: NotRequired[str]
    roomType: NotRequired[str]
    guests: NotRequired[int]
    bedrooms: NotRequired[float]
    beds: NotRequired[float]
    bathrooms: NotRequired[float]
    isPetFriendly: NotRequired[bool]
    isGuestFavorite: bool
    rating: NotRequired[float]
    reviews: NotRequired[int]
    ratingCategories: list[AirbnbListingResponseDataRatingCategoriesItem]
    ratingDistribution: list[AirbnbListingResponseDataRatingDistributionItem]
    hostId: NotRequired[str]
    hostName: NotRequired[str]
    hostIsSuperhost: bool
    hostIsVerified: bool
    hostRating: NotRequired[float]
    hostReviews: NotRequired[int]
    hostYearsHosting: NotRequired[int]
    hostBio: NotRequired[str]
    hostResponsePercent: NotRequired[float]
    hostResponseTime: NotRequired[str]
    hostHighlights: list[str]
    hostAvatarUrl: NotRequired[str]
    highlights: list[RedditSubredditResponseDataRulesItem]
    amenities: list[AirbnbListingResponseDataAmenitiesItem]
    houseRules: list[str]
    safety: list[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    isLocationExact: bool
    area: NotRequired[str]
    neighborhood: NotRequired[str]
    imageUrls: list[str]


class AirbnbListingResponse(TypedDict):
    success: Literal[True]
    data: AirbnbListingResponseData
    creditsUsed: int
    requestId: str


class AirbnbCalendarResponseDataResultsItem(TypedDict):
    date: str
    isAvailable: bool
    isBookable: bool
    isCheckInDay: bool
    isCheckOutDay: bool
    minNights: NotRequired[int]
    maxNights: NotRequired[int]
    priceText: NotRequired[str]


class AirbnbCalendarResponseData(TypedDict):
    results: list[AirbnbCalendarResponseDataResultsItem]


class AirbnbCalendarResponse(TypedDict):
    success: Literal[True]
    data: AirbnbCalendarResponseData
    creditsUsed: int
    requestId: str


class AirbnbReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    text: NotRequired[str]
    rating: NotRequired[float]
    publishedAt: NotRequired[str]
    language: NotRequired[str]
    stayLength: NotRequired[str]
    authorId: NotRequired[str]
    authorName: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorAddress: NotRequired[str]
    ownerReplyText: NotRequired[str]


class AirbnbReviewsResponseData(TypedDict):
    results: list[AirbnbReviewsResponseDataResultsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AirbnbReviewsResponse(TypedDict):
    success: Literal[True]
    data: AirbnbReviewsResponseData
    creditsUsed: int
    requestId: str


class RightmoveSearchResponseDataResultsItem(TypedDict):
    propertyId: NotRequired[str]
    propertyUrl: str
    addressFull: NotRequired[str]
    summary: NotRequired[str]
    price: NotRequired[float]
    priceText: NotRequired[str]
    priceQualifier: NotRequired[str]
    priceFrequency: NotRequired[str]
    priceCurrency: NotRequired[str]
    bedrooms: NotRequired[int]
    bathrooms: NotRequired[int]
    propertyType: NotRequired[str]
    sizeText: NotRequired[str]
    tenureType: NotRequired[str]
    firstListedAt: NotRequired[str]
    updateReason: NotRequired[str]
    updatedAt: NotRequired[str]
    isFeatured: bool
    isAuction: bool
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    agentName: NotRequired[str]
    agentBranchId: NotRequired[str]
    agentPhone: NotRequired[str]
    keyFeatures: NotRequired[list[str]]
    imageUrls: NotRequired[list[str]]


class RightmoveSearchResponseData(TypedDict):
    results: list[RightmoveSearchResponseDataResultsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class RightmoveSearchResponse(TypedDict):
    success: Literal[True]
    data: RightmoveSearchResponseData
    creditsUsed: int
    requestId: str


class RightmovePropertyResponseDataSizesItem(TypedDict):
    value: float
    unit: NotRequired[str]


class RightmovePropertyResponseDataNearestStationsItem(TypedDict):
    name: NotRequired[str]
    types: NotRequired[list[str]]
    distanceMiles: NotRequired[float]


class RightmovePropertyResponseData(TypedDict):
    propertyId: NotRequired[str]
    propertyUrl: str
    addressFull: NotRequired[str]
    addressPostalCode: NotRequired[str]
    addressCountry: NotRequired[str]
    description: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    priceText: NotRequired[str]
    priceQualifier: NotRequired[str]
    pricePerSqft: NotRequired[float]
    channel: NotRequired[str]
    bedrooms: NotRequired[int]
    bathrooms: NotRequired[int]
    propertyType: NotRequired[str]
    tenureType: NotRequired[str]
    tenureYearsRemaining: NotRequired[float]
    sizes: list[RightmovePropertyResponseDataSizesItem]
    councilTaxBand: NotRequired[str]
    annualServiceCharge: NotRequired[float]
    annualGroundRent: NotRequired[float]
    updateReason: NotRequired[str]
    tags: list[str]
    keyFeatures: list[str]
    imageUrls: list[str]
    floorplanUrls: list[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    nearestStations: list[RightmovePropertyResponseDataNearestStationsItem]
    agentName: NotRequired[str]
    agentBranchId: NotRequired[str]
    agentPhone: NotRequired[str]
    agentCompany: NotRequired[str]
    agentAddress: NotRequired[str]


class RightmovePropertyResponse(TypedDict):
    success: Literal[True]
    data: RightmovePropertyResponseData
    creditsUsed: int
    requestId: str


class ImmoscoutSearchResponseDataResultsItem(TypedDict):
    listingId: NotRequired[str]
    listingUrl: str
    title: NotRequired[str]
    type: NotRequired[str]
    addressFull: NotRequired[str]
    addressPostalCode: NotRequired[str]
    addressCountry: NotRequired[str]
    price: NotRequired[float]
    priceCurrency: NotRequired[str]
    priceText: NotRequired[str]
    livingSpace: NotRequired[float]
    rooms: NotRequired[float]
    energyClass: NotRequired[str]
    publishedAt: NotRequired[str]
    isPrivate: bool
    isProject: bool
    isNew: bool
    imageUrl: NotRequired[str]


class ImmoscoutSearchResponseData(TypedDict):
    results: list[ImmoscoutSearchResponseDataResultsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class ImmoscoutSearchResponse(TypedDict):
    success: Literal[True]
    data: ImmoscoutSearchResponseData
    creditsUsed: int
    requestId: str


class ImmoscoutListingResponseDataAttributesItem(TypedDict):
    group: NotRequired[str]
    label: NotRequired[str]
    value: NotRequired[str]


class ImmoscoutListingResponseDataTextsItem(TypedDict):
    title: NotRequired[str]
    text: NotRequired[str]


class ImmoscoutListingResponseData(TypedDict):
    listingId: NotRequired[str]
    listingUrl: str
    title: NotRequired[str]
    type: NotRequired[str]
    status: NotRequired[str]
    addressFull: NotRequired[str]
    addressPostalCode: NotRequired[str]
    addressCity: NotRequired[str]
    addressDistrict: NotRequired[str]
    addressCountry: NotRequired[str]
    priceCurrency: NotRequired[str]
    baseRent: NotRequired[float]
    totalRent: NotRequired[float]
    serviceCharge: NotRequired[float]
    price: NotRequired[float]
    livingSpace: NotRequired[float]
    rooms: NotRequired[float]
    yearBuilt: NotRequired[int]
    energyClass: NotRequired[str]
    attributes: list[ImmoscoutListingResponseDataAttributesItem]
    texts: list[ImmoscoutListingResponseDataTextsItem]
    imageUrls: list[str]
    agentName: NotRequired[str]
    agentCompany: NotRequired[str]
    agentPhone: NotRequired[str]
    agentRating: NotRequired[float]
    agentUrl: NotRequired[str]
    agentAddress: NotRequired[str]


class ImmoscoutListingResponse(TypedDict):
    success: Literal[True]
    data: ImmoscoutListingResponseData
    creditsUsed: int
    requestId: str


class PinterestSearchResponseDataResultsItem(TypedDict):
    pinId: NotRequired[str]
    pinUrl: str
    title: NotRequired[str]
    text: NotRequired[str]
    altText: NotRequired[str]
    linkUrl: NotRequired[str]
    domain: NotRequired[str]
    publishedAt: NotRequired[str]
    imageUrl: NotRequired[str]
    videoUrl: NotRequired[str]
    videoDurationSeconds: NotRequired[float]
    saves: NotRequired[int]
    reposts: NotRequired[int]
    comments: NotRequired[int]
    reactions: NotRequired[int]
    isPromoted: bool
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    boardId: NotRequired[str]
    boardName: NotRequired[str]
    boardUrl: NotRequired[str]


class PinterestSearchResponseData(TypedDict):
    results: list[PinterestSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class PinterestSearchResponse(TypedDict):
    success: Literal[True]
    data: PinterestSearchResponseData
    creditsUsed: int
    requestId: str


class PinterestPinResponse(TypedDict):
    success: Literal[True]
    data: PinterestSearchResponseDataResultsItem
    creditsUsed: int
    requestId: str


class PinterestBoardResponseData(TypedDict):
    boardId: NotRequired[str]
    boardUrl: str
    name: NotRequired[str]
    description: NotRequired[str]
    category: NotRequired[str]
    pins: NotRequired[int]
    followers: NotRequired[int]
    sections: NotRequired[int]
    thumbnailUrl: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    results: list[PinterestSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class PinterestBoardResponse(TypedDict):
    success: Literal[True]
    data: PinterestBoardResponseData
    creditsUsed: int
    requestId: str


class PinterestUserResponseData(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    userUrl: str
    name: NotRequired[str]
    avatarUrl: NotRequired[str]
    followers: NotRequired[int]
    bio: NotRequired[str]
    website: NotRequired[str]
    following: NotRequired[int]
    pins: NotRequired[int]
    boards: NotRequired[int]
    isVerified: bool
    isPrivate: bool
    createdAt: NotRequired[str]
    results: list[PinterestSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class PinterestUserResponse(TypedDict):
    success: Literal[True]
    data: PinterestUserResponseData
    creditsUsed: int
    requestId: str


class XPostResponseDataMediaItem(TypedDict):
    type: XPostResponseDataMediaItemType
    url: str
    thumbnailUrl: NotRequired[str]
    durationSeconds: NotRequired[float]


class XPostResponseData(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    language: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: NotRequired[bool]
    media: list[XPostResponseDataMediaItem]
    links: list[str]
    hashtags: list[str]
    mentions: list[str]
    replyToUrl: NotRequired[str]
    parentText: NotRequired[str]
    quotedUrl: NotRequired[str]
    quotedText: NotRequired[str]
    isEdited: bool
    isSensitive: bool


class XPostResponse(TypedDict):
    success: Literal[True]
    data: XPostResponseData
    creditsUsed: int
    requestId: str


class FinanceQuoteResponseDataResultsItem(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    exchange: NotRequired[str]
    currency: NotRequired[str]
    marketState: NotRequired[str]
    price: NotRequired[float]
    change: NotRequired[float]
    changePercent: NotRequired[float]
    open: NotRequired[float]
    high: NotRequired[float]
    low: NotRequired[float]
    previousClose: NotRequired[float]
    volume: NotRequired[float]
    averageVolume: NotRequired[float]
    marketCap: NotRequired[float]
    fiftyTwoWeekHigh: NotRequired[float]
    fiftyTwoWeekLow: NotRequired[float]
    peRatio: NotRequired[float]
    forwardPeRatio: NotRequired[float]
    earningsPerShare: NotRequired[float]
    dividendYield: NotRequired[float]
    preMarketPrice: NotRequired[float]
    postMarketPrice: NotRequired[float]
    updatedAt: NotRequired[str]


class FinanceQuoteResponseData(TypedDict):
    results: list[FinanceQuoteResponseDataResultsItem]


class FinanceQuoteResponse(TypedDict):
    success: Literal[True]
    data: FinanceQuoteResponseData
    creditsUsed: int
    requestId: str


class FinanceHistoryResponseDataResultsItem(TypedDict):
    openedAt: str
    open: NotRequired[float]
    high: NotRequired[float]
    low: NotRequired[float]
    close: NotRequired[float]
    adjustedClose: NotRequired[float]
    volume: NotRequired[float]


class FinanceHistoryResponseDataDividendsItem(TypedDict):
    date: str
    amount: float


class FinanceHistoryResponseDataSplitsItem(TypedDict):
    date: str
    ratio: NotRequired[str]


class FinanceHistoryResponseData(TypedDict):
    currency: NotRequired[str]
    timezone: NotRequired[str]
    results: list[FinanceHistoryResponseDataResultsItem]
    dividends: list[FinanceHistoryResponseDataDividendsItem]
    splits: list[FinanceHistoryResponseDataSplitsItem]


class FinanceHistoryResponse(TypedDict):
    success: Literal[True]
    data: FinanceHistoryResponseData
    creditsUsed: int
    requestId: str


class FinanceSearchResponseDataResultsItem(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    exchange: NotRequired[str]
    sector: NotRequired[str]
    industry: NotRequired[str]


class FinanceSearchResponseDataNewsItem(TypedDict):
    title: NotRequired[str]
    url: str
    publisherName: NotRequired[str]
    publishedAt: NotRequired[str]
    tickers: NotRequired[list[str]]


class FinanceSearchResponseData(TypedDict):
    results: list[FinanceSearchResponseDataResultsItem]
    news: list[FinanceSearchResponseDataNewsItem]


class FinanceSearchResponse(TypedDict):
    success: Literal[True]
    data: FinanceSearchResponseData
    creditsUsed: int
    requestId: str


class AdsSearchResponseDataOption0(TypedDict):
    results: NotRequired[list[MetaAdsPageResponseDataResultsItem]]
    cursor: NotRequired[str]


class AdsSearchResponseDataOption1ResultsItem(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserUrl: str
    domain: NotRequired[str]
    format: AdsSearchResponseDataOption1ResultsItemFormat
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    daysShown: NotRequired[int]
    previewUrl: NotRequired[str]
    imageUrl: NotRequired[str]


class AdsSearchResponseDataOption1(TypedDict):
    results: NotRequired[list[AdsSearchResponseDataOption1ResultsItem]]
    totalMin: NotRequired[int]
    totalMax: NotRequired[int]
    cursor: NotRequired[str]


class AdsSearchResponseDataOption2ResultsItem(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    advertiserName: NotRequired[str]
    headline: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    reachMin: NotRequired[int]
    reachMax: NotRequired[int]
    videoUrl: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    imageUrls: NotRequired[list[str]]


class AdsSearchResponseDataOption2(TypedDict):
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    results: NotRequired[list[AdsSearchResponseDataOption2ResultsItem]]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AdsSearchResponseDataOption3ResultsItem(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    creativeType: NotRequired[str]
    format: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserUrl: NotRequired[str]
    advertiserAvatarUrl: NotRequired[str]
    postedBy: NotRequired[str]
    text: NotRequired[str]
    headline: NotRequired[str]
    imageUrls: NotRequired[list[str]]


class AdsSearchResponseDataOption3(TypedDict):
    results: NotRequired[list[AdsSearchResponseDataOption3ResultsItem]]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AdsSearchResponseDataOption4ResultsItem(TypedDict):
    adId: NotRequired[str]
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    headline: NotRequired[str]
    text: NotRequired[str]
    linkUrl: NotRequired[str]
    linkCaption: NotRequired[str]
    imageUrls: NotRequired[list[str]]


class AdsSearchResponseDataOption4(TypedDict):
    results: NotRequired[list[AdsSearchResponseDataOption4ResultsItem]]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AdsSearchResponseDataOption5ResultsItemReachByCountryItem(TypedDict):
    country: NotRequired[str]
    reachMin: NotRequired[int]
    reachMax: NotRequired[int]


class AdsSearchResponseDataOption5ResultsItem(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    headline: NotRequired[str]
    text: NotRequired[str]
    advertisers: NotRequired[list[str]]
    imageUrl: NotRequired[str]
    videoUrl: NotRequired[str]
    links: NotRequired[list[str]]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    reachMin: NotRequired[int]
    reachMax: NotRequired[int]
    reachByCountry: NotRequired[list[AdsSearchResponseDataOption5ResultsItemReachByCountryItem]]
    countries: NotRequired[list[str]]
    ageRanges: NotRequired[list[str]]
    genders: NotRequired[list[str]]
    interests: NotRequired[list[str]]
    audienceTypes: NotRequired[list[str]]
    isCommercial: bool


class AdsSearchResponseDataOption5(TypedDict):
    results: NotRequired[list[AdsSearchResponseDataOption5ResultsItem]]
    cursor: NotRequired[str]


class AdsSearchResponse(TypedDict):
    success: Literal[True]
    data: (
        AdsSearchResponseDataOption0
        | AdsSearchResponseDataOption1
        | AdsSearchResponseDataOption2
        | AdsSearchResponseDataOption3
        | AdsSearchResponseDataOption4
        | AdsSearchResponseDataOption5
    )
    creditsUsed: int
    requestId: str


class AdsAdResponseDataOption0AudienceAgeGenderItem(TypedDict):
    age: NotRequired[str]
    female: float
    male: float
    unknown: float


class AdsAdResponseDataOption0AudienceRegionsItem(TypedDict):
    region: NotRequired[str]
    share: float


class AdsAdResponseDataOption0EuReachByCountryItem(TypedDict):
    country: NotRequired[str]
    age: NotRequired[str]
    female: int
    male: int
    unknown: int


class AdsAdResponseDataOption0PayersItem(TypedDict):
    paidBy: NotRequired[str]
    beneficiary: NotRequired[str]


class AdsAdResponseDataOption0(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    pageId: NotRequired[str]
    pageName: NotRequired[str]
    pageUrl: NotRequired[str]
    pageAvatarUrl: NotRequired[str]
    pageCategories: NotRequired[list[str]]
    pageLikes: NotRequired[int]
    isActive: bool
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    platforms: NotRequired[list[str]]
    format: NotRequired[str]
    text: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    linkDescription: NotRequired[str]
    ctaText: NotRequired[str]
    imageUrls: NotRequired[list[str]]
    videoUrls: NotRequired[list[str]]
    cards: NotRequired[list[MetaAdsPageResponseDataResultsItemCardsItem]]
    versions: int
    categories: NotRequired[list[str]]
    paidBy: NotRequired[str]
    spendMin: NotRequired[int]
    spendMax: NotRequired[int]
    spendCurrency: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    reachMin: NotRequired[int]
    reachMax: NotRequired[int]
    countries: NotRequired[list[str]]
    advertiserDescription: NotRequired[str]
    advertiserCategory: NotRequired[str]
    advertiserVerification: NotRequired[str]
    advertiserInstagram: NotRequired[str]
    advertiserInstagramFollowers: NotRequired[int]
    audienceAgeGender: NotRequired[list[AdsAdResponseDataOption0AudienceAgeGenderItem]]
    audienceRegions: NotRequired[list[AdsAdResponseDataOption0AudienceRegionsItem]]
    euReachTotal: NotRequired[int]
    euReachByCountry: NotRequired[list[AdsAdResponseDataOption0EuReachByCountryItem]]
    payers: NotRequired[list[AdsAdResponseDataOption0PayersItem]]


class AdsAdResponseDataOption1VariationsItem(TypedDict):
    previewUrl: NotRequired[str]
    imageUrl: NotRequired[str]
    videoUrl: NotRequired[str]


class AdsAdResponseDataOption1RegionsItem(TypedDict):
    country: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]


class AdsAdResponseDataOption1(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserUrl: str
    domain: NotRequired[str]
    format: AdsSearchResponseDataOption1ResultsItemFormat
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    daysShown: NotRequired[int]
    previewUrl: NotRequired[str]
    imageUrl: NotRequired[str]
    advertiserCountry: NotRequired[str]
    advertiserIsVerified: NotRequired[bool]
    paidBy: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    variations: NotRequired[list[AdsAdResponseDataOption1VariationsItem]]
    regions: NotRequired[list[AdsAdResponseDataOption1RegionsItem]]
    targetingIncluded: NotRequired[list[str]]
    targetingExcluded: NotRequired[list[str]]


class AdsAdResponseDataOption2RegionsItem(TypedDict):
    country: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    ages: NotRequired[list[str]]
    genders: NotRequired[list[str]]


class AdsAdResponseDataOption2(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    advertiserName: NotRequired[str]
    headline: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    reachMin: NotRequired[int]
    reachMax: NotRequired[int]
    videoUrl: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    imageUrls: NotRequired[list[str]]
    advertiserId: NotRequired[str]
    advertiserCountry: NotRequired[str]
    paidBy: NotRequired[str]
    linkUrl: NotRequired[str]
    ctaText: NotRequired[str]
    objective: NotRequired[str]
    category: NotRequired[str]
    audienceSizeMin: NotRequired[int]
    audienceSizeMax: NotRequired[int]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    countries: NotRequired[list[str]]
    languages: NotRequired[list[str]]
    interests: NotRequired[str]
    regions: NotRequired[list[AdsAdResponseDataOption2RegionsItem]]


class AdsAdResponseDataOption3CountriesItem(TypedDict):
    country: NotRequired[str]
    share: NotRequired[float]


class AdsAdResponseDataOption3TargetingItem(TypedDict):
    parameter: NotRequired[str]
    description: NotRequired[str]


class AdsAdResponseDataOption3TargetingUsedItem(TypedDict):
    parameter: NotRequired[str]
    isTargeted: bool
    isExcluded: bool


class AdsAdResponseDataOption3(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    creativeType: NotRequired[str]
    format: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserUrl: NotRequired[str]
    advertiserAvatarUrl: NotRequired[str]
    postedBy: NotRequired[str]
    text: NotRequired[str]
    headline: NotRequired[str]
    imageUrls: NotRequired[list[str]]
    paidBy: NotRequired[str]
    ctaText: NotRequired[str]
    videoUrls: NotRequired[list[str]]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    countries: NotRequired[list[AdsAdResponseDataOption3CountriesItem]]
    targeting: NotRequired[list[AdsAdResponseDataOption3TargetingItem]]
    targetingUsed: NotRequired[list[AdsAdResponseDataOption3TargetingUsedItem]]


class AdsAdResponseDataOption4TargetingItem(TypedDict):
    type: NotRequired[str]
    isExcluded: bool


class AdsAdResponseDataOption4(TypedDict):
    adId: NotRequired[str]
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    headline: NotRequired[str]
    text: NotRequired[str]
    linkUrl: NotRequired[str]
    linkCaption: NotRequired[str]
    imageUrls: NotRequired[list[str]]
    paidBy: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    countries: NotRequired[list[AdsAdResponseDataOption3CountriesItem]]
    targeting: NotRequired[list[AdsAdResponseDataOption4TargetingItem]]


class AdsAdResponse(TypedDict):
    success: Literal[True]
    data: (
        AdsAdResponseDataOption0
        | AdsAdResponseDataOption1
        | AdsAdResponseDataOption2
        | AdsAdResponseDataOption3
        | AdsAdResponseDataOption4
        | AdsSearchResponseDataOption5ResultsItem
    )
    creditsUsed: int
    requestId: str


class AdsAdvertisersResponseDataOption0ResultsItem(TypedDict):
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserCountry: NotRequired[str]
    advertiserUrl: str
    isVerified: bool
    adsMin: NotRequired[int]
    adsMax: NotRequired[int]


class AdsAdvertisersResponseDataOption0(TypedDict):
    results: NotRequired[list[AdsAdvertisersResponseDataOption0ResultsItem]]
    domains: NotRequired[list[str]]


class AdsAdvertisersResponseDataOption1ResultsItem(TypedDict):
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserCountry: NotRequired[str]
    isVerified: bool


class AdsAdvertisersResponseDataOption1(TypedDict):
    results: NotRequired[list[AdsAdvertisersResponseDataOption1ResultsItem]]
    total: NotRequired[int]


class AdsAdvertisersResponse(TypedDict):
    success: Literal[True]
    data: AdsAdvertisersResponseDataOption0 | AdsAdvertisersResponseDataOption1
    creditsUsed: int
    requestId: str


class SuggestResponseDataOption0ResultsItem(TypedDict):
    keyword: str
    rank: int


class SuggestResponseDataOption0(TypedDict):
    results: NotRequired[list[SuggestResponseDataOption0ResultsItem]]


class SuggestResponse(TypedDict):
    success: Literal[True]
    data: SuggestResponseDataOption0
    creditsUsed: int
    requestId: str


class GoogleTrendsResponseDataOption0ResultsItem(TypedDict):
    recordedAt: str
    values: NotRequired[list[float]]
    isPartial: bool


class GoogleTrendsResponseDataOption0(TypedDict):
    results: NotRequired[list[GoogleTrendsResponseDataOption0ResultsItem]]
    averages: NotRequired[list[float]]


class GoogleTrendsResponseDataOption1ResultsItem(TypedDict):
    code: NotRequired[str]
    name: NotRequired[str]
    values: NotRequired[list[float]]


class GoogleTrendsResponseDataOption1(TypedDict):
    results: NotRequired[list[GoogleTrendsResponseDataOption1ResultsItem]]


class GoogleTrendsResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsResponseDataOption0 | GoogleTrendsResponseDataOption1
    creditsUsed: int
    requestId: str


class FinanceStockResponse(TypedDict):
    success: Literal[True]
    data: Any
    creditsUsed: int
    requestId: str
