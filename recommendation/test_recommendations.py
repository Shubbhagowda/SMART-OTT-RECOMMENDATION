import unittest

from recommendation.preference_handler import validate_preferences
from recommendation.scoring import calculate_score
from recommendation.recommendation_engine import get_recommendations


class TestRecommendationSystem(unittest.TestCase):

    def setUp(self):
        self.preferences = {
            "genres": ["Action", "Comedy"],
            "languages": ["Kannada"],
            "content_types": ["Movies"],
            "budget": 500
        }

        self.platforms = {
            "Platform A": {
                "genres": ["Action", "Comedy"],
                "languages": ["Kannada"],
                "content_types": ["Movies"],
                "description": "Test platform A"
            },
            "Platform B": {
                "genres": ["Drama"],
                "languages": ["Hindi"],
                "content_types": ["Web Series"],
                "description": "Test platform B"
            }
        }

    def test_preference_validation(self):
        result = validate_preferences(self.preferences)
        self.assertEqual(result["budget"], 500.0)

    def test_invalid_budget(self):
        invalid = {
            "genres": ["Action"],
            "languages": ["Kannada"],
            "content_types": ["Movies"],
            "budget": -100
        }

        with self.assertRaises(ValueError):
            validate_preferences(invalid)

    def test_scoring(self):
        result = calculate_score(
            self.preferences,
            self.platforms["Platform A"]
        )

        self.assertEqual(result["score"], 100.0)

    def test_recommendation_ranking(self):
        results = get_recommendations(
            self.preferences,
            self.platforms
        )

        self.assertEqual(
            results[0]["platform"], "Platform A"
        )

    def test_recommendation_count(self):
        results = get_recommendations(
            self.preferences,
            self.platforms
        )

        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)