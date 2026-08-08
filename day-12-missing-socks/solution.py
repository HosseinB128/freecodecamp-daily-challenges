"""
Challenge: Missing Socks
Source: freeCodeCamp
Date: 2025-10-18

Problem: Given an integer representing the number of pairs of socks you
started with, and another integer representing how many wash cycles you
have gone through, return the number of complete pairs of socks you
currently have using the following constraints:
- Every 2 wash cycles, you lose a single sock.
- Every 3 wash cycles, you find a single missing sock.
- Every 5 wash cycles, a single sock is worn out and must be thrown away.
- Every 10 wash cycles, you buy a pair of socks.
- You can never have less than zero total socks. Whenever an operation
  would drop the total sock count below zero, the count is clamped to
  zero instead of going negative.
- Rules can overlap. For example, on wash cycle 10, you will lose a
  single sock, throw away a single sock, and buy a new pair of socks.
- Return the number of complete pairs of socks.
"""


def sock_pairs(pairs, cycles):
    socks = pairs * 2
    for i in range(1, cycles + 1):
        if i % 2 == 0:
            socks = max(socks - 1, 0)
        if i % 3 == 0:
            socks += 1
        if i % 5 == 0:
            socks = max(socks - 1, 0)
        if i % 10 == 0:
            socks += 2
    return socks // 2


# Tests
assert sock_pairs(2, 5) == 1
assert sock_pairs(1, 2) == 0
assert sock_pairs(5, 11) == 4
assert sock_pairs(6, 25) == 3
assert sock_pairs(1, 8) == 0
print("All tests passed!")


