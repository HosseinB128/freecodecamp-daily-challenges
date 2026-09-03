"""
Challenge: Email Signature Generator
Source: freeCodeCamp
Date: 2025-11-12
Problem: Given strings for a person's name, title, and company, return an
email signature as a single string using the following rules:
- The name should appear first, preceded by a prefix that depends on the
  first letter of the name (case-insensitive):
    - A-I: use ">>" as the prefix.
    - J-R: use "--" as the prefix.
    - S-Z: use "::" as the prefix.
- A comma and space (", ") should follow the name.
- The title and company should follow the comma and space, separated by
  " at " (with spaces around it).
Example: generate_signature("Quinn Waverly", "Founder and CEO", "TechCo")
returns "--Quinn Waverly, Founder and CEO at TechCo"
"""

def generate_signature(name, title, company):
    first_letter = name[0].lower()

    if first_letter <= "i":
        prefix = ">>"
    elif first_letter <= "r":
        prefix = "--"
    else:
        prefix = "::"

    return f"{prefix}{name}, {title} at {company}"


# Tests
assert generate_signature("Quinn Waverly", "Founder and CEO", "TechCo") == "--Quinn Waverly, Founder and CEO at TechCo"
assert generate_signature("Alice Reed", "Engineer", "TechCo") == ">>Alice Reed, Engineer at TechCo"
assert generate_signature("Tina Vaughn", "Developer", "example.com") == "::Tina Vaughn, Developer at example.com"
assert generate_signature("B. B.", "Product Tester", "AcmeCorp") == ">>B. B., Product Tester at AcmeCorp"
assert generate_signature("windstorm", "Cloud Architect", "Atmospheronics") == "::windstorm, Cloud Architect at Atmospheronics"
print("All tests passed!")

