"""
Challenge: Weekday Finder
Source: freeCodeCamp
Date: 2025-11-06
Problem: Given a string date in the format YYYY-MM-DD, return the day of the
week. Valid return days are: "Sunday", "Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday". Time zones should be ignored.
"""

from datetime import datetime

def get_weekday(date_string):
    return datetime.strftime(datetime.strptime(date_string, "%Y-%m-%d"), "%A")


# Tests
assert get_weekday("2025-11-06") == "Thursday"
assert get_weekday("1999-12-31") == "Friday"
assert get_weekday("1111-11-11") == "Saturday"
assert get_weekday("2112-12-21") == "Wednesday"
assert get_weekday("2345-10-01") == "Monday"

print("All tests passed!")

