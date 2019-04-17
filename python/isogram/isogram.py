import string
#from collections import Counter
def is_isogram(s=""):
    if s == "":
        return True

    s = s.lower()
    transtab = str.maketrans('','',string.whitespace+'-')
    s = s.translate(transtab)

    return len(s) == len(set(s))
