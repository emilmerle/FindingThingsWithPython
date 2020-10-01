#!/usr/bin/env python3
"""
numberInFile.py - Finds phone numbers in a given file
and copies them to the clipboard

Usage: call the program with a country as the first argument
and the location of the file as the second argument

Example:
>>> numberInFile.py germany C:\\Users\\ExampleUser\\Documents\\phoneNumbers.txt
"""

from countries import countryDict
import pyperclip
import re
import sys
import os


def main():
    # Check if sys.argv[1] is given and in countryDict
    argumentOne = ""
    try:
        argumentOne = sys.argv[1]
    except IndexError:
        exit("No argument given."
             " Try again with a country as an argument")

    if(argumentOne in countryDict):
        # Create regex object
        regexCompile = re.compile(countryDict[argumentOne], re.VERBOSE)
    else:
        exit("No number format for that country found")

    # Check if sys.argv[2] is given
    argumentTwo = ""
    try:
        argumentTwo = sys.argv[2]
    except IndexError:
        exit("No second argument given."
             " Try again with a file path as an argument")

    # Make absolute path if given path is a relative path
    if(not os.path.isabs(argumentTwo)):
        argumentTwo = os.path.abspath(argumentTwo)

    openedContent = ""

    # Check if argumentTwo is a valid path and file
    if(os.path.exists(argumentTwo) and os.path.isfile(argumentTwo)):
        # Try to open and read file
        try:
            openedFile = open(argumentTwo, "r")
            openedContent = openedFile.read()
        except OSError:
            exit("Could not open file")
    else:
        exit("Given file does not exist: " + argumentTwo)

    matches = []
    # Find all phone numbers and store them in matches
    for groups in regexCompile.findall(openedContent):
        phoneNumber = ''.join(groups)
        matches.append(phoneNumber)

    openedFile.close()

    if len(matches) > 0:
        pyperclip.copy(' -+- '.join(matches))
        print("Phone number(s) found:")
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')


if __name__ == "__main__":
    main()
