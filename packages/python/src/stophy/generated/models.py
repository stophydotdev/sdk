"""Generated from openapi.json by scripts/gen_python.py. Do not edit."""

from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

GoogleSearchTime = Literal[
    "pastHour",
    "past24Hours",
    "pastWeek",
    "pastMonth",
    "pastYear",
]

GoogleSearchResponseDataEngine = Literal[
    "google",
    "other",
]

GoogleNewsTopic = Literal[
    "world",
    "nation",
    "business",
    "technology",
    "entertainment",
    "sports",
    "science",
    "health",
]

GoogleNewsSort = Literal[
    "relevance",
    "newest",
]

GoogleImagesSize = Literal[
    "large",
    "medium",
    "icon",
]

GoogleImagesType = Literal[
    "clipArt",
    "lineDrawing",
    "gif",
]

GoogleImagesTime = Literal[
    "past24Hours",
    "pastWeek",
]

GoogleImagesUsageRights = Literal[
    "creativeCommons",
    "commercial",
]

GoogleAdsSearchMediaType = Literal[
    "text",
    "image",
    "video",
]

GoogleAdsSearchPlatform = Literal[
    "search",
    "youtube",
    "play",
    "maps",
    "shopping",
]

GoogleAdsSearchResponseDataResultsItemFormat = Literal[
    "text",
    "image",
    "video",
    "unknown",
]

GoogleScholarType = Literal[
    "any",
    "reviewArticles",
    "caseLaw",
]

GoogleScholarResponseDataResultsItemFormat = Literal[
    "pdf",
    "html",
    "book",
    "citation",
    "doc",
]

GoogleJobsDatePosted = Literal[
    "yesterday",
    "last3Days",
    "lastWeek",
    "lastMonth",
]

GoogleJobsJobType = Literal[
    "fullTime",
    "partTime",
    "contract",
    "internship",
]

GooglePatentsLanguage = Literal[
    "english",
    "german",
    "chinese",
    "french",
    "spanish",
    "arabic",
    "japanese",
    "korean",
    "portuguese",
    "russian",
    "italian",
    "dutch",
    "swedish",
    "finnish",
    "norwegian",
    "danish",
]

GooglePatentsDateType = Literal[
    "priority",
    "filing",
    "publication",
]

GooglePatentsStatus = Literal[
    "grant",
    "application",
]

GooglePatentsType = Literal[
    "patent",
    "design",
]

GooglePatentsLitigation = Literal[
    "has",
    "none",
]

GooglePatentsSort = Literal[
    "relevance",
    "newest",
    "oldest",
]

YoutubeSuggestCountry = Literal[
    "dz",
    "ar",
    "au",
    "at",
    "az",
    "bh",
    "bd",
    "by",
    "be",
    "bo",
    "ba",
    "br",
    "bg",
    "ca",
    "cl",
    "co",
    "cr",
    "hr",
    "cy",
    "cz",
    "dk",
    "do",
    "ec",
    "eg",
    "sv",
    "ee",
    "fi",
    "fr",
    "ge",
    "de",
    "gh",
    "gr",
    "gt",
    "hn",
    "hk",
    "hu",
    "is",
    "in",
    "id",
    "iq",
    "ie",
    "il",
    "it",
    "jm",
    "jp",
    "jo",
    "kz",
    "ke",
    "kw",
    "lv",
    "lb",
    "ly",
    "li",
    "lt",
    "lu",
    "my",
    "mt",
    "mx",
    "me",
    "ma",
    "np",
    "nl",
    "nz",
    "ni",
    "ng",
    "mk",
    "no",
    "om",
    "pk",
    "pa",
    "pg",
    "py",
    "pe",
    "ph",
    "pl",
    "pt",
    "pr",
    "qa",
    "ro",
    "ru",
    "sa",
    "sn",
    "rs",
    "sg",
    "sk",
    "si",
    "za",
    "kr",
    "es",
    "lk",
    "se",
    "ch",
    "tw",
    "tz",
    "th",
    "tn",
    "tr",
    "ug",
    "ua",
    "ae",
    "gb",
    "us",
    "uy",
    "ve",
    "vn",
    "ye",
    "zw",
]

YoutubeSearchType = Literal[
    "videos",
    "shorts",
    "channels",
    "playlists",
    "movies",
]

YoutubeSearchDuration = Literal[
    "under3Minutes",
    "3to20Minutes",
    "over20Minutes",
]

YoutubeSearchUploadDate = Literal[
    "today",
    "thisWeek",
    "thisMonth",
    "thisYear",
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
    "location",
    "purchased",
]

YoutubeSearchPrioritize = Literal[
    "relevance",
    "popularity",
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
    "podcasts",
    "releases",
    "posts",
]

