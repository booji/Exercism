from collections import defaultdict
import re


def word_count(phrase):
    phrase = phrase.lower().replace("\t", " ").replace("\n", " ")
    phrase = re.findall(r"((?:[A-Za-z]+\'?[a-z])|(?:[0-9]+))", phrase)
    count = defaultdict(int)

    for word in phrase:
        count[word] += 1

    return count
