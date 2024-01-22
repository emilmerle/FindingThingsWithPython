#! python3
# taskInFile.py - Finds tasks in a given markdown file, prints them to the terminal and copys them to the clipboards
# Usage: call the program with a file path as the first argument
# Example: >>> taskInFile.py C:\\Users\\ExampleUser\\Documents\\myTasks.md


# import pyperclip
import sys
import os


def main():
    # Check if sys.argv[1] is given
    argumentOne = ""
    try:
        argumentOne = sys.argv[1]
    except IndexError:
        exit("No argument given. Try again with a file path as an argument")

    # Make absolute path if given path is a relative path
    if not os.path.isabs(argumentOne):
        argumentOne = os.path.abspath(argumentOne)

    files = os.listdir(argumentOne)

    for file in files:
        if file.endswith(".md"):
            handleFile(argumentOne + "\\" + file)


def handleFile(markdownFile: str):
    with open(markdownFile, "r") as f:
        for line in f:
            if "!!!" in line:
                print(f"Task in line found: {line[:-1]}")


if __name__ == "__main__":
    main()
