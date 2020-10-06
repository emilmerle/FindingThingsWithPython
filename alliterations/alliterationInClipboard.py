#! python3
# alliterationInClipboard.py - Finds alliteration on the clipboard and copies them to the clipboard
# Usage: Copy some text and call the program
# Example: >>> alliterationInClipboard.py

import alliteration
import pyperclip


def main():
    # Find matches in clipboard text.
    text = " " + str(pyperclip.paste())
    matches = []
    for groups in alliteration.regexp.findall(text):
        alliterations = groups[0][1:]  # [1:] removes the space character
        matches.append(alliterations)

    if len(matches) > 0:
        pyperclip.copy(' -+- '.join(matches))
        print("Alliteration(s) found:")
        print('\n'.join(matches))
    else:
        print('No alliteration found.')


if __name__ == "__main__":
    main()
