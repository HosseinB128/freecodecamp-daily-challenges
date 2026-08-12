"""
Challenge: Speak Wisely, You Must
Source: freeCodeCamp
Date: 2025-10-22

Problem description:
Given a sentence, return a version of it that sounds like advice from a
wise teacher using the following rules:

- Words are separated by a single space.
- Find the first occurrence of one of the following words in the sentence:
  "have", "must", "are", "will", "can".
- Move all words before and including that word to the end of the sentence
  and:
    - Preserve the order of the words when you move them.
    - Make them all lowercase.
    - Add a comma and a space before them.
- Capitalize the first letter of the new first word of the sentence.
- All given sentences will end with a single punctuation mark. Keep the
  original punctuation of the sentence and move it to the end of the new
  sentence.
- Return the new sentence, making sure there is a single space between
  each word and no spaces at the beginning or end of the sentence.

Example:
wise_speak("You must speak wisely.") -> "Speak wisely, you must."
"""

WISE_WORDS = {"have", "must", "are", "will", "can"}


def wise_speak(sentence):
    punctuation = sentence[-1]
    words = sentence[:-1].split()

    index = next((i for i, w in enumerate(words) if w in WISE_WORDS), None)

    moved = " ".join(words[:index + 1]).lower()
    remaining = " ".join(words[index + 1:])

    result = f"{remaining}, {moved}{punctuation}"
    return result[0].upper() + result[1:]


# Tests
assert wise_speak("You must speak wisely.") == "Speak wisely, you must."
assert wise_speak("You can do it!") == "Do it, you can!"
assert wise_speak("Do you think you will complete this?") == "Complete this, do you think you will?"
assert wise_speak("All your base are belong to us.") == "Belong to us, all your base are."
assert wise_speak("You have much to learn.") == "Much to learn, you have."

print("All tests passed!")

