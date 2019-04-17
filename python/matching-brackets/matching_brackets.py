from collections import deque
import re
def is_paired(input_string):
    braces = 0
    square = 0
    paran = 0
    symbol = deque()
    for item in re.findall(r"[\(\)\{\}\[\]]",input_string):
        if item == '(':
            paran += 1
            symbol.append(item)
        elif item == '[':
            square += 1
            symbol.append(item)
        elif item == '{':
            braces += 1
            symbol.append(item)
        else:
            try:
                check = symbol.pop()
            except:
                return False
            if item == ')':
                if check != '(':
                    return False
                paran -= 1
            elif item == ']':
                if check != '[':
                    return False
                square -= 1
            elif item == '}':
                if check != '{':
                    return False
                braces -= 1
        if braces < 0 or square < 0 or paran < 0:
            return False

    return braces == 0 and square == 0 and paran == 0
