"""
Challenge: Counting Cards
Source: freeCodeCamp
Date: 2025-11-07

Problem:
A standard deck of playing cards has 13 unique cards in each suit.
Given an integer representing the number of cards to pick from the deck,
return the number of unique combinations of cards you can pick.

Order does not matter. Picking card A then card B is the same as
picking card B then card A.

For example, given 52, return 1. There's only one combination of
52 cards to pick from a 52 card deck. And given 2, return 1326,
there's 1326 card combinations you can end up with when picking
2 cards from the deck.
"""


def combinations(cards):
    n = 52
    k = min(cards, n - cards)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


# Tests
assert combinations(52) == 1
assert combinations(1) == 52
assert combinations(2) == 1326
assert combinations(5) == 2598960
assert combinations(10) == 15820024220
assert combinations(50) == 1326

print("All tests passed!")

