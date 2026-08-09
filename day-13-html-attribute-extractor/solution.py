"""
Challenge: HTML Attribute Extractor
Source: freeCodeCamp
Date: 2025-10-19

Problem:
Given a string of a valid HTML element, return the attributes of the
element using the following criteria:
- You will only be given one element.
- Attributes will be in the format: attribute="value".
- Return an array of strings with each attribute property and value,
  separated by a comma, in this format:
  ["attribute1, value1", "attribute2, value2"].
- Return attributes in the order they are given.
- If no attributes are found, return an empty array.
"""

import re


def extract_attributes(element):
    pairs = re.findall(r'(\w+)="([^"]*)"', element)
    return [f"{name}, {value}" for name, value in pairs]


assert extract_attributes('<span class="red"></span>') == ["class, red"]
assert extract_attributes('<meta charset="UTF-8" />') == ["charset, UTF-8"]
assert extract_attributes("<p>Lorem ipsum dolor sit amet</p>") == []
assert extract_attributes('<input name="email" type="email" required="true" />') == ["name, email","type, email","required, true"]
assert extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>') == ["id, submit", "class, btn btn-primary"]

print("All tests passed!")


