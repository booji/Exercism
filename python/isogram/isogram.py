import string
from collections import Counter
def is_isogram(s=""):
    if s == "":
        return True

    s = s.lower()
    transtab = str.maketrans('','',string.whitespace+'-')
    s = s.translate(transtab)
    counterString=Counter(s)
    count = [x[1] for x in counterString.most_common(1)]

    return count[0] < 2
