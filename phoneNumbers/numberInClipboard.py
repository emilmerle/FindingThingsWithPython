#! python3
# numberInClipboard.py - Finds phone numbers on the clipboard and copies them to the clipboard
# Usage: Copy some text and call the program with a country as the first argument
# Example: >>> numberOnClipboard.py germany

import pyperclip, re, sys

#Create dictionary to store regex expressions for different countries
countryDict = {}

#Create phone regex for country specific number format and add it to countryDict

germany = r'''(
    (\d{3}|\(\d{3}\))? # area code (optional)
    (\s|-|\.|/)? # separator (optional)
    (\d{7,9}) # 7 to 9 digits
    )'''
countryDict["germany"] = germany


# Check if sys.argv[1] in countryDict and create regex object
argumentOne = ""
try:
    argumentOne = sys.argv[1]
except IndexError:
    exit("No argument given. Try again with a country as an argument")

if(argumentOne in countryDict):
    #Create regex object
    regexCompile = re.compile(countryDict[argumentOne], re.VERBOSE)
else:
    exit("No number format for that country found")



# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in regexCompile.findall(text):
    phoneNumber = groups[0]
    matches.append(phoneNumber)

if len(matches) > 0:
    pyperclip.copy(' -+- '.join(matches))
    print("Phone number(s) found:")
    print('\n'.join(matches))
else:
    print('No phone number found.')
