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

    first_occurence = re.compile(r'^(\()?;([A-Z]+(\[[A-Za-z0-9]+\])+)\)?')
    matches_father = first_occurence.finditer(input_string)
    children = first_occurence.sub("", input_string)
    # modifica
    print(input_string,children)
    for match in matches_father:
        print(match[2])

    pass

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
'''

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


def node_parse(single_node):
    '''

    :param single_node: a string like "AA[bb][cc]BB[dd][n]"
    :return: Doctionary: {AA: [bb, cc], BB:[dd,n]}
    '''
    import re
    single_property_parse = re.compile(r"[A-Za-z]+(\[[a-z0-9]+\])+")
    single_property = re.finditer(single_property_parse, single_node)
    for j in single_property:
        print(j[0])

    property_pattern = re.compile(r"^([A-Z]+)")
    value_pattern = re.compile(r"\[([a-z0-9]+)\]")

    for a in re.findall(property_pattern, single_node):
        print(a)

    for a in re.findall(value_pattern, single_node):
        print(a)
    '''for line in input_string:
        parse(line)'''


# input_string = "(;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))"
input_string = ["(;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))",
                "(;A[B](;B[C][D])(;C[D]))",
                "(;A[B])",
                "(;A[b]C[d])",
                "(;a[b])",
                "(;Aa[b])",
                "(;A[B];B[C])",
                "(;A[B](;B[C])(;C[D]))",
                "(;A[b][c][d])",
                "(;A[\\]b\nc\nd\t\te \n\\]])"]


print(node_parse("AA[bb][cc][4]BB[dd][ee][4]"))



s = "AA[bb][cc][4]"


