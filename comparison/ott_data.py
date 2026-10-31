# OTT Platform Information

OTT_PLATFORMS = {
    "Netflix": {
        "name": "Netflix",
        "languages": [
            "English", "Hindi", "Kannada",
            "Tamil", "Telugu", "Malayalam"
        ],
        "genres": [
            "Action", "Comedy", "Drama",
            "Thriller", "Romance", "Horror"
        ],
        "content_types": ["Movies", "Web Series"],
        "description": "Global streaming platform"
    },

    "Amazon Prime Video": {
        "name": "Amazon Prime Video",
        "languages": [
            "English", "Hindi", "Kannada",
            "Tamil", "Telugu", "Malayalam"
        ],
        "genres": [
            "Action", "Comedy", "Drama",
            "Thriller", "Romance"
        ],
        "content_types": ["Movies", "Web Series"],
        "description": "Streaming and entertainment platform"
    },

    "JioHotstar": {
        "name": "JioHotstar",
        "languages": [
            "English", "Hindi", "Kannada",
            "Tamil", "Telugu", "Malayalam"
        ],
        "genres": [
            "Action", "Comedy", "Drama",
            "Sports", "Thriller"
        ],
        "content_types": [
            "Movies", "Web Series", "Sports"
        ],
        "description": "Indian entertainment streaming platform"
    },

    "ZEE5": {
        "name": "ZEE5",
        "languages": [
            "Hindi", "Kannada", "Tamil",
            "Telugu", "Malayalam", "English"
        ],
        "genres": [
            "Drama", "Comedy", "Thriller",
            "Romance", "Action"
        ],
        "content_types": ["Movies", "Web Series"],
        "description": "Indian digital entertainment platform"
    },

    "SonyLIV": {
        "name": "SonyLIV",
        "languages": [
            "Hindi", "English", "Kannada",
            "Tamil", "Telugu", "Malayalam"
        ],
        "genres": [
            "Drama", "Thriller", "Comedy",
            "Action", "Sports"
        ],
        "content_types": [
            "Movies", "Web Series", "Sports"
        ],
        "description": "Entertainment and sports streaming platform"
    }
}


def get_all_platforms():
    return OTT_PLATFORMS


def get_platform(platform_name):
    return OTT_PLATFORMS.get(platform_name)
