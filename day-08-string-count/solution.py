"""
Challenge: String Count
Source: freeCodeCamp
Date: 2025-10-14

Problem:
Given two strings, determine how many times the second string
appears in the first string. The pattern string can overlap in
the first string. For example, "aaa" contains "aa" twice - the
first two a's and the second two.

Examples:
count('abcdefg', 'def') -> 1
count('hello', 'world') -> 0
count('mississippi', 'iss') -> 2
count('she sells seashells by the seashore', 'sh') -> 3
count('101010101010101010101', '101') -> 10
"""

import re

def count(text, parameter):
    pattern = re.escape(parameter)
    return len(re.findall(f'(?={pattern})', text))


# Tests
assert count('abcdefg', 'def') == 1
assert count('hello', 'world') == 0
assert count('mississippi', 'iss') == 2
assert count('she sells seashells by the seashore', 'sh') == 3
assert count('101010101010101010101', '101') == 10

print("All tests passed!")

