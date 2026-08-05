"""
Challenge: HTML Tag Stripper
Source: freeCodeCamp
Date: 2025-10-15

Problem:
Given a string of HTML code, remove the tags and return the plain text content.
The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.

Examples:
strip_tags('<a href="#">Click here</a>') -> "Click here"
strip_tags('<p class="center">Hello <b>World</b>!</p>') -> "Hello World!"
strip_tags('<img src="cat.jpg" alt="Cat">') -> ""
strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') -> "sectionsection"
"""

import re

def strip_tags(html):
    return re.sub(r'<[^>]*>', '', html)


# Tests
assert strip_tags('<a href="#">Click here</a>') == "Click here"
assert strip_tags('<p class="center">Hello <b>World</b>!</p>') == "Hello World!"
assert strip_tags('<img src="cat.jpg" alt="Cat">') == ""
assert strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') == "sectionsection"

print("All tests passed!")

