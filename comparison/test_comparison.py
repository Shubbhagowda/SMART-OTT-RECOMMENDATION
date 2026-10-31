# Testing OTT Comparison Module

import unittest

from comparison import (
    compare_prices,
    compare_languages,
    compare_genres,
    compare_platforms,
    get_cheapest_platform
)


class TestOTTComparison(unittest.TestCase):

    def test_compare_prices(self):
        prices = compare_prices()

        self.assertIsInstance(prices, dict)
        self.assertGreater(len(prices), 0)

        for price in prices.values():
            self.assertGreater(price, 0)

    def test_compare_languages(self):
        languages = compare_languages()

        self.assertIsInstance(languages, dict)
        self.assertIn("Netflix", languages)

    def test_compare_genres(self):
        genres = compare_genres()

        self.assertIsInstance(genres, dict)
        self.assertIn("Amazon Prime Video", genres)

    def test_compare_platforms(self):
        platforms = compare_platforms()

        self.assertIsInstance(platforms, list)
        self.assertGreater(len(platforms), 0)

        for platform in platforms:
            self.assertIn("platform", platform)
            self.assertIn("starting_price", platform)

    def test_cheapest_platform(self):
        cheapest = get_cheapest_platform()

        self.assertIsNotNone(cheapest)
        self.assertIsInstance(cheapest, str)


if __name__ == "__main__":
    unittest.main()
