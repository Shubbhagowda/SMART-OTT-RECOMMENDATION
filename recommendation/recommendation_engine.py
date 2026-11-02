# recommendation_engine.py

from comparison.ott_data import get_all_platforms

from recommendation.preference_handler import validate_preferences
from recommendation.scoring import calculate_score


def get_recommendations(user_data, platforms=None):

    # Validate user preferences
    preferences = validate_preferences(user_data)

    # Get OTT data from Member 2
    if platforms is None:
        platforms = get_all_platforms()

    recommendations = []

    # Calculate score for every OTT platform
    for platform_name, details in platforms.items():

        result = calculate_score(
            preferences,
            details
        )

        recommendation = {
            "platform": platform_name,
            "score": result["score"],
            "matched_genres": result["genre_matches"],
            "matched_languages": result["language_matches"],
            "matched_content_types": result["content_type_matches"],
            "description": details.get("description", ""),
            "monthly_budget": preferences["budget"],
            "budget_status": "not_checked"
        }

        recommendations.append(recommendation)

    # Sort platforms from highest score to lowest
    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations


if __name__ == "__main__":

    user_preferences = {
        "genres": ["Action", "Comedy"],
        "languages": ["Kannada"],
        "content_types": ["Movies"],
        "budget": 500
    }

    results = get_recommendations(user_preferences)

    print("\nSMART OTT RECOMMENDATIONS")
    print("------------------------")

    for item in results:

        print("\nPlatform:", item["platform"])
        print("Matching Score:", item["score"], "%")
        print("Matched Genres:", item["matched_genres"])
        print("Matched Languages:", item["matched_languages"])
        print("Matched Content:", item["matched_content_types"])