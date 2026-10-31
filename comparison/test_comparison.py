# Testing OTT Comparison Module

import unittest

from comparison import (
    compare_prices,
    compare_languages,
    compare_genres,
    compare_platforms,
    get_cheapest_platform,
    compare_monthly_prices
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
   def test_compare_monthly_prices(self):
        monthly_prices = compare_monthly_prices()

        self.assertIsInstance(monthly_prices, dict)
        self.assertGreater(len(monthly_prices), 0)

        for price in monthly_prices.values():
            self.assertGreater(price, 0)


if __name__ == "__main__":
    unittest.main()
