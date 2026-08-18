"""
Challenge: Integer Sequence
Source: freeCodeCamp
Date: 2025-10-27

Problem:
Given a positive integer, return a string with all of the integers
from 1 up to, and including, the given number, in numerical order.

For example, given 5, return "12345".
"""


def sequence(n):
    return ''.join(str(i) for i in range(1, n + 1))


# Tests
assert sequence(5) == "12345"
assert sequence(10) == "12345678910"
assert sequence(1) == "1"
assert sequence(27) == "123456789101112131415161718192021222324252627"

print("All tests passed!")

