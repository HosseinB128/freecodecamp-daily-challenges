"""
Challenge: Character Limit
Source: freeCodeCamp Daily Coding Challenge
Date: 2025-11-08

Given a string, determine if it fits in a social media post:
- Return "short post" if the message length is 40 characters or fewer.
- Return "long post" if the message length is greater than 40 but at most 80 characters.
- Return "invalid post" if the message length exceeds 80 characters.
"""


def can_post(message):
    length = len(message)
    if length <= 40:
        return "short post"
    elif length <= 80:
        return "long post"
    else:
        return "invalid post"


# Tests
assert can_post("Hello world") == "short post"
assert can_post("This is a longer message but still under eighty characters.") == "long post"
assert can_post("This message is too long to fit into either of the character limits for a social media post.") == "invalid post"

print("All tests passed!")

