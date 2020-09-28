#! python3
# numberInFile.py - Finds phone numbers in a given file and copies them to the clipboard
# Usage: call the program with a country as the first argument and the location of the file as the second argument
# Example: >>> numberInFile.py germany C:\\Users\\ExampleUser\\Documents\\phoneNumbers.txt

import pyperclip, re, sys, os

#Create dictionary to store regex expressions for different countries
countryDict = {}

#Create phone regex for country specific number format and add it to countryDict
germany = r'''(
    (\d{3}|\(\d{3}\))? # area code (optional)
    (\s|-|\.|/)? # separator (optional)
    (\d{7,9}) # 7 to 9 digits
    )'''
spain = r"(^[98](\d{8}))"

countryDict["germany"] = germany
countryDict["spain"] = spain
# Check if sys.argv[1] is given and in countryDict
argumentOne = ""
try:
    argumentOne = sys.argv[1]
except IndexError:
    exit("No argument given. Try again with a country as an argument")

if(argumentOne in countryDict):
    #Create regex object
    regexCompile = re.compile(countryDict[argumentOne], re.VERBOSE|re.MULTILINE)
else:
    exit("No number format for that country found")

#Check if sys.argv[2] is given
argumentTwo = ""
try:
    argumentTwo = sys.argv[2]
except IndexError:
    exit("No second argument given. Try again with a file path as an argument")


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
#Find all phone numbers and store them in matches
for groups in regexCompile.findall(openedContent):
    phoneNumber = groups[0]
    matches.append(phoneNumber)

openedFile.close()

if len(matches) > 0:
  #  pyperclip.copy(' -+- '.join(matches))
    print("Phone number(s) found:")
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
