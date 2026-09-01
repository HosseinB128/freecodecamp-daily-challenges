"""
Challenge: Extension Extractor
Source: freeCodeCamp
Date: 2025-11-10

Problem:
Given a string representing a filename, return the extension of the file.

- The extension is the part of the filename that comes after the last period (.).
- If the filename does not contain a period or ends with a period, return "none".
- The extension should be returned as-is, preserving case.

Example:
get_extension("document.txt") -> "txt"
get_extension("README") -> "none"
get_extension("image.PNG") -> "PNG"
get_extension(".gitignore") -> "gitignore"
get_extension("archive.tar.gz") -> "gz"
get_extension("final.draft.") -> "none"
"""

def get_extension(filename):
    return filename.split('.')[-1] if '.' in filename and not filename.endswith('.') else "none"

# Tests
assert get_extension("document.txt") == "txt"
assert get_extension("README") == "none"
assert get_extension("image.PNG") == "PNG"
assert get_extension(".gitignore") == "gitignore"
assert get_extension("archive.tar.gz") == "gz"
assert get_extension("final.draft.") == "none"
print("All tests passed!")

