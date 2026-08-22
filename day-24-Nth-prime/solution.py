"""
Challenge: Nth Prime
Source: freeCodeCamp
Date: 2025-10-30
Problem: Given a positive integer n, return the nth prime number.
A prime number is a positive integer greater than 1 that is divisible only
by 1 and itself. For example, given n=5, return the 5th prime number: 11.
"""


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for divisor in range(3, int(num ** 0.5) + 1, 2):
        if num % divisor == 0:
            return False
    return True


def nth_prime(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate


# Tests
assert nth_prime(5) == 11
assert nth_prime(10) == 29
assert nth_prime(16) == 53
assert nth_prime(99) == 523
assert nth_prime(1000) == 7919

print("All tests passed!")

