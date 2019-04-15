import string

alphabet = list(string.ascii_uppercase)

def make_diamond(letter):
    depth_az = alphabet.index(letter)
    empty = [" "] * (depth_az * 2 + 1)
    result = []

    for i, item in enumerate(alphabet[depth_az::-1]):
        tmp = empty.copy()
        tmp[i] = item
        tmp[-i - 1] = item
        result.insert(0, "".join(tmp))
        result.insert(-1, "".join(tmp))

    # removes widest duplicate
    result = result[:-1]

    return "\n".join(result) + '\n'
