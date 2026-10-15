"""
Challenge: Pounds to Kilograms
Source: freeCodeCamp
Date: 2025-12-08
Problem: Given a weight in pounds, return the string
"(lbs) pounds equals (kgs) kilograms." where kgs is the value converted
using 1 pound = 0.453592 kilograms, rounded to two decimals (always two
decimal places shown). Use "pound" if the input is 1, and "kilogram" if
the converted value is 1.
Example: 2.20462 -> "2.20462 pounds equals 1.00 kilogram."
"""

def convert_to_kgs(lbs):
    kgs = round(lbs * 0.453592, 2)
    pound_word = "pound" if lbs == 1 else "pounds"
    kg_word = "kilogram" if kgs == 1 else "kilograms"
    return f"{lbs} {pound_word} equals {kgs:.2f} {kg_word}."


# Tests
assert convert_to_kgs(1) == "1 pound equals 0.45 kilograms."
assert convert_to_kgs(0) == "0 pounds equals 0.00 kilograms."
assert convert_to_kgs(100) == "100 pounds equals 45.36 kilograms."
assert convert_to_kgs(2.5) == "2.5 pounds equals 1.13 kilograms."
assert convert_to_kgs(2.20462) == "2.20462 pounds equals 1.00 kilogram."
print("All tests passed!")

