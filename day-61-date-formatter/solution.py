"""
Challenge: Date Formatter
Source: freeCodeCamp
Date: 2025-12-06
Problem: Given a date in the format "Month day, year", return the date in the
format "YYYY-MM-DD". The month is the full English month name, and the month
and day are padded with leading zeros to two digits if necessary.
Example: "December 6, 2025" → "2025-12-06"
"""

from datetime import datetime

def format_date(date_string):
    month_day, year = date_string.split(", ")
    month_name, day = month_day.split(" ")
    month = datetime.strptime(month_name, "%B").month
    return f"{year}-{month:02d}-{int(day):02d}"


# Tests
assert format_date("December 6, 2025") == "2025-12-06"
assert format_date("January 1, 2000") == "2000-01-01"
assert format_date("November 11, 1111") == "1111-11-11"
assert format_date("September 7, 512") == "512-09-07"
assert format_date("May 4, 1950") == "1950-05-04"
assert format_date("February 29, 1992") == "1992-02-29"
print("All tests passed!")

