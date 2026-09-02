"""
Challenge: Vowels and Consonants
Source: freeCodeCamp
Date: 2025-11-11

Given a string, return an array with the number of vowels and number of
consonants in the string.

- Vowels consist of 'a', 'e', 'i', 'o', 'u' in any case.
- Consonants consist of all other letters in any case.
- Ignore any non-letter characters.

Example:
    count("Hello World") -> [3, 7]
"""


def count(sentence):
    result = [0, 0]
    for char in sentence.lower():
        if char in "aeiou":
            result[0] += 1
        elif char.isalpha():
            result[1] += 1
    return result


# Tests
assert count("Hello World") == [3, 7]
assert count("JavaScript") == [3, 7]
assert count("Python") == [1, 5]
assert count("freeCodeCamp") == [5, 7]
assert count("Hello, World!") == [3, 7]
assert count("The quick brown fox jumps over the lazy dog.") == [11, 24]

print("All tests passed!")

