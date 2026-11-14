"""
Challenge: Inventory Update
Source: freeCodeCamp
Date: 2025-12-12
Problem: Given a 2D array representing the inventory of your store, and another
2D array representing a shipment you have received, return your updated inventory.
Each element in the arrays has the format [quantity, "item"]. Update items in the
inventory by adding the quantity of any matching items from the shipment. If a
received item does not exist in the current inventory, add it as a new entry to
the end of the inventory. Return the inventory in the order it was given, with
new items at the end in the order they appear in the shipment.
Example: update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]])
         → [[3, "apples"], [8, "bananas"]]
"""


def update_inventory(inventory, shipment):
    inventory = {item: qty for qty, item in inventory}
    for qty, item in shipment:
        inventory[item] = inventory.get(item, 0) + qty
    return [[qty, item] for item, qty in inventory.items()]


# Tests
assert update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]) == [[3, "apples"], [8, "bananas"]]
assert update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]) == [[3, "apples"], [8, "bananas"], [4, "oranges"]]
assert update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]) == [[10, "apples"], [30, "bananas"], [20, "oranges"]]
assert update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) == [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]]
print("All tests passed!")

