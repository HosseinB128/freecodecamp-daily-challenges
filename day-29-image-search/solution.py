"""
Challenge: Image Search
Source: freeCodeCamp
Date: 2025-11-04
Problem: Given an array of image names and a search term, return an array of
image names containing the search term (case-insensitive), preserving the
original order.
"""

def image_search(images, term):
    return [item for item in images if term.lower() in item.lower()]


# Tests
assert image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog") == ["dog.png"]
assert image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun") == ["Sunset.jpg", "sunflower.jpeg"]
assert image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG") == ["Moon.png", "stars.png"]
assert image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat") == ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"]

print("All tests passed!")

