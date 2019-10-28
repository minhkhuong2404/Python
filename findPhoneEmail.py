import pyperclip
import re
import sys
import logging
# -*- coding: utf8 -*-

# logging.disable(logging.CRITICAL) #use to hide the content of logging
logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program')
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|\.|\-)?
    (\d{3})
    (\s|\.|\-)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)

#works for VNese name without sounds
fullNameRegex = re.compile(r'''(
    ([A-Z]([a-z]){2,5}(\s)){2,4}
)''',re.VERBOSE)
#MM/DD/YYYY
dayRegex = re.compile(r'''(
    ([0-1][0-9]
    (\s|\/|\-)
    [0-3][0-9]
    (\s|\/|\-)
    [1-2][0-9]{3})|
    ([1-2][0-9]{3}
    (\s|\/|\-)
    [0-1][0-9]
    (\s|\/|\-)
    [0-3][0-9])
)''',re.VERBOSE)

strongPWRegex = re.compile(r'''(
    ^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$
)''',re.VERBOSE)
phonenum = 0
email = 0
fullName = 0
day = 0

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(groups[0])
    phonenum += 1

for groups in emailRegex.findall(text):
    matches.append(groups[0])
    email += 1

for groups in fullNameRegex.findall(text):
    matches.append(groups[0])
    fullName += 1

for groups in dayRegex.findall(text):
    matches.append(groups[0])
    day += 1

for groups in strongPWRegex.findall(text):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Coopied to clipboard")
    print('\n'.join(matches))
    print("Number of phone number",phonenum)
    print("Number of email",email)
    print("Number of full name",fullName)
    print("Number of day ",day)

else:
    print('No phone and email was found')


# ============================================

def password_check(password):
    flag = 0
    if (len(password)<8):
        flag = -1

    elif not re.search("[a-z]", password):
        flag = -1

    elif not re.search("[A-Z]", password):
        flag = -1

    elif not re.search("[0-9]", password):
        flag = -1

    elif not re.search(r"\W", password):
        flag = -1

    elif re.search("\s", password):
        flag = -1

    else:
        flag = 0
        return True


    if flag ==-1:
        print("Not a Valid Password")
valid = []
for groups in strongPWRegex.findall(text):
    valid.append(groups)
if len(valid) != 0:
    valids = 0
    for pw in valid:
        if password_check(pw) == True:
            valids += 1
    print("There are %d" % valids + " valid password(s)")

logging.debug('End of the program')
