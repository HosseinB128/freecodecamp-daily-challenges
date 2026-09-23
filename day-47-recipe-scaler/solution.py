"""
Challenge: Recipe Scaler
Source: freeCodeCamp
Date: 2025-11-22
Problem: Given an array of recipe ingredients and a number to scale the
recipe, return an array with the quantities scaled accordingly. Each item
is a string in the format "quantity unit ingredient" (e.g. "2 C Flour").
Scale the quantity by the given number, omit trailing zeros, and do not
convert units. Preserve the original order of items.
Example: scale_recipe(["2 C Flour", "1.5 T Sugar"], 2) → ["4 C Flour", "3 T Sugar"]
"""

def scale_recipe(ingredients, scale):
    ingredients = [item.split() for item in ingredients]
    return [f"{float(parts[0]) * scale:g} " + " ".join(parts[1:]) for parts in ingredients]

# Tests
assert scale_recipe(["2 C Flour", "1.5 T Sugar"], 2) == ["4 C Flour", "3 T Sugar"]
assert scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5) == ["6 T Flour", "1.5 C Milk", "3 T Oil"]
assert scale_recipe(["3 C Milk", "2 C Oats"], 0.5) == ["1.5 C Milk", "1 C Oats"]
assert scale_recipe(
    ["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter",
     "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"],
    2.5
) == ["5 C All-purpose Flour", "2.5 t Baking Soda", "2.5 t Salt", "2.5 C Butter",
      "1.25 C Sugar", "1.25 C Brown Sugar", "2.5 t Vanilla Extract", "5 C Chocolate Chips"]
print("All tests passed!")

