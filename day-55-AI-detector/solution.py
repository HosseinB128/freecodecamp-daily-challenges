"""
Challenge: AI Detector
Source: freeCodeCamp
Date: 2025-11-30
Problem: Given a string of one or more sentences, return "AI" if it contains
two or more dashes, two or more sets of parentheses, or three or more words
with 7 or more letters (words contain only letters; punctuation is ignored).
Otherwise, return "Human".
Example: "The extraordinary students were studying vivaciously." → "AI"
"""

def detect_ai(text):
    long_words = sum(
        sum(ch.isalpha() for ch in word) >= 7
        for word in text.split()
    )
    if (
        text.count("-") >= 2
        or text.count("(") + text.count(")") >= 4
        or long_words >= 3
    ):
        return "AI"
    return "Human"


# Tests
assert detect_ai("The quick brown fox jumped over the lazy dog.") == "Human"
assert detect_ai("The hypersonic brown fox - jumped (over) the lazy dog.") == "Human"
assert detect_ai("Yes - you're right! I made a mistake there - let me try again.") == "AI"
assert detect_ai("The extraordinary students were studying vivaciously.") == "AI"
assert detect_ai("The (excited) student was (coding) in the library.") == "AI"
print("All tests passed!")

