"""
Challenge: BuzzFizz
Source: freeCodeCamp
Date: 2025-11-26
Problem: Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if numbers that are multiples of 3 are replaced with "Fizz", multiples of 5 are replaced with "Buzz", multiples of both 3 and 5 are replaced with "FizzBuzz", all other numbers remain as integers in ascending order starting from 1, and the array must start at 1 with no missing or extra elements.
Example: is_fizz_buzz([1, 2, "Fizz", 4]) -> True
"""

def is_fizz_buzz(sequence):
    for i in range(1, len(sequence) + 1):
        if i % 3 == 0 and i % 5 == 0:
            if not sequence[i - 1] == "FizzBuzz":
                return False
        elif i % 3 == 0:
            if not sequence[i - 1] == "Fizz":
                return False
        elif i % 5 == 0:
            if not sequence[i - 1] == "Buzz":
                return False
        elif not i == sequence[i - 1]:
            return False
    return True


# Tests
assert is_fizz_buzz([1, 2, "Fizz", 4]) == True
assert is_fizz_buzz([1, 2, 3, 4]) == False
assert is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]) == False
assert is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]) == False
assert is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]) == False
assert is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]) == False
assert is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]) == True
print("All tests passed!")

