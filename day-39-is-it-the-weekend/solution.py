"""
Challenge: Is It the Weekend?
Source: freeCodeCamp
Date: 2025-11-14
Problem: Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.
The weekend starts on Saturday. If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Example: days_until_weekend("2025-11-14") returns "1 day until the weekend."
"""

from datetime import datetime

def days_until_weekend(date_string):
    to_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    weekday = to_date.weekday()

    if weekday in (5, 6):
        return "It's the weekend!"

    days_left = 5 - weekday
    if days_left == 1:
        return "1 day until the weekend."
    return f"{days_left} days until the weekend."


# Tests
assert days_until_weekend("2025-11-14") == "1 day until the weekend."
assert days_until_weekend("2025-01-01") == "3 days until the weekend."
assert days_until_weekend("2025-12-06") == "It's the weekend!"
assert days_until_weekend("2026-01-27") == "4 days until the weekend."
assert days_until_weekend("2026-09-07") == "5 days until the weekend."
assert days_until_weekend("2026-11-29") == "It's the weekend!"
print("All tests passed!")

