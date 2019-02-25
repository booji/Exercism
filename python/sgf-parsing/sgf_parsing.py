import re

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other

#Thanks to Quitz321's solution helped me get past the point I was stuck
def parse(input_string):
    #cleaning input
    input_string = input_string.replace("\\", "").replace("\t", " ")
    if not input_string:
        raise ValueError('No input string')
    if input_string == '(;)':
        return SgfTree()


    regex_key = r"\;?(?P<keys>[A-Z]+)?"
    regex_val = r"(?:\[(?P<values>(?:.|\s)+?\]?)\])"

    #included finding open and closing Paren incase multiple nested SgfTree
    #becomes a test case.
    regex_opening = r"(?P<opening>\(?)"
    regex_closing = r"(?P<closing>\)?)"
    regex_tree = r"(?P<Tree>"+regex_opening+regex_key+regex_val+"+"+regex_closing+")"
    matches = re.finditer(regex_tree, input_string)

    properties = {}
    children = []
    new_node = 0
    if not re.match(regex_tree, input_string):
        raise ValueError(f'Incorrect Syntax check input string: {input_string}')

    for match in matches:
        tree = match.group('Tree')
        key = match.group('keys')

        value = []
        if ';' in tree:
            new_node += 1
        for values in re.finditer(regex_val,tree):
            value.append(values.group('values'))
        if new_node == 1:
            properties[key] = value
        else:
            children.append(SgfTree({key: value}))


    return SgfTree(properties, children)
