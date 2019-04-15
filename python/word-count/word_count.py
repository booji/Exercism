from collections import Counter
import re


def word_count(phrase):
    return Counter(re.findall(r"((?:[a-z]+\'?[a-z])|"
                              r"(?:[0-9]+))", phrase.lower()))
