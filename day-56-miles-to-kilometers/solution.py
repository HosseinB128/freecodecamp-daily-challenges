"""
Challenge: Miles to Kilometers
Source: freeCodeCamp
Date: 2025-12-01
Problem: Given a distance in miles as a number, return the equivalent distance
in kilometers. The input will always be a non-negative number. 1 mile equals
1.60934 kilometers. Round the result to two decimal places and remove
unnecessary trailing zeros from the rounded result.
Example: convert_to_km(1) → 1.61
"""

def convert_to_km(miles):
    return round(miles * 1.60934, 2)


# Tests
assert convert_to_km(1) == 1.61
assert convert_to_km(21) == 33.8
assert convert_to_km(3.5) == 5.63
assert convert_to_km(0) == 0
assert convert_to_km(0.621371) == 1
print("All tests passed!")

