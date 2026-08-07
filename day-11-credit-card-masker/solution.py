"""
Challenge: Credit Card Masker
Source: freeCodeCamp
Date: 2025-10-17
Problem: Given a string of credit card numbers, return a masked version of it
using the following constraints:
- The string will contain four sets of four digits (0-9), with all sets
  being separated by a single space, or a single hyphen (-).
- Replace all numbers, except the last four, with an asterisk (*).
- Leave the remaining characters unchanged.
"""


def mask(card):
    sep = " " if " " in card else "-"
    groups = card.split(sep)
    masked_groups = ["****" for _ in groups[:-1]] + [groups[-1]]
    return sep.join(masked_groups)


# Tests
assert mask("4012-8888-8888-1881") == "****-****-****-1881"
assert mask("5105 1051 0510 5100") == "**** **** **** 5100"
assert mask("6011 1111 1111 1117") == "**** **** **** 1117"
assert mask("2223-0000-4845-0010") == "****-****-****-0010"

print("All tests passed!")

