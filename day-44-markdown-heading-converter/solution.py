"""
Challenge: Markdown Heading Converter
Source: freeCodeCamp
Date: 2025-11-19

Problem:
Given a string representing a Markdown heading, return the equivalent HTML heading.
A valid Markdown heading must:
- Start with zero or more spaces, followed by
- 1 to 6 hash characters (#) in a row, then
- At least one space. And finally,
- The heading text.

The number of hash symbols determines the heading level. For example, one hash
symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.
If the given string doesn't have the exact format above, return "Invalid format".

Example:
convert("# My level 1 heading") ➞ "<h1>My level 1 heading</h1>"
"""

import re

def convert(heading):
    match = re.match(r"^ *(#{1,6}) +(.*)$", heading)

    if not match:
        return "Invalid format"

    count_numbersign = len(match.group(1))
    text = match.group(2)

    return f"<h{count_numbersign}>{text}</h{count_numbersign}>"


assert convert("# My level 1 heading") == "<h1>My level 1 heading</h1>"
assert convert("My heading") == "Invalid format"
assert convert("##### My level 5 heading") == "<h5>My level 5 heading</h5>"
assert convert("#My heading") == "Invalid format"
assert convert("  ###  My level 3 heading") == "<h3>My level 3 heading</h3>"
assert convert("####### My level 7 heading") == "Invalid format"
assert convert("## My #2 heading") == "<h2>My #2 heading</h2>"

print("All tests passed!")

