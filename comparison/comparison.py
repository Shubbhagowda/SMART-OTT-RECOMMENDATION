# OTT Platform Comparison Module

from ott_data import get_all_platforms
from plan_details import get_all_plans


def compare_prices():
    plans = get_all_plans()
    result = {}

    for platform, platform_plans in plans.items():
        prices = [plan["price"] for plan in platform_plans]

        if prices:
            result[platform] = min(prices)

    return result


def compare_languages():
    platforms = get_all_platforms()
    result = {}

    for platform, details in platforms.items():
        result[platform] = details["languages"]

    return result


def compare_genres():
    platforms = get_all_platforms()
    result = {}

    for platform, details in platforms.items():
        result[platform] = details["genres"]

    return result


def compare_platforms():
    platforms = get_all_platforms()
    prices = compare_prices()

    result = []

    for platform, details in platforms.items():
        result.append({
            "platform": platform,
            "starting_price": prices.get(platform),
            "languages": details["languages"],
            "genres": details["genres"],
            "content_types": details["content_types"]
        })

    return result


def get_cheapest_platform():
    prices = compare_prices()

    if not prices:
        return None

    return min(prices, key=prices.get)
    def compare_monthly_prices():
    plans = get_all_plans()
    result = {}

    for platform, platform_plans in plans.items():
        monthly_prices = []

        for plan in platform_plans:
            price = plan["price"]
            validity = plan["validity"]

            months = int(validity.split()[0])

            if months > 0:
                monthly_prices.append(price / months)

        if monthly_prices:
            result[platform] = round(min(monthly_prices), 2)

    return result


if __name__ == "__main__":
    print("OTT PLATFORM COMPARISON")
    print("-----------------------")

    for item in compare_platforms():
        print("\nPlatform:", item["platform"])
        print("Starting Price: ₹", item["starting_price"])
        print("Languages:", ", ".join(item["languages"]))
        print("Genres:", ", ".join(item["genres"]))
        print("Content Types:", ", ".join(item["content_types"]))

    print("\nCheapest Platform:",
          get_cheapest_platform())
  
