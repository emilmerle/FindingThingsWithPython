#! python3
# emailInFile.py - Finds email addresses in a given file and copies them to the clipboard
# Usage: call the program with a file path as the first argument
# Example: >>> emailInFile.py C:\\Users\\ExampleUser\\Documents\\addresses.txt

import pyperclip, re, sys, os

#Check if sys.argv[1] is given
argumentOne = ""
try:
    argumentOne = sys.argv[1]
except IndexError:
    exit("No second argument given. Try again with a file path as an argument")

# Make absolute path if given path is a relative path
if(not os.path.isabs(argumentOne)):
    argumentOne = os.path.abspath(argumentOne)

openedContent = ""

# Check if argumentOne is a valid path and file
if(os.path.exists(argumentOne) and os.path.isfile(argumentOne)):
    # Try to open and read file
    try:
        openedFile = open(argumentOne, "r",encoding='ascii',errors='ignore')
        openedContent = openedFile.read()
    except OSError:
        exit("Could not open file")
else:
    exit("Given file does not exist: " + argumentOne)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
    )''', re.VERBOSE)

matches = []
for groups in emailRegex.findall(openedContent):
    emails = groups[0]
    matches.append(emails)

openedFile.close()

if len(matches) > 0:
    pyperclip.copy(' -+- '.join(matches))
    print("Email address(es) found:")
    print('\n'.join(matches))
else:
    print('No email address found.')
