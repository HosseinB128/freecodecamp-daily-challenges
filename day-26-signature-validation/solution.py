"""
Challenge: Signature Validation
Source: freeCodeCamp
Date: 2025-11-01

Problem:
Given a message string, a secret key string, and a signature number,
determine if the signature is valid using this encoding method:
- Letters 'a' to 'z' have values 1 to 26 respectively.
- Letters 'A' to 'Z' have values 27 to 52 respectively.
- All other characters have no value (they are ignored).
- The signature is computed as the sum of the message's letter values
  plus the sum of the secret key's letter values.
Return True if the computed signature matches the provided signature,
otherwise return False.
"""

import string


def verify(message, key, signature):
    all_letters = {letter: index for index, letter in enumerate(string.ascii_letters, start=1)}
    message_sum = sum(all_letters.get(i, 0) for i in message)
    key_sum = sum(all_letters.get(i, 0) for i in key)
    return signature == message_sum + key_sum


# Tests
assert verify("foo", "bar", 57) == True
assert verify("foo", "bar", 54) == False
assert verify("freeCodeCamp", "Rocks", 238) == True
assert verify("Is this valid?", "No", 210) == False
assert verify("Is this valid?", "Yes", 233) == True
assert verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) == True

print("All tests passed!")

