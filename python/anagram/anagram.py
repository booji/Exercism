from collections import defaultdict

def find_anagrams(word, candidates):
    word = word.lower()
    anagram  = []
    for candidate in candidates:
        if word != candidate.lower():
            if append_check(word, candidate.lower()):
                anagram.append(candidate)
    return anagram

def letter_counter(word):
    count = defaultdict(int)
    for letter in word:
        count[letter] += 1
    return count

def append_check(word,candidate):
    word = letter_counter(word)
    candidate = letter_counter(candidate)
    count = 0
    for key in word.keys() & candidate.keys():
        count += 1
        if word[key] - candidate[key] != 0:
            return False
    if count != len(word) or word != candidate:
        return False
    return True
