"""
Challenge: Longest Word
Source: freeCodeCamp
Date: 2025-11-20
Problem: Given a sentence string, return the longest word in the sentence.
    - Words are separated by a single space.
    - Only letters (a-z, case-insensitive) count toward the word's length.
    - If there are multiple words with the same length, return the first one that appears.
    - Return the word as it appears in the given string, with punctuation removed.
Example: longest_word("The quick red fox") -> "quick"
"""

import re

def longest_word(sentence):
    words = sentence.split(' ')
    cleaned = [re.sub(r'[^a-zA-Z]', '', word) for word in words]
    return max(cleaned, key=len)


assert longest_word("The quick red fox") == "quick"
assert longest_word("Hello coding challenge.") == "challenge"
assert longest_word("Do Try This At Home.") == "This"
assert longest_word("This sentence... has commas, ellipses, and an exclamation point!") == "exclamation"
assert longest_word("A tie? No way!") == "tie"
assert longest_word("Wouldn't you like to know.") == "Wouldnt"

print("All tests passed!")

