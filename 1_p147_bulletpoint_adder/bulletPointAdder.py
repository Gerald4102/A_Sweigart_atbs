#!/usr/bin/env python3
# bulletPointAdder.py - Adds bullet points to the start
# of each line of text on the clipboard.

import pyperclip
TEXT = pyperclip.paste()

# Separate lines and add asteriks to each.
LINES = TEXT.split('\n')
for i in range(len(LINES)):
    LINES[i] = '* ' + LINES[i]

TEXT = '\n'.join(LINES)

pyperclip.copy(TEXT)