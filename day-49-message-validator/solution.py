"""
Challenge: Message Validator
Source: freeCodeCamp
Date: 2025-11-24
Problem: Given a message string and a validation string, determine if the message is valid.
A message is valid if each word in the message starts with the corresponding letter in the
validation string, in order. Letters are case-insensitive. Words are separated by single spaces.
Example: is_valid_message("hello world", "hw") -> True
"""

def is_valid_message(message, validation):
    return "".join([word[0] for word in message.lower().split()]) == validation.lower()


# Tests
assert is_valid_message("hello world", "hw") == True
assert is_valid_message("ALL CAPITAL LETTERS", "acl") == True
assert is_valid_message("Coding challenge are boring.", "cca") == False
assert is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") == True
assert is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT") == False
print("All tests passed!")

