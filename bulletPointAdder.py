# paste text from clipboard
#do somethign with it
#copy text to clipboard

import pyperclip
import sys

text = pyperclip.paste()

#separate lines and add stars

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
