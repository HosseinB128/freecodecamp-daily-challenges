"""
Challenge: Markdown Ordered List Item Converter
Source: freeCodeCamp
Date: 2025-12-03
Problem: Given a string representing an ordered list item in Markdown,
return the equivalent HTML string. A valid item starts with zero or more
spaces, then a number (1 or greater) and a period, then at least one space,
then the item text. Otherwise return "Invalid format".
Example: "1. My item" → "<li>My item</li>"
"""

import re

def convert_list_item(markdown):
    match = re.fullmatch(r" *[1-9]\d*\.\s+(\S.*)", markdown)
    if match is None:
        return "Invalid format"
    return f"<li>{match.group(1)}</li>"


# Tests
assert convert_list_item("1. My item") == "<li>My item</li>"
assert convert_list_item(" 1.  Another item") == "<li>Another item</li>"
assert convert_list_item("1 . invalid item") == "Invalid format"
assert convert_list_item("2. list item text") == "<li>list item text</li>"
assert convert_list_item(". invalid again") == "Invalid format"
assert convert_list_item("A. last invalid") == "Invalid format"
print("All tests passed!")

