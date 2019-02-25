import string
import re

def abbreviate(words):
    words = re.findall(r"[A-Za-z\']+", words)
    firstLetters = [word[0].upper() for word in words]
    return ''.join(firstLetters)