YoutubeChannelSort = Literal[
    "latest",
    "popular",
    "oldest",
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

RedditSearchTime = Literal[
    "pastHour",
    "today",
    "pastWeek",
    "pastMonth",
    "pastYear",
    "allTime",
]

RedditPostSort = Literal[
    "best",
    "top",
    "newest",
    "controversial",
    "old",
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

RedditSubredditsSort = Literal[
    "popular",
    "newest",
]

GoogleMapsSearchMinRating = Literal[
    2,
    2.5,
    3,
    3.5,
    4,
    4.5,
]

GoogleMapsReviewsSort = Literal[
    "relevance",
    "newest",
    "highest",
    "lowest",
]

InstagramPostResponseDataType = Literal[
    "photo",
    "video",
    "reel",
    "carousel",
]

TiktokProfileResponseDataResultsItemType = Literal[
    "video",
    "photo",
]

TiktokSearchType = Literal[
    "videos",
    "users",
]

TiktokSearchSort = Literal[
    "relevance",
    "mostLiked",
    "datePosted",
]

TiktokSearchDatePosted = Literal[
    "past24Hours",
    "thisWeek",
    "thisMonth",
    "last3Months",
    "last6Months",
]

MetaAdsPageStatus = Literal[
    "active",
    "inactive",
    "all",
]

MetaAdsPageMediaType = Literal[
    "image",
    "video",
    "text",
]

MetaAdsPagePlatformsItem = Literal[
    "facebook",
    "instagram",
    "audienceNetwork",
    "messenger",
    "whatsapp",
    "threads",
]

LinkedinJobsSearchDatePosted = Literal[
    "anyTime",
    "pastMonth",
    "pastWeek",
    "past24Hours",
]

LinkedinJobsSearchResponseDataResultsItemSalaryPeriod = Literal[
    "hour",
    "month",
    "year",
]

ZillowSearchStatus = Literal[
    "forSale",
    "forRent",
    "sold",
]

ZillowSearchDaysOnZillow = Literal[
    "1Day",
    "7Days",
    "14Days",
    "30Days",
    "90Days",
    "6Months",
    "12Months",
    "24Months",
    "36Months",
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
    "bedrooms",
    "bathrooms",
    "squareFeet",
    "lotSize",
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

UpworkSearchExperienceLevel = Literal[
    "entry",
    "intermediate",
    "expert",
]

UpworkSearchWorkload = Literal[
    "fullTime",
    "partTime",
    "asNeeded",
]

UpworkSearchDuration = Literal[
    "underOneMonth",
    "oneToThreeMonths",
    "threeToSixMonths",
    "overSixMonths",
]

GoogleTrendsRelatedTime = Literal[
    "pastHour",
    "past4Hours",
    "pastDay",
    "past7Days",
    "past30Days",
    "past90Days",
    "past12Months",
    "past5Years",
    "since2004",
]

GoogleTrendsRelatedSearchType = Literal[
    "web",
    "images",
    "news",
    "shopping",
    "youtube",
]

GoogleTrendsRelatedCategory = Literal[
    "artsEntertainment",
    "autosVehicles",
    "beautyFitness",
    "booksLiterature",
    "businessIndustrial",
    "computersElectronics",
    "finance",
    "foodDrink",
    "games",
    "health",
    "hobbiesLeisure",
    "homeGarden",
    "internetTelecom",
    "jobsEducation",
    "lawGovernment",
    "news",
    "onlineCommunities",
    "peopleSociety",
    "petsAnimals",
    "realEstate",
    "reference",
    "science",
    "shopping",
    "sports",
    "travel",
]

GoogleTrendsTrendingTime = Literal[
    "past4Hours",
    "past24Hours",
    "past48Hours",
    "past7Days",
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

GoogleTrendsTrendingStatus = Literal[
    "all",
    "active",
]

GoogleTrendsTrendingSort = Literal[
    "relevance",
    "searchVolume",
    "recency",
    "title",
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
    "pl",
    "cz",
    "hu",
    "ro",
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

IndeedSearchDistanceMiles = Literal[
    0,
    5,
    10,
    15,
    25,
    35,
    50,
    100,
]

IndeedSearchDatePosted = Literal[
    "last24Hours",
    "last3Days",
    "last7Days",
    "last14Days",
]

IndeedSearchRemote = Literal[
    "remote",
    "hybrid",
]

IndeedSearchJobType = Literal[
    "fullTime",
    "partTime",
    "contract",
    "temporary",
    "internship",
]

IndeedSearchExperienceLevel = Literal[
    "noExperience",
    "entry",
    "mid",
    "senior",
]

IndeedSearchEducation = Literal[
    "highSchool",
    "associate",
    "bachelor",
    "master",
]

IndeedSearchResponseDataResultsItemSalaryPeriod = Literal[
    "hour",
    "day",
    "week",
    "month",
    "year",
]

CareersJobsResponseDataResultsItemWorkplaceType = Literal[
    "remote",
    "hybrid",
    "onsite",
]

TripadvisorSearchType = Literal[
    "all",
    "hotels",
    "restaurants",
    "attractions",
    "geos",
]

TripadvisorReviewsTravelerTypesItem = Literal[
    "families",
    "couples",
    "solo",
    "business",
    "friends",
]

TripadvisorReviewsMonthsItem = Literal[
    "marMay",
    "junAug",
    "sepNov",
    "decFeb",
]

TripadvisorReviewsSort = Literal[
    "mostRecent",
    "detailed",
]

GoogleFlightsCabin = Literal[
    "economy",
    "premiumEconomy",
    "business",
    "first",
]

GoogleFlightsStops = Literal[
    "any",
    "nonstop",
    "oneStopOrFewer",
    "twoStopsOrFewer",
]

GoogleFlightsResponseDataTripType = Literal[
    "oneWay",
    "roundTrip",
]

GoogleHotelsMinRating = Literal[
    "3.5+",
    "4+",
    "4.5+",
]

GoogleHotelsAmenitiesItem = Literal[
    "freeWifi",
    "freeBreakfast",
    "restaurant",
    "bar",
    "kidFriendly",
    "petFriendly",
    "freeParking",
    "parking",
    "evCharger",
    "roomService",
    "fitnessCenter",
    "spa",
    "pool",
    "indoorPool",
    "outdoorPool",
    "airConditioned",
    "wheelchairAccessible",
    "beachAccess",
    "allInclusiveAvailable",
]

GoogleHotelsPropertyTypesItem = Literal[
    "beachHotels",
    "boutiqueHotels",
    "hostels",
    "inns",
    "motels",
    "resorts",
    "spaHotels",
    "bedAndBreakfasts",
    "other",
    "apartmentHotels",
]

GoogleHotelsSort = Literal[
    "relevance",
    "lowestPrice",
    "highestRating",
    "mostReviewed",
]

BookingSearchSort = Literal[
    "relevance",
    "distance",
]

BookingHotelReviewsSort = Literal[
    "newest",
    "mostRelevant",
    "lowestScore",
]

AmazonSearchSort = Literal[
    "relevance",
    "priceLow",
    "priceHigh",
    "avgCustomerReview",
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

GooglePlayReviewsSort = Literal[
    "newest",
    "relevance",
    "highest",
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

LinkedinAdsSearchWithin = Literal[
    "month",
    "year",
    "all",
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

GoogleTrendsRegionsResolution = Literal[
    "country",
    "region",
    "metro",
]

TrustpilotCompanyReviewsDatePublished = Literal[
    "last30Days",
    "last3Months",
    "last6Months",
    "last12Months",
]

EbaySearchCondition = Literal[
    "new",
    "used",
]

EbaySearchSort = Literal[
    "bestMatch",
    "priceLow",
    "priceHigh",
    "endingSoonest",
]

AirbnbSearchRoomType = Literal[
    "entireHome",
    "privateRoom",
]

AirbnbSearchCurrency = Literal[
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CAD",
    "AUD",
    "CHF",
    "MXN",
    "BRL",
]

FacebookPostResponseDataMediaItemType = Literal[
    "photo",
    "video",
]

FacebookMarketplaceSearchSort = Literal[
    "newest",
    "priceLow",
    "priceHigh",
]

LinkedinProfileResponseDataRolesItem = TypedDict(
    "LinkedinProfileResponseDataRolesItem",
    {
        "title": NotRequired[str],
        "companyName": NotRequired[str],
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
    pricing: NotRequired[str | None]
    keyless: bool
    cacheTtlSeconds: int
    input: NotRequired[dict[str, Any]]
    example: dict[str, Any] | None


class EndpointCatalog(TypedDict):
    sources: list[EndpointCatalogSourcesItem]
    endpoints: list[EndpointCatalogEndpointsItem]


class GoogleSearchResponseDataAiOverviewSourcesItem(TypedDict):
    url: str
    title: NotRequired[str]


class GoogleSearchResponseDataAiOverview(TypedDict):
    text: str
    sources: NotRequired[list[GoogleSearchResponseDataAiOverviewSourcesItem]]


class GoogleSearchResponseDataKnowledgeGraphProfilesItem(TypedDict):
    site: str
    url: str


class GoogleSearchResponseDataKnowledgeGraph(TypedDict):
    title: str
    type: NotRequired[str]
    website: NotRequired[str]
    imageUrl: NotRequired[str]
    description: NotRequired[str]
    descriptionSource: NotRequired[str]
    descriptionUrl: NotRequired[str]
    attributes: NotRequired[dict[str, str]]
    profiles: NotRequired[list[GoogleSearchResponseDataKnowledgeGraphProfilesItem]]


class GoogleSearchResponseDataResultsItemOption0SitelinksItem(TypedDict):
    title: str
    url: str


class GoogleSearchResponseDataResultsItemOption0(TypedDict):
    type: Literal["web"]
    url: str
    title: str
    description: NotRequired[str]
    date: NotRequired[str]
    sitelinks: NotRequired[list[GoogleSearchResponseDataResultsItemOption0SitelinksItem]]
    position: int
    markdown: NotRequired[str]
    scrapeError: NotRequired[str]


class GoogleSearchResponseDataResultsItemOption1(TypedDict):
    type: Literal["news"]
    url: str
    title: str
    source: NotRequired[str]
    publishedAt: NotRequired[str]
    position: int


class GoogleSearchResponseDataResultsItemOption2(TypedDict):
    type: Literal["video"]
    url: str
    title: str
    site: NotRequired[str]
    channelName: NotRequired[str]
    durationSeconds: NotRequired[int]
    publishedAt: NotRequired[str]
    position: int


class GoogleSearchResponseDataResultsItemOption3(TypedDict):
    type: Literal["post"]
    url: str
    text: str
    site: NotRequired[str]
    authorName: NotRequired[str]
    comments: NotRequired[int]
    likes: NotRequired[int]
    publishedAt: NotRequired[str]
    position: int


class GoogleSearchResponseDataPeopleAlsoAskItem(TypedDict):
    question: str
    answer: NotRequired[str]
    title: NotRequired[str]
    url: NotRequired[str]


class GoogleSearchResponseData(TypedDict):
    aiOverview: NotRequired[GoogleSearchResponseDataAiOverview]
    knowledgeGraph: NotRequired[GoogleSearchResponseDataKnowledgeGraph]
    engine: NotRequired[GoogleSearchResponseDataEngine]
    results: list[
        GoogleSearchResponseDataResultsItemOption0
        | GoogleSearchResponseDataResultsItemOption1
        | GoogleSearchResponseDataResultsItemOption2
        | GoogleSearchResponseDataResultsItemOption3
    ]
    peopleAlsoAsk: NotRequired[list[GoogleSearchResponseDataPeopleAlsoAskItem]]
    relatedSearches: NotRequired[list[str]]
    page: NotRequired[int]


class GoogleSearchResponse(TypedDict):
    success: Literal[True]
    data: GoogleSearchResponseData
    creditsUsed: int
    requestId: str


class GoogleNewsResponseDataResultsItem(TypedDict):
    url: str
    title: str
    source: NotRequired[str]
    description: NotRequired[str]
    publishedAt: NotRequired[str]
    position: int


class GoogleNewsResponseData(TypedDict):
    results: list[GoogleNewsResponseDataResultsItem]
    page: int


class GoogleNewsResponse(TypedDict):
    success: Literal[True]
    data: GoogleNewsResponseData
    creditsUsed: int
    requestId: str


class GoogleImagesResponseDataResultsItem(TypedDict):
    imageUrl: str
    title: NotRequired[str]
    pageUrl: str
    source: NotRequired[str]
    width: int
    height: int
    thumbnailUrl: str
    position: int


class GoogleImagesResponseData(TypedDict):
    results: list[GoogleImagesResponseDataResultsItem]


class GoogleImagesResponse(TypedDict):
    success: Literal[True]
    data: GoogleImagesResponseData
    creditsUsed: int
    requestId: str


class GoogleAiModeResponseDataSourcesItem(TypedDict):
    url: str
    title: NotRequired[str]


class GoogleAiModeResponseData(TypedDict):
    query: NotRequired[str]
    answer: str
    sources: list[GoogleAiModeResponseDataSourcesItem]


class GoogleAiModeResponse(TypedDict):
    success: Literal[True]
    data: GoogleAiModeResponseData
    creditsUsed: int
    requestId: str


class GoogleShoppingResponseDataFiltersItemOptionsItem(TypedDict):
    label: str
    filter: str
    isSelected: bool


class GoogleShoppingResponseDataFiltersItem(TypedDict):
    group: str
    options: NotRequired[list[GoogleShoppingResponseDataFiltersItemOptionsItem]]


class GoogleShoppingResponseDataResultsItem(TypedDict):
    productId: str
    title: str
    price: float
    priceCurrency: NotRequired[str]
    originalPrice: NotRequired[float]
    seller: NotRequired[str]
    delivery: NotRequired[str]
    returns: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    position: int


class GoogleShoppingResponseData(TypedDict):
    filters: NotRequired[list[GoogleShoppingResponseDataFiltersItem]]
    results: list[GoogleShoppingResponseDataResultsItem]
    page: int


class GoogleShoppingResponse(TypedDict):
    success: Literal[True]
    data: GoogleShoppingResponseData
    creditsUsed: int
    requestId: str


class GoogleSuggestResponseDataResultsItem(TypedDict):
    keyword: str
    rank: int


class GoogleSuggestResponseData(TypedDict):
    results: list[GoogleSuggestResponseDataResultsItem]


class GoogleSuggestResponse(TypedDict):
    success: Literal[True]
    data: GoogleSuggestResponseData
    creditsUsed: int
    requestId: str


class GoogleAdsSearchResponseDataResultsItem(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserUrl: str
    domain: NotRequired[str]
    format: GoogleAdsSearchResponseDataResultsItemFormat
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    daysShown: NotRequired[int]
    previewUrl: NotRequired[str]
    imageUrl: NotRequired[str]


class GoogleAdsSearchResponseData(TypedDict):
    totalMin: NotRequired[int]
    totalMax: NotRequired[int]
    results: list[GoogleAdsSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class GoogleAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: GoogleAdsSearchResponseData
    creditsUsed: int
    requestId: str


class GoogleAdsAdResponseDataVariationsItem(TypedDict):
    previewUrl: NotRequired[str]
    imageUrl: NotRequired[str]
    videoUrl: NotRequired[str]


class GoogleAdsAdResponseDataRegionsItem(TypedDict):
    country: NotRequired[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]


class GoogleAdsAdResponseData(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserUrl: str
    domain: NotRequired[str]
    format: GoogleAdsSearchResponseDataResultsItemFormat
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
    variations: list[GoogleAdsAdResponseDataVariationsItem]
    regions: list[GoogleAdsAdResponseDataRegionsItem]
    targetingIncluded: list[str]
    targetingExcluded: list[str]


class GoogleAdsAdResponse(TypedDict):
    success: Literal[True]
    data: GoogleAdsAdResponseData
    creditsUsed: int
    requestId: str


class GoogleAdsAdvertisersResponseDataResultsItem(TypedDict):
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    advertiserCountry: NotRequired[str]
    advertiserUrl: str
    isVerified: bool
    adsMin: NotRequired[int]
    adsMax: NotRequired[int]


class GoogleAdsAdvertisersResponseData(TypedDict):
    domains: list[str]
    results: list[GoogleAdsAdvertisersResponseDataResultsItem]


class GoogleAdsAdvertisersResponse(TypedDict):
    success: Literal[True]
    data: GoogleAdsAdvertisersResponseData
    creditsUsed: int
    requestId: str


class GoogleScholarResponseDataResultsItem(TypedDict):
    title: str
    url: NotRequired[str]
    format: NotRequired[GoogleScholarResponseDataResultsItemFormat]
    authors: NotRequired[list[str]]
    publication: NotRequired[str]
    year: NotRequired[int]
    publisher: NotRequired[str]
    snippet: NotRequired[str]
    citations: NotRequired[int]
    citesId: NotRequired[str]
    versions: NotRequired[int]
    pdfUrl: NotRequired[str]
    position: int


class GoogleScholarResponseData(TypedDict):
    results: list[GoogleScholarResponseDataResultsItem]
    page: int


class GoogleScholarResponse(TypedDict):
    success: Literal[True]
    data: GoogleScholarResponseData
    creditsUsed: int
    requestId: str


class GoogleJobsResponseDataResultsItem(TypedDict):
    jobId: str
    title: str
    companyName: NotRequired[str]
    location: NotRequired[str]
    via: NotRequired[str]
    publishedAt: NotRequired[str]
    jobType: NotRequired[str]
    salary: NotRequired[str]
    benefits: NotRequired[list[str]]
    apply: NotRequired[list[GoogleSearchResponseDataKnowledgeGraphProfilesItem]]
    qualifications: NotRequired[list[str]]
    responsibilities: NotRequired[list[str]]
    description: NotRequired[str]
    jobUrl: str
    position: int


class GoogleJobsResponseData(TypedDict):
    results: list[GoogleJobsResponseDataResultsItem]
    cursor: NotRequired[str]


class GoogleJobsResponse(TypedDict):
    success: Literal[True]
    data: GoogleJobsResponseData
    creditsUsed: int
    requestId: str


class GooglePatentsResponseDataResultsItem(TypedDict):
    patentId: str
    title: str
    snippet: NotRequired[str]
    assignee: NotRequired[str]
    inventor: NotRequired[str]
    priorityDate: NotRequired[str]
    filingDate: NotRequired[str]
    grantDate: NotRequired[str]
    publicationDate: NotRequired[str]
    language: NotRequired[str]
    patentUrl: str
    pdfUrl: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    position: int


class GooglePatentsResponseData(TypedDict):
    results: list[GooglePatentsResponseDataResultsItem]
    page: int


class GooglePatentsResponse(TypedDict):
    success: Literal[True]
    data: GooglePatentsResponseData
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
    channelAvatarUrl: NotRequired[str]


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


class YoutubeTranscriptResponseDataSegmentsItem(TypedDict):
    startSeconds: float
    endSeconds: float
    text: NotRequired[str]


class YoutubeTranscriptResponseData(TypedDict):
    videoId: NotRequired[str]
    videoUrl: str
    language: NotRequired[str]
    isAutoGenerated: bool
    durationSeconds: NotRequired[float]
    transcribedSeconds: NotRequired[float]
    text: NotRequired[str]
    segments: NotRequired[list[YoutubeTranscriptResponseDataSegmentsItem]]


class YoutubeTranscriptResponse(TypedDict):
    success: Literal[True]
    data: YoutubeTranscriptResponseData
    creditsUsed: int
    requestId: str


class YoutubeVideoResponseDataChaptersItem(TypedDict):
    title: NotRequired[str]
    startSeconds: int


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
    comments: NotRequired[int]
    channelSubscribers: NotRequired[int]
    chapters: list[YoutubeVideoResponseDataChaptersItem]
    mostReplayedAtSeconds: list[int]


class YoutubeVideoResponse(TypedDict):
    success: Literal[True]
    data: YoutubeVideoResponseData
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


class YoutubeChannelResponseDataResultsItemOption0(TypedDict):
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
        YoutubeChannelResponseDataResultsItemOption0
        | YoutubeSearchResponseDataResultsItemOption2
        | YoutubeChannelResponseDataResultsItemOption2
    ]
    cursor: NotRequired[str]


class YoutubeChannelResponse(TypedDict):
    success: Literal[True]
    data: YoutubeChannelResponseData
    creditsUsed: int
    requestId: str


class YoutubePostResponseDataResultsItem(TypedDict):
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


class YoutubePostResponseData(TypedDict):
    postId: NotRequired[str]
    postUrl: NotRequired[str]
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    comments: NotRequired[int]
    imageUrls: NotRequired[list[str]]
    videoId: NotRequired[str]
    videoTitle: NotRequired[str]
    pollChoices: NotRequired[list[str]]
    pollTotalVotes: NotRequired[int]
    results: list[YoutubePostResponseDataResultsItem]
    cursor: NotRequired[str]


class YoutubePostResponse(TypedDict):
    success: Literal[True]
    data: YoutubePostResponseData
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
    hiddenVideos: NotRequired[int]
    thumbnailUrl: NotRequired[str]
    results: list[YoutubeChannelResponseDataResultsItemOption0]
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


class RedditPostResponseDataResultsItem(TypedDict):
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
    postUrl: NotRequired[str]
    title: NotRequired[str]
    text: NotRequired[str]
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: NotRequired[str]
    subreddit: NotRequired[str]
    score: NotRequired[int]
    upvotePercent: NotRequired[float]
    comments: NotRequired[int]
    publishedAt: NotRequired[str]
    flair: NotRequired[str]
    linkUrl: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    isNsfw: NotRequired[bool]
    isVideo: NotRequired[bool]
    isPinned: NotRequired[bool]
    imageUrls: NotRequired[list[str]]
    videoUrl: NotRequired[str]
    videoHlsUrl: NotRequired[str]
    videoDurationSeconds: NotRequired[float]
    pollOptions: NotRequired[list[RedditSearchResponseDataResultsItemOption0PollOptionsItem]]
    pollTotalVotes: NotRequired[int]
    pollEndsAt: NotRequired[str]
    repostOfUrl: NotRequired[str]
    results: list[RedditPostResponseDataResultsItem]
    cursor: NotRequired[str]


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


class RedditDiscussionsResponseData(TypedDict):
    results: list[RedditSearchResponseDataResultsItemOption0]
    cursor: NotRequired[str]


class RedditDiscussionsResponse(TypedDict):
    success: Literal[True]
    data: RedditDiscussionsResponseData
    creditsUsed: int
    requestId: str


class RedditSubredditsResponseData(TypedDict):
    results: list[RedditSearchResponseDataResultsItemOption1]
    cursor: NotRequired[str]


class RedditSubredditsResponse(TypedDict):
    success: Literal[True]
    data: RedditSubredditsResponseData
    creditsUsed: int
    requestId: str


class GoogleMapsSearchResponseDataResultsItemHoursItem(TypedDict):
    days: NotRequired[str]
    times: NotRequired[list[str]]


class GoogleMapsSearchResponseDataResultsItem(TypedDict):
    placeId: NotRequired[str]
    googlePlaceId: NotRequired[str]
    placeUrl: str
    name: NotRequired[str]
    categories: NotRequired[list[str]]
    address: NotRequired[str]
    latitude: float
    longitude: float
    rating: NotRequired[float]
    reviews: NotRequired[int]
    photos: NotRequired[int]
    phone: NotRequired[str]
    website: NotRequired[str]
    description: NotRequired[str]
    hours: NotRequired[list[GoogleMapsSearchResponseDataResultsItemHoursItem]]
    hoursToday: NotRequired[str]
    openStatus: NotRequired[str]
    timezone: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    reservationUrl: NotRequired[str]
    attributes: NotRequired[list[str]]


class GoogleMapsSearchResponseData(TypedDict):
    results: list[GoogleMapsSearchResponseDataResultsItem]
    page: int


class GoogleMapsSearchResponse(TypedDict):
    success: Literal[True]
    data: GoogleMapsSearchResponseData
    creditsUsed: int
    requestId: str


class GoogleMapsPlaceResponseData(TypedDict):
    placeId: NotRequired[str]
    googlePlaceId: NotRequired[str]
    placeUrl: str
    name: NotRequired[str]
    categories: list[str]
    address: NotRequired[str]
    latitude: float
    longitude: float
    rating: NotRequired[float]
    reviews: NotRequired[int]
    photos: NotRequired[int]
    phone: NotRequired[str]
    website: NotRequired[str]
    description: NotRequired[str]
    hours: list[GoogleMapsSearchResponseDataResultsItemHoursItem]
    hoursToday: NotRequired[str]
    openStatus: NotRequired[str]
    timezone: NotRequired[str]
    plusCode: NotRequired[str]
    thumbnailUrl: NotRequired[str]
    reservationUrl: NotRequired[str]
    attributes: list[str]


class GoogleMapsPlaceResponse(TypedDict):
    success: Literal[True]
    data: GoogleMapsPlaceResponseData
    creditsUsed: int
    requestId: str


class GoogleMapsReviewsResponseDataResultsItemDetailsItem(TypedDict):
    label: NotRequired[str]
    value: NotRequired[str]
    rating: NotRequired[float]


class GoogleMapsReviewsResponseDataResultsItem(TypedDict):
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
    details: NotRequired[list[GoogleMapsReviewsResponseDataResultsItemDetailsItem]]
    ownerReplyText: NotRequired[str]
    ownerReplyAt: NotRequired[str]


class GoogleMapsReviewsResponseData(TypedDict):
    results: list[GoogleMapsReviewsResponseDataResultsItem]
    cursor: NotRequired[str]


class GoogleMapsReviewsResponse(TypedDict):
    success: Literal[True]
    data: GoogleMapsReviewsResponseData
    creditsUsed: int
    requestId: str


class InstagramCommentsResponseDataResultsItem(TypedDict):
    commentId: NotRequired[str]
    commentUrl: str
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: NotRequired[str]
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: bool
    text: NotRequired[str]
    likes: NotRequired[int]
    publishedAt: NotRequired[str]


class InstagramCommentsResponseData(TypedDict):
    results: list[InstagramCommentsResponseDataResultsItem]
    cursor: NotRequired[str]


class InstagramCommentsResponse(TypedDict):
    success: Literal[True]
    data: InstagramCommentsResponseData
    creditsUsed: int
    requestId: str


class InstagramPostResponseData(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    type: InstagramPostResponseDataType
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
    comments: NotRequired[int]
    results: list[InstagramCommentsResponseDataResultsItem]


class InstagramPostResponse(TypedDict):
    success: Literal[True]
    data: InstagramPostResponseData
    creditsUsed: int
    requestId: str


class InstagramProfileResponseDataResultsItem(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    type: InstagramPostResponseDataType
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
    isVerified: NotRequired[bool]
    isPrivate: NotRequired[bool]
    followers: NotRequired[int]
    following: NotRequired[int]
    posts: NotRequired[int]
    avatarUrl: NotRequired[str]
    postsAnalyzed: NotRequired[int]
    averageLikes: NotRequired[float]
    averageComments: NotRequired[float]
    engagementRate: NotRequired[float]
    postsPerWeek: NotRequired[float]
    lastPostAt: NotRequired[str]
    results: list[InstagramProfileResponseDataResultsItem]
    cursor: NotRequired[str]


class InstagramProfileResponse(TypedDict):
    success: Literal[True]
    data: InstagramProfileResponseData
    creditsUsed: int
    requestId: str


class InstagramProfileReelsResponseDataResultsItem(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    likes: NotRequired[int]
    comments: NotRequired[int]
    views: NotRequired[int]
    imageUrl: NotRequired[str]
    isPinned: bool
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]


class InstagramProfileReelsResponseData(TypedDict):
    results: list[InstagramProfileReelsResponseDataResultsItem]
    cursor: NotRequired[str]


class InstagramProfileReelsResponse(TypedDict):
    success: Literal[True]
    data: InstagramProfileReelsResponseData
    creditsUsed: int
    requestId: str


class TiktokProfileResponseDataResultsItem(TypedDict):
    videoId: NotRequired[str]
    videoUrl: str
    type: TiktokProfileResponseDataResultsItemType
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
    results: list[TiktokProfileResponseDataResultsItem]
    cursor: NotRequired[str]


class TiktokProfileResponse(TypedDict):
    success: Literal[True]
    data: TiktokProfileResponseData
    creditsUsed: int
    requestId: str


class TiktokVideoResponseData(TypedDict):
    videoId: NotRequired[str]
    videoUrl: str
    type: TiktokProfileResponseDataResultsItemType
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
    results: list[TiktokProfileResponseDataResultsItem]
    cursor: NotRequired[str]


class TiktokHashtagResponse(TypedDict):
    success: Literal[True]
    data: TiktokHashtagResponseData
    creditsUsed: int
    requestId: str


class TiktokSoundResponseData(TypedDict):
    audioId: NotRequired[str]
    audioTitle: NotRequired[str]
    audioArtist: NotRequired[str]
    audioIsOriginal: NotRequired[bool]
    videos: NotRequired[int]
    results: list[TiktokProfileResponseDataResultsItem]
    cursor: NotRequired[str]


class TiktokSoundResponse(TypedDict):
    success: Literal[True]
    data: TiktokSoundResponseData
    creditsUsed: int
    requestId: str


class TiktokCommentsResponseDataResultsItem(TypedDict):
    commentId: NotRequired[str]
    text: NotRequired[str]
    imageUrls: NotRequired[list[str]]
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
    results: list[TiktokProfileResponseDataResultsItem | TiktokSearchResponseDataResultsItemOption1]
    cursor: NotRequired[str]


class TiktokSearchResponse(TypedDict):
    success: Literal[True]
    data: TiktokSearchResponseData
    creditsUsed: int
    requestId: str


class TiktokAdsSearchResponseDataResultsItem(TypedDict):
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


class TiktokAdsSearchResponseData(TypedDict):
    advertiserId: NotRequired[str]
    advertiserName: NotRequired[str]
    total: NotRequired[int]
    results: list[TiktokAdsSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class TiktokAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: TiktokAdsSearchResponseData
    creditsUsed: int
    requestId: str


class TiktokAdsAdResponseDataRegionsItem(TypedDict):
    country: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    ages: NotRequired[list[str]]
    genders: NotRequired[list[str]]


class TiktokAdsAdResponseData(TypedDict):
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
    imageUrls: list[str]
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
    countries: list[str]
    languages: list[str]
    interests: NotRequired[str]
    regions: list[TiktokAdsAdResponseDataRegionsItem]


class TiktokAdsAdResponse(TypedDict):
    success: Literal[True]
    data: TiktokAdsAdResponseData
    creditsUsed: int
    requestId: str


class TiktokShopSearchResponseDataResultsItem(TypedDict):
    productId: NotRequired[str]
    title: NotRequired[str]
    productUrl: str
    price: float
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    sold: NotRequired[int]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    imageUrl: NotRequired[str]
    shopId: NotRequired[str]
    shopName: NotRequired[str]


class TiktokShopSearchResponseData(TypedDict):
    results: list[TiktokShopSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class TiktokShopSearchResponse(TypedDict):
    success: Literal[True]
    data: TiktokShopSearchResponseData
    creditsUsed: int
    requestId: str


class TiktokShopProductsResponseData(TypedDict):
    shopId: NotRequired[str]
    shopName: NotRequired[str]
    rating: NotRequired[float]
    sold: NotRequired[int]
    products: NotRequired[int]
    reviews: NotRequired[int]
    followers: NotRequired[int]
    shopUrl: NotRequired[str]
    results: list[TiktokShopSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class TiktokShopProductsResponse(TypedDict):
    success: Literal[True]
    data: TiktokShopProductsResponseData
    creditsUsed: int
    requestId: str


class TiktokShopProductResponseDataVideosItem(TypedDict):
    videoId: NotRequired[str]
    videoUrl: str
    title: NotRequired[str]
    authorName: NotRequired[str]
    authorId: NotRequired[str]
    plays: NotRequired[int]
    likes: NotRequired[int]
    durationSeconds: NotRequired[float]


class TiktokShopProductResponseData(TypedDict):
    productId: NotRequired[str]
    title: NotRequired[str]
    productUrl: str
    price: float
    originalPrice: NotRequired[float]
    currency: NotRequired[str]
    sold: NotRequired[int]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    stock: NotRequired[int]
    shopId: NotRequired[str]
    shopName: NotRequired[str]
    shopUrl: NotRequired[str]
    shopRating: NotRequired[float]
    shopProducts: NotRequired[int]
    shopFollowers: NotRequired[int]
    imageUrls: list[str]
    videoUrl: NotRequired[str]
    videoDurationSeconds: NotRequired[float]
    videos: list[TiktokShopProductResponseDataVideosItem]


class TiktokShopProductResponse(TypedDict):
    success: Literal[True]
    data: TiktokShopProductResponseData
    creditsUsed: int
    requestId: str


class TiktokShopReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    rating: int
    text: NotRequired[str]
    authorName: NotRequired[str]
    isVerified: bool
    publishedAt: NotRequired[str]
    country: NotRequired[str]
    imageUrls: NotRequired[list[str]]


class TiktokShopReviewsResponseData(TypedDict):
    rating: NotRequired[float]
    reviews: NotRequired[int]
    results: list[TiktokShopReviewsResponseDataResultsItem]


class TiktokShopReviewsResponse(TypedDict):
    success: Literal[True]
    data: TiktokShopReviewsResponseData
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
    versions: NotRequired[int]
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
    salaryMin: NotRequired[float]
    salaryMax: NotRequired[float]
    salaryCurrency: NotRequired[str]
    salaryPeriod: NotRequired[LinkedinJobsSearchResponseDataResultsItemSalaryPeriod]
    salaryText: NotRequired[str]
    isEasyApply: NotRequired[bool]
    insight: NotRequired[str]


class LinkedinJobsSearchResponseData(TypedDict):
    results: list[LinkedinJobsSearchResponseDataResultsItem]
    page: int


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
    salaryMin: NotRequired[float]
    salaryMax: NotRequired[float]
    salaryCurrency: NotRequired[str]
    salaryPeriod: NotRequired[LinkedinJobsSearchResponseDataResultsItemSalaryPeriod]
    salaryText: NotRequired[str]
    isEasyApply: NotRequired[bool]
    applicants: NotRequired[int]
    applicantsText: NotRequired[str]
    applyUrl: NotRequired[str]
    seniority: NotRequired[str]
    employmentType: NotRequired[str]
    jobFunction: NotRequired[str]
    industries: NotRequired[str]
    description: NotRequired[str]
    descriptionHtml: NotRequired[str]


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
    isAboutTruncated: bool
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
    comments: NotRequired[int]
    imageUrls: NotRequired[list[str]]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]


class LinkedinPostsResponseData(TypedDict):
    results: list[LinkedinPostsResponseDataResultsItem]
    cursor: NotRequired[str]


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
    priceCurrency: NotRequired[Literal["USD"]]
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
    total: NotRequired[int]
    results: list[ZillowSearchResponseDataResultsItem]
    page: int
    totalPages: NotRequired[int]


class ZillowSearchResponse(TypedDict):
    success: Literal[True]
    data: ZillowSearchResponseData
    creditsUsed: int
    requestId: str


class ZillowPropertyResponseDataPriceHistoryItem(TypedDict):
    eventDate: str
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
    priceCurrency: NotRequired[Literal["USD"]]
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
    experienceLevel: NotRequired[UpworkSearchExperienceLevel]
    workload: NotRequired[UpworkSearchWorkload]
    duration: NotRequired[UpworkSearchDuration]
    hourlyRateMin: NotRequired[float]
    hourlyRateMax: NotRequired[float]
    fixedBudget: NotRequired[float]
    budgetCurrency: NotRequired[str]
    durationWeeks: NotRequired[int]
    publishedAt: NotRequired[str]


class UpworkSearchResponseData(TypedDict):
    total: NotRequired[int]
    results: list[UpworkSearchResponseDataResultsItem]
    page: int


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
    experienceLevel: NotRequired[UpworkSearchExperienceLevel]
    workload: NotRequired[UpworkSearchWorkload]
    duration: NotRequired[UpworkSearchDuration]
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


class GoogleTrendsRelatedResponseDataRisingItem(TypedDict):
    query: NotRequired[str]
    increasePercent: NotRequired[float]
    isBreakout: bool


class GoogleTrendsRelatedResponseDataResultsItem(TypedDict):
    query: NotRequired[str]
    value: float


class GoogleTrendsRelatedResponseData(TypedDict):
    rising: list[GoogleTrendsRelatedResponseDataRisingItem]
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
    trendUrl: str


class GoogleTrendsTrendingResponseData(TypedDict):
    results: list[GoogleTrendsTrendingResponseDataResultsItem]


class GoogleTrendsTrendingResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsTrendingResponseData
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
    jobTypes: NotRequired[list[IndeedSearchJobType]]
    isRemote: bool
    isHybrid: bool
    experienceLevels: NotRequired[list[IndeedSearchExperienceLevel]]
    educationLevels: NotRequired[list[IndeedSearchEducation]]
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
    jobTypes: list[IndeedSearchJobType]
    isRemote: bool
    isHybrid: bool
    experienceLevels: list[IndeedSearchExperienceLevel]
    educationLevels: list[IndeedSearchEducation]
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


class CareersJobsResponseDataResultsItem(TypedDict):
    jobId: NotRequired[str]
    jobUrl: str
    title: NotRequired[str]
    department: NotRequired[str]
    team: NotRequired[str]
    location: NotRequired[str]
    workplaceType: NotRequired[CareersJobsResponseDataResultsItemWorkplaceType]
    employmentType: NotRequired[str]
    publishedAt: NotRequired[str]
    updatedAt: NotRequired[str]
    postedText: NotRequired[str]
    boardUrl: str


class CareersJobsResponseData(TypedDict):
    results: list[CareersJobsResponseDataResultsItem]
    cursor: NotRequired[str]


class CareersJobsResponse(TypedDict):
    success: Literal[True]
    data: CareersJobsResponseData
    creditsUsed: int
    requestId: str


class CareersJobResponseData(TypedDict):
    jobId: NotRequired[str]
    jobUrl: str
    title: NotRequired[str]
    department: NotRequired[str]
    team: NotRequired[str]
    location: NotRequired[str]
    workplaceType: NotRequired[CareersJobsResponseDataResultsItemWorkplaceType]
    employmentType: NotRequired[str]
    publishedAt: NotRequired[str]
    updatedAt: NotRequired[str]
    postedText: NotRequired[str]
    description: NotRequired[str]
    salaryMin: NotRequired[float]
    salaryMax: NotRequired[float]
    salaryCurrency: NotRequired[str]
    salaryPeriod: NotRequired[IndeedSearchResponseDataResultsItemSalaryPeriod]
    applyUrl: NotRequired[str]
    boardUrl: str


class CareersJobResponse(TypedDict):
    success: Literal[True]
    data: CareersJobResponseData
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
    hours: list[GoogleMapsSearchResponseDataResultsItemHoursItem]
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
    stayMonth: NotRequired[str]
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
    page: int


class TripadvisorReviewsResponse(TypedDict):
    success: Literal[True]
    data: TripadvisorReviewsResponseData
    creditsUsed: int
    requestId: str


class GoogleFlightsDepartureTime(TypedDict):
    earliest: NotRequired[int]
    latest: NotRequired[int]


class GoogleFlightsArrivalTime(TypedDict):
    earliest: NotRequired[int]
    latest: NotRequired[int]


class GoogleFlightsResponseDataResultsItemLegsItem(TypedDict):
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


class GoogleFlightsResponseDataResultsItemLayoversItem(TypedDict):
    airport: NotRequired[str]
    name: NotRequired[str]
    city: NotRequired[str]
    durationSeconds: NotRequired[int]


class GoogleFlightsResponseDataResultsItem(TypedDict):
    isBest: bool
    price: NotRequired[float]
    priceCurrency: NotRequired[Literal["USD"]]
    airlines: NotRequired[list[str]]
    stops: int
    durationSeconds: NotRequired[int]
    departureLocalTime: NotRequired[str]
    arrivalLocalTime: NotRequired[str]
    legs: NotRequired[list[GoogleFlightsResponseDataResultsItemLegsItem]]
    layovers: NotRequired[list[GoogleFlightsResponseDataResultsItemLayoversItem]]
    emissionsGrams: NotRequired[int]
    typicalEmissionsGrams: NotRequired[int]


class GoogleFlightsResponseData(TypedDict):
    cabin: GoogleFlightsCabin
    tripType: GoogleFlightsResponseDataTripType
    adults: int
    results: list[GoogleFlightsResponseDataResultsItem]


class GoogleFlightsResponse(TypedDict):
    success: Literal[True]
    data: GoogleFlightsResponseData
    creditsUsed: int
    requestId: str


class GoogleHotelsResponseDataResultsItem(TypedDict):
    name: str
    hotelId: str
    hotelUrl: str
    price: NotRequired[float]
    totalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    deal: NotRequired[str]
    dealDescription: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    hotelClass: NotRequired[int]
    amenities: NotRequired[list[str]]
    position: int


class GoogleHotelsResponseData(TypedDict):
    checkIn: str
    checkOut: str
    results: list[GoogleHotelsResponseDataResultsItem]
    cursor: NotRequired[str]


class GoogleHotelsResponse(TypedDict):
    success: Literal[True]
    data: GoogleHotelsResponseData
    creditsUsed: int
    requestId: str


class BookingSearchResponseDataResultsItem(TypedDict):
    position: int
    hotelId: NotRequired[str]
    hotelUrl: str
    name: NotRequired[str]
    reviewScore: NotRequired[float]
    reviews: NotRequired[int]
    price: NotRequired[float]
    taxesAndFees: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    stars: NotRequired[int]
    address: NotRequired[str]
    city: NotRequired[str]
    countryCode: NotRequired[str]
    area: NotRequired[str]
    distanceText: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    imageUrl: NotRequired[str]
    hasFreeCancellation: bool


class BookingSearchResponseData(TypedDict):
    place: NotRequired[str]
    checkIn: str
    checkOut: str
    total: NotRequired[int]
    results: list[BookingSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class BookingSearchResponse(TypedDict):
    success: Literal[True]
    data: BookingSearchResponseData
    creditsUsed: int
    requestId: str


class BookingHotelResponseDataScoresItem(TypedDict):
    category: NotRequired[str]
    score: float


class BookingHotelResponseDataFacilitiesItem(TypedDict):
    group: NotRequired[str]
    name: NotRequired[str]


class BookingHotelResponseDataRoomsItem(TypedDict):
    roomId: NotRequired[str]
    name: NotRequired[str]
    sizeSquareMeters: NotRequired[float]
    description: NotRequired[str]


class BookingHotelResponseData(TypedDict):
    hotelId: NotRequired[str]
    hotelUrl: str
    name: NotRequired[str]
    type: NotRequired[str]
    stars: NotRequired[int]
    reviewScore: NotRequired[float]
    reviews: NotRequired[int]
    description: NotRequired[str]
    scores: list[BookingHotelResponseDataScoresItem]
    addressFull: NotRequired[str]
    addressStreet: NotRequired[str]
    addressCity: NotRequired[str]
    addressCountryCode: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    checkInFrom: NotRequired[str]
    checkOutUntil: NotRequired[str]
    facilities: list[BookingHotelResponseDataFacilitiesItem]
    rooms: list[BookingHotelResponseDataRoomsItem]
    imageUrls: list[str]


class BookingHotelResponse(TypedDict):
    success: Literal[True]
    data: BookingHotelResponseData
    creditsUsed: int
    requestId: str


class BookingHotelReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    score: NotRequired[float]
    title: NotRequired[str]
    positiveText: NotRequired[str]
    negativeText: NotRequired[str]
    language: NotRequired[str]
    createdAt: NotRequired[str]
    travelerType: NotRequired[str]
    authorCountryCode: NotRequired[str]
    roomName: NotRequired[str]
    nights: NotRequired[int]
    checkIn: NotRequired[str]
    checkOut: NotRequired[str]
    ownerReplyText: NotRequired[str]


class BookingHotelReviewsResponseData(TypedDict):
    hotelId: NotRequired[str]
    total: int
    results: list[BookingHotelReviewsResponseDataResultsItem]
    cursor: NotRequired[str]


class BookingHotelReviewsResponse(TypedDict):
    success: Literal[True]
    data: BookingHotelReviewsResponseData
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
    total: NotRequired[int]
    results: list[AmazonSearchResponseDataResultsItem]
    page: int


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
    page: int


class AmazonBestsellersResponse(TypedDict):
    success: Literal[True]
    data: AmazonBestsellersResponseData
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
    page: int


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


class GooglePlayAppResponseData(TypedDict):
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


class GooglePlayAppResponse(TypedDict):
    success: Literal[True]
    data: GooglePlayAppResponseData
    creditsUsed: int
    requestId: str


class GooglePlaySearchResponseDataResultsItem(TypedDict):
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


class GooglePlaySearchResponseData(TypedDict):
    results: list[GooglePlaySearchResponseDataResultsItem]


class GooglePlaySearchResponse(TypedDict):
    success: Literal[True]
    data: GooglePlaySearchResponseData
    creditsUsed: int
    requestId: str


class GooglePlayReviewsResponseDataResultsItem(TypedDict):
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


class GooglePlayReviewsResponseData(TypedDict):
    results: list[GooglePlayReviewsResponseDataResultsItem]
    cursor: NotRequired[str]


class GooglePlayReviewsResponse(TypedDict):
    success: Literal[True]
    data: GooglePlayReviewsResponseData
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
    imageWidth: NotRequired[int]
    imageHeight: NotRequired[int]
    dominantColor: NotRequired[str]
    videoUrl: NotRequired[str]
    videoDurationSeconds: NotRequired[float]
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


class PinterestPinResponseData(TypedDict):
    pinId: NotRequired[str]
    pinUrl: str
    title: NotRequired[str]
    text: NotRequired[str]
    altText: NotRequired[str]
    linkUrl: NotRequired[str]
    domain: NotRequired[str]
    publishedAt: NotRequired[str]
    imageUrl: NotRequired[str]
    imageWidth: NotRequired[int]
    imageHeight: NotRequired[int]
    dominantColor: NotRequired[str]
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


class PinterestPinResponse(TypedDict):
    success: Literal[True]
    data: PinterestPinResponseData
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
    results: list[PinterestPinResponseData]
    cursor: NotRequired[str]


class PinterestBoardResponse(TypedDict):
    success: Literal[True]
    data: PinterestBoardResponseData
    creditsUsed: int
    requestId: str


class PinterestProfileResponseData(TypedDict):
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
    results: list[PinterestPinResponseData]
    cursor: NotRequired[str]


class PinterestProfileResponse(TypedDict):
    success: Literal[True]
    data: PinterestProfileResponseData
    creditsUsed: int
    requestId: str


class XProfileResponseData(TypedDict):
    userId: NotRequired[str]
    username: NotRequired[str]
    profileUrl: str
    name: NotRequired[str]
    bio: NotRequired[str]
    location: NotRequired[str]
    website: NotRequired[str]
    joinedAt: NotRequired[str]
    followers: NotRequired[int]
    following: NotRequired[int]
    posts: NotRequired[int]
    isVerified: bool
    verifiedType: NotRequired[str]
    isProtected: bool
    avatarUrl: NotRequired[str]
    bannerUrl: NotRequired[str]


class XProfileResponse(TypedDict):
    success: Literal[True]
    data: XProfileResponseData
    creditsUsed: int
    requestId: str


class XPostResponseDataMediaItem(TypedDict):
    type: XPostResponseDataMediaItemType
    url: str
    thumbnailUrl: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    durationSeconds: NotRequired[float]
    altText: NotRequired[str]


class XPostResponseData(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    language: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    reposts: NotRequired[int]
    quotes: NotRequired[int]
    bookmarks: NotRequired[int]
    views: NotRequired[int]
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
    quotedUrl: NotRequired[str]
    quotedText: NotRequired[str]
    quotedAuthorUsername: NotRequired[str]
    isEdited: bool
    isSensitive: bool


class XPostResponse(TypedDict):
    success: Literal[True]
    data: XPostResponseData
    creditsUsed: int
    requestId: str


class MetaAdsAdResponseDataAudienceAgeGenderItem(TypedDict):
    age: NotRequired[str]
    female: float
    male: float
    unknown: float


class MetaAdsAdResponseDataAudienceRegionsItem(TypedDict):
    region: NotRequired[str]
    share: float


class MetaAdsAdResponseDataEuReachByCountryItem(TypedDict):
    country: NotRequired[str]
    age: NotRequired[str]
    female: int
    male: int
    unknown: int


class MetaAdsAdResponseDataPayersItem(TypedDict):
    paidBy: NotRequired[str]
    beneficiary: NotRequired[str]


class MetaAdsAdResponseData(TypedDict):
    adId: NotRequired[str]
    adUrl: str
    pageId: NotRequired[str]
    pageName: NotRequired[str]
    pageUrl: NotRequired[str]
    pageAvatarUrl: NotRequired[str]
    pageCategories: list[str]
    pageLikes: NotRequired[int]
    isActive: bool
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    platforms: list[str]
    format: NotRequired[str]
    text: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    linkDescription: NotRequired[str]
    ctaText: NotRequired[str]
    imageUrls: list[str]
    videoUrls: list[str]
    cards: list[MetaAdsPageResponseDataResultsItemCardsItem]
    versions: NotRequired[int]
    categories: list[str]
    paidBy: NotRequired[str]
    spendMin: NotRequired[int]
    spendMax: NotRequired[int]
    spendCurrency: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    reachMin: NotRequired[int]
    reachMax: NotRequired[int]
    countries: list[str]
    advertiserDescription: NotRequired[str]
    advertiserCategory: NotRequired[str]
    advertiserVerification: NotRequired[str]
    advertiserInstagram: NotRequired[str]
    advertiserInstagramFollowers: NotRequired[int]
    audienceAgeGender: list[MetaAdsAdResponseDataAudienceAgeGenderItem]
    audienceRegions: list[MetaAdsAdResponseDataAudienceRegionsItem]
    euReachTotal: NotRequired[int]
    euReachByCountry: list[MetaAdsAdResponseDataEuReachByCountryItem]
    payers: list[MetaAdsAdResponseDataPayersItem]


class MetaAdsAdResponse(TypedDict):
    success: Literal[True]
    data: MetaAdsAdResponseData
    creditsUsed: int
    requestId: str


class LinkedinAdsSearchResponseDataResultsItem(TypedDict):
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


class LinkedinAdsSearchResponseData(TypedDict):
    total: NotRequired[int]
    results: list[LinkedinAdsSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class LinkedinAdsSearchResponse(TypedDict):
    success: Literal[True]
    data: LinkedinAdsSearchResponseData
    creditsUsed: int
    requestId: str


class LinkedinAdsAdResponseDataCountriesItem(TypedDict):
    country: NotRequired[str]
    share: NotRequired[float]


class LinkedinAdsAdResponseDataTargetingItem(TypedDict):
    parameter: NotRequired[str]
    description: NotRequired[str]


class LinkedinAdsAdResponseDataTargetingUsedItem(TypedDict):
    parameter: NotRequired[str]
    isTargeted: bool
    isExcluded: bool


class LinkedinAdsAdResponseData(TypedDict):
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
    imageUrls: list[str]
    paidBy: NotRequired[str]
    ctaText: NotRequired[str]
    videoUrls: list[str]
    firstShownAt: NotRequired[str]
    lastShownAt: NotRequired[str]
    impressionsMin: NotRequired[int]
    impressionsMax: NotRequired[int]
    countries: list[LinkedinAdsAdResponseDataCountriesItem]
    targeting: list[LinkedinAdsAdResponseDataTargetingItem]
    targetingUsed: list[LinkedinAdsAdResponseDataTargetingUsedItem]


class LinkedinAdsAdResponse(TypedDict):
    success: Literal[True]
    data: LinkedinAdsAdResponseData
    creditsUsed: int
    requestId: str


class GoogleTrendsInterestResponseDataResultsItem(TypedDict):
    recordedAt: str
    values: NotRequired[dict[str, float]]
    isPartial: bool


class GoogleTrendsInterestResponseData(TypedDict):
    averages: NotRequired[dict[str, float]]
    results: list[GoogleTrendsInterestResponseDataResultsItem]


class GoogleTrendsInterestResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsInterestResponseData
    creditsUsed: int
    requestId: str


class GoogleTrendsRegionsResponseDataResultsItem(TypedDict):
    code: NotRequired[str]
    name: NotRequired[str]
    values: NotRequired[dict[str, float]]


class GoogleTrendsRegionsResponseData(TypedDict):
    results: list[GoogleTrendsRegionsResponseDataResultsItem]


class GoogleTrendsRegionsResponse(TypedDict):
    success: Literal[True]
    data: GoogleTrendsRegionsResponseData
    creditsUsed: int
    requestId: str


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
    threads: NotRequired[int]
    avatarUrl: NotRequired[str]


class ThreadsProfileResponse(TypedDict):
    success: Literal[True]
    data: ThreadsProfileResponseData
    creditsUsed: int
    requestId: str


class ThreadsProfilePostsResponseDataResultsItem(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    reposts: NotRequired[int]
    quotes: NotRequired[int]
    shares: NotRequired[int]
    imageUrls: NotRequired[list[str]]
    videoUrls: NotRequired[list[str]]
    imageDescription: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    quotedPostUrl: NotRequired[str]
    isPinned: bool
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: str
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: bool


class ThreadsProfilePostsResponseData(TypedDict):
    results: list[ThreadsProfilePostsResponseDataResultsItem]
    cursor: NotRequired[str]


class ThreadsProfilePostsResponse(TypedDict):
    success: Literal[True]
    data: ThreadsProfilePostsResponseData
    creditsUsed: int
    requestId: str


class ThreadsPostResponseData(TypedDict):
    postId: NotRequired[str]
    postCode: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]
    reposts: NotRequired[int]
    quotes: NotRequired[int]
    shares: NotRequired[int]
    imageUrls: list[str]
    videoUrls: list[str]
    imageDescription: NotRequired[str]
    linkUrl: NotRequired[str]
    linkTitle: NotRequired[str]
    quotedPostUrl: NotRequired[str]
    isPinned: bool
    authorId: NotRequired[str]
    authorUsername: NotRequired[str]
    authorUrl: str
    authorAvatarUrl: NotRequired[str]
    authorIsVerified: bool
    results: list[ThreadsProfilePostsResponseDataResultsItem]
    cursor: NotRequired[str]


class ThreadsPostResponse(TypedDict):
    success: Literal[True]
    data: ThreadsPostResponseData
    creditsUsed: int
    requestId: str


class TrustpilotCompanyResponseData(TypedDict):
    companyId: NotRequired[str]
    companyDomain: NotRequired[str]
    companyUrl: str
    name: NotRequired[str]
    website: NotRequired[str]
    description: NotRequired[str]
    trustScore: NotRequired[float]
    stars: NotRequired[float]
    reviews: NotRequired[int]
    ratingsOne: NotRequired[int]
    ratingsTwo: NotRequired[int]
    ratingsThree: NotRequired[int]
    ratingsFour: NotRequired[int]
    ratingsFive: NotRequired[int]
    categories: list[str]
    isClaimed: bool
    isClosed: bool
    email: NotRequired[str]
    phone: NotRequired[str]
    addressStreet: NotRequired[str]
    addressCity: NotRequired[str]
    addressPostalCode: NotRequired[str]
    addressCountry: NotRequired[str]
    negativeReviewsRepliedPercent: NotRequired[float]
    averageDaysToReply: NotRequired[float]


class TrustpilotCompanyResponse(TypedDict):
    success: Literal[True]
    data: TrustpilotCompanyResponseData
    creditsUsed: int
    requestId: str


class TrustpilotCompanyReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    reviewUrl: str
    rating: int
    title: NotRequired[str]
    text: NotRequired[str]
    language: NotRequired[str]
    publishedAt: NotRequired[str]
    experiencedDate: NotRequired[str]
    isVerified: bool
    authorName: NotRequired[str]
    authorCountry: NotRequired[str]
    ownerReplyText: NotRequired[str]
    ownerReplyAt: NotRequired[str]


class TrustpilotCompanyReviewsResponseData(TypedDict):
    companyDomain: NotRequired[str]
    companyName: NotRequired[str]
    total: NotRequired[int]
    results: list[TrustpilotCompanyReviewsResponseDataResultsItem]
    page: int


class TrustpilotCompanyReviewsResponse(TypedDict):
    success: Literal[True]
    data: TrustpilotCompanyReviewsResponseData
    creditsUsed: int
    requestId: str


class TrustpilotSearchResponseDataResultsItem(TypedDict):
    companyId: NotRequired[str]
    companyDomain: NotRequired[str]
    companyUrl: str
    name: NotRequired[str]
    website: NotRequired[str]
    trustScore: NotRequired[float]
    stars: NotRequired[float]
    reviews: NotRequired[int]
    categories: NotRequired[list[str]]
    addressStreet: NotRequired[str]
    addressCity: NotRequired[str]
    addressPostalCode: NotRequired[str]
    addressCountry: NotRequired[str]


class TrustpilotSearchResponseData(TypedDict):
    total: NotRequired[int]
    results: list[TrustpilotSearchResponseDataResultsItem]
    page: int


class TrustpilotSearchResponse(TypedDict):
    success: Literal[True]
    data: TrustpilotSearchResponseData
    creditsUsed: int
    requestId: str


class EbaySearchResponseDataResultsItem(TypedDict):
    itemId: NotRequired[str]
    itemUrl: str
    title: NotRequired[str]
    imageUrl: NotRequired[str]
    price: NotRequired[float]
    priceMax: NotRequired[float]
    isPriceHidden: bool
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    shippingCost: NotRequired[float]
    isPickupOnly: bool
    totalPrice: NotRequired[float]
    condition: NotRequired[str]
    isAuction: bool
    bids: NotRequired[int]
    timeLeft: NotRequired[str]
    hasBestOffer: bool
    itemLocation: NotRequired[str]
    quantitySold: NotRequired[int]
    watchers: NotRequired[int]
    sellerName: NotRequired[str]
    sellerFeedbackPercent: NotRequired[float]
    sellerFeedbackScore: NotRequired[int]


class EbaySearchResponseData(TypedDict):
    total: NotRequired[int]
    results: list[EbaySearchResponseDataResultsItem]
    page: int


class EbaySearchResponse(TypedDict):
    success: Literal[True]
    data: EbaySearchResponseData
    creditsUsed: int
    requestId: str


class EbayItemResponseData(TypedDict):
    itemId: NotRequired[str]
    itemUrl: str
    title: NotRequired[str]
    price: NotRequired[float]
    originalPrice: NotRequired[float]
    priceCurrency: NotRequired[str]
    condition: NotRequired[str]
    isAuction: bool
    bids: NotRequired[int]
    isEnded: bool
    endedAt: NotRequired[str]
    isSold: bool
    soldPrice: NotRequired[float]
    soldAt: NotRequired[str]
    isAvailable: NotRequired[bool]
    quantityAvailable: NotRequired[int]
    quantitySold: NotRequired[int]
    brand: NotRequired[str]
    model: NotRequired[str]
    specifics: list[ZillowPropertyResponseDataFactsItem]
    categories: list[str]
    sellerName: NotRequired[str]
    sellerFeedbackScore: NotRequired[int]
    sellerFeedbackPercent: NotRequired[float]
    shippingCost: NotRequired[float]
    shippingPostalCode: NotRequired[str]
    itemLocation: NotRequired[str]
    returnsAccepted: NotRequired[bool]
    returnDays: NotRequired[int]
    listedAt: NotRequired[str]
    imageUrls: list[str]
    description: NotRequired[str]


class EbayItemResponse(TypedDict):
    success: Literal[True]
    data: EbayItemResponseData
    creditsUsed: int
    requestId: str


class AirbnbSearchResponseDataResultsItem(TypedDict):
    listingId: NotRequired[str]
    listingUrl: str
    title: NotRequired[str]
    propertyType: NotRequired[str]
    area: NotRequired[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    priceTotal: NotRequired[float]
    priceBeforeDiscount: NotRequired[float]
    pricePerNight: NotRequired[float]
    priceCurrency: NotRequired[AirbnbSearchCurrency]
    badges: NotRequired[list[str]]
    imageUrls: NotRequired[list[str]]
    latitude: NotRequired[float]
    longitude: NotRequired[float]


class AirbnbSearchResponseData(TypedDict):
    location: NotRequired[str]
    results: list[AirbnbSearchResponseDataResultsItem]
    cursor: NotRequired[str]


class AirbnbSearchResponse(TypedDict):
    success: Literal[True]
    data: AirbnbSearchResponseData
    creditsUsed: int
    requestId: str


class AirbnbListingResponseData(TypedDict):
    listingId: NotRequired[str]
    listingUrl: str
    title: NotRequired[str]
    description: NotRequired[str]
    propertyType: NotRequired[str]
    location: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]
    hostName: NotRequired[str]
    hostIsSuperhost: NotRequired[bool]
    guests: NotRequired[int]
    bedrooms: NotRequired[int]
    beds: NotRequired[int]
    bathrooms: NotRequired[float]
    amenities: list[str]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    isGuestFavorite: NotRequired[bool]
    ratingAccuracy: NotRequired[float]
    ratingCheckin: NotRequired[float]
    ratingCleanliness: NotRequired[float]
    ratingCommunication: NotRequired[float]
    ratingLocation: NotRequired[float]
    ratingValue: NotRequired[float]
    houseRules: list[str]
    imageUrls: list[str]
    isAvailable: NotRequired[bool]
    priceTotal: NotRequired[float]
    priceBeforeDiscount: NotRequired[float]
    pricePerNight: NotRequired[float]
    priceCurrency: NotRequired[AirbnbSearchCurrency]


class AirbnbListingResponse(TypedDict):
    success: Literal[True]
    data: AirbnbListingResponseData
    creditsUsed: int
    requestId: str


class AirbnbReviewsResponseDataResultsItem(TypedDict):
    reviewId: NotRequired[str]
    rating: NotRequired[float]
    text: NotRequired[str]
    language: NotRequired[str]
    translatedText: NotRequired[str]
    createdAt: NotRequired[str]
    authorName: NotRequired[str]
    stayNote: NotRequired[str]
    hostReplyText: NotRequired[str]


class AirbnbReviewsResponseData(TypedDict):
    listingId: NotRequired[str]
    total: NotRequired[int]
    results: list[AirbnbReviewsResponseDataResultsItem]
    page: int


class AirbnbReviewsResponse(TypedDict):
    success: Literal[True]
    data: AirbnbReviewsResponseData
    creditsUsed: int
    requestId: str


class FacebookPageResponseData(TypedDict):
    pageId: NotRequired[str]
    username: NotRequired[str]
    pageUrl: str
    name: NotRequired[str]
    category: NotRequired[str]
    isVerified: bool
    followers: NotRequired[int]
    likes: NotRequired[int]
    talkingAboutThis: NotRequired[int]
    bio: NotRequired[str]
    address: NotRequired[str]
    phone: NotRequired[str]
    email: NotRequired[str]
    websites: list[str]
    priceRange: NotRequired[str]
    avatarUrl: NotRequired[str]
    coverUrl: NotRequired[str]


class FacebookPageResponse(TypedDict):
    success: Literal[True]
    data: FacebookPageResponseData
    creditsUsed: int
    requestId: str


class FacebookPostResponseDataMediaItem(TypedDict):
    type: FacebookPostResponseDataMediaItemType
    url: NotRequired[str]
    imageUrl: NotRequired[str]
    videoUrl: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    durationSeconds: NotRequired[float]
    altText: NotRequired[str]


class FacebookPostResponseDataReactions(TypedDict):
    total: int
    like: int
    love: int
    care: int
    haha: int
    wow: int
    sad: int
    angry: int


class FacebookPostResponseData(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    authorId: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    media: list[FacebookPostResponseDataMediaItem]
    reactions: NotRequired[FacebookPostResponseDataReactions]
    comments: NotRequired[int]
    shares: NotRequired[int]


class FacebookPostResponse(TypedDict):
    success: Literal[True]
    data: FacebookPostResponseData
    creditsUsed: int
    requestId: str


class FacebookPostCommentsResponseDataResultsItem(TypedDict):
    commentId: NotRequired[str]
    commentUrl: NotRequired[str]
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    authorId: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    likes: NotRequired[int]
    replies: NotRequired[int]


class FacebookPostCommentsResponseData(TypedDict):
    results: list[FacebookPostCommentsResponseDataResultsItem]
    cursor: NotRequired[str]


class FacebookPostCommentsResponse(TypedDict):
    success: Literal[True]
    data: FacebookPostCommentsResponseData
    creditsUsed: int
    requestId: str


class FacebookPagePostsResponseDataResultsItem(TypedDict):
    postId: NotRequired[str]
    postUrl: str
    text: NotRequired[str]
    publishedAt: NotRequired[str]
    authorId: NotRequired[str]
    authorName: NotRequired[str]
    authorUrl: NotRequired[str]
    media: NotRequired[list[FacebookPostResponseDataMediaItem]]
    reactions: NotRequired[FacebookPostResponseDataReactions]
    comments: NotRequired[int]
    shares: NotRequired[int]


class FacebookPagePostsResponseData(TypedDict):
    results: list[FacebookPagePostsResponseDataResultsItem]
    cursor: NotRequired[str]


class FacebookPagePostsResponse(TypedDict):
    success: Literal[True]
    data: FacebookPagePostsResponseData
    creditsUsed: int
    requestId: str


class FacebookMarketplaceSearchResponseDataResultsItem(TypedDict):
    listingId: NotRequired[str]
    listingUrl: str
    title: NotRequired[str]
    price: NotRequired[float]
    priceText: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    imageUrl: NotRequired[str]
    publishedAt: NotRequired[str]
    isPending: bool


class FacebookMarketplaceSearchResponseData(TypedDict):
    location: NotRequired[str]
    latitude: float
    longitude: float
    results: list[FacebookMarketplaceSearchResponseDataResultsItem]


class FacebookMarketplaceSearchResponse(TypedDict):
    success: Literal[True]
    data: FacebookMarketplaceSearchResponseData
    creditsUsed: int
    requestId: str


WebSearchResponse = GoogleSearchResponse
WebSearchResponseData = GoogleSearchResponseData
