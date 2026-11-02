# preference_handler.py

SUPPORTED_GENRES = [
    "Action", "Comedy", "Drama", "Thriller",
    "Romance", "Horror", "Sports"
]

SUPPORTED_LANGUAGES = [
    "English", "Hindi", "Kannada",
    "Tamil", "Telugu", "Malayalam"
]

SUPPORTED_CONTENT_TYPES = [
    "Movies", "Web Series", "Sports"
]


def validate_preferences(data):

    if not isinstance(data, dict):
        raise ValueError("Invalid preference data.")

    genres = data.get("genres", [])
    languages = data.get("languages", [])
    content_types = data.get("content_types", [])
    budget = data.get("budget")

    if not isinstance(genres, list):
        raise ValueError("Genres must be a list.")

    if not isinstance(languages, list):
        raise ValueError("Languages must be a list.")

    if not isinstance(content_types, list):
        raise ValueError("Content types must be a list.")

    if budget is None or isinstance(budget, bool):
        raise ValueError("Please enter your monthly budget.")

    try:
        budget = float(budget)
    except (ValueError, TypeError):
        raise ValueError("Budget must be a valid number.")

    if budget <= 0:
        raise ValueError("Budget must be greater than zero.")

    def clean_values(values, supported, field):

        result = []

        for value in values:

            if not isinstance(value, str):
                raise ValueError(f"Invalid {field}.")

            value = value.strip()

            if not value:
                continue

            match = next(
                (
                    item for item in supported
                    if item.lower() == value.lower()
                ),
                None
            )

            if match is None:
                raise ValueError(
                    f"Unsupported {field}: {value}"
                )

            if match not in result:
                result.append(match)

        return result

    preferences = {
        "genres": clean_values(
            genres, SUPPORTED_GENRES, "genre"
        ),
        "languages": clean_values(
            languages, SUPPORTED_LANGUAGES, "language"
        ),
        "content_types": clean_values(
            content_types,
            SUPPORTED_CONTENT_TYPES,
            "content type"
        ),
        "budget": budget
    }

    if not any([
        preferences["genres"],
        preferences["languages"],
        preferences["content_types"]
    ]):
        raise ValueError(
            "Please select at least one preference."
        )

    return preferences