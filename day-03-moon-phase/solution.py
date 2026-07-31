"""
Challenge: Moon Phase (Space Week Day 6)
Source: freeCodeCamp - Space Week
Date: 2025-10-09

Problem:
Given a date string in the format "YYYY-MM-DD", determine the phase of
the moon for that day using a simplified 28-day lunar cycle divided into
four equal phases:
    - "New": days 1-7
    - "Waxing": days 8-14
    - "Full": days 15-21
    - "Waning": days 22-28
After day 28, the cycle repeats starting from day 1 (a new moon).
The reference new moon (day 1 of the cycle) is "2000-01-06".
Day 1 represents the day of the new moon itself, meaning 0 days have
passed since the last new moon. No input date will be earlier than
the reference date.

Example:
    moon_phase("2000-01-13") -> "Waxing"
"""

import datetime

def moon_phase(date_string):
    reference_date = datetime.date(year=2000, month=1, day=6)
    target_date = datetime.date(year=int(date_string[0:4]),
                                 month=int(date_string[5:7]),
                                 day=int(date_string[8:]))

    distance = (target_date - reference_date).days
    remainder = distance % 28

    return ["New", "Waxing", "Full", "Waning"][remainder // 7]


assert moon_phase("2000-01-12") == "New"
assert moon_phase("2000-01-13") == "Waxing"
assert moon_phase("2014-10-15") == "Full"
assert moon_phase("2012-10-21") == "Waning"
assert moon_phase("2022-12-14") == "New"

print("All tests passed!")


