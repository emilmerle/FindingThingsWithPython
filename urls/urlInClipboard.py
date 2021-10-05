#! python3
# urlInClipboard.py - Finds urls on the clipboard and copies them to the clipboard
# Usage: Copy some text call the program
# Example: >>> numberOnClipboard.py

import url
import pyperclip


def main():
    # Find matches in clipboard text.
    text = str(pyperclip.paste())
    matches = []
    for url_match in url.regexp.findall(text):
        matches.append(url_match)

    if len(matches) > 0:
        pyperclip.copy(' -+- '.join(matches))
        print("Url(s) found:")
        print('\n'.join(matches))
    else:
        print('No Url found.')


if __name__ == "__main__":
    main()
