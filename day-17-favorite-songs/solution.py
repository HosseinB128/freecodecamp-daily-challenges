"""
Challenge: Favorite Songs
Source: freeCodeCamp
Date: 2025-10-23
Problem: Given an array of song objects representing your iPod playlist,
return an array with the titles of the two most played songs, with the
most played song first. Each object has a "title" property (string) and
a "plays" property (integer).
Example: favoriteSongs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2}]) returns ["Sync or Swim", "Earbud Blues"]
"""

def favorite_songs(playlist):
    return [i['title'] for i in sorted(playlist, key=lambda p: p['plays'], reverse=True)][:2]

# Tests
assert favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2}]) == ["Sync or Swim", "Earbud Blues"]
assert favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100}]) == ["Clickwheel Love", "99 Downloads"]
assert favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75}]) == ["Song B", "Song C"]
print("All tests passed!")

