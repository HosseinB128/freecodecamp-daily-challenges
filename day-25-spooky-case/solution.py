"""
Challenge: SpOoKy~CaSe
Source: freeCodeCamp
Date: 2025-10-31

Problem:
Given a string representing a variable name, convert it to "spooky case"
using the following constraints:

- Replace all underscores (_) and hyphens (-) with a tilde (~).
- Capitalize the first letter of the string, and every other letter after
  that. Ignore the tilde character when counting. Make all other letters
  lowercase.

For example, given "hello_world", return "HeLlO~wOrLd".
"""


def spookify(boo):
    result = []
    count = 0
    for ch in boo:
        if ch in "_-":
            result.append("~")
        else:
            result.append(ch.upper() if count % 2 == 0 else ch.lower())
            count += 1
    return "".join(result)


# Tests
assert spookify("hello_world") == "HeLlO~wOrLd"
assert spookify("Spooky_Case") == "SpOoKy~CaSe"
assert spookify("TRICK-or-TREAT") == "TrIcK~oR~tReAt"
assert spookify("c_a-n_d-y_-b-o_w_l") == "C~a~N~d~Y~~b~O~w~L"
assert spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") == "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS"

print("All tests passed!")

