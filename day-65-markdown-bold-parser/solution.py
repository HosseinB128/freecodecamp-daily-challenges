"""
Challenge: Markdown Bold Parser
Source: freeCodeCamp
Date: 2025-12-10
Problem: Given a string that may include some bold text in Markdown, return
the equivalent HTML string. Bold text is any text that starts and ends with
two asterisks (**) or two underscores (__), with no spaces between the text
and the asterisks or underscores (spaces inside the text are allowed).
Convert all bold occurrences to HTML <b> tags and return the string.
Example: "**This is bold**" → "<b>This is bold</b>"
"""

import re

def parse_bold(markdown):
    return re.sub(r"(\*\*|__)(\S.*?\S)\1", r"<b>\2</b>", markdown)


# Tests
assert parse_bold("**This is bold**") == "<b>This is bold</b>"
assert parse_bold("__This is also bold__") == "<b>This is also bold</b>"
assert parse_bold("**This is not bold **") == "**This is not bold **"
assert parse_bold("__ This is also not bold__") == "__ This is also not bold__"
assert (
    parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.")
    == "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog."
)
print("All tests passed!")

