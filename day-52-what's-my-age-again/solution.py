"""
Challenge: What's My Age Again?
Source: freeCodeCamp
Date: 2025-11-27
Problem: Given a birthday in the format YYYY-MM-DD, return the person's
age as an integer as of November 27th, 2025. Account for whether the
person has already had their birthday in 2025.
Example: "2000-12-01" → 24
"""

from datetime import datetime


def calculate_age(birthday):
    born = datetime.strptime(birthday, "%Y-%m-%d").date()
    ref = datetime.strptime("2025-11-27", "%Y-%m-%d").date()
    age = ref.year - born.year
    if (born.month, born.day) > (ref.month, ref.day):
        age -= 1
    return age


# Tests
assert calculate_age("2000-11-20") == 25
assert calculate_age("2000-12-01") == 24
assert calculate_age("2014-10-25") == 11
assert calculate_age("1994-01-06") == 31
assert calculate_age("1994-12-14") == 30
print("All tests passed!")

