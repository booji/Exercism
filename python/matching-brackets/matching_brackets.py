def is_paired(input_string):
    symbol = []
    for chr in input_string:
        if chr in '([{':
            symbol.append(chr)
        elif chr in ')]}':
            try:
                last = symbol.pop()
                if (chr == ')' and last != '(') or \
                   (chr == ']' and last != '[') or \
                   (chr == '}' and last != '{'):

                    return False
            except IndexError:
                return False

    return len(symbol) == 0
