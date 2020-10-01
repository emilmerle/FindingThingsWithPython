#! python3
# alliterationInFile.py - Finds alliterations in a given file and copies them to the clipboard
# Usage: call the program with a file path as the first argument
# Example: >>> alliterationInFile.py C:\\Users\\ExampleUser\\Documents\\aRealText.txt

import alliteration
import pyperclip
import sys
import os


def main():
    # Check if sys.argv[1] is given
    argumentOne = ""
    try:
<<<<<<< HEAD
        argumentOne = sys.argv[1]
    except IndexError:
        exit("No second argument given. "
             "Try again with a file path as an argument")

    # Make absolute path if given path is a relative path
    if(not os.path.isabs(argumentOne)):
        argumentOne = os.path.abspath(argumentOne)

    openedContent = ""

    # Check if argumentOne is a valid path and file
    if(os.path.exists(argumentOne) and os.path.isfile(argumentOne)):
        # Try to open and read file
        try:
            openedFile = open(argumentOne, "r")
            openedContent = openedFile.read()
        except OSError:
            exit("Could not open file")
    else:
        exit("Given file does not exist: " + argumentOne)

    matches = []
    for groups in alliteration.regexp.findall(openedContent):
        alliterations = groups[0][1:]
        matches.append(alliterations)

    openedFile.close()

    if len(matches) > 0:
        pyperclip.copy(' -+- '.join(matches))
        print("Alliteration(s) found:")
        print('\n'.join(matches))
    else:
        print('No alliteration found.')


if __name__ == "__main__":
    main()
=======
        openedFile = open(argumentOne, "r",encoding='ascii',errors='ignore')
        openedContent = openedFile.read()
    except OSError:
        exit("Could not open file")
else:
    exit("Given file does not exist: " + argumentOne)

# Create alliteration regex.
alliRegex = re.compile(r"((\s)(\w)\w*\s\3\w*((\s\3\w*)?)*)", re.IGNORECASE)

matches = []
for groups in alliRegex.findall(openedContent):
    alliterations = groups[0][1:]
    matches.append(alliterations)

openedFile.close()

if len(matches) > 0:
    pyperclip.copy(' -+- '.join(matches))
    print("Alliteration(s) found:")
    print('\n'.join(matches))
else:
    print('No alliteration found.')
>>>>>>> 3c73d451606203216ef00f7bfb7a176bce5a8c43
