import re
import string
def hey(phrase):
    transtab = str.maketrans('','',string.whitespace)
    phrase = phrase.translate(transtab)
    if len(phrase) > 0:
        punctuation = phrase[-1]
    else:
        punctuation = 'None'

    shouting = phrase.isupper()

    if shouting:
        if punctuation == '?':
            response = "Calm down, I know what I'm doing!"
        else:
            response = "Whoa, chill out!"
    else:
        if phrase == "":
            response = "Fine. Be that way!"
        elif punctuation == '?':
            response = "Sure."
        else:
            response = "Whatever."

    return response
