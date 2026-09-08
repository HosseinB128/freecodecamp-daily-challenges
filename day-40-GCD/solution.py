"""
Challenge: GCD
Source: freeCodeCamp
Date: 2025-11-15
Problem: Given two positive integers, return their greatest common divisor (GCD).
The GCD of two integers is the largest number that divides evenly into both
numbers without leaving a remainder.
Example: The divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6.
So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
"""

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Tests
assert gcd(4, 6) == 2
assert gcd(20, 15) == 5
assert gcd(13, 17) == 1
assert gcd(654, 456) == 6
assert gcd(3456, 4320) == 864
print("All tests passed!")

