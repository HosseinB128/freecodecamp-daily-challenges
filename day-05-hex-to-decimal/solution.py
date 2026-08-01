"""
Challenge: Hex to Decimal
Source: freeCodeCamp
Date: 2025-10-11

Given a string representing a hexadecimal number (base 16), return its
decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:
0-9 represent values 0 through 9.
A-F represent values 10 through 15.

Example:
hex_to_decimal("A") -> 10
hex_to_decimal("FF") -> 255
hex_to_decimal("A3F") -> 2623

The string will only contain characters 0-9 and A-F.
"""


def hex_to_decimal(hex_str):
    return int(hex_str, base=16)


# Tests
assert hex_to_decimal("A") == 10
assert hex_to_decimal("15") == 21
assert hex_to_decimal("2E") == 46
assert hex_to_decimal("FF") == 255
assert hex_to_decimal("A3F") == 2623

print("All tests passed!")

