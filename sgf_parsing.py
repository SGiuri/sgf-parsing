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
    pattern = re.compile(r';(\w+)\[(\w+)\]')

    matches_par1 = pattern_par1.finditer(input_string)
    matches_par2 = pattern.finditer(input_string)

    for match in matches_par1:
        print(match)
    for match in matches_par2:
        print(match[0
              ])
    pass
# modifica dal Dell

#input_string = "(;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))"
input_string = "(;A[B](;B[C][D])(;C[D]))"
parse(input_string)
