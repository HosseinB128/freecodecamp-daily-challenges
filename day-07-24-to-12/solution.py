"""
Challenge: 24 to 12
Source: freeCodeCamp
Date: 2025-10-13

Given a string representing a time of the day in the 24-hour format of "HHMM",
return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format,
from "0000" to "2359".

Example:
to_12("1124") -> "11:24 AM"
"""

import datetime


def to_12(time):
    time = datetime.datetime.strptime(time, "%H%M")
    return f"{int(time.strftime('%I'))}:{time.strftime('%M %p')}"


assert to_12("1124") == "11:24 AM"
assert to_12("0900") == "9:00 AM"
assert to_12("1455") == "2:55 PM"
assert to_12("2346") == "11:46 PM"
assert to_12("0030") == "12:30 AM"

print("All tests passed!")

