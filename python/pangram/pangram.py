def is_pangram(sentence):
    sentence = sentence.lower()
    sentence = set(sentence)
    count = 0
    for item in sentence:
        if item in 'abcdefghijklmnopqrstuvwxyz':
            count += 1
    if count == 26:
        return True
    else:
        return False
