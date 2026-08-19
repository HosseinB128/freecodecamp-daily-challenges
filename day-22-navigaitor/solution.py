"""
Challenge: Navigator
Source: freeCodeCamp Daily Challenge
Date: 2025-10-28

Problem:
On October 28, 1994, Netscape Navigator was released, helping millions
explore the early web.

Given an array of browser commands you executed on Netscape Navigator,
return the current page you are on after executing all the commands
using the following rules:

- You always start on the "Home" page, which will not be included in
  the commands array.
- Valid commands are:
    - "Visit Page": Where "Page" is the name of the page you are
      visiting. For example, "Visit About" takes you to the "About"
      page. When you visit a new page, make sure to discard any
      forward history you have.
    - "Back": Takes you to the previous page in your history, or
      stays on the current page if there isn't one.
    - "Forward": Takes you forward in the history to the page you
      came from, or stays on the current page if there isn't one.

Example:
navigate(["Visit About Us", "Back", "Forward"]) returns "About Us"
"""


def navigate(commands):
    current = "Home"
    back_stack = []
    forward_stack = []

    for command in commands:
        if command.startswith("Visit "):
            back_stack.append(current)
            current = command[len("Visit "):]
            forward_stack = []
        elif command == "Back" and back_stack:
            forward_stack.append(current)
            current = back_stack.pop()
        elif command == "Forward" and forward_stack:
            back_stack.append(current)
            current = forward_stack.pop()

    return current


# Tests
assert navigate(["Visit About Us", "Back", "Forward"]) == "About Us"
assert navigate(["Forward"]) == "Home"
assert navigate(["Back"]) == "Home"
assert navigate(["Visit About Us", "Visit Gallery"]) == "Gallery"
assert navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) == "Home"
assert navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) == "Contact"
assert navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) == "Visit Us"
print("All tests passed!")

