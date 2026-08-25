"""
Challenge: Word Counter
Source: freeCodeCamp
Date: 2025-11-03

Problem:
Given a sentence string, return the number of words that are in the sentence.
Words are any sequence of non-space characters and are separated by a single space.
"""


def count_words(sentence):
    return len(sentence.split())


assert count_words("Hello world") == 2
assert count_words("The quick brown fox jumps over the lazy dog.") == 9
assert count_words("I like coding challenges!") == 4
assert count_words("Complete the challenge in JavaScript and Python.") == 7
assert count_words("The missing semi-colon crashed the entire internet.") == 7

print("All tests passed!")

