#! python3
# phoneAndEmail.py - Find phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 # area code
    (\s|-|\.)?                         # separator
    (\d{3})                            # first 3 digits
    (\s|-|\.)                          # separator
    (\d{4})                            # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extention
)''', re.VERBOSE)

# Creat email Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                  # username
    @                                  # @ sign
    [a-zA-Z0-9.-]+                     # domain name
    (\.[a-zA-Z]{2,4})                  # dot-something
)''', re.VERBOSE)


# TODO: Find matches in clipboard text

# TODO: Copy results to the clipboard.