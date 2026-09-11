"""
Challenge: 100 Characters
Source: freeCodeCamp
Date: 2025-11-18
Problem: Given a string, repeat its characters until the result is exactly 100 characters long. If the repetitions go over 100 characters, trim the extra so it's exactly 100.
Example: one_hundred("One hundred ") should return "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One "
"""

def one_hundred(chars):
    result = ""
    while len(result) < 100:
        result += chars
    return result[:100]

# Tests
assert one_hundred("One hundred ") == "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One "
assert one_hundred("freeCodeCamp ") == "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC"
assert one_hundred("daily challenges ") == "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge"
assert one_hundred("!") == "!" * 100
print("All tests passed!")

