"""
Challenge: Tip Calculator
Source: freeCodeCamp
Date: 2025-10-20
Problem: Given the price of your meal and a custom tip percent, return an
array with three tip values: 15%, 20%, and the custom amount.
Prices are given as "$N.NN" and custom tip percents as "N%". Return amounts
in the same "$N.NN" format, rounded to two decimal places.
"""


def calculate_tips(meal_price, custom_tip):
    price = float(meal_price.replace("$", ""))
    custom_percent = float(custom_tip.replace("%", "")) / 100

    tip_rates = [0.15, 0.20, custom_percent]
    return [f"${price * rate:.2f}" for rate in tip_rates]


assert calculate_tips("$10.00", "25%") == ["$1.50", "$2.00", "$2.50"]
assert calculate_tips("$89.67", "26%") == ["$13.45", "$17.93", "$23.31"]
assert calculate_tips("$19.85", "9%") == ["$2.98", "$3.97", "$1.79"]

print("All tests passed!")


