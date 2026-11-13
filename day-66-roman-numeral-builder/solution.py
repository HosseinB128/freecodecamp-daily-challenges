"""
Challenge: Roman Numeral Builder
Source: freeCodeCamp
Date: 2025-12-11
Problem: Given an integer, return its equivalent value in Roman numerals.
Roman numerals are written from largest to smallest, left to right.
Addition is used when a symbol is followed by one of equal or smaller value.
Subtraction is used when a smaller symbol appears before a larger one, to
represent 4 or 9 in any place value. No symbol may be repeated more than
three times in a row, so the largest number you can write is 3999.
Example: 1464 → "MCDLXIV"
"""

def to_roman(num):
    values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
              (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
              (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    result = ""
    for value, symbol in values:
        count, num = divmod(num, value)
        result += symbol * count
    return result


# Tests
assert to_roman(18) == "XVIII"
assert to_roman(19) == "XIX"
assert to_roman(1464) == "MCDLXIV"
assert to_roman(2025) == "MCDLXIV"
assert to_roman(3999) == "MCDLXIV"
print("All tests passed!")