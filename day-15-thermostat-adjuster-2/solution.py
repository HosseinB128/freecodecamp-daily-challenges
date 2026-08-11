"""
Challenge: Thermostat Adjuster 2
Source: freeCodeCamp
Date: 2025-10-21

Problem:
Given the current temperature of a room in Fahrenheit and a target
temperature in Celsius, return a string indicating how to adjust the
room temperature based on these constraints:

- Return "Heat: X degrees Fahrenheit" if the current temperature is
  below the target. X is the number of degrees in Fahrenheit to heat
  the room to reach the target, rounded to 1 decimal place.
- Return "Cool: X degrees Fahrenheit" if the current temperature is
  above the target. X is the number of degrees in Fahrenheit to cool
  the room to reach the target, rounded to 1 decimal place.
- Return "Hold" if the current temperature is equal to the target.

To convert Celsius to Fahrenheit, multiply the Celsius temperature by
1.8 and add 32 to the result (F = (C * 1.8) + 32).

Example:
adjust_thermostat(70, 25) -> "Heat: 7.0 degrees Fahrenheit"
"""


def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32
    if current_f < target_f:
        return f"Heat: {target_f - current_f:.1f} degrees Fahrenheit"
    elif current_f > target_f:
        return f"Cool: {current_f - target_f:.1f} degrees Fahrenheit"
    else:
        return "Hold"


# Tests
assert adjust_thermostat(32, 0) == "Hold"
assert adjust_thermostat(70, 25) == "Heat: 7.0 degrees Fahrenheit"
assert adjust_thermostat(72, 18) == "Cool: 7.6 degrees Fahrenheit"
assert adjust_thermostat(212, 100) == "Hold"
assert adjust_thermostat(59, 22) == "Heat: 12.6 degrees Fahrenheit"

print("All tests passed!")

