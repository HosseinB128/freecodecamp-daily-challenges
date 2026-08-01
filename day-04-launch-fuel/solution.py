"""
Challenge: Launch Fuel
Source: freeCodeCamp - Space Week Day 7
Date: 2025-10-10

Problem:
Given the mass in kilograms (kg) of a payload to send to orbit, determine
the amount of fuel needed to send it to orbit using the following rules:

- Rockets require 1 kg of fuel per 5 kg of mass they must lift.
- Fuel itself has mass, so adding fuel increases the total mass, which
  requires more fuel, and so on.
- Starting from the payload mass, repeatedly calculate the fuel needed
  for the current total mass, and add that fuel to the total. Stop when
  the additional fuel required is less than 1 kg.
- Ignore the mass of the rocket itself.

Example:
    A payload of 50 kg requires 10 kg of fuel (50 / 5), bringing the
    total mass to 60 kg, which requires 12 kg of fuel (2 kg more),
    bringing the total to 62 kg, which requires 12.4 kg of fuel
    (0.4 kg more, which is less than 1 kg, so we stop). The total fuel
    needed is 12.4 kg.

Return the amount of fuel needed rounded to one decimal place.
"""


def launch_fuel(payload):
    total_fuel = 0
    weight_to_lift = payload
    while True:
        weight_additional_fuel = weight_to_lift / 5
        total_fuel += weight_additional_fuel
        weight_to_lift = weight_additional_fuel
        if weight_additional_fuel < 1:
            break
    return round(total_fuel, 1)


# Tests
assert launch_fuel(50) == 12.4
assert launch_fuel(500) == 124.8
assert launch_fuel(243) == 60.7
assert launch_fuel(11000) == 2749.8
assert launch_fuel(6214) == 1553.4

print("All tests passed!")

