"""
Challenge: Battle of Words
Source: freeCodeCamp
Date: 2025-10-12

Given two sentences representing your team and an opposing team, where each word from
your team battles the corresponding word from the opposing team, determine which team
wins using the following rules:

- The given sentences will always contain the same number of words.
- Words are separated by a single space and will only contain letters.
- The value of each word is the sum of its letters.
- Letters 'a' to 'z' correspond to the values 1 through 26. For example, 'a' is 1, and
  'z' is 26.
- A capital letter doubles the value of the letter. For example, 'A' is 2, and 'Z' is 52.
- Words battle in order: the first word of your team battles the first word of the
  opposing team, and so on.
- A word wins if its value is greater than the opposing word's value.
- The team with more winning words is the winner.

Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if
both teams have the same number of wins.

Example:
battle("hello world", "hello word") returns "We win"
"""


def value_of_word(word):
    return sum(2 * (ord(c) - 64) if c.isupper() else (ord(c) - 96) for c in word)


def battle(our_team, opponent):
    our_words = our_team.split()
    opponent_words = opponent.split()

    our_score = 0
    opponent_score = 0

    for our_word, opp_word in zip(our_words, opponent_words):
        our_value = value_of_word(our_word)
        opp_value = value_of_word(opp_word)
        if our_value > opp_value:
            our_score += 1
        elif our_value < opp_value:
            opponent_score += 1

    if our_score > opponent_score:
        return "We win"
    elif our_score < opponent_score:
        return "We lose"
    return "Draw"


# Tests
assert battle("hello world", "hello word") == "We win"
assert battle("Hello world", "hello world") == "We win"
assert battle("lorem ipsum", "kitty ipsum") == "We lose"
assert battle("hello world", "world hello") == "Draw"
assert battle("git checkout", "git switch") == "We win"
assert battle("Cheeseburger with fries", "Cheeseburger with Fries") == "We lose"
assert battle("We must never surrender", "Our team must win") == "Draw"

print("All tests passed!")

