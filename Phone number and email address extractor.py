import re
import pyperclip

# Step 1: Create phoneRegex
phoneRegex = re.compile(r'''
    # Match phone numbers like (123) 456-7890, 123-456-7890, 123.456.7890, 123 456 7890, etc.
    (
    (\d{3}|\(\d{3}\))?              # area code (optional)
    (\s|-|\.)?                      # separator (optional)
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (optional)
    )
''', re.VERBOSE)

# Step 2: Create emailRegex
emailRegex = re.compile(r'''
    # Match email addresses
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
''', re.VERBOSE)

# Step 3: Find Matches in Clipboard Text
text = str(pyperclip.paste())
matches = []

# Find all phone numbers
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8]:  # if extension exists
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

# Find all email addresses
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Step 4: Copy Results to the Clipboard
if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
