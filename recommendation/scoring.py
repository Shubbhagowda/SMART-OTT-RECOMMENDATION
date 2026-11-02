# scoring.py


def calculate_score(preferences, platform_details):

    genres = preferences.get("genres", [])
    languages = preferences.get("languages", [])
    content_types = preferences.get("content_types", [])

    platform_genres = platform_details.get("genres", [])
    platform_languages = platform_details.get("languages", [])
    platform_content = platform_details.get("content_types", [])

    genre_matches = [
        item for item in genres
        if item.lower() in [x.lower() for x in platform_genres]
    ]

    language_matches = [
        item for item in languages
        if item.lower() in [x.lower() for x in platform_languages]
    ]

    content_matches = [
        item for item in content_types
        if item.lower() in [x.lower() for x in platform_content]
    ]

    weights = {
        "genres": 40,
        "languages": 30,
        "content_types": 30
    }

    categories = [
        ("genres", genres, genre_matches),
        ("languages", languages, language_matches),
        ("content_types", content_types, content_matches)
    ]

    active_weight = sum(
        weights[name]
        for name, selected, matches in categories
        if selected
    )

    total_score = 0

    if active_weight > 0:
        for name, selected, matches in categories:

            if selected:
                category_score = (
                    len(matches) / len(selected)
                ) * 100

                total_score += (
                    category_score * weights[name]
                ) / active_weight

    return {
        "score": round(total_score, 2),
        "genre_matches": genre_matches,
        "language_matches": language_matches,
        "content_type_matches": content_matches
    }