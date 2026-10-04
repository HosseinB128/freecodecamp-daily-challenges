"""
Challenge: Camel to Snake
Source: freeCodeCamp
Date: 2025-12-02
Problem: Given a string in camel case, return the snake case version of the string.
The input contains only letters (A-Z and a-z) and always starts with a lowercase letter.
Every uppercase letter starts a new word. Convert all letters to lowercase
and separate words with an underscore (_).
Example: "helloWorld" → "hello_world"
"""


def to_snake(camel_str):
    result = ""
    for char in camel_str:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result


# Tests
assert to_snake("helloWorld") == "hello_world"
assert to_snake("myVariableName") == "my_variable_name"
assert to_snake("freecodecampDailyChallenges") == "freecodecamp_daily_challenges"
print("All tests passed!")

