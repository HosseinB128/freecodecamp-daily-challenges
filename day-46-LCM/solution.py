"""
Challenge: LCM
Source: freeCodeCamp
Date: 2025-11-21
Problem: Given two integers, return the least common multiple (LCM) of the two numbers. The LCM of two numbers is the smallest positive integer that is a multiple of both numbers.
Example: lcm(4, 6) → 12
"""

def lcm(a, b):
    larger = max(a, b)
    for i in range(larger, (a * b) + 1, larger):
        if i % a == 0 and i % b == 0:
            return i

# Tests
assert lcm(4, 6) == 12
assert lcm(9, 6) == 18
assert lcm(10, 100) == 100
assert lcm(13, 17) == 221
assert lcm(45, 70) == 630
print("All tests passed!")

