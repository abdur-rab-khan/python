"""
 * 🟡 N-ary tree is a type of tree data structure where they don't have fixed number of children's like in "binary tree", they might have "n" number of children.
 """

class NaryNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def nary_preorder(root):
    if root is None:
        return []
    result = [root.value]
    for child in root.children:
        result.extend(nary_preorder(child))
    return result
