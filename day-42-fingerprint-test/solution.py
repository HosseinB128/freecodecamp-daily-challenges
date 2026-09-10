"""
Challenge: Fingerprint Test
Source: freeCodeCamp
Date: 2025-11-17
Problem: Given two strings representing fingerprints, determine if they are a match using the following rules: Each fingerprint will consist only of lowercase letters (a-z). Two fingerprints are considered a match if they are the same length, and the number of differing characters does not exceed 10% of the fingerprint length.
Example: is_match("helloworld", "jelloworld") returns True
"""

def is_match(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b):
        return False
    diffrence_a_b = sum(a != b for a, b in zip(fingerprint_a, fingerprint_b))
    return diffrence_a_b <= len(fingerprint_a) * 0.1

# Tests
assert is_match("helloworld", "helloworld") == True
assert is_match("helloworld", "helloworlds") == False
assert is_match("helloworld", "jelloworld") == True
assert is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") == True
assert is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") == True
assert is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") == False
print("All tests passed!")

