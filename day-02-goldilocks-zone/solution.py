"""
Challenge: Goldilocks Zone
Source: freeCodeCamp - Space Week, Day 5
Date: 2025-10-08

Problem:
Given the mass of a star, return an array with the start and end distances
of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:
1. Find the luminosity of the star by raising its mass to the power of 3.5.
2. The start of the zone is 0.95 times the square root of its luminosity.
3. The end of the zone is 1.37 times the square root of its luminosity.

Return the distances rounded to two decimal places.

Example: goldilocks_zone(1) returns [0.95, 1.37]
"""

import math

def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    luminosity_sqrt = math.sqrt(luminosity)

    start = round(0.95 * luminosity_sqrt, 2)
    end = round(1.37 * luminosity_sqrt, 2)

    return [start, end]

assert goldilocks_zone(1) == [0.95, 1.37]
assert goldilocks_zone(0.5) == [0.28, 0.41]
assert goldilocks_zone(6) == [21.85, 31.51]
assert goldilocks_zone(3.7) == [9.38, 13.52]
assert goldilocks_zone(20) == [179.69, 259.13]

print("All tests passed!")
