# OTT Subscription Plan Details

# Sample prices for project development.
# Verify actual prices before final deployment.

SUBSCRIPTION_PLANS = {
    "Netflix": [
        {
            "plan_name": "Mobile",
            "price": 149,
            "validity": "1 Month",
            "quality": "HD",
            "screens": 1
        },
        {
            "plan_name": "Basic",
            "price": 199,
            "validity": "1 Month",
            "quality": "HD",
            "screens": 1
        }
    ],

    "Amazon Prime Video": [
        {
            "plan_name": "Monthly",
            "price": 299,
            "validity": "1 Month",
            "quality": "HD",
            "screens": 2
        }
    ],

    "JioHotstar": [
        {
            "plan_name": "Mobile",
            "price": 149,
            "validity": "3 Months",
            "quality": "HD",
            "screens": 1
        }
    ],

    "ZEE5": [
        {
            "plan_name": "Premium",
            "price": 299,
            "validity": "3 Months",
            "quality": "HD",
            "screens": 2
        }
    ],

    "SonyLIV": [
        {
            "plan_name": "Premium",
            "price": 399,
            "validity": "1 Month",
            "quality": "HD",
            "screens": 2
        }
    ]
}


def get_all_plans():
    return SUBSCRIPTION_PLANS


def get_platform_plans(platform_name):
    return SUBSCRIPTION_PLANS.get(platform_name, [])


def get_plan_price(platform_name):
    plans = get_platform_plans(platform_name)
    return [plan["price"] for plan in plans]
