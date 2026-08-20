"""
Challenge: Email Sorter
Source: freeCodeCamp
Date: 2025-10-29

Problem:
Given a list of email addresses, sort them alphabetically by domain name
first (the part after the '@'), and username second (the part before the
'@').
- Sorting should be case-insensitive.
- If more than one email has the same domain, sort them by their username.
- Return an array of the sorted addresses.
- Returned addresses should retain their original case.

Example:
Given ["jill@mail.com", "john@example.com", "jane@example.com"], return
["jane@example.com", "john@example.com", "jill@mail.com"].
"""


def sort(emails):
    return sorted(emails, key=lambda address: tuple(part.lower() for part in reversed(address.split('@'))))


# Tests
assert sort(["jill@mail.com", "john@example.com", "jane@example.com"]) == ["jane@example.com", "john@example.com", "jill@mail.com"]
assert sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]) == ["bob@mail.com", "carol@mail.com", "alice@zoo.com"]
assert sort(["user@z.com", "user@y.com", "user@x.com"]) == ["user@x.com", "user@y.com", "user@z.com"]
assert sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]) == ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"]
assert sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]) == ["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com", "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"]

print("All tests passed!")

