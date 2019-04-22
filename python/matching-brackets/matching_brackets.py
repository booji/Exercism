def is_paired(input_string):
    symbol = []
    for char in input_string:
        if char in '([{':
            symbol.append(char)
        elif char in ')]}':
            try:
                last = symbol.pop()
                if (char == ')' and last != '(') or \
                   (char == ']' and last != '[') or \
                   (char == '}' and last != '{'):

                    return False
            except IndexError:
                return False

    return len(symbol) == 0
