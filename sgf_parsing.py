class SgfTree:
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


# Piccola modifica

import re


def parse(input_string):
    '''
    input_string = "(;A[b]C[d])"    -->
            SgfTree(properties={"A": ["b"], "C": ["d"]})
    input_string = "(;A[b][c][d])"  -->
            SgfTree(properties={"A": ["b", "c", "d"]})
    input_string = "(;A[B](;B[C])(;C[D]))"
            SgfTree(
            properties={"A": ["B"]},
            children=[SgfTree({"B": ["C"]}), SgfTree({"C": ["D"]})],
            )

    (;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))
    '''

    pattern_par1 = re.compile(r'\(.+\.+?\).?\)')
    pattern_par2 = re.compile(r'\)')
    pattern = re.compile(r';([A-Z]+(\[[A-Za-z]+\])+)')

    matches_par1 = pattern_par1.finditer(input_string)
    matches_par2 = pattern.finditer(input_string)

    father = re.compile(r'^\(?;([A-Z]+(\[[A-Za-z]\])+)\)?')
    matches_father = father.finditer(input_string)
    children = father.sub("",input_string)
    # modifica
    print(children)
    for match in matches_father:
        print(match[1])

    pass



# modifica dal Dell
# modifica dal fisso
# e questac???'


# input_string = "(;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))"
input_string = "(;A[B](;B[C][D])(;C[D]))"
print(input_string)
parse(input_string)



'''

    # loocking for apen-close parentesys match:
    parentesys = sorted([(k, v) for k, v in find_parentheses(input_string).items()])

    # each parentesys group identifies a node, if one node is inside one onother it
    # identify a children:
    nodes = [input_string[
             parentesys[j][0]+1:parentesys[j][1]] for j in range(len(parentesys))]
    print(nodes)






    """pattern_node = re.compile(r'(?<=;)([A-Z]+(\[[A-Za-z]+\])+)')
    nidification_pattern = re.compile(r'\(.+(\(.+\))?\)')
    pattern_par2 = re.compile(r'\)')
    pattern = re.compile(r';(\w+)\[(\w+)\]')

    nodes = pattern_node.finditer(input_string)

    nidification = nidification_pattern.finditer(input_string)
    matches_par2 = pattern.finditer(input_string)
    print(f"\nparsing: {input_string}")
    for node in nodes:
        print(f"node= {node[0]}")
"""
    pass


# modifica dal Dell
# modifica dal fisso
# e questac???'


# parse(line)


def find_parentheses(s):
    """ Find and return the location of the matching parentheses pairs in s.

    Given a string, s, return a dictionary of start: end pairs giving the
    indexes of the matching parentheses in s. Suitable exceptions are
    raised if s contains unbalanced parentheses.

    """

    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    stack = []
    parentheses_locs = {}
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                parentheses_locs[stack.pop()] = i
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'
                                 .format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs


# input_string = "(;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))"
input_string = ["(;A[B](;B[C][D])(;C[D]))",
                "(;A[B])",
                "(;A[b]C[d])",
                "(;a[b])",
                "(;Aa[b])",
                "(;A[B];B[C])",
                "(;A[B](;B[C])(;C[D]))",
                "(;A[b][c][d])",
                "(;A[\\]b\nc\nd\t\te \n\\]])"]


for line in input_string:
    parse(line)
'''
