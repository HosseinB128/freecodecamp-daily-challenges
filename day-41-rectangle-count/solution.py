"""
Challenge: Rectangle Count
Source: freeCodeCamp
Date: 2025-11-16
Problem: Given two positive integers representing the width and height
of a rectangle, determine how many rectangles (with integer width and
height) can fit inside the given rectangle.
Example: count_rectangles(1, 3) returns 6 (three 1x1 rectangles, two
1x2 rectangles, and one 1x3 rectangle).
"""


def count_rectangles(width, height):
    width_options = width * (width + 1) // 2
    height_options = height * (height + 1) // 2
    return width_options * height_options


assert count_rectangles(1, 3) == 6
assert count_rectangles(3, 2) == 18
assert count_rectangles(1, 2) == 3
assert count_rectangles(5, 4) == 150
assert count_rectangles(11, 19) == 12540

print("All tests passed!")

