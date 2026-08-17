"""
Challenge: Duration Formatter
Source: freeCodeCamp
Date: 2025-10-26

Problem:
Given an integer number of seconds, return a string representing the same
duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is
the number of minutes, and "SS" is the number of seconds, following these
rules:
- Seconds should always be two digits.
- Minutes should omit leading zeros when they aren't needed. Use "0" if the
  duration is less than one minute.
- Hours should be included only if they're greater than zero.
"""


def format(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    return f"{minutes}:{seconds:02d}"


# Tests
assert format(500) == "8:20"
assert format(4000) == "1:06:40"
assert format(1) == "0:01"
assert format(5555) == "1:32:35"
assert format(99999) == "27:46:39"
print("All tests passed!")

