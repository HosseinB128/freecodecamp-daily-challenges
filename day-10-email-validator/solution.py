"""
Challenge: Email Validator
Source: freeCodeCamp
Date: 2025-10-16

Problem description:
Given a string, determine if it is a valid email address using the following constraints:
- It must contain exactly one '@' symbol.
- The local part (before the '@'):
    - Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
    - Cannot start or end with a dot.
- The domain part (after the '@'):
    - Must contain at least one dot.
    - Must end with a dot followed by at least two letters.
- Neither the local nor domain part can have two dots in a row.

Example:
    validate("a@b.cd") -> True
    validate(".b@sh.rc") -> False
"""

import re

def validate(email):
    pattern = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@[^.@]+(\.[^.@]+)*\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# Tests
assert validate("a@b.cd") == True
assert validate("hell.-w.rld@example.com") == True
assert validate(".b@sh.rc") == False
assert validate("example@test.c0") == False
assert validate("freecodecamp.org") == False
assert validate("develop.ment_user@c0D!NG.R.CKS") == True
assert validate("hello.@wo.rld") == False
assert validate("hello@world..com") == False
assert validate("develop..ment_user@c0D!NG.R.CKS") == False
assert validate("git@commit@push.io") == False

print("All tests passed!")

