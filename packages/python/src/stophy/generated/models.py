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

YoutubeSearchDuration = Literal[
    "all",
    "short",
    "medium",
    "long",
]

YoutubeSearchSort = Literal[
    "relevance",
    "top",
]

YoutubeSearchFeaturesItem = Literal[
    "360",
    "live",
    "4k",
    "hd",
    "subtitles",
    "creativeCommons",
    "vr180",
    "3d",
    "hdr",
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
    "search",
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
    "controversial",
    "oldest",
    "qa",
]

RedditSubredditSort = Literal[
    "hot",
    "newest",
    "top",
    "rising",
    "controversial",
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
    "controversial",
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

InstagramPostsType = Literal[
    "all",
    "reels",
    "videos",
    "photos",
]

InstagramSearchType = Literal[
    "all",
    "posts",
    "reels",
]

TiktokVideoResponseDataVideoType = Literal[
    "video",
    "photo",
]

TiktokSearchType = Literal[
    "videos",
    "users",
]

BlueskyPostsType = Literal[
    "all",
    "posts",
    "media",
    "video",
    "threads",
]

ThreadsPostsResponseDataPostsItemType = Literal[
    "text",
    "photo",
    "video",
    "carousel",
]

TelegramChannelResponseDataChannelType = Literal[
    "channel",
    "group",
]

TelegramPostsResponseDataPostsItemMediaItemType = Literal[
    "photo",
    "video",
    "roundVideo",
    "sticker",
    "voice",
    "audio",
    "document",
    "poll",
]

MetaAdsSearchAdType = Literal[
    "all",
    "politicalAndIssue",
]

MetaAdsSearchStatus = Literal[
    "active",
    "inactive",
    "all",
]

MetaAdsSearchMediaType = Literal[
    "all",
    "image",
    "video",
    "meme",
    "none",
]

MetaAdsSearchPlatformsItem = Literal[
    "facebook",
    "instagram",
    "messenger",
    "audienceNetwork",
]

LinkedinJobsSearchWithin = Literal[
    "day",
    "week",
    "month",
    "all",
]

LinkedinJobsSearchJobTypesItem = Literal[
    "fullTime",
    "partTime",
    "contract",
    "temporary",
    "internship",
]

LinkedinJobsSearchExperienceItem = Literal[
    "internship",
    "entry",
    "associate",
    "midSenior",
    "director",
    "executive",
]

LinkedinJobsSearchWorkplaceItem = Literal[
    "onsite",
    "remote",
    "hybrid",
]

LinkedinJobsSearchSort = Literal[
    "relevance",
    "newest",
]

LinkedinAdsSearchWithin = Literal[
    "month",
    "year",
    "all",
]

ZillowSearchStatus = Literal[
    "forSale",
    "forRent",
    "sold",
]

ZillowSearchSort = Literal[
    "relevance",
    "newest",
    "priceHigh",
    "priceLow",
    "bedrooms",
    "bathrooms",
    "sqft",
    "lot",
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

ZillowSearchListingTypesItem = Literal[
    "agent",
    "owner",
    "newConstruction",
    "comingSoon",
    "auction",
    "foreclosure",
]

ZillowSearchWithin = Literal[
    "day",
    "week",
    "twoWeeks",
    "month",
    "threeMonths",
    "sixMonths",
    "year",
    "twoYears",
    "threeYears",
    "all",
]

ZillowSearchFeaturesItem = Literal[
    "garage",
    "pool",
    "airConditioning",
    "waterfront",
    "singleStory",
    "openHouse",
    "tour3d",
    "cityView",
    "parkView",
    "waterView",
    "mountainView",
    "catsAllowed",
    "furnished",
]

ZillowSearchResponseDataListingsItemStatus = Literal[
    "forSale",
    "forRent",
    "sold",
    "other",
]

GoogleAdsSearchMediaType = Literal[
    "text",
    "image",
    "video",
]

GoogleAdsSearchPlatform = Literal[
    "play",
    "maps",
    "search",
    "shopping",
    "youtube",
]

GoogleAdsSearchResponseDataAdsItemFormat = Literal[
    "text",
    "image",
    "video",
    "unknown",
]

GoogleAdsAdResponseDataAdRegionsItemPlatformsItemPlatform = Literal[
    "play",
    "maps",
    "search",
    "shopping",
    "youtube",
    "unknown",
]

UpworkSearchSort = Literal[
    "newest",
    "relevance",
]

UpworkSearchJobType = Literal[
    "hourly",
    "fixed",
]

UpworkSearchExperienceItem = Literal[
    "entry",
    "intermediate",
    "expert",
]

UpworkSearchDurationItem = Literal[
    "week",
    "month",
    "semester",
    "ongoing",
]

UpworkSearchWorkloadItem = Literal[
    "asNeeded",
    "partTime",
    "fullTime",
]

UpworkSearchClientHiresItem = Literal[
    "none",
    "oneToNine",
    "tenPlus",
]

GoogleSuggestExpand = Literal[
    "none",
    "alphabet",
    "questions",
    "all",
]

GoogleSuggestVertical = Literal[
    "web",
    "shopping",
]

AmazonSuggestCountry = Literal[
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

GoogleTrendsInterestVertical = Literal[
    "web",
    "images",
    "news",
    "youtube",
    "shopping",
]

GoogleTrendsRegionsResolution = Literal[
    "country",
    "region",
    "metro",
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

SiteMapResponseDataSource = Literal[
    "sitemap",
    "crawl",
]

DomainDnsTypesItem = Literal[
    "A",
    "AAAA",
    "CNAME",
    "MX",
    "NS",
    "TXT",
    "SOA",
    "CAA",
]

DomainTechResponseDataTechnologiesItemEvidence = Literal[
    "html",
    "script",
    "cookie",
    "generator",
    "dns",
]

EmailCheckResponseDataEmailsItemStatus = Literal[
    "ok",
    "risky",
    "invalid",
]

CryptoCoinsSort = Literal[
    "marketCap",
    "volume",
    "id",
]

CryptoCoinsOrder = Literal[
    "asc",
    "desc",
]

CryptoCoinsResponseDataCoinsItemSource = Literal[
    "coingecko",
    "coinmarketcap",
]

CryptoHistoryWithin = Literal[
    "day",
    "week",
    "twoWeeks",
    "month",
    "threeMonths",
    "sixMonths",
    "year",
]

CryptoCategoriesSort = Literal[
    "marketCap",
    "change",
    "name",
]

CryptoMoversWithin = Literal[
    "hour",
    "day",
    "week",
    "month",
]

CryptoMoversRankUpTo = Literal[
    100,
    200,
    500,
]

CryptoDexNewType = Literal[
    "profiles",
    "boosts",
    "topBoosts",
    "takeovers",
]

CryptoPumpCoinsSort = Literal[
    "newest",
    "lastTrade",
    "marketCap",
    "lastReply",
    "live",
]

CryptoPumpTradesResponseDataTradesItemType = Literal[
    "buy",
    "sell",
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

CryptoTokenHoldersChain = Literal[
    "ethereum",
    "base",
    "arbitrum",
    "optimism",
    "polygon",
    "gnosis",
]

CryptoBinanceAnnouncementsCategory = Literal[
    "listings",
    "delistings",
    "news",
    "activities",
    "airdrops",
    "maintenance",
    "api",
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

IndeedSearchJobType = Literal[
    "fullTime",
    "partTime",
    "contract",
    "internship",
]

IndeedSearchWithin = Literal[
    "day",
    "threeDays",
    "week",
    "twoWeeks",
    "month",
    "all",
]

IndeedSearchResponseDataJobsItemSalaryPeriod = Literal[
    "hour",
    "day",
    "week",
    "month",
    "year",
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

GoogleplayReviewsSort = Literal[
    "newest",
    "relevance",
    "highest",
]

AirbnbSearchRoomType = Literal[
    "entireHome",
    "privateRoom",
    "sharedRoom",
    "hotelRoom",
]

AirbnbSearchAmenitiesItem = Literal[
    "wifi",
    "kitchen",
    "washer",
    "dryer",
    "airConditioning",
    "heating",
    "workspace",
    "tv",
    "hairDryer",
    "iron",
    "pool",
    "hotTub",
    "freeParking",
    "evCharger",
    "crib",
    "gym",
    "bbqGrill",
    "breakfast",
    "fireplace",
    "smokingAllowed",
    "smokeAlarm",
    "carbonMonoxideAlarm",
    "selfCheckIn",
]

RedfinSearchStatus = Literal[
    "forSale",
    "sold",
]

RedfinSearchSoldWithin = Literal[
    "week",
    "month",
    "threeMonths",
    "sixMonths",
    "year",
    "twoYears",
    "threeYears",
    "fiveYears",
]

RedfinSearchSort = Literal[
    "relevance",
    "newest",
    "priceLow",
    "priceHigh",
    "sqft",
    "pricePerSqft",
]

RedfinSearchHomeTypesItem = Literal[
    "house",
    "condo",
    "townhouse",
    "multiFamily",
    "land",
    "other",
    "manufactured",
    "coop",
]

RealtorSearchStatus = Literal[
    "forSale",
    "forRent",
    "sold",
    "pending",
]

RealtorSearchSort = Literal[
    "relevance",
    "newest",
    "priceLow",
    "priceHigh",
    "sqft",
    "recentlySold",
]

RealtorSearchHomeTypesItem = Literal[
    "house",
    "condo",
    "townhouse",
    "multiFamily",
    "duplex",
    "apartment",
    "mobile",
    "land",
    "farm",
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

RightmoveSearchPropertyTypesItem = Literal[
    "detached",
    "semiDetached",
    "terraced",
    "flat",
    "bungalow",
    "land",
    "parkHome",
]

RightmoveSearchMustHaveItem = Literal[
    "garden",
    "parking",
    "newHome",
    "retirement",
    "sharedOwnership",
    "auction",
]

RightmoveSearchWithin = Literal[
    "day",
    "threeDays",
    "week",
    "twoWeeks",
    "all",
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

ImmoscoutSearchEquipmentItem = Literal[
    "balcony",
    "builtInKitchen",
    "garden",
    "cellar",
    "parking",
    "lift",
    "stepFree",
    "guestToilet",
]

PinterestSearchType = Literal[
    "pins",
    "videos",
]

XTweetResponseDataTweetMediaItemType = Literal[
    "photo",
    "video",
    "gif",
]

FinanceHistoryWithin = Literal[
    "day",
    "fiveDays",
    "month",
    "threeMonths",
    "sixMonths",
    "year",
    "twoYears",
    "fiveYears",
    "tenYears",
    "yearToDate",
    "all",
]

FinanceHistoryInterval = Literal[
    "minute",
    "twoMinutes",
    "fiveMinutes",
    "fifteenMinutes",
    "thirtyMinutes",
    "hour",
    "ninetyMinutes",
    "day",
    "fiveDays",
    "week",
    "month",
    "threeMonths",
]

SnapchatProfileResponseDataStoriesItemType = Literal[
    "image",
    "video",
]

SnapchatAdsSearchStatus = Literal[
    "active",
    "paused",
]

TumblrPostsType = Literal[
    "text",
    "photo",
    "quote",
    "link",
    "chat",
    "audio",
    "video",
    "answer",
]

LinkedinProfileResponseDataProfileRolesItem = TypedDict(
    "LinkedinProfileResponseDataProfileRolesItem",
    {
        "title": NotRequired[str],
        "company": NotRequired[str],
        "url": NotRequired[str],
        "from": NotRequired[str],
        "to": NotRequired[str],
        "isCurrent": bool,
    },
)

LinkedinProfileResponseDataProfileEducationItem = TypedDict(
    "LinkedinProfileResponseDataProfileEducationItem",
    {
        "school": NotRequired[str],
        "degree": NotRequired[str],
        "url": NotRequired[str],
        "from": NotRequired[str],
        "to": NotRequired[str],
    },
)

CryptoWalletResponseDataTransactionsItem = TypedDict(
    "CryptoWalletResponseDataTransactionsItem",
    {
        "id": NotRequired[str],
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
    summary: str


class EndpointCatalogEndpointsItem(TypedDict):
    id: str
    summary: str
    method: Literal["POST"]
    path: str
    credits: int
    keyless: bool
    perItems: int | None
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


class WebNewsResponseDataArticlesItemPublisher(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]


class WebNewsResponseDataArticlesItem(TypedDict):
    title: str
    url: str
    publisher: NotRequired[WebNewsResponseDataArticlesItemPublisher]
    createdAt: NotRequired[str]
    domain: NotRequired[str]
    position: int


class WebNewsResponseData(TypedDict):
    articles: list[WebNewsResponseDataArticlesItem]


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
    url: str
    pages: list[str]


class WebContactsResponse(TypedDict):
    success: Literal[True]
    data: WebContactsResponseData
    creditsUsed: int
    requestId: str


class YoutubeSearchResponseDataResultsItemOption0Channel(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: NotRequired[bool]


class YoutubeSearchResponseDataResultsItemOption0(TypedDict):
    type: Literal["video"]
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    channel: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    durationSeconds: NotRequired[int]
    views: NotRequired[int]
    thumbnail: NotRequired[str]
    isShort: bool
    isLive: bool
    createdAt: NotRequired[str]


class YoutubeSearchResponseDataResultsItemOption1(TypedDict):
    type: Literal["channel"]
    id: NotRequired[str]
    url: str
    name: NotRequired[str]
    username: NotRequired[str]
    description: NotRequired[str]
    subscribers: NotRequired[int]
    thumbnail: NotRequired[str]


class YoutubeSearchResponseDataResultsItemOption2(TypedDict):
    type: Literal["playlist"]
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    channel: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    videos: NotRequired[int]
    thumbnail: NotRequired[str]


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
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    channel: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    durationSeconds: NotRequired[int]
    views: NotRequired[int]
    thumbnail: NotRequired[str]
    isShort: bool
    isLive: bool
    createdAt: NotRequired[str]
    description: NotRequired[str]
    likes: NotRequired[int]
    category: NotRequired[str]
    tags: list[str]


class YoutubeVideoResponse(TypedDict):
    success: Literal[True]
    data: YoutubeVideoResponseData
    creditsUsed: int
    requestId: str


class YoutubeTranscriptResponseDataSegmentsItem(TypedDict):
    startSeconds: float
    endSeconds: float
    text: NotRequired[str]


class YoutubeTranscriptResponseData(TypedDict):
    id: NotRequired[str]
    url: str
    language: NotRequired[str]
    isAutoGenerated: bool
    durationSeconds: NotRequired[float]
    text: NotRequired[str]
    segments: NotRequired[list[YoutubeTranscriptResponseDataSegmentsItem]]


class YoutubeTranscriptResponse(TypedDict):
    success: Literal[True]
    data: YoutubeTranscriptResponseData
    creditsUsed: int
    requestId: str


class YoutubeCommentsResponseDataCommentsItem(TypedDict):
    id: NotRequired[str]
    url: str
    text: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    likes: int
    replies: int
    createdAt: NotRequired[str]
    isPinned: bool
    isHearted: bool
    isChannelOwner: bool
    repliesCursor: NotRequired[str]


class YoutubeCommentsResponseData(TypedDict):
    comments: list[YoutubeCommentsResponseDataCommentsItem]
    cursor: NotRequired[str]


class YoutubeCommentsResponse(TypedDict):
    success: Literal[True]
    data: YoutubeCommentsResponseData
    creditsUsed: int
    requestId: str


class YoutubeCommentsRepliesResponseData(TypedDict):
    replies: list[YoutubeCommentsResponseDataCommentsItem]
    cursor: NotRequired[str]


class YoutubeCommentsRepliesResponse(TypedDict):
    success: Literal[True]
    data: YoutubeCommentsRepliesResponseData
    creditsUsed: int
    requestId: str


class YoutubeChannelResponseDataChannelAboutLinksItem(TypedDict):
    title: NotRequired[str]
    url: str


class YoutubeChannelResponseDataChannelAbout(TypedDict):
    country: NotRequired[str]
    joinedDate: NotRequired[str]
    views: NotRequired[int]
    links: NotRequired[list[YoutubeChannelResponseDataChannelAboutLinksItem]]


class YoutubeChannelResponseDataChannel(TypedDict):
    id: NotRequired[str]
    url: str
    name: NotRequired[str]
    username: NotRequired[str]
    description: NotRequired[str]
    subscribers: NotRequired[int]
    videos: NotRequired[int]
    avatar: NotRequired[str]
    banner: NotRequired[str]
    about: NotRequired[YoutubeChannelResponseDataChannelAbout]


class YoutubeChannelResponseDataItemsItemOption2ImagesItem(TypedDict):
    url: str
    caption: NotRequired[str]
    alt: NotRequired[str]


class YoutubeChannelResponseDataItemsItemOption2Video(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str]


class YoutubeChannelResponseDataItemsItemOption2Poll(TypedDict):
    choices: NotRequired[list[str]]
    totalVotes: NotRequired[int]


class YoutubeChannelResponseDataItemsItemOption2(TypedDict):
    type: Literal["post"]
    id: NotRequired[str]
    url: str
    text: NotRequired[str]
    createdAt: NotRequired[str]
    likes: NotRequired[int]
    comments: NotRequired[int]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    video: NotRequired[YoutubeChannelResponseDataItemsItemOption2Video]
    poll: NotRequired[YoutubeChannelResponseDataItemsItemOption2Poll]


class YoutubeChannelResponseData(TypedDict):
    channel: NotRequired[YoutubeChannelResponseDataChannel]
    items: list[
        YoutubeSearchResponseDataResultsItemOption0
        | YoutubeSearchResponseDataResultsItemOption2
        | YoutubeChannelResponseDataItemsItemOption2
    ]
    cursor: NotRequired[str]


class YoutubeChannelResponse(TypedDict):
    success: Literal[True]
    data: YoutubeChannelResponseData
    creditsUsed: int
    requestId: str


class YoutubePlaylistResponseDataPlaylist(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    description: NotRequired[str]
    channel: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    videos: NotRequired[int]
    views: NotRequired[int]
    thumbnail: NotRequired[str]


class YoutubePlaylistResponseData(TypedDict):
    playlist: NotRequired[YoutubePlaylistResponseDataPlaylist]
    videos: list[YoutubeSearchResponseDataResultsItemOption0]
    cursor: NotRequired[str]


class YoutubePlaylistResponse(TypedDict):
    success: Literal[True]
    data: YoutubePlaylistResponseData
    creditsUsed: int
    requestId: str


class RedditSearchResponseDataResultsItemOption0Link(TypedDict):
    url: str
    title: NotRequired[str]
    description: NotRequired[str]
    image: NotRequired[str]


class RedditSearchResponseDataResultsItemOption0Video(TypedDict):
    url: str
    hls: NotRequired[str]
    durationSeconds: NotRequired[float]


class RedditSearchResponseDataResultsItemOption0PollOptionsItem(TypedDict):
    text: NotRequired[str]
    votes: NotRequired[int]


class RedditSearchResponseDataResultsItemOption0Poll(TypedDict):
    options: NotRequired[list[RedditSearchResponseDataResultsItemOption0PollOptionsItem]]
    totalVotes: NotRequired[int]
    endsAt: NotRequired[str]


class RedditSearchResponseDataResultsItemOption0RepostOf(TypedDict):
    id: NotRequired[str]
    url: NotRequired[str]
    subreddit: NotRequired[str]
    title: NotRequired[str]


class RedditSearchResponseDataResultsItemOption0(TypedDict):
    type: Literal["post"]
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    text: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    subreddit: NotRequired[str]
    score: int
    upvotePercent: NotRequired[float]
    comments: int
    createdAt: NotRequired[str]
    flair: NotRequired[str]
    link: NotRequired[RedditSearchResponseDataResultsItemOption0Link]
    thumbnail: NotRequired[str]
    isNsfw: bool
    isVideo: bool
    isPinned: bool
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    video: NotRequired[RedditSearchResponseDataResultsItemOption0Video]
    poll: NotRequired[RedditSearchResponseDataResultsItemOption0Poll]
    repostOf: NotRequired[RedditSearchResponseDataResultsItemOption0RepostOf]


class RedditSearchResponseDataResultsItemOption1RulesItem(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]


class RedditSearchResponseDataResultsItemOption1(TypedDict):
    type: Literal["subreddit"]
    id: NotRequired[str]
    name: NotRequired[str]
    url: str
    title: NotRequired[str]
    description: NotRequired[str]
    members: NotRequired[int]
    createdAt: NotRequired[str]
    avatar: NotRequired[str]
    isNsfw: bool
    rules: NotRequired[list[RedditSearchResponseDataResultsItemOption1RulesItem]]


class RedditSearchResponseDataResultsItemOption2(TypedDict):
    type: Literal["user"]
    id: NotRequired[str]
    username: NotRequired[str]
    url: str
    postKarma: NotRequired[int]
    commentKarma: NotRequired[int]
    createdAt: NotRequired[str]
    avatar: NotRequired[str]
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


class RedditPostSchema0(TypedDict):
    id: NotRequired[str]
    url: str
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    text: NotRequired[str]
    score: int
    createdAt: NotRequired[str]
    depth: int
    isSubmitter: bool
    isPinned: bool
    children: NotRequired[list[RedditPostSchema0]]
    repliesCursor: NotRequired[str]


class RedditPostResponseData(TypedDict):
    post: RedditSearchResponseDataResultsItemOption0
    comments: list[RedditPostSchema0]
    commentsCursor: NotRequired[str]


class RedditPostResponse(TypedDict):
    success: Literal[True]
    data: RedditPostResponseData
    creditsUsed: int
    requestId: str


class RedditCommentsMoreSchema0(TypedDict):
    id: NotRequired[str]
    url: str
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    text: NotRequired[str]
    score: int
    createdAt: NotRequired[str]
    depth: int
    isSubmitter: bool
    isPinned: bool
    children: NotRequired[list[RedditCommentsMoreSchema0]]
    repliesCursor: NotRequired[str]


class RedditCommentsMoreResponseData(TypedDict):
    comments: list[RedditCommentsMoreSchema0]
    cursor: NotRequired[str]


class RedditCommentsMoreResponse(TypedDict):
    success: Literal[True]
    data: RedditCommentsMoreResponseData
    creditsUsed: int
    requestId: str


class RedditSubredditResponseData(TypedDict):
    subreddit: NotRequired[RedditSearchResponseDataResultsItemOption1]
    posts: list[RedditSearchResponseDataResultsItemOption0]
    cursor: NotRequired[str]


class RedditSubredditResponse(TypedDict):
    success: Literal[True]
    data: RedditSubredditResponseData
    creditsUsed: int
    requestId: str


class RedditUserResponseDataItemsItemOption1(TypedDict):
    type: Literal["comment"]
    id: NotRequired[str]
    url: str
    text: NotRequired[str]
    score: int
    createdAt: NotRequired[str]
    subreddit: NotRequired[str]
    postId: NotRequired[str]
    postTitle: NotRequired[str]


class RedditUserResponseData(TypedDict):
    user: NotRequired[RedditSearchResponseDataResultsItemOption2]
    items: list[RedditSearchResponseDataResultsItemOption0 | RedditUserResponseDataItemsItemOption1]
    cursor: NotRequired[str]


class RedditUserResponse(TypedDict):
    success: Literal[True]
    data: RedditUserResponseData
    creditsUsed: int
    requestId: str


class RedditDomainResponseData(TypedDict):
    posts: list[RedditSearchResponseDataResultsItemOption0]
    cursor: NotRequired[str]


class RedditDomainResponse(TypedDict):
    success: Literal[True]
    data: RedditDomainResponseData
    creditsUsed: int
    requestId: str


class MapsSearchCenter(TypedDict):
    lat: float
    lng: float


class MapsSearchResponseDataPlacesItemAddress(TypedDict):
    full: NotRequired[str]
    street: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postalCode: NotRequired[str]
    country: NotRequired[str]


class MapsSearchResponseDataPlacesItemLocation(TypedDict):
    lat: float
    lng: float


class MapsSearchResponseDataPlacesItem(TypedDict):
    id: NotRequired[str]
    placeId: NotRequired[str]
    url: str
    name: NotRequired[str]
    categories: NotRequired[list[str]]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    location: MapsSearchResponseDataPlacesItemLocation
    rating: NotRequired[float]
    photos: NotRequired[int]
    phone: NotRequired[str]
    website: NotRequired[str]
    description: NotRequired[str]
    hoursToday: NotRequired[str]
    openStatus: NotRequired[str]
    timezone: NotRequired[str]
    plusCode: NotRequired[str]
    thumbnail: NotRequired[str]
    reservation: NotRequired[str]
    attributes: NotRequired[list[str]]


class MapsSearchResponseData(TypedDict):
    places: list[MapsSearchResponseDataPlacesItem]


class MapsSearchResponse(TypedDict):
    success: Literal[True]
    data: MapsSearchResponseData
    creditsUsed: int
    requestId: str


class MapsPlaceResponseData(TypedDict):
    place: MapsSearchResponseDataPlacesItem


class MapsPlaceResponse(TypedDict):
    success: Literal[True]
    data: MapsPlaceResponseData
    creditsUsed: int
    requestId: str


class MapsReviewsResponseDataReviewsItemAuthor(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: NotRequired[bool]
    reviews: NotRequired[int]
    photos: NotRequired[int]
    isLocalGuide: bool


class MapsReviewsResponseDataReviewsItemDetailsItem(TypedDict):
    label: NotRequired[str]
    value: NotRequired[str]
    rating: NotRequired[float]


class MapsReviewsResponseDataReviewsItemOwnerReply(TypedDict):
    text: NotRequired[str]
    createdAt: NotRequired[str]


class MapsReviewsResponseDataReviewsItem(TypedDict):
    id: NotRequired[str]
    url: NotRequired[str]
    rating: int
    text: NotRequired[str]
    language: NotRequired[str]
    createdAt: NotRequired[str]
    author: MapsReviewsResponseDataReviewsItemAuthor
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    details: NotRequired[list[MapsReviewsResponseDataReviewsItemDetailsItem]]
    ownerReply: NotRequired[MapsReviewsResponseDataReviewsItemOwnerReply]


class MapsReviewsResponseData(TypedDict):
    reviews: list[MapsReviewsResponseDataReviewsItem]
    cursor: NotRequired[str]


class MapsReviewsResponse(TypedDict):
    success: Literal[True]
    data: MapsReviewsResponseData
    creditsUsed: int
    requestId: str


class InstagramProfileResponseDataProfile(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    bioLinks: NotRequired[list[YoutubeChannelResponseDataChannelAboutLinksItem]]
    pronouns: NotRequired[list[str]]
    isVerified: bool
    isPrivate: bool
    followers: NotRequired[int]
    following: NotRequired[int]
    posts: NotRequired[int]
    avatar: NotRequired[str]


class InstagramProfileResponseDataStats(TypedDict):
    postsAnalyzed: int
    averageLikes: NotRequired[float]
    averageComments: NotRequired[float]
    engagementRate: NotRequired[float]
    postsPerWeek: NotRequired[float]
    lastPostAt: NotRequired[str]


class InstagramProfileResponseDataPostsItemVideosItem(TypedDict):
    url: str


class InstagramProfileResponseDataPostsItemAudio(TypedDict):
    title: NotRequired[str]
    artist: NotRequired[str]
    isOriginal: bool


class InstagramProfileResponseDataPostsItem(TypedDict):
    id: NotRequired[str]
    code: NotRequired[str]
    url: str
    type: InstagramProfileResponseDataPostsItemType
    text: NotRequired[str]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    createdAt: NotRequired[str]
    likes: NotRequired[int]
    comments: NotRequired[int]
    views: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    thumbnail: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    videos: NotRequired[list[InstagramProfileResponseDataPostsItemVideosItem]]
    imageDescription: NotRequired[str]
    isPinned: bool
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    taggedUsers: NotRequired[list[str]]
    coauthors: NotRequired[list[str]]
    audio: NotRequired[InstagramProfileResponseDataPostsItemAudio]
    isPaidPartnership: bool
    sponsors: NotRequired[list[str]]


class InstagramProfileResponseData(TypedDict):
    profile: InstagramProfileResponseDataProfile
    stats: NotRequired[InstagramProfileResponseDataStats]
    posts: list[InstagramProfileResponseDataPostsItem]


class InstagramProfileResponse(TypedDict):
    success: Literal[True]
    data: InstagramProfileResponseData
    creditsUsed: int
    requestId: str


class InstagramPostsResponseData(TypedDict):
    posts: list[InstagramProfileResponseDataPostsItem]
    cursor: NotRequired[str]


class InstagramPostsResponse(TypedDict):
    success: Literal[True]
    data: InstagramPostsResponseData
    creditsUsed: int
    requestId: str


class InstagramPostResponseDataCommentsItem(TypedDict):
    id: NotRequired[str]
    url: str
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    text: NotRequired[str]
    likes: int
    replies: int
    createdAt: NotRequired[str]


class InstagramPostResponseData(TypedDict):
    post: InstagramProfileResponseDataPostsItem
    comments: list[InstagramPostResponseDataCommentsItem]


class InstagramPostResponse(TypedDict):
    success: Literal[True]
    data: InstagramPostResponseData
    creditsUsed: int
    requestId: str


class InstagramUrlResponseDataOption0(TypedDict):
    kind: Literal["profile"]
    profile: InstagramProfileResponseDataProfile
    stats: NotRequired[InstagramProfileResponseDataStats]
    posts: NotRequired[list[InstagramProfileResponseDataPostsItem]]


class InstagramUrlResponseDataOption1(TypedDict):
    kind: Literal["post"]
    post: InstagramProfileResponseDataPostsItem
    comments: NotRequired[list[InstagramPostResponseDataCommentsItem]]


class InstagramUrlResponse(TypedDict):
    success: Literal[True]
    data: InstagramUrlResponseDataOption0 | InstagramUrlResponseDataOption1
    creditsUsed: int
    requestId: str


class InstagramSearchResponseData(TypedDict):
    posts: list[InstagramProfileResponseDataPostsItem]


class InstagramSearchResponse(TypedDict):
    success: Literal[True]
    data: InstagramSearchResponseData
    creditsUsed: int
    requestId: str


class InstagramTranscriptResponseData(TypedDict):
    id: NotRequired[str]
    url: str
    transcripts: list[YoutubeTranscriptResponseData]


class InstagramTranscriptResponse(TypedDict):
    success: Literal[True]
    data: InstagramTranscriptResponseData
    creditsUsed: int
    requestId: str


class InstagramCommentsResponseData(TypedDict):
    comments: list[InstagramPostResponseDataCommentsItem]
    cursor: NotRequired[str]


class InstagramCommentsResponse(TypedDict):
    success: Literal[True]
    data: InstagramCommentsResponseData
    creditsUsed: int
    requestId: str


class InstagramCommentsRepliesResponseData(TypedDict):
    replies: list[InstagramPostResponseDataCommentsItem]
    cursor: NotRequired[str]


class InstagramCommentsRepliesResponse(TypedDict):
    success: Literal[True]
    data: InstagramCommentsRepliesResponseData
    creditsUsed: int
    requestId: str


class TiktokProfileResponseDataProfile(TypedDict):
    id: NotRequired[str]
    secUid: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    bioLinks: NotRequired[list[InstagramProfileResponseDataPostsItemVideosItem]]
    avatar: NotRequired[str]
    isVerified: bool
    isPrivate: bool
    isOrganization: bool
    language: NotRequired[str]
    createdAt: NotRequired[str]
    followers: NotRequired[int]
    following: NotRequired[int]
    likes: NotRequired[int]
    videos: NotRequired[int]


class TiktokProfileResponseData(TypedDict):
    profile: TiktokProfileResponseDataProfile


class TiktokProfileResponse(TypedDict):
    success: Literal[True]
    data: TiktokProfileResponseData
    creditsUsed: int
    requestId: str


class TiktokVideoResponseDataVideoAudio(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str]
    artist: NotRequired[str]
    isOriginal: bool


class TiktokVideoResponseDataVideo(TypedDict):
    id: NotRequired[str]
    url: str
    type: TiktokVideoResponseDataVideoType
    text: NotRequired[str]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    createdAt: NotRequired[str]
    durationSeconds: NotRequired[float]
    width: NotRequired[int]
    height: NotRequired[int]
    thumbnail: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    views: NotRequired[int]
    likes: NotRequired[int]
    comments: NotRequired[int]
    shares: NotRequired[int]
    saves: NotRequired[int]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    audio: NotRequired[TiktokVideoResponseDataVideoAudio]
    country: NotRequired[str]
    isAd: bool
    isAiGenerated: bool


class TiktokVideoResponseData(TypedDict):
    video: TiktokVideoResponseDataVideo


class TiktokVideoResponse(TypedDict):
    success: Literal[True]
    data: TiktokVideoResponseData
    creditsUsed: int
    requestId: str


class TiktokUrlResponseDataOption0(TypedDict):
    kind: Literal["profile"]
    profile: TiktokProfileResponseDataProfile


class TiktokUrlResponseDataOption1(TypedDict):
    kind: Literal["video"]
    video: TiktokVideoResponseDataVideo


class TiktokUrlResponse(TypedDict):
    success: Literal[True]
    data: TiktokUrlResponseDataOption0 | TiktokUrlResponseDataOption1
    creditsUsed: int
    requestId: str


class TiktokPostsResponseDataPostsItem(TypedDict):
    id: NotRequired[str]
    url: str
    type: TiktokVideoResponseDataVideoType
    text: NotRequired[str]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    createdAt: NotRequired[str]
    durationSeconds: NotRequired[float]
    width: NotRequired[int]
    height: NotRequired[int]
    thumbnail: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    views: NotRequired[int]
    likes: NotRequired[int]
    comments: NotRequired[int]
    shares: NotRequired[int]
    saves: NotRequired[int]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    audio: NotRequired[TiktokVideoResponseDataVideoAudio]
    isAd: bool
    isAiGenerated: bool


class TiktokPostsResponseData(TypedDict):
    posts: list[TiktokPostsResponseDataPostsItem]
    cursor: NotRequired[str]


class TiktokPostsResponse(TypedDict):
    success: Literal[True]
    data: TiktokPostsResponseData
    creditsUsed: int
    requestId: str


class TiktokHashtagResponseData(TypedDict):
    videos: list[TiktokPostsResponseDataPostsItem]
    cursor: NotRequired[str]


class TiktokHashtagResponse(TypedDict):
    success: Literal[True]
    data: TiktokHashtagResponseData
    creditsUsed: int
    requestId: str


class TiktokCommentsResponseDataCommentsItem(TypedDict):
    id: NotRequired[str]
    text: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    likes: int
    replies: int
    createdAt: NotRequired[str]


class TiktokCommentsResponseData(TypedDict):
    comments: list[TiktokCommentsResponseDataCommentsItem]
    cursor: NotRequired[str]


class TiktokCommentsResponse(TypedDict):
    success: Literal[True]
    data: TiktokCommentsResponseData
    creditsUsed: int
    requestId: str


class TiktokCommentsRepliesResponseData(TypedDict):
    replies: list[TiktokCommentsResponseDataCommentsItem]
    cursor: NotRequired[str]


class TiktokCommentsRepliesResponse(TypedDict):
    success: Literal[True]
    data: TiktokCommentsRepliesResponseData
    creditsUsed: int
    requestId: str


class TiktokSearchResponseDataUsersItem(TypedDict):
    id: NotRequired[str]
    secUid: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: bool
    followers: NotRequired[int]
    likes: NotRequired[int]


class TiktokSearchResponseData(TypedDict):
    videos: list[TiktokPostsResponseDataPostsItem]
    users: list[TiktokSearchResponseDataUsersItem]
    cursor: NotRequired[str]


class TiktokSearchResponse(TypedDict):
    success: Literal[True]
    data: TiktokSearchResponseData
    creditsUsed: int
    requestId: str


class BlueskyProfileResponseDataProfile(TypedDict):
    id: NotRequired[str]
    did: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    avatar: NotRequired[str]
    banner: NotRequired[str]
    followers: NotRequired[int]
    following: NotRequired[int]
    posts: NotRequired[int]
    isVerified: bool
    pinnedPost: NotRequired[str]
    createdAt: NotRequired[str]


class BlueskyProfileResponseData(TypedDict):
    profile: BlueskyProfileResponseDataProfile


class BlueskyProfileResponse(TypedDict):
    success: Literal[True]
    data: BlueskyProfileResponseData
    creditsUsed: int
    requestId: str


class BlueskyPostsResponseDataPostsItemReplyTo(TypedDict):
    id: NotRequired[str]
    url: NotRequired[str]
    username: NotRequired[str]


class BlueskyPostsResponseDataPostsItemImagesItem(TypedDict):
    url: str
    thumbnail: NotRequired[str]
    alt: NotRequired[str]


class BlueskyPostsResponseDataPostsItemQuoted(TypedDict):
    id: NotRequired[str]
    url: str
    text: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]


class BlueskyPostsResponseDataPostsItem(TypedDict):
    id: NotRequired[str]
    cid: NotRequired[str]
    url: str
    text: NotRequired[str]
    language: NotRequired[str]
    createdAt: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    likes: int
    reposts: int
    replies: int
    quotes: int
    replyTo: NotRequired[BlueskyPostsResponseDataPostsItemReplyTo]
    repostedBy: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    links: NotRequired[list[str]]
    images: NotRequired[list[BlueskyPostsResponseDataPostsItemImagesItem]]
    video: NotRequired[BlueskyPostsResponseDataPostsItemImagesItem]
    link: NotRequired[RedditSearchResponseDataResultsItemOption0Link]
    quoted: NotRequired[BlueskyPostsResponseDataPostsItemQuoted]


class BlueskyPostsResponseData(TypedDict):
    posts: list[BlueskyPostsResponseDataPostsItem]
    cursor: NotRequired[str]


class BlueskyPostsResponse(TypedDict):
    success: Literal[True]
    data: BlueskyPostsResponseData
    creditsUsed: int
    requestId: str


class BlueskyPostResponseDataRepliesItem(TypedDict):
    id: NotRequired[str]
    cid: NotRequired[str]
    url: str
    text: NotRequired[str]
    language: NotRequired[str]
    createdAt: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    likes: int
    reposts: int
    replies: int
    quotes: int
    replyTo: NotRequired[BlueskyPostsResponseDataPostsItemReplyTo]
    repostedBy: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    links: NotRequired[list[str]]
    images: NotRequired[list[BlueskyPostsResponseDataPostsItemImagesItem]]
    video: NotRequired[BlueskyPostsResponseDataPostsItemImagesItem]
    link: NotRequired[RedditSearchResponseDataResultsItemOption0Link]
    quoted: NotRequired[BlueskyPostsResponseDataPostsItemQuoted]
    depth: int


class BlueskyPostResponseData(TypedDict):
    post: BlueskyPostsResponseDataPostsItem
    replies: list[BlueskyPostResponseDataRepliesItem]


class BlueskyPostResponse(TypedDict):
    success: Literal[True]
    data: BlueskyPostResponseData
    creditsUsed: int
    requestId: str


class BlueskyFollowersResponseDataFollowersItem(TypedDict):
    id: NotRequired[str]
    did: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    avatar: NotRequired[str]
    createdAt: NotRequired[str]


class BlueskyFollowersResponseData(TypedDict):
    followers: list[BlueskyFollowersResponseDataFollowersItem]
    cursor: NotRequired[str]


class BlueskyFollowersResponse(TypedDict):
    success: Literal[True]
    data: BlueskyFollowersResponseData
    creditsUsed: int
    requestId: str


class MastodonProfileResponseDataProfileFieldsItem(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
    verifiedAt: NotRequired[str]


class MastodonProfileResponseDataProfile(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    bioHtml: NotRequired[str]
    avatar: NotRequired[str]
    banner: NotRequired[str]
    followers: NotRequired[int]
    following: NotRequired[int]
    posts: NotRequired[int]
    isBot: bool
    isLocked: bool
    isGroup: bool
    fields: NotRequired[list[MastodonProfileResponseDataProfileFieldsItem]]
    createdAt: NotRequired[str]
    lastPostAt: NotRequired[str]


class MastodonProfileResponseData(TypedDict):
    profile: MastodonProfileResponseDataProfile


class MastodonProfileResponse(TypedDict):
    success: Literal[True]
    data: MastodonProfileResponseData
    creditsUsed: int
    requestId: str


class MastodonPostsResponseDataPostsItemMediaItem(TypedDict):
    type: NotRequired[str]
    url: str
    thumbnail: NotRequired[str]
    description: NotRequired[str]


class MastodonPostsResponseDataPostsItem(TypedDict):
    id: NotRequired[str]
    url: str
    uri: NotRequired[str]
    text: NotRequired[str]
    html: NotRequired[str]
    spoiler: NotRequired[str]
    language: NotRequired[str]
    visibility: NotRequired[str]
    isSensitive: bool
    createdAt: NotRequired[str]
    editedAt: NotRequired[str]
    replyTo: NotRequired[BlueskyPostsResponseDataPostsItemReplyTo]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    replies: int
    reposts: int
    likes: int
    quotes: int
    repostedBy: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    media: NotRequired[list[MastodonPostsResponseDataPostsItemMediaItem]]
    link: NotRequired[RedditSearchResponseDataResultsItemOption0Link]


class MastodonPostsResponseData(TypedDict):
    posts: list[MastodonPostsResponseDataPostsItem]
    cursor: NotRequired[str]


class MastodonPostsResponse(TypedDict):
    success: Literal[True]
    data: MastodonPostsResponseData
    creditsUsed: int
    requestId: str


class MastodonPostResponseData(TypedDict):
    post: MastodonPostsResponseDataPostsItem
    ancestors: list[MastodonPostsResponseDataPostsItem]
    replies: list[MastodonPostsResponseDataPostsItem]


class MastodonPostResponse(TypedDict):
    success: Literal[True]
    data: MastodonPostResponseData
    creditsUsed: int
    requestId: str


class ThreadsProfileResponseDataProfile(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    bioLinks: NotRequired[list[YoutubeChannelResponseDataChannelAboutLinksItem]]
    isVerified: bool
    isPrivate: bool
    followers: NotRequired[int]
    avatar: NotRequired[str]


class ThreadsProfileResponseData(TypedDict):
    profile: ThreadsProfileResponseDataProfile


class ThreadsProfileResponse(TypedDict):
    success: Literal[True]
    data: ThreadsProfileResponseData
    creditsUsed: int
    requestId: str


class ThreadsPostsResponseDataPostsItemQuoted(TypedDict):
    id: NotRequired[str]
    code: NotRequired[str]
    url: str
    type: ThreadsPostsResponseDataPostsItemType
    text: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    createdAt: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    reposts: NotRequired[int]
    quotes: NotRequired[int]
    shares: NotRequired[int]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    videos: NotRequired[list[InstagramProfileResponseDataPostsItemVideosItem]]
    link: NotRequired[RedditSearchResponseDataResultsItemOption0Link]
    isReply: bool
    replyTo: NotRequired[BlueskyPostsResponseDataPostsItemReplyTo]
    isPinned: bool


class ThreadsPostsResponseDataPostsItem(TypedDict):
    id: NotRequired[str]
    code: NotRequired[str]
    url: str
    type: ThreadsPostsResponseDataPostsItemType
    text: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    createdAt: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    reposts: NotRequired[int]
    quotes: NotRequired[int]
    shares: NotRequired[int]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    videos: NotRequired[list[InstagramProfileResponseDataPostsItemVideosItem]]
    link: NotRequired[RedditSearchResponseDataResultsItemOption0Link]
    isReply: bool
    replyTo: NotRequired[BlueskyPostsResponseDataPostsItemReplyTo]
    isPinned: bool
    quoted: NotRequired[ThreadsPostsResponseDataPostsItemQuoted]
    repostOf: NotRequired[ThreadsPostsResponseDataPostsItemQuoted]


class ThreadsPostsResponseData(TypedDict):
    posts: list[ThreadsPostsResponseDataPostsItem]
    cursor: NotRequired[str]


class ThreadsPostsResponse(TypedDict):
    success: Literal[True]
    data: ThreadsPostsResponseData
    creditsUsed: int
    requestId: str


class ThreadsPostResponseData(TypedDict):
    post: ThreadsPostsResponseDataPostsItem
    thread: list[ThreadsPostsResponseDataPostsItem]
    replies: list[ThreadsPostsResponseDataPostsItem]
    cursor: NotRequired[str]


class ThreadsPostResponse(TypedDict):
    success: Literal[True]
    data: ThreadsPostResponseData
    creditsUsed: int
    requestId: str


class ThreadsSearchResponseData(TypedDict):
    posts: list[ThreadsPostsResponseDataPostsItem]


class ThreadsSearchResponse(TypedDict):
    success: Literal[True]
    data: ThreadsSearchResponseData
    creditsUsed: int
    requestId: str


class TelegramChannelResponseDataChannel(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    url: str
    type: TelegramChannelResponseDataChannelType
    name: NotRequired[str]
    description: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: bool
    subscribers: NotRequired[int]
    hasPreview: bool
    photos: NotRequired[int]
    videos: NotRequired[int]
    files: NotRequired[int]
    links: NotRequired[int]


class TelegramChannelResponseData(TypedDict):
    channel: TelegramChannelResponseDataChannel


class TelegramChannelResponse(TypedDict):
    success: Literal[True]
    data: TelegramChannelResponseData
    creditsUsed: int
    requestId: str


class TelegramPostsResponseDataPostsItemRepostOf(TypedDict):
    url: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]


class TelegramPostsResponseDataPostsItemMediaItem(TypedDict):
    type: TelegramPostsResponseDataPostsItemMediaItemType
    url: NotRequired[str]
    thumbnail: NotRequired[str]
    durationSeconds: NotRequired[int]


class TelegramPostsResponseDataPostsItemLink(TypedDict):
    url: str
    title: NotRequired[str]
    description: NotRequired[str]
    image: NotRequired[str]
    siteName: NotRequired[str]


class TelegramPostsResponseDataPostsItemReactionsItem(TypedDict):
    emoji: NotRequired[str]
    customEmojiId: NotRequired[str]
    isPaid: bool
    count: int


class TelegramPostsResponseDataPostsItem(TypedDict):
    id: NotRequired[str]
    channel: NotRequired[str]
    url: str
    text: NotRequired[str]
    links: NotRequired[list[str]]
    createdAt: NotRequired[str]
    isEdited: bool
    views: NotRequired[int]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    repostOf: NotRequired[TelegramPostsResponseDataPostsItemRepostOf]
    replyTo: NotRequired[BlueskyPostsResponseDataPostsItemReplyTo]
    media: NotRequired[list[TelegramPostsResponseDataPostsItemMediaItem]]
    link: NotRequired[TelegramPostsResponseDataPostsItemLink]
    reactions: NotRequired[list[TelegramPostsResponseDataPostsItemReactionsItem]]


class TelegramPostsResponseData(TypedDict):
    posts: list[TelegramPostsResponseDataPostsItem]
    cursor: NotRequired[str]


class TelegramPostsResponse(TypedDict):
    success: Literal[True]
    data: TelegramPostsResponseData
    creditsUsed: int
    requestId: str


class TelegramPostResponseData(TypedDict):
    post: TelegramPostsResponseDataPostsItem


class TelegramPostResponse(TypedDict):
    success: Literal[True]
    data: TelegramPostResponseData
    creditsUsed: int
    requestId: str


class MetaAdsSearchResponseDataAdsItemPage(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    categories: NotRequired[list[str]]
    likes: NotRequired[int]


class MetaAdsSearchResponseDataAdsItemLink(TypedDict):
    url: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    caption: NotRequired[str]


class MetaAdsSearchResponseDataAdsItemCta(TypedDict):
    text: NotRequired[str]
    type: NotRequired[str]


class MetaAdsSearchResponseDataAdsItemVideosItem(TypedDict):
    url: str
    thumbnail: NotRequired[str]


class MetaAdsSearchResponseDataAdsItemCardsItem(TypedDict):
    text: NotRequired[str]
    link: NotRequired[MetaAdsSearchResponseDataAdsItemLink]
    cta: NotRequired[MetaAdsSearchResponseDataAdsItemCta]
    image: NotRequired[str]
    video: NotRequired[MetaAdsSearchResponseDataAdsItemVideosItem]


class MetaAdsSearchResponseDataAdsItemSpend(TypedDict):
    min: NotRequired[int]
    max: NotRequired[int]


class MetaAdsSearchResponseDataAdsItem(TypedDict):
    id: NotRequired[str]
    url: str
    page: NotRequired[MetaAdsSearchResponseDataAdsItemPage]
    isActive: bool
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    platforms: NotRequired[list[str]]
    format: NotRequired[str]
    text: NotRequired[str]
    link: NotRequired[MetaAdsSearchResponseDataAdsItemLink]
    cta: NotRequired[MetaAdsSearchResponseDataAdsItemCta]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    videos: NotRequired[list[MetaAdsSearchResponseDataAdsItemVideosItem]]
    cards: NotRequired[list[MetaAdsSearchResponseDataAdsItemCardsItem]]
    versions: int
    categories: NotRequired[list[str]]
    paidBy: NotRequired[str]
    spend: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    currency: NotRequired[str]
    impressions: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    reach: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    countries: NotRequired[list[str]]


class MetaAdsSearchResponseData(TypedDict):
    ads: list[MetaAdsSearchResponseDataAdsItem]
    cursor: NotRequired[str]


class MetaAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: MetaAdsSearchResponseData
    creditsUsed: int
    requestId: str


class MetaAdsAdResponseDataDetailsAdvertiser(TypedDict):
    description: NotRequired[str]
    category: NotRequired[str]
    likes: NotRequired[int]
    verification: NotRequired[str]
    instagram: NotRequired[str]
    instagramFollowers: NotRequired[int]


class MetaAdsAdResponseDataDetailsAudienceAgeGenderItem(TypedDict):
    age: NotRequired[str]
    female: float
    male: float
    unknown: float


class MetaAdsAdResponseDataDetailsAudienceRegionsItem(TypedDict):
    region: NotRequired[str]
    share: float


class MetaAdsAdResponseDataDetailsAudience(TypedDict):
    ageGender: NotRequired[list[MetaAdsAdResponseDataDetailsAudienceAgeGenderItem]]
    regions: NotRequired[list[MetaAdsAdResponseDataDetailsAudienceRegionsItem]]


class MetaAdsAdResponseDataDetailsEuReachByCountryItem(TypedDict):
    country: NotRequired[str]
    age: NotRequired[str]
    female: int
    male: int
    unknown: int


class MetaAdsAdResponseDataDetailsEuReach(TypedDict):
    total: NotRequired[int]
    byCountry: NotRequired[list[MetaAdsAdResponseDataDetailsEuReachByCountryItem]]


class MetaAdsAdResponseDataDetailsPayersItem(TypedDict):
    paidBy: NotRequired[str]
    beneficiary: NotRequired[str]


class MetaAdsAdResponseDataDetails(TypedDict):
    advertiser: NotRequired[MetaAdsAdResponseDataDetailsAdvertiser]
    audience: NotRequired[MetaAdsAdResponseDataDetailsAudience]
    euReach: NotRequired[MetaAdsAdResponseDataDetailsEuReach]
    payers: NotRequired[list[MetaAdsAdResponseDataDetailsPayersItem]]


class MetaAdsAdResponseData(TypedDict):
    ad: MetaAdsSearchResponseDataAdsItem
    details: NotRequired[MetaAdsAdResponseDataDetails]


class MetaAdsAdResponse(TypedDict):
    success: Literal[True]
    data: MetaAdsAdResponseData
    creditsUsed: int
    requestId: str


class LinkedinJobsSearchResponseDataJobsItemCompany(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]


class LinkedinJobsSearchResponseDataJobsItem(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    company: NotRequired[LinkedinJobsSearchResponseDataJobsItemCompany]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    createdAt: NotRequired[str]
    salaryText: NotRequired[str]
    isEasyApply: NotRequired[bool]
    insight: NotRequired[str]


class LinkedinJobsSearchResponseData(TypedDict):
    jobs: list[LinkedinJobsSearchResponseDataJobsItem]
    cursor: NotRequired[str]


class LinkedinJobsSearchResponse(TypedDict):
    success: Literal[True]
    data: LinkedinJobsSearchResponseData
    creditsUsed: int
    requestId: str


class LinkedinJobsJobResponseDataJobDescription(TypedDict):
    text: NotRequired[str]
    html: NotRequired[str]


class LinkedinJobsJobResponseDataJob(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    company: NotRequired[LinkedinJobsSearchResponseDataJobsItemCompany]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    createdAt: NotRequired[str]
    applicants: NotRequired[int]
    applicantsText: NotRequired[str]
    salaryText: NotRequired[str]
    isEasyApply: NotRequired[bool]
    applyUrl: NotRequired[str]
    seniority: NotRequired[str]
    employmentType: NotRequired[str]
    jobFunction: NotRequired[str]
    industries: NotRequired[str]
    description: NotRequired[LinkedinJobsJobResponseDataJobDescription]


class LinkedinJobsJobResponseData(TypedDict):
    job: LinkedinJobsJobResponseDataJob


class LinkedinJobsJobResponse(TypedDict):
    success: Literal[True]
    data: LinkedinJobsJobResponseData
    creditsUsed: int
    requestId: str


class LinkedinAdsSearchResponseDataAdsItem(TypedDict):
    id: NotRequired[str]
    url: str
    creativeType: NotRequired[str]
    format: NotRequired[str]
    advertiser: NotRequired[LinkedinJobsSearchResponseDataJobsItemCompany]
    postedBy: NotRequired[str]
    text: NotRequired[str]
    headline: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]


class LinkedinAdsSearchResponseData(TypedDict):
    ads: list[LinkedinAdsSearchResponseDataAdsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class LinkedinAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: LinkedinAdsSearchResponseData
    creditsUsed: int
    requestId: str


class LinkedinAdsAdResponseDataAdCountriesItem(TypedDict):
    country: NotRequired[str]
    share: NotRequired[float]


class LinkedinAdsAdResponseDataAdTargetingItem(TypedDict):
    parameter: NotRequired[str]
    description: NotRequired[str]


class LinkedinAdsAdResponseDataAdTargetingUsedItem(TypedDict):
    parameter: NotRequired[str]
    isTargeted: bool
    isExcluded: bool


class LinkedinAdsAdResponseDataAd(TypedDict):
    id: NotRequired[str]
    url: str
    creativeType: NotRequired[str]
    format: NotRequired[str]
    advertiser: NotRequired[LinkedinJobsSearchResponseDataJobsItemCompany]
    postedBy: NotRequired[str]
    text: NotRequired[str]
    headline: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    paidBy: NotRequired[str]
    cta: NotRequired[MetaAdsSearchResponseDataAdsItemCta]
    videos: NotRequired[list[InstagramProfileResponseDataPostsItemVideosItem]]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressions: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    countries: NotRequired[list[LinkedinAdsAdResponseDataAdCountriesItem]]
    targeting: NotRequired[list[LinkedinAdsAdResponseDataAdTargetingItem]]
    targetingUsed: NotRequired[list[LinkedinAdsAdResponseDataAdTargetingUsedItem]]


class LinkedinAdsAdResponseData(TypedDict):
    ad: LinkedinAdsAdResponseDataAd


class LinkedinAdsAdResponse(TypedDict):
    success: Literal[True]
    data: LinkedinAdsAdResponseData
    creditsUsed: int
    requestId: str


class LinkedinCompanyResponseDataCompany(TypedDict):
    id: NotRequired[str]
    url: str
    name: NotRequired[str]
    industry: NotRequired[str]
    size: NotRequired[str]
    employees: NotRequired[int]
    headquarters: NotRequired[str]
    website: NotRequired[str]
    followers: NotRequired[int]
    description: NotRequired[str]
    specialties: NotRequired[list[str]]
    founded: NotRequired[str]


class LinkedinCompanyResponseData(TypedDict):
    company: LinkedinCompanyResponseDataCompany


class LinkedinCompanyResponse(TypedDict):
    success: Literal[True]
    data: LinkedinCompanyResponseData
    creditsUsed: int
    requestId: str


class LinkedinProfileResponseDataProfile(TypedDict):
    id: NotRequired[str]
    url: str
    name: NotRequired[str]
    headline: NotRequired[str]
    location: NotRequired[str]
    about: NotRequired[str]
    isAboutTruncated: bool
    followers: NotRequired[int]
    roles: NotRequired[list[LinkedinProfileResponseDataProfileRolesItem]]
    education: NotRequired[list[LinkedinProfileResponseDataProfileEducationItem]]


class LinkedinProfileResponseData(TypedDict):
    profile: LinkedinProfileResponseDataProfile


class LinkedinProfileResponse(TypedDict):
    success: Literal[True]
    data: LinkedinProfileResponseData
    creditsUsed: int
    requestId: str


class LinkedinPostsResponseDataPostsItem(TypedDict):
    id: NotRequired[str]
    url: str
    text: NotRequired[str]
    createdAt: NotRequired[str]
    likes: NotRequired[int]
    author: NotRequired[WebNewsResponseDataArticlesItemPublisher]


class LinkedinPostsResponseData(TypedDict):
    posts: list[LinkedinPostsResponseDataPostsItem]


class LinkedinPostsResponse(TypedDict):
    success: Literal[True]
    data: LinkedinPostsResponseData
    creditsUsed: int
    requestId: str


class ZillowSearchBounds(TypedDict):
    west: float
    east: float
    south: float
    north: float


class ZillowSearchPrice(TypedDict):
    min: NotRequired[float]
    max: NotRequired[float]


class ZillowSearchHoa(TypedDict):
    max: float


class ZillowSearchResponseDataListingsItemBroker(TypedDict):
    name: NotRequired[str]


class ZillowSearchResponseDataListingsItemBuildingUnitsItem(TypedDict):
    bedrooms: NotRequired[float]
    price: NotRequired[float]


class ZillowSearchResponseDataListingsItemBuilding(TypedDict):
    name: NotRequired[str]
    minRent: NotRequired[float]
    maxRent: NotRequired[float]
    availableUnits: NotRequired[int]
    units: NotRequired[list[ZillowSearchResponseDataListingsItemBuildingUnitsItem]]


class ZillowSearchResponseDataListingsItem(TypedDict):
    id: NotRequired[str]
    url: str
    status: ZillowSearchResponseDataListingsItemStatus
    statusText: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    bedrooms: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    homeType: NotRequired[str]
    daysOnZillow: NotRequired[int]
    lastSoldAt: NotRequired[str]
    zestimate: NotRequired[float]
    rentZestimate: NotRequired[float]
    broker: NotRequired[ZillowSearchResponseDataListingsItemBroker]
    image: NotRequired[str]
    building: NotRequired[ZillowSearchResponseDataListingsItemBuilding]


class ZillowSearchResponseData(TypedDict):
    listings: list[ZillowSearchResponseDataListingsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class ZillowSearchResponse(TypedDict):
    success: Literal[True]
    data: ZillowSearchResponseData
    creditsUsed: int
    requestId: str


class ZillowPropertyResponseDataPropertyLotSize(TypedDict):
    value: float
    unit: NotRequired[str]


class ZillowPropertyResponseDataPropertyPriceHistoryItem(TypedDict):
    date: str
    price: NotRequired[float]
    event: NotRequired[str]


class ZillowPropertyResponseDataPropertyMls(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]


class ZillowPropertyResponseDataPropertyBroker(TypedDict):
    name: NotRequired[str]
    phone: NotRequired[str]


class ZillowPropertyResponseDataPropertyAgent(TypedDict):
    name: NotRequired[str]
    phone: NotRequired[str]
    email: NotRequired[str]


class ZillowPropertyResponseDataProperty(TypedDict):
    id: NotRequired[str]
    url: str
    status: NotRequired[str]
    homeType: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    zestimate: NotRequired[float]
    rentZestimate: NotRequired[float]
    lastSoldPrice: NotRequired[float]
    lastSoldAt: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    bedrooms: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    lotSize: NotRequired[ZillowPropertyResponseDataPropertyLotSize]
    yearBuilt: NotRequired[int]
    description: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    priceHistory: NotRequired[list[ZillowPropertyResponseDataPropertyPriceHistoryItem]]
    daysOnZillow: NotRequired[int]
    views: NotRequired[int]
    saves: NotRequired[int]
    monthlyHoa: NotRequired[float]
    propertyTaxRate: NotRequired[float]
    mls: NotRequired[ZillowPropertyResponseDataPropertyMls]
    broker: NotRequired[ZillowPropertyResponseDataPropertyBroker]
    agent: NotRequired[ZillowPropertyResponseDataPropertyAgent]
    facts: NotRequired[dict[str, str | float | bool | list[str]]]


class ZillowPropertyResponseData(TypedDict):
    property: ZillowPropertyResponseDataProperty


class ZillowPropertyResponse(TypedDict):
    success: Literal[True]
    data: ZillowPropertyResponseData
    creditsUsed: int
    requestId: str


class GoogleAdsAdvertisersResponseDataAdvertisersItemAds(TypedDict):
    min: int
    max: NotRequired[int]


class GoogleAdsAdvertisersResponseDataAdvertisersItem(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    country: NotRequired[str]
    isVerified: bool
    ads: NotRequired[GoogleAdsAdvertisersResponseDataAdvertisersItemAds]
    url: str


class GoogleAdsAdvertisersResponseData(TypedDict):
    advertisers: list[GoogleAdsAdvertisersResponseDataAdvertisersItem]
    domains: list[str]


class GoogleAdsAdvertisersResponse(TypedDict):
    success: Literal[True]
    data: GoogleAdsAdvertisersResponseData
    creditsUsed: int
    requestId: str


class GoogleAdsSearchResponseDataAdsItemAdvertiser(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    url: str
    country: NotRequired[str]
    isVerified: NotRequired[bool]


class GoogleAdsSearchResponseDataAdsItem(TypedDict):
    id: NotRequired[str]
    url: str
    advertiser: GoogleAdsSearchResponseDataAdsItemAdvertiser
    domain: NotRequired[str]
    format: GoogleAdsSearchResponseDataAdsItemFormat
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    daysShown: NotRequired[int]
    preview: NotRequired[str]
    image: NotRequired[str]


class GoogleAdsSearchResponseDataTotal(TypedDict):
    min: int
    max: int


class GoogleAdsSearchResponseData(TypedDict):
    ads: list[GoogleAdsSearchResponseDataAdsItem]
    total: NotRequired[GoogleAdsSearchResponseDataTotal]
    cursor: NotRequired[str]


class GoogleAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: GoogleAdsSearchResponseData
    creditsUsed: int
    requestId: str


class GoogleAdsAdResponseDataAdVariationsItem(TypedDict):
    preview: NotRequired[str]
    image: NotRequired[str]
    video: NotRequired[str]


class GoogleAdsAdResponseDataAdRegionsItemPlatformsItem(TypedDict):
    platform: GoogleAdsAdResponseDataAdRegionsItemPlatformsItemPlatform
    impressions: GoogleAdsAdvertisersResponseDataAdvertisersItemAds


class GoogleAdsAdResponseDataAdRegionsItem(TypedDict):
    country: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressions: NotRequired[GoogleAdsAdvertisersResponseDataAdvertisersItemAds]
    platforms: NotRequired[list[GoogleAdsAdResponseDataAdRegionsItemPlatformsItem]]


class GoogleAdsAdResponseDataAdTargetingDemographics(TypedDict):
    isIncluded: bool
    isExcluded: bool


class GoogleAdsAdResponseDataAdTargeting(TypedDict):
    demographics: GoogleAdsAdResponseDataAdTargetingDemographics
    geography: GoogleAdsAdResponseDataAdTargetingDemographics
    contextual: GoogleAdsAdResponseDataAdTargetingDemographics
    interests: GoogleAdsAdResponseDataAdTargetingDemographics
    customerLists: GoogleAdsAdResponseDataAdTargetingDemographics


class GoogleAdsAdResponseDataAd(TypedDict):
    id: NotRequired[str]
    url: str
    advertiser: GoogleAdsSearchResponseDataAdsItemAdvertiser
    domain: NotRequired[str]
    format: GoogleAdsSearchResponseDataAdsItemFormat
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    daysShown: NotRequired[int]
    preview: NotRequired[str]
    image: NotRequired[str]
    paidBy: NotRequired[str]
    variations: NotRequired[list[GoogleAdsAdResponseDataAdVariationsItem]]
    impressions: NotRequired[GoogleAdsAdvertisersResponseDataAdvertisersItemAds]
    regions: NotRequired[list[GoogleAdsAdResponseDataAdRegionsItem]]
    targeting: NotRequired[GoogleAdsAdResponseDataAdTargeting]


class GoogleAdsAdResponseData(TypedDict):
    ad: GoogleAdsAdResponseDataAd


class GoogleAdsAdResponse(TypedDict):
    success: Literal[True]
    data: GoogleAdsAdResponseData
    creditsUsed: int
    requestId: str


class TiktokAdsSearchResponseDataAdsItemAdvertiser(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    country: NotRequired[str]


class TiktokAdsSearchResponseDataAdsItem(TypedDict):
    id: NotRequired[str]
    url: str
    advertiser: NotRequired[TiktokAdsSearchResponseDataAdsItemAdvertiser]
    headline: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    reach: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    video: NotRequired[str]
    thumbnail: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]


class TiktokAdsSearchResponseData(TypedDict):
    ads: list[TiktokAdsSearchResponseDataAdsItem]
    advertiser: NotRequired[ZillowPropertyResponseDataPropertyMls]
    total: NotRequired[int]
    cursor: NotRequired[str]


class TiktokAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: TiktokAdsSearchResponseData
    creditsUsed: int
    requestId: str


class TiktokAdsAdResponseDataAdTargetingRegionsItemBreakdownItem(TypedDict):
    age: NotRequired[str]
    gender: NotRequired[str]
    impressions: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]


class TiktokAdsAdResponseDataAdTargetingRegionsItem(TypedDict):
    country: NotRequired[str]
    impressions: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    ages: NotRequired[list[str]]
    genders: NotRequired[list[str]]
    breakdown: NotRequired[list[TiktokAdsAdResponseDataAdTargetingRegionsItemBreakdownItem]]


class TiktokAdsAdResponseDataAdTargeting(TypedDict):
    audienceSize: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    impressions: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    countries: NotRequired[list[str]]
    languages: NotRequired[list[str]]
    interests: NotRequired[str]
    regions: NotRequired[list[TiktokAdsAdResponseDataAdTargetingRegionsItem]]


class TiktokAdsAdResponseDataAd(TypedDict):
    id: NotRequired[str]
    url: str
    advertiser: NotRequired[TiktokAdsSearchResponseDataAdsItemAdvertiser]
    headline: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    reach: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    video: NotRequired[str]
    thumbnail: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    paidBy: NotRequired[str]
    link: NotRequired[MetaAdsSearchResponseDataAdsItemLink]
    cta: NotRequired[MetaAdsSearchResponseDataAdsItemCta]
    objective: NotRequired[str]
    category: NotRequired[str]
    targeting: NotRequired[TiktokAdsAdResponseDataAdTargeting]


class TiktokAdsAdResponseData(TypedDict):
    ad: TiktokAdsAdResponseDataAd


class TiktokAdsAdResponse(TypedDict):
    success: Literal[True]
    data: TiktokAdsAdResponseData
    creditsUsed: int
    requestId: str


class UpworkSearchHourlyRate(TypedDict):
    min: NotRequired[int]
    max: NotRequired[int]


class UpworkSearchResponseDataJobsItemHourlyRate(TypedDict):
    min: NotRequired[float]
    max: NotRequired[float]


class UpworkSearchResponseDataJobsItemFixedBudget(TypedDict):
    amount: float


class UpworkSearchResponseDataJobsItem(TypedDict):
    id: NotRequired[str]
    ciphertext: NotRequired[str]
    url: str
    title: NotRequired[str]
    description: NotRequired[str]
    skills: NotRequired[list[str]]
    type: NotRequired[UpworkSearchJobType]
    experience: NotRequired[UpworkSearchExperienceItem]
    hourlyRate: NotRequired[UpworkSearchResponseDataJobsItemHourlyRate]
    fixedBudget: NotRequired[UpworkSearchResponseDataJobsItemFixedBudget]
    currency: NotRequired[str]
    durationWeeks: NotRequired[int]
    createdAt: NotRequired[str]
    publishedAt: NotRequired[str]


class UpworkSearchResponseData(TypedDict):
    jobs: list[UpworkSearchResponseDataJobsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class UpworkSearchResponse(TypedDict):
    success: Literal[True]
    data: UpworkSearchResponseData
    creditsUsed: int
    requestId: str


class UpworkJobResponseDataJobActivity(TypedDict):
    applicants: NotRequired[int]
    hired: NotRequired[int]
    interviewing: NotRequired[int]
    invitesSent: NotRequired[int]
    unansweredInvites: NotRequired[int]
    positions: NotRequired[int]
    lastClientActivityAt: NotRequired[str]


class UpworkJobResponseDataJobClient(TypedDict):
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    timezone: NotRequired[str]
    totalSpent: NotRequired[float]
    hires: NotRequired[int]
    jobsWithHires: NotRequired[int]
    activeContracts: NotRequired[int]
    reviews: NotRequired[int]
    rating: NotRequired[float]
    openJobs: NotRequired[int]
    postedJobs: NotRequired[int]
    joinedAt: NotRequired[str]
    industry: NotRequired[str]
    companySizeText: NotRequired[str]


class UpworkJobResponseDataJob(TypedDict):
    id: NotRequired[str]
    ciphertext: NotRequired[str]
    url: str
    title: NotRequired[str]
    description: NotRequired[str]
    skills: NotRequired[list[str]]
    type: NotRequired[UpworkSearchJobType]
    experience: NotRequired[UpworkSearchExperienceItem]
    hourlyRate: NotRequired[UpworkSearchResponseDataJobsItemHourlyRate]
    fixedBudget: NotRequired[UpworkSearchResponseDataJobsItemFixedBudget]
    currency: NotRequired[str]
    durationWeeks: NotRequired[int]
    createdAt: NotRequired[str]
    publishedAt: NotRequired[str]
    status: NotRequired[str]
    category: NotRequired[str]
    categoryGroup: NotRequired[str]
    durationText: NotRequired[str]
    activity: NotRequired[UpworkJobResponseDataJobActivity]
    client: NotRequired[UpworkJobResponseDataJobClient]


class UpworkJobResponseData(TypedDict):
    job: UpworkJobResponseDataJob


class UpworkJobResponse(TypedDict):
    success: Literal[True]
    data: UpworkJobResponseData
    creditsUsed: int
    requestId: str


class GoogleSuggestResponseDataKeywordsItem(TypedDict):
    keyword: str
    seed: NotRequired[str]
    rank: int


class GoogleSuggestResponseData(TypedDict):
    query: NotRequired[str]
    keywords: list[GoogleSuggestResponseDataKeywordsItem]


class GoogleSuggestResponse(TypedDict):
    success: Literal[True]
    data: GoogleSuggestResponseData
    creditsUsed: int
    requestId: str


class GoogleTrendsInterestResponseDataPointsItem(TypedDict):
    recordedAt: str
    values: NotRequired[list[float]]
    isPartial: bool


class GoogleTrendsInterestResponseData(TypedDict):
    queries: list[str]
    points: list[GoogleTrendsInterestResponseDataPointsItem]
    averages: list[float]


class GoogleTrendsInterestResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsInterestResponseData
    creditsUsed: int
    requestId: str


class GoogleTrendsRegionsResponseDataRegionsItem(TypedDict):
    code: NotRequired[str]
    name: NotRequired[str]
    values: NotRequired[list[float]]


class GoogleTrendsRegionsResponseData(TypedDict):
    queries: list[str]
    regions: list[GoogleTrendsRegionsResponseDataRegionsItem]


class GoogleTrendsRegionsResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsRegionsResponseData
    creditsUsed: int
    requestId: str


class GoogleTrendsRelatedResponseDataQueriesItem(TypedDict):
    query: NotRequired[str]
    value: float


class GoogleTrendsRelatedResponseData(TypedDict):
    query: NotRequired[str]
    queries: list[GoogleTrendsRelatedResponseDataQueriesItem]


class GoogleTrendsRelatedResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsRelatedResponseData
    creditsUsed: int
    requestId: str


class GoogleTrendsTrendingResponseDataTrendsItem(TypedDict):
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
    trends: list[GoogleTrendsTrendingResponseDataTrendsItem]


class GoogleTrendsTrendingResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsTrendingResponseData
    creditsUsed: int
    requestId: str


class SiteMapResponseDataUrlsItem(TypedDict):
    url: str
    lastModifiedAt: NotRequired[str]


class SiteMapResponseData(TypedDict):
    urls: list[SiteMapResponseDataUrlsItem]
    source: SiteMapResponseDataSource
    sitemaps: list[str]
    cursor: NotRequired[str]


class SiteMapResponse(TypedDict):
    success: Literal[True]
    data: SiteMapResponseData
    creditsUsed: int
    requestId: str


class SiteSeoResponseDataTitle(TypedDict):
    text: NotRequired[str]
    length: int


class SiteSeoResponseDataCanonical(TypedDict):
    url: NotRequired[str]
    isSelf: bool


class SiteSeoResponseDataRobots(TypedDict):
    meta: NotRequired[str]
    isNoindex: bool
    isNofollow: bool
    isAllowedByRobotsTxt: NotRequired[bool]


class SiteSeoResponseDataHeadingsOutlineItem(TypedDict):
    level: int
    text: NotRequired[str]


class SiteSeoResponseDataHeadings(TypedDict):
    h1: NotRequired[list[str]]
    h2: NotRequired[list[str]]
    outline: NotRequired[list[SiteSeoResponseDataHeadingsOutlineItem]]


class SiteSeoResponseDataHreflangItem(TypedDict):
    language: NotRequired[str]
    url: str


class SiteSeoResponseDataJsonLd(TypedDict):
    blocks: int
    invalid: int
    types: NotRequired[list[str]]


class SiteSeoResponseDataImages(TypedDict):
    total: int
    missingAlt: int
    emptyAlt: int
    missingAltExamples: NotRequired[list[str]]


class SiteSeoResponseDataLinksCheckedItem(TypedDict):
    url: str
    status: NotRequired[int]


class SiteSeoResponseDataLinks(TypedDict):
    internal: int
    external: int
    nofollow: int
    checked: NotRequired[list[SiteSeoResponseDataLinksCheckedItem]]
    broken: NotRequired[list[SiteSeoResponseDataLinksCheckedItem]]


class SiteSeoResponseData(TypedDict):
    url: str
    title: SiteSeoResponseDataTitle
    description: SiteSeoResponseDataTitle
    language: NotRequired[str]
    hasViewport: bool
    canonical: SiteSeoResponseDataCanonical
    robots: SiteSeoResponseDataRobots
    headings: NotRequired[SiteSeoResponseDataHeadings]
    hreflang: list[SiteSeoResponseDataHreflangItem]
    openGraph: NotRequired[dict[str, str]]
    twitter: NotRequired[dict[str, str]]
    jsonLd: SiteSeoResponseDataJsonLd
    images: SiteSeoResponseDataImages
    links: SiteSeoResponseDataLinks
    words: int
    issues: list[str]


class SiteSeoResponse(TypedDict):
    success: Literal[True]
    data: SiteSeoResponseData
    creditsUsed: int
    requestId: str


class DomainWhoisResponseDataRegistrar(TypedDict):
    name: NotRequired[str]
    ianaId: NotRequired[str]
    url: NotRequired[str]
    abuseEmail: NotRequired[str]
    abusePhone: NotRequired[str]


class DomainWhoisResponseDataRegistrant(TypedDict):
    name: NotRequired[str]
    organization: NotRequired[str]
    email: NotRequired[str]
    phone: NotRequired[str]
    country: NotRequired[str]


class DomainWhoisResponseData(TypedDict):
    domain: NotRequired[str]
    registryId: NotRequired[str]
    status: list[str]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    expiresAt: NotRequired[str]
    registrar: NotRequired[DomainWhoisResponseDataRegistrar]
    registrant: NotRequired[DomainWhoisResponseDataRegistrant]
    nameservers: list[str]
    hasDnssec: NotRequired[bool]
    rdap: str


class DomainWhoisResponse(TypedDict):
    success: Literal[True]
    data: DomainWhoisResponseData
    creditsUsed: int
    requestId: str


class DomainDnsResponseDataRecordsItem(TypedDict):
    type: DomainDnsTypesItem
    name: NotRequired[str]
    value: NotRequired[str]
    ttlSeconds: int


class DomainDnsResponseDataMxItem(TypedDict):
    priority: int
    exchange: NotRequired[str]


class DomainDnsResponseDataDmarc(TypedDict):
    record: NotRequired[str]
    policy: NotRequired[str]


class DomainDnsResponseData(TypedDict):
    domain: NotRequired[str]
    isResolvable: bool
    records: list[DomainDnsResponseDataRecordsItem]
    mx: list[DomainDnsResponseDataMxItem]
    spf: NotRequired[str]
    dmarc: NotRequired[DomainDnsResponseDataDmarc]


class DomainDnsResponse(TypedDict):
    success: Literal[True]
    data: DomainDnsResponseData
    creditsUsed: int
    requestId: str


class DomainTechResponseDataTechnologiesItem(TypedDict):
    name: NotRequired[str]
    category: NotRequired[str]
    version: NotRequired[str]
    evidence: DomainTechResponseDataTechnologiesItemEvidence


class DomainTechResponseData(TypedDict):
    url: str
    generator: NotRequired[str]
    technologies: list[DomainTechResponseDataTechnologiesItem]


class DomainTechResponse(TypedDict):
    success: Literal[True]
    data: DomainTechResponseData
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


class CryptoCoinsResponseDataCoinsItem(TypedDict):
    id: NotRequired[str]
    source: CryptoCoinsResponseDataCoinsItemSource
    symbol: NotRequired[str]
    name: NotRequired[str]
    url: str
    image: NotRequired[str]
    rank: NotRequired[int]
    currency: NotRequired[str]
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
    coins: list[CryptoCoinsResponseDataCoinsItem]
    cursor: NotRequired[str]


class CryptoCoinsResponse(TypedDict):
    success: Literal[True]
    data: CryptoCoinsResponseData
    creditsUsed: int
    requestId: str


class CryptoCoinResponseDataCoinSocialsItem(TypedDict):
    type: NotRequired[str]
    url: str


class CryptoCoinResponseDataCoinContractsItem(TypedDict):
    chain: NotRequired[str]
    address: NotRequired[str]
    decimals: NotRequired[int]


class CryptoCoinResponseDataCoin(TypedDict):
    id: NotRequired[str]
    source: CryptoCoinsResponseDataCoinsItemSource
    symbol: NotRequired[str]
    name: NotRequired[str]
    url: str
    image: NotRequired[str]
    rank: NotRequired[int]
    currency: NotRequired[str]
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
    chains: NotRequired[list[str]]
    addedAt: NotRequired[str]
    updatedAt: NotRequired[str]
    description: NotRequired[str]
    categories: NotRequired[list[str]]
    change1y: NotRequired[float]
    websites: NotRequired[list[str]]
    whitepaper: NotRequired[str]
    explorers: NotRequired[list[str]]
    socials: NotRequired[list[CryptoCoinResponseDataCoinSocialsItem]]
    contracts: NotRequired[list[CryptoCoinResponseDataCoinContractsItem]]
    launchedAt: NotRequired[str]
    watchlists: NotRequired[int]


class CryptoCoinResponseData(TypedDict):
    coin: CryptoCoinResponseDataCoin


class CryptoCoinResponse(TypedDict):
    success: Literal[True]
    data: CryptoCoinResponseData
    creditsUsed: int
    requestId: str


class CryptoHistoryResponseDataPricesItem(TypedDict):
    recordedAt: str
    price: NotRequired[float]
    marketCap: NotRequired[float]
    volume: NotRequired[float]


class CryptoHistoryResponseDataCandlesItem(TypedDict):
    openedAt: str
    open: float
    high: float
    low: float
    close: float


class CryptoHistoryResponseData(TypedDict):
    coin: NotRequired[str]
    currency: NotRequired[str]
    prices: list[CryptoHistoryResponseDataPricesItem]
    candles: list[CryptoHistoryResponseDataCandlesItem]


class CryptoHistoryResponse(TypedDict):
    success: Literal[True]
    data: CryptoHistoryResponseData
    creditsUsed: int
    requestId: str


class CryptoTrendingResponseDataCoinsItem(TypedDict):
    id: NotRequired[str]
    source: CryptoCoinsResponseDataCoinsItemSource
    symbol: NotRequired[str]
    name: NotRequired[str]
    url: str
    image: NotRequired[str]
    rank: NotRequired[int]
    currency: NotRequired[str]
    price: NotRequired[float]
    marketCap: NotRequired[float]
    volume24h: NotRequired[float]
    change24h: NotRequired[float]


class CryptoTrendingResponseDataCategoriesItem(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    url: str
    marketCap: NotRequired[float]
    change24h: NotRequired[float]
    volume24h: NotRequired[float]
    coins: NotRequired[int]
    topCoins: NotRequired[list[str]]
    updatedAt: NotRequired[str]


class CryptoTrendingResponseDataNftsItem(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    symbol: NotRequired[str]
    url: str
    image: NotRequired[str]
    floorPriceText: NotRequired[str]
    floorChange24h: NotRequired[float]


class CryptoTrendingResponseData(TypedDict):
    coins: list[CryptoTrendingResponseDataCoinsItem]
    categories: list[CryptoTrendingResponseDataCategoriesItem]
    nfts: list[CryptoTrendingResponseDataNftsItem]


class CryptoTrendingResponse(TypedDict):
    success: Literal[True]
    data: CryptoTrendingResponseData
    creditsUsed: int
    requestId: str


class CryptoCategoriesResponseData(TypedDict):
    categories: list[CryptoTrendingResponseDataCategoriesItem]
    total: int


class CryptoCategoriesResponse(TypedDict):
    success: Literal[True]
    data: CryptoCategoriesResponseData
    creditsUsed: int
    requestId: str


class CryptoMoversResponseDataGainersItem(TypedDict):
    id: NotRequired[str]
    source: CryptoCoinsResponseDataCoinsItemSource
    symbol: NotRequired[str]
    name: NotRequired[str]
    url: str
    image: NotRequired[str]
    rank: NotRequired[int]
    currency: NotRequired[str]
    price: NotRequired[float]
    marketCap: NotRequired[float]
    volume24h: NotRequired[float]
    change1h: NotRequired[float]
    change24h: NotRequired[float]
    change7d: NotRequired[float]
    change30d: NotRequired[float]
    updatedAt: NotRequired[str]


class CryptoMoversResponseData(TypedDict):
    gainers: list[CryptoMoversResponseDataGainersItem]
    losers: list[CryptoMoversResponseDataGainersItem]


class CryptoMoversResponse(TypedDict):
    success: Literal[True]
    data: CryptoMoversResponseData
    creditsUsed: int
    requestId: str


class CryptoNewResponseDataCoinsItem(TypedDict):
    id: NotRequired[str]
    source: CryptoCoinsResponseDataCoinsItemSource
    symbol: NotRequired[str]
    name: NotRequired[str]
    url: str
    image: NotRequired[str]
    rank: NotRequired[int]
    currency: NotRequired[str]
    price: NotRequired[float]
    marketCap: NotRequired[float]
    fullyDilutedValue: NotRequired[float]
    volume24h: NotRequired[float]
    change1h: NotRequired[float]
    change24h: NotRequired[float]
    change7d: NotRequired[float]
    change30d: NotRequired[float]
    chains: NotRequired[list[str]]
    addedAt: NotRequired[str]
    updatedAt: NotRequired[str]


class CryptoNewResponseData(TypedDict):
    coins: list[CryptoNewResponseDataCoinsItem]


class CryptoNewResponse(TypedDict):
    success: Literal[True]
    data: CryptoNewResponseData
    creditsUsed: int
    requestId: str


class CryptoDexSearchResponseDataPairsItemBaseToken(TypedDict):
    address: NotRequired[str]
    name: NotRequired[str]
    symbol: NotRequired[str]


class CryptoDexSearchResponseDataPairsItemTransactionsM5(TypedDict):
    buys: int
    sells: int


class CryptoDexSearchResponseDataPairsItemTransactions(TypedDict):
    m5: CryptoDexSearchResponseDataPairsItemTransactionsM5
    h1: CryptoDexSearchResponseDataPairsItemTransactionsM5
    h6: CryptoDexSearchResponseDataPairsItemTransactionsM5
    h24: CryptoDexSearchResponseDataPairsItemTransactionsM5


class CryptoDexSearchResponseDataPairsItemVolume(TypedDict):
    m5: NotRequired[float]
    h1: NotRequired[float]
    h6: NotRequired[float]
    h24: NotRequired[float]


class CryptoDexSearchResponseDataPairsItemLiquidity(TypedDict):
    usd: NotRequired[float]
    base: NotRequired[float]
    quote: NotRequired[float]


class CryptoDexSearchResponseDataPairsItem(TypedDict):
    id: NotRequired[str]
    chain: NotRequired[str]
    dex: NotRequired[str]
    url: str
    labels: NotRequired[list[str]]
    baseToken: NotRequired[CryptoDexSearchResponseDataPairsItemBaseToken]
    quoteToken: NotRequired[CryptoDexSearchResponseDataPairsItemBaseToken]
    price: NotRequired[float]
    currency: NotRequired[str]
    priceNative: NotRequired[float]
    transactions: CryptoDexSearchResponseDataPairsItemTransactions
    volume: NotRequired[CryptoDexSearchResponseDataPairsItemVolume]
    priceChange: NotRequired[CryptoDexSearchResponseDataPairsItemVolume]
    liquidity: NotRequired[CryptoDexSearchResponseDataPairsItemLiquidity]
    fullyDilutedValue: NotRequired[float]
    marketCap: NotRequired[float]
    createdAt: NotRequired[str]
    image: NotRequired[str]
    websites: NotRequired[list[str]]
    socials: NotRequired[list[CryptoCoinResponseDataCoinSocialsItem]]
    boosts: NotRequired[int]


class CryptoDexSearchResponseData(TypedDict):
    pairs: list[CryptoDexSearchResponseDataPairsItem]


class CryptoDexSearchResponse(TypedDict):
    success: Literal[True]
    data: CryptoDexSearchResponseData
    creditsUsed: int
    requestId: str


class CryptoDexTokenResponseDataToken(TypedDict):
    id: NotRequired[str]
    chain: NotRequired[str]
    name: NotRequired[str]
    symbol: NotRequired[str]
    url: str
    image: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    marketCap: NotRequired[float]
    fullyDilutedValue: NotRequired[float]
    liquidity: float
    volume24h: float
    pairs: int
    websites: NotRequired[list[str]]
    socials: NotRequired[list[CryptoCoinResponseDataCoinSocialsItem]]


class CryptoDexTokenResponseData(TypedDict):
    token: CryptoDexTokenResponseDataToken
    pairs: list[CryptoDexSearchResponseDataPairsItem]


class CryptoDexTokenResponse(TypedDict):
    success: Literal[True]
    data: CryptoDexTokenResponseData
    creditsUsed: int
    requestId: str


class CryptoDexNewResponseDataTokensItemLinksItem(TypedDict):
    type: NotRequired[str]
    label: NotRequired[str]
    url: str


class CryptoDexNewResponseDataTokensItem(TypedDict):
    id: NotRequired[str]
    chain: NotRequired[str]
    url: str
    description: NotRequired[str]
    image: NotRequired[str]
    banner: NotRequired[str]
    links: NotRequired[list[CryptoDexNewResponseDataTokensItemLinksItem]]
    boosts: NotRequired[int]
    totalBoosts: NotRequired[int]
    claimedAt: NotRequired[str]
    pair: NotRequired[CryptoDexSearchResponseDataPairsItem]


class CryptoDexNewResponseData(TypedDict):
    tokens: list[CryptoDexNewResponseDataTokensItem]


class CryptoDexNewResponse(TypedDict):
    success: Literal[True]
    data: CryptoDexNewResponseData
    creditsUsed: int
    requestId: str


class CryptoPumpCoinsResponseDataCoinsItem(TypedDict):
    id: NotRequired[str]
    url: str
    name: NotRequired[str]
    symbol: NotRequired[str]
    description: NotRequired[str]
    image: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    createdAt: NotRequired[str]
    lastTradeAt: NotRequired[str]
    marketCap: NotRequired[float]
    athMarketCap: NotRequired[float]
    currency: NotRequired[str]
    athAt: NotRequired[str]
    isGraduated: bool
    bondingCurveProgress: NotRequired[float]
    pool: NotRequired[str]
    replies: NotRequired[int]
    isLive: bool
    isNsfw: bool
    website: NotRequired[str]
    twitter: NotRequired[str]
    telegram: NotRequired[str]


class CryptoPumpCoinsResponseData(TypedDict):
    coins: list[CryptoPumpCoinsResponseDataCoinsItem]
    cursor: NotRequired[str]


class CryptoPumpCoinsResponse(TypedDict):
    success: Literal[True]
    data: CryptoPumpCoinsResponseData
    creditsUsed: int
    requestId: str


class CryptoPumpCoinResponseData(TypedDict):
    coin: CryptoPumpCoinsResponseDataCoinsItem


class CryptoPumpCoinResponse(TypedDict):
    success: Literal[True]
    data: CryptoPumpCoinResponseData
    creditsUsed: int
    requestId: str


class CryptoPumpTradesResponseDataTradesItem(TypedDict):
    id: NotRequired[str]
    createdAt: NotRequired[str]
    type: CryptoPumpTradesResponseDataTradesItemType
    wallet: NotRequired[str]
    price: NotRequired[float]
    priceSol: NotRequired[float]
    value: NotRequired[float]
    currency: NotRequired[str]
    amountSol: NotRequired[float]
    tokenAmount: NotRequired[float]
    program: NotRequired[str]


class CryptoPumpTradesResponseData(TypedDict):
    trades: list[CryptoPumpTradesResponseDataTradesItem]
    cursor: NotRequired[str]


class CryptoPumpTradesResponse(TypedDict):
    success: Literal[True]
    data: CryptoPumpTradesResponseData
    creditsUsed: int
    requestId: str


class CryptoWalletResponseDataTokensItem(TypedDict):
    address: NotRequired[str]
    symbol: NotRequired[str]
    name: NotRequired[str]
    decimals: NotRequired[int]
    amount: NotRequired[str]
    value: NotRequired[float]
    currency: NotRequired[str]


class CryptoWalletResponseData(TypedDict):
    chain: NotRequired[str]
    address: NotRequired[str]
    symbol: NotRequired[str]
    balance: NotRequired[str]
    balanceValue: NotRequired[float]
    currency: NotRequired[str]
    tokens: NotRequired[list[CryptoWalletResponseDataTokensItem]]
    transactions: list[CryptoWalletResponseDataTransactionsItem]
    cursor: NotRequired[str]


class CryptoWalletResponse(TypedDict):
    success: Literal[True]
    data: CryptoWalletResponseData
    creditsUsed: int
    requestId: str


class CryptoTokenHoldersResponseDataToken(TypedDict):
    address: NotRequired[str]
    name: NotRequired[str]
    symbol: NotRequired[str]
    decimals: NotRequired[int]
    holders: NotRequired[int]
    totalSupply: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]


class CryptoTokenHoldersResponseDataHoldersItem(TypedDict):
    address: NotRequired[str]
    amount: NotRequired[str]
    percent: NotRequired[float]
    isContract: NotRequired[bool]
    label: NotRequired[str]


class CryptoTokenHoldersResponseData(TypedDict):
    token: NotRequired[CryptoTokenHoldersResponseDataToken]
    holders: list[CryptoTokenHoldersResponseDataHoldersItem]
    cursor: NotRequired[str]


class CryptoTokenHoldersResponse(TypedDict):
    success: Literal[True]
    data: CryptoTokenHoldersResponseData
    creditsUsed: int
    requestId: str


class CryptoBinanceAnnouncementsResponseDataAnnouncementsItem(TypedDict):
    id: NotRequired[str]
    code: NotRequired[str]
    title: NotRequired[str]
    url: str
    createdAt: NotRequired[str]
    symbols: NotRequired[list[str]]


class CryptoBinanceAnnouncementsResponseData(TypedDict):
    announcements: list[CryptoBinanceAnnouncementsResponseDataAnnouncementsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class CryptoBinanceAnnouncementsResponse(TypedDict):
    success: Literal[True]
    data: CryptoBinanceAnnouncementsResponseData
    creditsUsed: int
    requestId: str


class IndeedSearchSalary(TypedDict):
    min: int


class IndeedSearchResponseDataJobsItemCompany(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    website: NotRequired[str]
    industry: NotRequired[str]
    employeesText: NotRequired[str]
    revenueText: NotRequired[str]
    description: NotRequired[str]


class IndeedSearchResponseDataJobsItemSalary(TypedDict):
    min: NotRequired[float]
    max: NotRequired[float]
    period: NotRequired[IndeedSearchResponseDataJobsItemSalaryPeriod]
    currency: NotRequired[str]
    isEstimate: bool


class IndeedSearchResponseDataJobsItem(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    company: NotRequired[IndeedSearchResponseDataJobsItemCompany]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    salary: NotRequired[IndeedSearchResponseDataJobsItemSalary]
    jobTypes: NotRequired[list[IndeedSearchJobType]]
    isRemote: bool
    attributes: NotRequired[list[str]]
    createdAt: NotRequired[str]
    indexedAt: NotRequired[str]
    applyUrl: NotRequired[str]
    isEasyApply: bool
    isUrgent: bool
    source: NotRequired[str]
    description: NotRequired[str]


class IndeedSearchResponseData(TypedDict):
    jobs: list[IndeedSearchResponseDataJobsItem]
    cursor: NotRequired[str]


class IndeedSearchResponse(TypedDict):
    success: Literal[True]
    data: IndeedSearchResponseData
    creditsUsed: int
    requestId: str


class IndeedJobResponseDataJob(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    company: NotRequired[IndeedSearchResponseDataJobsItemCompany]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    salary: NotRequired[IndeedSearchResponseDataJobsItemSalary]
    jobTypes: NotRequired[list[IndeedSearchJobType]]
    isRemote: bool
    attributes: NotRequired[list[str]]
    createdAt: NotRequired[str]
    indexedAt: NotRequired[str]
    applyUrl: NotRequired[str]
    isEasyApply: bool
    isUrgent: bool
    source: NotRequired[str]
    description: NotRequired[str]
    descriptionHtml: NotRequired[str]
    isExpired: bool
    language: NotRequired[str]


class IndeedJobResponseData(TypedDict):
    job: IndeedJobResponseDataJob


class IndeedJobResponse(TypedDict):
    success: Literal[True]
    data: IndeedJobResponseData
    creditsUsed: int
    requestId: str


class TripadvisorSearchResponseDataResultsItemLocation(TypedDict):
    lat: float
    lng: float


class TripadvisorSearchResponseDataResultsItem(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    parent: NotRequired[str]
    location: NotRequired[TripadvisorSearchResponseDataResultsItemLocation]
    image: NotRequired[str]


class TripadvisorSearchResponseData(TypedDict):
    results: list[TripadvisorSearchResponseDataResultsItem]


class TripadvisorSearchResponse(TypedDict):
    success: Literal[True]
    data: TripadvisorSearchResponseData
    creditsUsed: int
    requestId: str


class TripadvisorPlaceResponseDataPlaceRanking(TypedDict):
    text: NotRequired[str]
    position: NotRequired[int]
    of: NotRequired[int]
    geo: NotRequired[str]


class TripadvisorPlaceResponseDataPlaceHoursItem(TypedDict):
    days: NotRequired[str]
    times: NotRequired[list[str]]


class TripadvisorPlaceResponseDataPlace(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    subtypes: NotRequired[list[str]]
    url: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    ranking: NotRequired[TripadvisorPlaceResponseDataPlaceRanking]
    priceLevel: NotRequired[str]
    priceRangeText: NotRequired[str]
    hotelClass: NotRequired[float]
    description: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    location: NotRequired[TripadvisorSearchResponseDataResultsItemLocation]
    phone: NotRequired[str]
    website: NotRequired[str]
    email: NotRequired[str]
    neighborhoods: NotRequired[list[str]]
    parents: NotRequired[list[ZillowPropertyResponseDataPropertyMls]]
    cuisines: NotRequired[list[str]]
    hours: NotRequired[list[TripadvisorPlaceResponseDataPlaceHoursItem]]
    tags: NotRequired[list[str]]
    image: NotRequired[str]
    timezone: NotRequired[str]
    isClosed: bool


class TripadvisorPlaceResponseData(TypedDict):
    place: TripadvisorPlaceResponseDataPlace


class TripadvisorPlaceResponse(TypedDict):
    success: Literal[True]
    data: TripadvisorPlaceResponseData
    creditsUsed: int
    requestId: str


class TripadvisorReviewsResponseDataPlace(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


class TripadvisorReviewsResponseDataReviewsItemSubRatingsItem(TypedDict):
    name: NotRequired[str]
    rating: float


class TripadvisorReviewsResponseDataReviewsItemAuthor(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: NotRequired[bool]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    contributions: NotRequired[int]


class TripadvisorReviewsResponseDataReviewsItemOwnerReply(TypedDict):
    text: NotRequired[str]
    publishedDate: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]


class TripadvisorReviewsResponseDataReviewsItem(TypedDict):
    id: NotRequired[str]
    url: NotRequired[str]
    rating: NotRequired[float]
    title: NotRequired[str]
    text: NotRequired[str]
    language: NotRequired[str]
    createdDate: NotRequired[str]
    publishedDate: NotRequired[str]
    stayDate: NotRequired[str]
    tripType: NotRequired[str]
    helpful: int
    subRatings: NotRequired[list[TripadvisorReviewsResponseDataReviewsItemSubRatingsItem]]
    author: NotRequired[TripadvisorReviewsResponseDataReviewsItemAuthor]
    ownerReply: NotRequired[TripadvisorReviewsResponseDataReviewsItemOwnerReply]


class TripadvisorReviewsResponseData(TypedDict):
    place: NotRequired[TripadvisorReviewsResponseDataPlace]
    total: NotRequired[int]
    reviews: list[TripadvisorReviewsResponseDataReviewsItem]
    cursor: NotRequired[str]


class TripadvisorReviewsResponse(TypedDict):
    success: Literal[True]
    data: TripadvisorReviewsResponseData
    creditsUsed: int
    requestId: str


class GoogletravelFlightsResponseDataFlightsItemLegsItemOrigin(TypedDict):
    code: NotRequired[str]
    name: NotRequired[str]


class GoogletravelFlightsResponseDataFlightsItemLegsItem(TypedDict):
    flightNumber: NotRequired[str]
    airline: NotRequired[str]
    origin: NotRequired[GoogletravelFlightsResponseDataFlightsItemLegsItemOrigin]
    destination: NotRequired[GoogletravelFlightsResponseDataFlightsItemLegsItemOrigin]
    departureLocalTime: NotRequired[str]
    arrivalLocalTime: NotRequired[str]
    durationSeconds: NotRequired[int]
    aircraft: NotRequired[str]
    legroom: NotRequired[str]


class GoogletravelFlightsResponseDataFlightsItemLayoversItem(TypedDict):
    airport: NotRequired[str]
    name: NotRequired[str]
    city: NotRequired[str]
    durationSeconds: NotRequired[int]


class GoogletravelFlightsResponseDataFlightsItem(TypedDict):
    isBest: bool
    price: NotRequired[float]
    airlines: NotRequired[list[str]]
    stops: int
    durationSeconds: NotRequired[int]
    departureLocalTime: NotRequired[str]
    arrivalLocalTime: NotRequired[str]
    legs: NotRequired[list[GoogletravelFlightsResponseDataFlightsItemLegsItem]]
    layovers: NotRequired[list[GoogletravelFlightsResponseDataFlightsItemLayoversItem]]
    emissionsGrams: NotRequired[int]
    typicalEmissionsGrams: NotRequired[int]


class GoogletravelFlightsResponseData(TypedDict):
    url: str
    currency: NotRequired[str]
    flights: list[GoogletravelFlightsResponseDataFlightsItem]


class GoogletravelFlightsResponse(TypedDict):
    success: Literal[True]
    data: GoogletravelFlightsResponseData
    creditsUsed: int
    requestId: str


class AmazonSearchResponseDataProductsItem(TypedDict):
    position: int
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    image: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    boughtPastMonth: NotRequired[int]
    isSponsored: bool


class AmazonSearchResponseData(TypedDict):
    products: list[AmazonSearchResponseDataProductsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AmazonSearchResponse(TypedDict):
    success: Literal[True]
    data: AmazonSearchResponseData
    creditsUsed: int
    requestId: str


class AmazonProductResponseDataProductVariantsItem(TypedDict):
    id: NotRequired[str]
    attributes: NotRequired[dict[str, str]]


class AmazonProductResponseDataProductSeller(TypedDict):
    name: NotRequired[str]
    id: NotRequired[str]
    shipsFrom: NotRequired[str]


class AmazonProductResponseDataProductBestSellersRankItem(TypedDict):
    rank: int
    category: NotRequired[str]


class AmazonProductResponseDataProductTopReviewsItem(TypedDict):
    id: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    rating: NotRequired[float]
    title: NotRequired[str]
    text: NotRequired[str]
    createdAt: NotRequired[str]
    isVerified: bool
    variant: NotRequired[str]
    helpful: NotRequired[int]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]


class AmazonProductResponseDataProduct(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    brand: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    availability: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    bullets: NotRequired[list[str]]
    description: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    variants: NotRequired[list[AmazonProductResponseDataProductVariantsItem]]
    seller: NotRequired[AmazonProductResponseDataProductSeller]
    categories: NotRequired[list[str]]
    bestSellersRank: NotRequired[list[AmazonProductResponseDataProductBestSellersRankItem]]
    specs: NotRequired[dict[str, str]]
    topReviews: NotRequired[list[AmazonProductResponseDataProductTopReviewsItem]]


class AmazonProductResponseData(TypedDict):
    product: AmazonProductResponseDataProduct


class AmazonProductResponse(TypedDict):
    success: Literal[True]
    data: AmazonProductResponseData
    creditsUsed: int
    requestId: str


class AmazonBestsellersResponseDataProductsItem(TypedDict):
    rank: int
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    image: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]


class AmazonBestsellersResponseData(TypedDict):
    category: NotRequired[str]
    products: list[AmazonBestsellersResponseDataProductsItem]
    cursor: NotRequired[str]


class AmazonBestsellersResponse(TypedDict):
    success: Literal[True]
    data: AmazonBestsellersResponseData
    creditsUsed: int
    requestId: str


class ShopifyProductsResponseDataProductsItemOptionsItem(TypedDict):
    name: NotRequired[str]
    values: NotRequired[list[str]]


class ShopifyProductsResponseDataProductsItemVariantsItem(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str]
    sku: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    isAvailable: bool
    options: NotRequired[list[str]]
    weightGrams: NotRequired[float]


class ShopifyProductsResponseDataProductsItem(TypedDict):
    id: NotRequired[str]
    slug: NotRequired[str]
    url: str
    title: NotRequired[str]
    vendor: NotRequired[str]
    productType: NotRequired[str]
    tags: NotRequired[list[str]]
    description: NotRequired[str]
    price: NotRequired[float]
    maxPrice: NotRequired[float]
    originalPrice: NotRequired[float]
    isAvailable: bool
    options: NotRequired[list[ShopifyProductsResponseDataProductsItemOptionsItem]]
    variants: NotRequired[list[ShopifyProductsResponseDataProductsItemVariantsItem]]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    publishedAt: NotRequired[str]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]


class ShopifyProductsResponseData(TypedDict):
    products: list[ShopifyProductsResponseDataProductsItem]
    cursor: NotRequired[str]


class ShopifyProductsResponse(TypedDict):
    success: Literal[True]
    data: ShopifyProductsResponseData
    creditsUsed: int
    requestId: str


class ShopifyCollectionsResponseDataCollectionsItem(TypedDict):
    id: NotRequired[str]
    slug: NotRequired[str]
    url: str
    title: NotRequired[str]
    description: NotRequired[str]
    image: NotRequired[str]
    products: NotRequired[int]
    publishedAt: NotRequired[str]
    updatedAt: NotRequired[str]


class ShopifyCollectionsResponseData(TypedDict):
    collections: list[ShopifyCollectionsResponseDataCollectionsItem]
    cursor: NotRequired[str]


class ShopifyCollectionsResponse(TypedDict):
    success: Literal[True]
    data: ShopifyCollectionsResponseData
    creditsUsed: int
    requestId: str


class ShopifyStoreResponseDataStore(TypedDict):
    id: NotRequired[str]
    url: str
    isShopify: bool
    name: NotRequired[str]
    description: NotRequired[str]
    myshopifyDomain: NotRequired[str]
    domain: NotRequired[str]
    currency: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    shipsTo: NotRequired[list[str]]
    products: NotRequired[int]
    collections: NotRequired[int]


class ShopifyStoreResponseData(TypedDict):
    store: ShopifyStoreResponseDataStore


class ShopifyStoreResponse(TypedDict):
    success: Literal[True]
    data: ShopifyStoreResponseData
    creditsUsed: int
    requestId: str


class WalmartSearchResponseDataProductsItem(TypedDict):
    position: int
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    image: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    seller: NotRequired[ZillowSearchResponseDataListingsItemBroker]
    availability: NotRequired[str]
    isSponsored: bool


class WalmartSearchResponseData(TypedDict):
    products: list[WalmartSearchResponseDataProductsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class WalmartSearchResponse(TypedDict):
    success: Literal[True]
    data: WalmartSearchResponseData
    creditsUsed: int
    requestId: str


class WalmartProductResponseDataProductTopReviewsItem(TypedDict):
    id: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    rating: NotRequired[float]
    title: NotRequired[str]
    text: NotRequired[str]
    createdAt: NotRequired[str]
    helpful: NotRequired[int]


class WalmartProductResponseDataProduct(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    brand: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    availability: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    seller: NotRequired[ZillowPropertyResponseDataPropertyMls]
    categories: NotRequired[list[str]]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    description: NotRequired[str]
    highlights: NotRequired[str]
    specs: NotRequired[dict[str, str]]
    variants: NotRequired[list[ShopifyProductsResponseDataProductsItemOptionsItem]]
    upc: NotRequired[str]
    model: NotRequired[str]
    topReviews: NotRequired[list[WalmartProductResponseDataProductTopReviewsItem]]


class WalmartProductResponseData(TypedDict):
    product: WalmartProductResponseDataProduct


class WalmartProductResponse(TypedDict):
    success: Literal[True]
    data: WalmartProductResponseData
    creditsUsed: int
    requestId: str


class AliexpressSearchResponseDataProductsItem(TypedDict):
    position: int
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    image: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    rating: NotRequired[float]
    sold: NotRequired[int]
    isSponsored: bool


class AliexpressSearchResponseData(TypedDict):
    products: list[AliexpressSearchResponseDataProductsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AliexpressSearchResponse(TypedDict):
    success: Literal[True]
    data: AliexpressSearchResponseData
    creditsUsed: int
    requestId: str


class AliexpressProductResponseDataProductStore(TypedDict):
    name: NotRequired[str]
    id: NotRequired[str]
    sellerId: NotRequired[str]
    positivePercent: NotRequired[float]


class AliexpressProductResponseDataProductSkusItem(TypedDict):
    id: NotRequired[str]
    attributes: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    stock: NotRequired[int]
    isAvailable: bool


class AliexpressProductResponseDataProduct(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    sold: NotRequired[int]
    store: NotRequired[AliexpressProductResponseDataProductStore]
    options: NotRequired[list[ShopifyProductsResponseDataProductsItemOptionsItem]]
    skus: NotRequired[list[AliexpressProductResponseDataProductSkusItem]]
    specs: NotRequired[dict[str, str]]
    categoryId: NotRequired[str]


class AliexpressProductResponseData(TypedDict):
    product: AliexpressProductResponseDataProduct


class AliexpressProductResponse(TypedDict):
    success: Literal[True]
    data: AliexpressProductResponseData
    creditsUsed: int
    requestId: str


class AppstoreAppResponseDataAppDeveloper(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]


class AppstoreAppResponseDataAppHistogram(TypedDict):
    one: int
    two: int
    three: int
    four: int
    five: int


class AppstoreAppResponseDataAppChart(TypedDict):
    name: NotRequired[str]
    genre: NotRequired[str]
    position: int


class AppstoreAppResponseDataApp(TypedDict):
    id: NotRequired[str]
    bundleId: NotRequired[str]
    name: NotRequired[str]
    subtitle: NotRequired[str]
    url: str
    developer: NotRequired[AppstoreAppResponseDataAppDeveloper]
    seller: NotRequired[str]
    website: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    priceText: NotRequired[str]
    hasInAppPurchases: NotRequired[bool]
    genres: NotRequired[list[str]]
    primaryGenre: NotRequired[ZillowPropertyResponseDataPropertyMls]
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
    histogram: NotRequired[AppstoreAppResponseDataAppHistogram]
    chart: NotRequired[AppstoreAppResponseDataAppChart]
    icon: NotRequired[str]
    screenshots: NotRequired[list[str]]
    ipadScreenshots: NotRequired[list[str]]


class AppstoreAppResponseData(TypedDict):
    app: AppstoreAppResponseDataApp


class AppstoreAppResponse(TypedDict):
    success: Literal[True]
    data: AppstoreAppResponseData
    creditsUsed: int
    requestId: str


class AppstoreSearchResponseDataAppsItem(TypedDict):
    id: NotRequired[str]
    bundleId: NotRequired[str]
    name: NotRequired[str]
    url: str
    developer: NotRequired[AppstoreAppResponseDataAppDeveloper]
    seller: NotRequired[str]
    website: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    priceText: NotRequired[str]
    genres: NotRequired[list[str]]
    primaryGenre: NotRequired[ZillowPropertyResponseDataPropertyMls]
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
    icon: NotRequired[str]
    screenshots: NotRequired[list[str]]
    ipadScreenshots: NotRequired[list[str]]


class AppstoreSearchResponseData(TypedDict):
    apps: list[AppstoreSearchResponseDataAppsItem]


class AppstoreSearchResponse(TypedDict):
    success: Literal[True]
    data: AppstoreSearchResponseData
    creditsUsed: int
    requestId: str


class AppstoreReviewsResponseDataReviewsItem(TypedDict):
    id: NotRequired[str]
    rating: int
    title: NotRequired[str]
    text: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    createdAt: NotRequired[str]
    isEdited: bool


class AppstoreReviewsResponseData(TypedDict):
    reviews: list[AppstoreReviewsResponseDataReviewsItem]
    cursor: NotRequired[str]


class AppstoreReviewsResponse(TypedDict):
    success: Literal[True]
    data: AppstoreReviewsResponseData
    creditsUsed: int
    requestId: str


class AppstoreTopResponseDataAppsItem(TypedDict):
    rank: int
    id: NotRequired[str]
    bundleId: NotRequired[str]
    name: NotRequired[str]
    url: str
    developer: NotRequired[AppstoreAppResponseDataAppDeveloper]
    price: NotRequired[float]
    currency: NotRequired[str]
    genre: NotRequired[ZillowPropertyResponseDataPropertyMls]
    releasedAt: NotRequired[str]
    summary: NotRequired[str]
    icon: NotRequired[str]


class AppstoreTopResponseData(TypedDict):
    apps: list[AppstoreTopResponseDataAppsItem]


class AppstoreTopResponse(TypedDict):
    success: Literal[True]
    data: AppstoreTopResponseData
    creditsUsed: int
    requestId: str


class GoogleplayAppResponseDataAppDeveloper(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    email: NotRequired[str]
    website: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]


class GoogleplayAppResponseDataAppInstalls(TypedDict):
    text: NotRequired[str]
    min: NotRequired[int]
    exact: NotRequired[int]


class GoogleplayAppResponseDataApp(TypedDict):
    id: NotRequired[str]
    url: str
    name: NotRequired[str]
    summary: NotRequired[str]
    description: NotRequired[str]
    developer: NotRequired[GoogleplayAppResponseDataAppDeveloper]
    privacyPolicy: NotRequired[str]
    genre: NotRequired[ZillowPropertyResponseDataPropertyMls]
    contentRating: NotRequired[str]
    installs: NotRequired[GoogleplayAppResponseDataAppInstalls]
    rating: NotRequired[float]
    ratings: NotRequired[int]
    reviews: NotRequired[int]
    histogram: NotRequired[AppstoreAppResponseDataAppHistogram]
    price: NotRequired[float]
    currency: NotRequired[str]
    hasInAppPurchases: bool
    inAppPriceText: NotRequired[str]
    hasAds: bool
    version: NotRequired[str]
    recentChanges: NotRequired[str]
    releasedAt: NotRequired[str]
    updatedAt: NotRequired[str]
    icon: NotRequired[str]
    banner: NotRequired[str]
    screenshots: NotRequired[list[str]]


class GoogleplayAppResponseData(TypedDict):
    app: GoogleplayAppResponseDataApp


class GoogleplayAppResponse(TypedDict):
    success: Literal[True]
    data: GoogleplayAppResponseData
    creditsUsed: int
    requestId: str


class GoogleplaySearchResponseDataAppsItemInstalls(TypedDict):
    text: NotRequired[str]
    min: NotRequired[int]


class GoogleplaySearchResponseDataAppsItem(TypedDict):
    id: NotRequired[str]
    url: str
    name: NotRequired[str]
    developer: NotRequired[ZillowSearchResponseDataListingsItemBroker]
    summary: NotRequired[str]
    genre: NotRequired[ZillowSearchResponseDataListingsItemBroker]
    installs: NotRequired[GoogleplaySearchResponseDataAppsItemInstalls]
    rating: NotRequired[float]
    price: NotRequired[float]
    currency: NotRequired[str]
    icon: NotRequired[str]


class GoogleplaySearchResponseData(TypedDict):
    apps: list[GoogleplaySearchResponseDataAppsItem]


class GoogleplaySearchResponse(TypedDict):
    success: Literal[True]
    data: GoogleplaySearchResponseData
    creditsUsed: int
    requestId: str


class GoogleplayReviewsResponseDataReviewsItem(TypedDict):
    id: NotRequired[str]
    url: str
    rating: int
    text: NotRequired[str]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    createdAt: NotRequired[str]
    likes: int
    appVersion: NotRequired[str]
    ownerReply: NotRequired[MapsReviewsResponseDataReviewsItemOwnerReply]


class GoogleplayReviewsResponseData(TypedDict):
    reviews: list[GoogleplayReviewsResponseDataReviewsItem]
    cursor: NotRequired[str]


class GoogleplayReviewsResponse(TypedDict):
    success: Literal[True]
    data: GoogleplayReviewsResponseData
    creditsUsed: int
    requestId: str


class AirbnbSearchBedrooms(TypedDict):
    min: int


class AirbnbSearchBathrooms(TypedDict):
    min: float


class AirbnbSearchResponseDataListingsItem(TypedDict):
    id: NotRequired[str]
    url: str
    name: NotRequired[str]
    title: NotRequired[str]
    subtitle: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    priceText: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    bedrooms: NotRequired[float]
    beds: NotRequired[float]
    bathrooms: NotRequired[float]
    location: NotRequired[TripadvisorSearchResponseDataResultsItemLocation]
    badges: NotRequired[list[str]]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]


class AirbnbSearchResponseData(TypedDict):
    listings: list[AirbnbSearchResponseDataListingsItem]
    cursor: NotRequired[str]


class AirbnbSearchResponse(TypedDict):
    success: Literal[True]
    data: AirbnbSearchResponseData
    creditsUsed: int
    requestId: str


class AirbnbListingResponseDataListingHost(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    isSuperhost: bool
    isVerified: bool
    rating: NotRequired[float]
    reviews: NotRequired[int]
    yearsHosting: NotRequired[int]
    bio: NotRequired[str]
    responsePercent: NotRequired[float]
    responseTime: NotRequired[str]
    highlights: NotRequired[list[str]]
    avatar: NotRequired[str]


class AirbnbListingResponseDataListingAmenitiesItem(TypedDict):
    group: NotRequired[str]
    name: NotRequired[str]
    isAvailable: bool


class AirbnbListingResponseDataListing(TypedDict):
    id: NotRequired[str]
    url: str
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
    ratingCategories: NotRequired[dict[str, float]]
    ratingDistribution: NotRequired[dict[str, float]]
    host: AirbnbListingResponseDataListingHost
    highlights: NotRequired[list[RedditSearchResponseDataResultsItemOption1RulesItem]]
    amenities: NotRequired[list[AirbnbListingResponseDataListingAmenitiesItem]]
    houseRules: NotRequired[list[str]]
    safety: NotRequired[list[str]]
    location: NotRequired[TripadvisorSearchResponseDataResultsItemLocation]
    isLocationExact: bool
    area: NotRequired[str]
    neighborhood: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]


class AirbnbListingResponseData(TypedDict):
    listing: AirbnbListingResponseDataListing


class AirbnbListingResponse(TypedDict):
    success: Literal[True]
    data: AirbnbListingResponseData
    creditsUsed: int
    requestId: str


class AirbnbCalendarResponseDataDaysItem(TypedDict):
    date: str
    isAvailable: bool
    isBookable: bool
    isCheckInDay: bool
    isCheckOutDay: bool
    minNights: NotRequired[int]
    maxNights: NotRequired[int]
    priceText: NotRequired[str]


class AirbnbCalendarResponseData(TypedDict):
    days: list[AirbnbCalendarResponseDataDaysItem]


class AirbnbCalendarResponse(TypedDict):
    success: Literal[True]
    data: AirbnbCalendarResponseData
    creditsUsed: int
    requestId: str


class AirbnbReviewsResponseDataReviewsItemAuthor(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: NotRequired[bool]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]


class AirbnbReviewsResponseDataReviewsItemOwnerReply(TypedDict):
    text: NotRequired[str]


class AirbnbReviewsResponseDataReviewsItem(TypedDict):
    id: NotRequired[str]
    text: NotRequired[str]
    rating: NotRequired[float]
    createdAt: NotRequired[str]
    language: NotRequired[str]
    stayLength: NotRequired[str]
    author: NotRequired[AirbnbReviewsResponseDataReviewsItemAuthor]
    ownerReply: NotRequired[AirbnbReviewsResponseDataReviewsItemOwnerReply]


class AirbnbReviewsResponseData(TypedDict):
    reviews: list[AirbnbReviewsResponseDataReviewsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class AirbnbReviewsResponse(TypedDict):
    success: Literal[True]
    data: AirbnbReviewsResponseData
    creditsUsed: int
    requestId: str


class RedfinSearchBathrooms(TypedDict):
    min: float


class RedfinSearchResponseDataListingsItemAddress(TypedDict):
    full: NotRequired[str]
    street: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postalCode: NotRequired[str]
    country: NotRequired[str]
    unit: NotRequired[str]


class RedfinSearchResponseDataListingsItem(TypedDict):
    id: NotRequired[str]
    listingId: NotRequired[str]
    url: str
    status: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    bedrooms: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    lotSqft: NotRequired[float]
    pricePerSqft: NotRequired[float]
    yearBuilt: NotRequired[int]
    hoa: NotRequired[float]
    daysOnMarket: NotRequired[int]
    lastSoldAt: NotRequired[str]
    homeType: NotRequired[str]
    mlsId: NotRequired[str]
    neighborhood: NotRequired[str]
    address: NotRequired[RedfinSearchResponseDataListingsItemAddress]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    remarks: NotRequired[str]
    tags: NotRequired[list[str]]


class RedfinSearchResponseDataMedian(TypedDict):
    price: NotRequired[float]
    sqft: NotRequired[float]
    pricePerSqft: NotRequired[float]
    daysOnMarket: NotRequired[float]


class RedfinSearchResponseData(TypedDict):
    listings: list[RedfinSearchResponseDataListingsItem]
    median: NotRequired[RedfinSearchResponseDataMedian]
    cursor: NotRequired[str]


class RedfinSearchResponse(TypedDict):
    success: Literal[True]
    data: RedfinSearchResponseData
    creditsUsed: int
    requestId: str


class RedfinPropertyResponseDataPropertyPriceHistoryItem(TypedDict):
    date: str
    event: NotRequired[str]
    price: NotRequired[float]
    source: NotRequired[str]
    mlsId: NotRequired[str]


class RedfinPropertyResponseDataPropertyTaxHistoryItem(TypedDict):
    year: int
    landValue: NotRequired[float]
    improvementValue: NotRequired[float]
    taxes: NotRequired[float]


class RedfinPropertyResponseDataPropertyFactsItem(TypedDict):
    group: NotRequired[str]
    name: NotRequired[str]
    values: NotRequired[list[str]]


class RedfinPropertyResponseDataPropertySchoolsItem(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    grades: NotRequired[str]
    rating: NotRequired[float]
    parentRating: NotRequired[float]
    distanceMiles: NotRequired[float]
    students: NotRequired[int]
    isServingHome: bool
    district: NotRequired[str]
    url: str


class RedfinPropertyResponseDataPropertyComparablesItem(TypedDict):
    id: NotRequired[str]
    url: str
    status: NotRequired[str]
    price: NotRequired[float]
    bedrooms: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    lastSoldAt: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]


class RedfinPropertyResponseDataProperty(TypedDict):
    id: NotRequired[str]
    url: str
    status: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    priceText: NotRequired[str]
    estimate: NotRequired[float]
    lastSoldPrice: NotRequired[float]
    lastSoldAt: NotRequired[str]
    bedrooms: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    lotSqft: NotRequired[float]
    yearBuilt: NotRequired[int]
    stories: NotRequired[float]
    propertyType: NotRequired[str]
    apn: NotRequired[str]
    county: NotRequired[str]
    description: NotRequired[str]
    address: NotRequired[RedfinSearchResponseDataListingsItemAddress]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    priceHistory: NotRequired[list[RedfinPropertyResponseDataPropertyPriceHistoryItem]]
    taxHistory: NotRequired[list[RedfinPropertyResponseDataPropertyTaxHistoryItem]]
    facts: NotRequired[list[RedfinPropertyResponseDataPropertyFactsItem]]
    schools: NotRequired[list[RedfinPropertyResponseDataPropertySchoolsItem]]
    comparables: NotRequired[list[RedfinPropertyResponseDataPropertyComparablesItem]]


class RedfinPropertyResponseData(TypedDict):
    property: RedfinPropertyResponseDataProperty


class RedfinPropertyResponse(TypedDict):
    success: Literal[True]
    data: RedfinPropertyResponseData
    creditsUsed: int
    requestId: str


class RealtorSearchResponseDataListingsItemPriceRange(TypedDict):
    min: NotRequired[float]
    max: NotRequired[float]


class RealtorSearchResponseDataListingsItemFlags(TypedDict):
    isPending: bool
    isContingent: bool
    isNewConstruction: bool
    isForeclosure: bool


class RealtorSearchResponseDataListingsItemAddress(TypedDict):
    full: NotRequired[str]
    street: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postalCode: NotRequired[str]
    country: NotRequired[str]
    unit: NotRequired[str]
    county: NotRequired[str]


class RealtorSearchResponseDataListingsItem(TypedDict):
    id: NotRequired[str]
    listingId: NotRequired[str]
    url: NotRequired[str]
    status: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    priceRange: NotRequired[RealtorSearchResponseDataListingsItemPriceRange]
    bedrooms: NotRequired[float]
    bedroomsMax: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    lotSqft: NotRequired[float]
    yearBuilt: NotRequired[int]
    homeType: NotRequired[str]
    pricePerSqft: NotRequired[float]
    hoa: NotRequired[float]
    createdAt: NotRequired[str]
    lastSoldPrice: NotRequired[float]
    lastSoldAt: NotRequired[str]
    flags: RealtorSearchResponseDataListingsItemFlags
    address: NotRequired[RealtorSearchResponseDataListingsItemAddress]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    image: NotRequired[str]
    totalImages: NotRequired[int]
    broker: NotRequired[ZillowSearchResponseDataListingsItemBroker]
    tags: NotRequired[list[str]]


class RealtorSearchResponseData(TypedDict):
    listings: list[RealtorSearchResponseDataListingsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class RealtorSearchResponse(TypedDict):
    success: Literal[True]
    data: RealtorSearchResponseData
    creditsUsed: int
    requestId: str


class RealtorPropertyResponseDataPropertyMls(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    listingId: NotRequired[str]


class RealtorPropertyResponseDataPropertyDetailsItem(TypedDict):
    category: NotRequired[str]
    items: NotRequired[list[str]]


class RealtorPropertyResponseDataPropertyEstimatesItem(TypedDict):
    source: NotRequired[str]
    estimate: NotRequired[float]
    low: NotRequired[float]
    high: NotRequired[float]
    date: NotRequired[str]


class RealtorPropertyResponseDataPropertyPriceHistoryItem(TypedDict):
    date: str
    event: NotRequired[str]
    price: NotRequired[float]
    source: NotRequired[str]


class RealtorPropertyResponseDataPropertyTaxHistoryItem(TypedDict):
    year: int
    tax: NotRequired[float]
    assessedTotal: NotRequired[float]
    assessedLand: NotRequired[float]
    assessedBuilding: NotRequired[float]


class RealtorPropertyResponseDataPropertySchoolsItem(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    rating: NotRequired[float]
    parentRating: NotRequired[float]
    distanceMiles: NotRequired[float]
    levels: NotRequired[list[str]]
    grades: NotRequired[list[str]]
    funding: NotRequired[str]
    students: NotRequired[int]
    district: NotRequired[str]


class RealtorPropertyResponseDataPropertyAgentsItem(TypedDict):
    name: NotRequired[str]
    type: NotRequired[str]
    email: NotRequired[str]
    phones: NotRequired[list[str]]
    office: NotRequired[str]


class RealtorPropertyResponseDataProperty(TypedDict):
    id: NotRequired[str]
    listingId: NotRequired[str]
    url: NotRequired[str]
    status: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    priceRange: NotRequired[RealtorSearchResponseDataListingsItemPriceRange]
    bedrooms: NotRequired[float]
    bedroomsMax: NotRequired[float]
    bathrooms: NotRequired[float]
    sqft: NotRequired[float]
    lotSqft: NotRequired[float]
    yearBuilt: NotRequired[int]
    homeType: NotRequired[str]
    pricePerSqft: NotRequired[float]
    hoa: NotRequired[float]
    createdAt: NotRequired[str]
    lastSoldPrice: NotRequired[float]
    lastSoldAt: NotRequired[str]
    flags: RealtorSearchResponseDataListingsItemFlags
    address: NotRequired[RealtorSearchResponseDataListingsItemAddress]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    image: NotRequired[str]
    totalImages: NotRequired[int]
    broker: NotRequired[ZillowSearchResponseDataListingsItemBroker]
    tags: NotRequired[list[str]]
    description: NotRequired[str]
    stories: NotRequired[float]
    garage: NotRequired[float]
    daysOnMarket: NotRequired[int]
    mls: NotRequired[RealtorPropertyResponseDataPropertyMls]
    neighborhoods: NotRequired[list[str]]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    details: NotRequired[list[RealtorPropertyResponseDataPropertyDetailsItem]]
    estimates: NotRequired[list[RealtorPropertyResponseDataPropertyEstimatesItem]]
    priceHistory: NotRequired[list[RealtorPropertyResponseDataPropertyPriceHistoryItem]]
    taxHistory: NotRequired[list[RealtorPropertyResponseDataPropertyTaxHistoryItem]]
    schools: NotRequired[list[RealtorPropertyResponseDataPropertySchoolsItem]]
    agents: NotRequired[list[RealtorPropertyResponseDataPropertyAgentsItem]]


class RealtorPropertyResponseData(TypedDict):
    property: RealtorPropertyResponseDataProperty


class RealtorPropertyResponse(TypedDict):
    success: Literal[True]
    data: RealtorPropertyResponseData
    creditsUsed: int
    requestId: str


class RightmoveSearchResponseDataListingsItemTenure(TypedDict):
    type: NotRequired[str]
    yearsRemaining: NotRequired[float]


class RightmoveSearchResponseDataListingsItemAgent(TypedDict):
    name: NotRequired[str]
    branchId: NotRequired[str]
    phone: NotRequired[str]


class RightmoveSearchResponseDataListingsItem(TypedDict):
    id: NotRequired[str]
    url: str
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    summary: NotRequired[str]
    price: NotRequired[float]
    priceText: NotRequired[str]
    priceQualifier: NotRequired[str]
    frequency: NotRequired[str]
    currency: NotRequired[str]
    bedrooms: NotRequired[int]
    bathrooms: NotRequired[int]
    propertyType: NotRequired[str]
    sizeText: NotRequired[str]
    tenure: NotRequired[RightmoveSearchResponseDataListingsItemTenure]
    firstListedAt: NotRequired[str]
    updateReason: NotRequired[str]
    updatedAt: NotRequired[str]
    isFeatured: bool
    isAuction: bool
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    agent: NotRequired[RightmoveSearchResponseDataListingsItemAgent]
    keyFeatures: NotRequired[list[str]]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]


class RightmoveSearchResponseData(TypedDict):
    listings: list[RightmoveSearchResponseDataListingsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class RightmoveSearchResponse(TypedDict):
    success: Literal[True]
    data: RightmoveSearchResponseData
    creditsUsed: int
    requestId: str


class RightmovePropertyResponseDataPropertyImagesItem(TypedDict):
    url: str
    caption: NotRequired[str]


class RightmovePropertyResponseDataPropertyNearestStationsItem(TypedDict):
    name: NotRequired[str]
    types: NotRequired[list[str]]
    distanceMiles: NotRequired[float]


class RightmovePropertyResponseDataPropertyAgent(TypedDict):
    name: NotRequired[str]
    branchId: NotRequired[str]
    phone: NotRequired[str]
    company: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]


class RightmovePropertyResponseDataProperty(TypedDict):
    id: NotRequired[str]
    url: str
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    description: NotRequired[str]
    price: NotRequired[float]
    currency: NotRequired[str]
    priceText: NotRequired[str]
    priceQualifier: NotRequired[str]
    pricePerSqft: NotRequired[float]
    channel: NotRequired[str]
    bedrooms: NotRequired[int]
    bathrooms: NotRequired[int]
    propertyType: NotRequired[str]
    tenure: NotRequired[RightmoveSearchResponseDataListingsItemTenure]
    sizes: NotRequired[list[ZillowPropertyResponseDataPropertyLotSize]]
    councilTaxBand: NotRequired[str]
    annualServiceCharge: NotRequired[float]
    annualGroundRent: NotRequired[float]
    updateReason: NotRequired[str]
    tags: NotRequired[list[str]]
    keyFeatures: NotRequired[list[str]]
    images: NotRequired[list[RightmovePropertyResponseDataPropertyImagesItem]]
    floorplans: NotRequired[list[str]]
    location: NotRequired[MapsSearchResponseDataPlacesItemLocation]
    nearestStations: NotRequired[list[RightmovePropertyResponseDataPropertyNearestStationsItem]]
    agent: NotRequired[RightmovePropertyResponseDataPropertyAgent]


class RightmovePropertyResponseData(TypedDict):
    property: RightmovePropertyResponseDataProperty


class RightmovePropertyResponse(TypedDict):
    success: Literal[True]
    data: RightmovePropertyResponseData
    creditsUsed: int
    requestId: str


class ImmoscoutSearchResponseDataListingsItem(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    type: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    price: NotRequired[float]
    currency: NotRequired[str]
    priceText: NotRequired[str]
    livingSpace: NotRequired[float]
    rooms: NotRequired[float]
    energyClass: NotRequired[str]
    createdAt: NotRequired[str]
    isPrivate: bool
    isProject: bool
    isNew: bool
    image: NotRequired[str]


class ImmoscoutSearchResponseData(TypedDict):
    listings: list[ImmoscoutSearchResponseDataListingsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class ImmoscoutSearchResponse(TypedDict):
    success: Literal[True]
    data: ImmoscoutSearchResponseData
    creditsUsed: int
    requestId: str


class ImmoscoutListingResponseDataListingAddress(TypedDict):
    full: NotRequired[str]
    street: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postalCode: NotRequired[str]
    country: NotRequired[str]
    district: NotRequired[str]


class ImmoscoutListingResponseDataListingAttributesItem(TypedDict):
    group: NotRequired[str]
    label: NotRequired[str]
    value: NotRequired[str]


class ImmoscoutListingResponseDataListingTextsItem(TypedDict):
    title: NotRequired[str]
    text: NotRequired[str]


class ImmoscoutListingResponseDataListingAgent(TypedDict):
    name: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    rating: NotRequired[float]
    url: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]


class ImmoscoutListingResponseDataListing(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    type: NotRequired[str]
    status: NotRequired[str]
    address: NotRequired[ImmoscoutListingResponseDataListingAddress]
    currency: NotRequired[str]
    baseRent: NotRequired[float]
    totalRent: NotRequired[float]
    serviceCharge: NotRequired[float]
    price: NotRequired[float]
    livingSpace: NotRequired[float]
    rooms: NotRequired[float]
    yearBuilt: NotRequired[int]
    energyClass: NotRequired[str]
    attributes: NotRequired[list[ImmoscoutListingResponseDataListingAttributesItem]]
    texts: NotRequired[list[ImmoscoutListingResponseDataListingTextsItem]]
    images: NotRequired[list[RightmovePropertyResponseDataPropertyImagesItem]]
    agent: NotRequired[ImmoscoutListingResponseDataListingAgent]


class ImmoscoutListingResponseData(TypedDict):
    listing: ImmoscoutListingResponseDataListing


class ImmoscoutListingResponse(TypedDict):
    success: Literal[True]
    data: ImmoscoutListingResponseData
    creditsUsed: int
    requestId: str


class PinterestSearchResponseDataPinsItemVideo(TypedDict):
    url: str
    durationSeconds: NotRequired[float]


class PinterestSearchResponseDataPinsItemAuthor(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: NotRequired[bool]
    followers: NotRequired[int]


class PinterestSearchResponseDataPinsItemBoard(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    url: str


class PinterestSearchResponseDataPinsItem(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    text: NotRequired[str]
    altText: NotRequired[str]
    link: NotRequired[RedditSearchResponseDataResultsItemOption0Link]
    domain: NotRequired[str]
    createdAt: NotRequired[str]
    image: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    dominantColor: NotRequired[str]
    video: NotRequired[PinterestSearchResponseDataPinsItemVideo]
    saves: NotRequired[int]
    reposts: NotRequired[int]
    comments: NotRequired[int]
    reactions: NotRequired[int]
    isPromoted: bool
    author: NotRequired[PinterestSearchResponseDataPinsItemAuthor]
    board: NotRequired[PinterestSearchResponseDataPinsItemBoard]


class PinterestSearchResponseData(TypedDict):
    pins: list[PinterestSearchResponseDataPinsItem]
    cursor: NotRequired[str]


class PinterestSearchResponse(TypedDict):
    success: Literal[True]
    data: PinterestSearchResponseData
    creditsUsed: int
    requestId: str


class PinterestPinResponseData(TypedDict):
    pin: PinterestSearchResponseDataPinsItem


class PinterestPinResponse(TypedDict):
    success: Literal[True]
    data: PinterestPinResponseData
    creditsUsed: int
    requestId: str


class PinterestBoardResponseDataBoard(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    url: str
    description: NotRequired[str]
    category: NotRequired[str]
    pins: NotRequired[int]
    followers: NotRequired[int]
    sections: NotRequired[int]
    thumbnail: NotRequired[str]
    author: NotRequired[PinterestSearchResponseDataPinsItemAuthor]


class PinterestBoardResponseData(TypedDict):
    board: PinterestBoardResponseDataBoard
    pins: list[PinterestSearchResponseDataPinsItem]
    cursor: NotRequired[str]


class PinterestBoardResponse(TypedDict):
    success: Literal[True]
    data: PinterestBoardResponseData
    creditsUsed: int
    requestId: str


class PinterestUserResponseDataProfile(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    name: NotRequired[str]
    url: str
    avatar: NotRequired[str]
    followers: NotRequired[int]
    bio: NotRequired[str]
    website: NotRequired[str]
    following: NotRequired[int]
    pins: NotRequired[int]
    boards: NotRequired[int]
    isVerified: bool
    isPrivate: bool
    createdAt: NotRequired[str]


class PinterestUserResponseData(TypedDict):
    profile: PinterestUserResponseDataProfile
    pins: list[PinterestSearchResponseDataPinsItem]
    cursor: NotRequired[str]


class PinterestUserResponse(TypedDict):
    success: Literal[True]
    data: PinterestUserResponseData
    creditsUsed: int
    requestId: str


class PinterestAdsSearchResponseDataAdsItemReachByCountryItem(TypedDict):
    country: NotRequired[str]
    reach: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]


class PinterestAdsSearchResponseDataAdsItem(TypedDict):
    id: NotRequired[str]
    url: str
    headline: NotRequired[str]
    text: NotRequired[str]
    advertisers: NotRequired[list[str]]
    image: NotRequired[str]
    video: NotRequired[str]
    links: NotRequired[list[str]]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    euReach: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    reachByCountry: NotRequired[list[PinterestAdsSearchResponseDataAdsItemReachByCountryItem]]
    countries: NotRequired[list[str]]
    ageRanges: NotRequired[list[str]]
    genders: NotRequired[list[str]]
    interests: NotRequired[list[str]]
    audienceTypes: NotRequired[list[str]]
    isCommercial: bool


class PinterestAdsSearchResponseData(TypedDict):
    ads: list[PinterestAdsSearchResponseDataAdsItem]
    cursor: NotRequired[str]


class PinterestAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: PinterestAdsSearchResponseData
    creditsUsed: int
    requestId: str


class PinterestAdsAdResponseData(TypedDict):
    ad: PinterestAdsSearchResponseDataAdsItem


class PinterestAdsAdResponse(TypedDict):
    success: Literal[True]
    data: PinterestAdsAdResponseData
    creditsUsed: int
    requestId: str


class XTweetResponseDataTweetAuthor(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: NotRequired[bool]
    verifiedType: NotRequired[str]


class XTweetResponseDataTweetMediaItem(TypedDict):
    type: XTweetResponseDataTweetMediaItemType
    url: str
    thumbnail: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    durationSeconds: NotRequired[float]


class XTweetResponseDataTweetParent(TypedDict):
    id: NotRequired[str]
    url: str
    text: NotRequired[str]
    createdAt: NotRequired[str]
    language: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    author: NotRequired[XTweetResponseDataTweetAuthor]
    media: NotRequired[list[XTweetResponseDataTweetMediaItem]]
    links: NotRequired[list[str]]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    replyTo: NotRequired[BlueskyPostsResponseDataPostsItemReplyTo]
    isEdited: bool
    isSensitive: bool


class XTweetResponseDataTweet(TypedDict):
    id: NotRequired[str]
    url: str
    text: NotRequired[str]
    createdAt: NotRequired[str]
    language: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    author: NotRequired[XTweetResponseDataTweetAuthor]
    media: NotRequired[list[XTweetResponseDataTweetMediaItem]]
    links: NotRequired[list[str]]
    hashtags: NotRequired[list[str]]
    mentions: NotRequired[list[str]]
    replyTo: NotRequired[BlueskyPostsResponseDataPostsItemReplyTo]
    isEdited: bool
    isSensitive: bool
    parent: NotRequired[XTweetResponseDataTweetParent]
    quoted: NotRequired[XTweetResponseDataTweetParent]


class XTweetResponseData(TypedDict):
    tweet: XTweetResponseDataTweet


class XTweetResponse(TypedDict):
    success: Literal[True]
    data: XTweetResponseData
    creditsUsed: int
    requestId: str


class KickChannelResponseDataChannelSocialsItem(TypedDict):
    name: NotRequired[str]
    username: NotRequired[str]


class KickChannelResponseDataChannelRecentCategoriesItem(TypedDict):
    name: NotRequired[str]
    slug: NotRequired[str]


class KickChannelResponseDataChannelLive(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str]
    viewers: NotRequired[int]
    startedAt: NotRequired[str]
    language: NotRequired[str]
    isMature: bool
    categories: NotRequired[list[KickChannelResponseDataChannelRecentCategoriesItem]]


class KickChannelResponseDataChannel(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    avatar: NotRequired[str]
    banner: NotRequired[str]
    followers: NotRequired[int]
    isVerified: bool
    isAffiliate: bool
    isBanned: bool
    socials: NotRequired[list[KickChannelResponseDataChannelSocialsItem]]
    recentCategories: NotRequired[list[KickChannelResponseDataChannelRecentCategoriesItem]]
    live: NotRequired[KickChannelResponseDataChannelLive]


class KickChannelResponseData(TypedDict):
    channel: KickChannelResponseDataChannel


class KickChannelResponse(TypedDict):
    success: Literal[True]
    data: KickChannelResponseData
    creditsUsed: int
    requestId: str


class KickVideosResponseDataVideosItem(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    startedAt: NotRequired[str]
    durationSeconds: NotRequired[float]
    views: NotRequired[int]
    language: NotRequired[str]
    isMature: bool
    thumbnail: NotRequired[str]
    stream: NotRequired[str]
    categories: NotRequired[list[KickChannelResponseDataChannelRecentCategoriesItem]]


class KickVideosResponseData(TypedDict):
    videos: list[KickVideosResponseDataVideosItem]


class KickVideosResponse(TypedDict):
    success: Literal[True]
    data: KickVideosResponseData
    creditsUsed: int
    requestId: str


class KickClipsResponseDataClipsItem(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    views: NotRequired[int]
    likes: NotRequired[int]
    durationSeconds: NotRequired[float]
    createdAt: NotRequired[str]
    isMature: bool
    thumbnail: NotRequired[str]
    video: NotRequired[str]
    category: NotRequired[KickChannelResponseDataChannelRecentCategoriesItem]
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]


class KickClipsResponseData(TypedDict):
    clips: list[KickClipsResponseDataClipsItem]
    cursor: NotRequired[str]


class KickClipsResponse(TypedDict):
    success: Literal[True]
    data: KickClipsResponseData
    creditsUsed: int
    requestId: str


class FinanceQuoteResponseDataQuotesItem(TypedDict):
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
    quotes: list[FinanceQuoteResponseDataQuotesItem]


class FinanceQuoteResponse(TypedDict):
    success: Literal[True]
    data: FinanceQuoteResponseData
    creditsUsed: int
    requestId: str


class FinanceHistoryResponseDataHistoryCandlesItem(TypedDict):
    openedAt: str
    open: NotRequired[float]
    high: NotRequired[float]
    low: NotRequired[float]
    close: NotRequired[float]
    adjustedClose: NotRequired[float]
    volume: NotRequired[float]


class FinanceHistoryResponseDataHistoryDividendsItem(TypedDict):
    date: str
    amount: float


class FinanceHistoryResponseDataHistorySplitsItem(TypedDict):
    date: str
    ratio: NotRequired[str]


class FinanceHistoryResponseDataHistory(TypedDict):
    symbol: NotRequired[str]
    currency: NotRequired[str]
    timezone: NotRequired[str]
    interval: NotRequired[str]
    candles: NotRequired[list[FinanceHistoryResponseDataHistoryCandlesItem]]
    dividends: NotRequired[list[FinanceHistoryResponseDataHistoryDividendsItem]]
    splits: NotRequired[list[FinanceHistoryResponseDataHistorySplitsItem]]


class FinanceHistoryResponseData(TypedDict):
    history: NotRequired[FinanceHistoryResponseDataHistory]


class FinanceHistoryResponse(TypedDict):
    success: Literal[True]
    data: FinanceHistoryResponseData
    creditsUsed: int
    requestId: str


class FinanceSearchResponseDataQuotesItem(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    exchange: NotRequired[str]
    sector: NotRequired[str]
    industry: NotRequired[str]


class FinanceSearchResponseDataNewsItem(TypedDict):
    title: NotRequired[str]
    url: str
    publisher: NotRequired[ZillowSearchResponseDataListingsItemBroker]
    createdAt: NotRequired[str]
    tickers: NotRequired[list[str]]


class FinanceSearchResponseData(TypedDict):
    quotes: list[FinanceSearchResponseDataQuotesItem]
    news: list[FinanceSearchResponseDataNewsItem]


class FinanceSearchResponse(TypedDict):
    success: Literal[True]
    data: FinanceSearchResponseData
    creditsUsed: int
    requestId: str


class FinanceProfileResponseDataProfileOfficersItem(TypedDict):
    name: NotRequired[str]
    title: NotRequired[str]
    age: NotRequired[int]
    totalPay: NotRequired[float]


class FinanceProfileResponseDataProfile(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    exchange: NotRequired[str]
    currency: NotRequired[str]
    sector: NotRequired[str]
    industry: NotRequired[str]
    employees: NotRequired[int]
    website: NotRequired[str]
    summary: NotRequired[str]
    address: NotRequired[MapsSearchResponseDataPlacesItemAddress]
    phone: NotRequired[str]
    officers: NotRequired[list[FinanceProfileResponseDataProfileOfficersItem]]
    recommendation: NotRequired[str]
    stats: NotRequired[dict[str, float]]


class FinanceProfileResponseData(TypedDict):
    profile: NotRequired[FinanceProfileResponseDataProfile]


class FinanceProfileResponse(TypedDict):
    success: Literal[True]
    data: FinanceProfileResponseData
    creditsUsed: int
    requestId: str


class MicrosoftAdsSearchResponseDataAdsItemLink(TypedDict):
    url: NotRequired[str]
    caption: NotRequired[str]


class MicrosoftAdsSearchResponseDataAdsItem(TypedDict):
    id: NotRequired[str]
    advertiser: NotRequired[ZillowPropertyResponseDataPropertyMls]
    headline: NotRequired[str]
    text: NotRequired[str]
    link: NotRequired[MicrosoftAdsSearchResponseDataAdsItemLink]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]


class MicrosoftAdsSearchResponseData(TypedDict):
    ads: list[MicrosoftAdsSearchResponseDataAdsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class MicrosoftAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: MicrosoftAdsSearchResponseData
    creditsUsed: int
    requestId: str


class MicrosoftAdsAdResponseDataAdTargetingItem(TypedDict):
    type: NotRequired[str]
    isExcluded: bool


class MicrosoftAdsAdResponseDataAd(TypedDict):
    id: NotRequired[str]
    advertiser: NotRequired[ZillowPropertyResponseDataPropertyMls]
    headline: NotRequired[str]
    text: NotRequired[str]
    link: NotRequired[MicrosoftAdsSearchResponseDataAdsItemLink]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    paidBy: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressions: NotRequired[MetaAdsSearchResponseDataAdsItemSpend]
    countries: NotRequired[list[LinkedinAdsAdResponseDataAdCountriesItem]]
    targeting: NotRequired[list[MicrosoftAdsAdResponseDataAdTargetingItem]]


class MicrosoftAdsAdResponseData(TypedDict):
    ad: NotRequired[MicrosoftAdsAdResponseDataAd]


class MicrosoftAdsAdResponse(TypedDict):
    success: Literal[True]
    data: MicrosoftAdsAdResponseData
    creditsUsed: int
    requestId: str


class MicrosoftAdsAdvertisersResponseDataAdvertisersItem(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    country: NotRequired[str]
    isVerified: bool


class MicrosoftAdsAdvertisersResponseData(TypedDict):
    advertisers: list[MicrosoftAdsAdvertisersResponseDataAdvertisersItem]
    total: NotRequired[int]


class MicrosoftAdsAdvertisersResponse(TypedDict):
    success: Literal[True]
    data: MicrosoftAdsAdvertisersResponseData
    creditsUsed: int
    requestId: str


class SnapchatProfileResponseDataProfile(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    bio: NotRequired[str]
    website: NotRequired[str]
    avatar: NotRequired[str]
    banner: NotRequired[str]
    subscribers: NotRequired[int]
    category: NotRequired[str]
    subcategory: NotRequired[str]
    isVerified: bool
    isBusiness: bool
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    related: NotRequired[list[str]]


class SnapchatProfileResponseDataSpotlightsItem(TypedDict):
    id: NotRequired[str]
    url: str
    video: NotRequired[str]
    thumbnail: NotRequired[str]
    views: NotRequired[int]
    shares: NotRequired[int]
    createdAt: NotRequired[str]
    durationSeconds: NotRequired[float]
    width: NotRequired[int]
    height: NotRequired[int]
    hashtags: NotRequired[list[str]]


class SnapchatProfileResponseDataStoriesItem(TypedDict):
    id: NotRequired[str]
    type: SnapchatProfileResponseDataStoriesItemType
    url: NotRequired[str]
    thumbnail: NotRequired[str]
    createdAt: NotRequired[str]


class SnapchatProfileResponseData(TypedDict):
    profile: SnapchatProfileResponseDataProfile
    spotlights: list[SnapchatProfileResponseDataSpotlightsItem]
    stories: list[SnapchatProfileResponseDataStoriesItem]


class SnapchatProfileResponse(TypedDict):
    success: Literal[True]
    data: SnapchatProfileResponseData
    creditsUsed: int
    requestId: str


class SnapchatAdsSearchResponseDataAdsItemMedia(TypedDict):
    type: NotRequired[str]
    url: NotRequired[str]


class SnapchatAdsSearchResponseDataAdsItemCountriesItem(TypedDict):
    country: NotRequired[str]
    impressions: int


class SnapchatAdsSearchResponseDataAdsItemTargeting(TypedDict):
    ageRanges: NotRequired[list[str]]
    hasRegulatedContent: bool


class SnapchatAdsSearchResponseDataAdsItem(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    paidBy: NotRequired[str]
    brand: NotRequired[str]
    profile: NotRequired[str]
    account: NotRequired[str]
    status: NotRequired[str]
    type: NotRequired[str]
    creativeType: NotRequired[str]
    headline: NotRequired[str]
    cta: NotRequired[MetaAdsSearchResponseDataAdsItemCta]
    languages: NotRequired[list[str]]
    media: NotRequired[SnapchatAdsSearchResponseDataAdsItemMedia]
    link: NotRequired[MetaAdsSearchResponseDataAdsItemLink]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressions: NotRequired[int]
    countries: NotRequired[list[SnapchatAdsSearchResponseDataAdsItemCountriesItem]]
    targeting: SnapchatAdsSearchResponseDataAdsItemTargeting


class SnapchatAdsSearchResponseData(TypedDict):
    ads: list[SnapchatAdsSearchResponseDataAdsItem]
    cursor: NotRequired[str]


class SnapchatAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: SnapchatAdsSearchResponseData
    creditsUsed: int
    requestId: str


class SnapchatAdsAdResponseData(TypedDict):
    ad: SnapchatAdsSearchResponseDataAdsItem


class SnapchatAdsAdResponse(TypedDict):
    success: Literal[True]
    data: SnapchatAdsAdResponseData
    creditsUsed: int
    requestId: str


class TumblrBlogResponseDataBlog(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    url: str
    name: NotRequired[str]
    description: NotRequired[str]
    avatar: NotRequired[str]
    posts: NotRequired[int]
    updatedAt: NotRequired[str]
    isNsfw: bool


class TumblrBlogResponseData(TypedDict):
    blog: TumblrBlogResponseDataBlog


class TumblrBlogResponse(TypedDict):
    success: Literal[True]
    data: TumblrBlogResponseData
    creditsUsed: int
    requestId: str


class TumblrPostsResponseDataPostsItemRepostOf(TypedDict):
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]


class TumblrPostsResponseDataPostsItem(TypedDict):
    id: NotRequired[str]
    url: str
    author: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    type: NotRequired[str]
    createdAt: NotRequired[str]
    summary: NotRequired[str]
    text: NotRequired[str]
    images: NotRequired[list[YoutubeChannelResponseDataItemsItemOption2ImagesItem]]
    videos: NotRequired[list[InstagramProfileResponseDataPostsItemVideosItem]]
    links: NotRequired[list[str]]
    tags: NotRequired[list[str]]
    notes: NotRequired[int]
    likes: NotRequired[int]
    reposts: NotRequired[int]
    replies: NotRequired[int]
    repostOf: NotRequired[TumblrPostsResponseDataPostsItemRepostOf]
    repostedFrom: NotRequired[YoutubeSearchResponseDataResultsItemOption0Channel]
    isNsfw: bool


class TumblrPostsResponseData(TypedDict):
    blog: TumblrBlogResponseDataBlog
    posts: list[TumblrPostsResponseDataPostsItem]
    total: NotRequired[int]
    cursor: NotRequired[str]


class TumblrPostsResponse(TypedDict):
    success: Literal[True]
    data: TumblrPostsResponseData
    creditsUsed: int
    requestId: str


class TumblrPostResponseData(TypedDict):
    post: TumblrPostsResponseDataPostsItem
    blog: TumblrBlogResponseDataBlog


class TumblrPostResponse(TypedDict):
    success: Literal[True]
    data: TumblrPostResponseData
    creditsUsed: int
    requestId: str


class TumblrSearchResponseData(TypedDict):
    posts: list[TumblrPostsResponseDataPostsItem]
    cursor: NotRequired[str]


class TumblrSearchResponse(TypedDict):
    success: Literal[True]
    data: TumblrSearchResponseData
    creditsUsed: int
    requestId: str


class QuoraQuestionResponseDataQuestion(TypedDict):
    id: NotRequired[str]
    url: str
    title: NotRequired[str]
    answers: NotRequired[int]
    topics: NotRequired[list[str]]


class QuoraQuestionResponseDataAnswersItemAuthor(TypedDict):
    id: NotRequired[str]
    username: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    avatar: NotRequired[str]
    isVerified: NotRequired[bool]
    credential: NotRequired[str]


class QuoraQuestionResponseDataAnswersItem(TypedDict):
    id: NotRequired[str]
    url: NotRequired[str]
    text: NotRequired[str]
    author: NotRequired[QuoraQuestionResponseDataAnswersItemAuthor]
    likes: NotRequired[int]
    views: NotRequired[int]
    shares: NotRequired[int]
    comments: NotRequired[int]
    createdAt: NotRequired[str]


class QuoraQuestionResponseData(TypedDict):
    question: QuoraQuestionResponseDataQuestion
    answers: list[QuoraQuestionResponseDataAnswersItem]


class QuoraQuestionResponse(TypedDict):
    success: Literal[True]
    data: QuoraQuestionResponseData
    creditsUsed: int
    requestId: str
