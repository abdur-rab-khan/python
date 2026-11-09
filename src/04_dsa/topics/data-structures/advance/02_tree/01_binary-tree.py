"""
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                            🌲TREE                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                              |
| 🟡 A Tree a non-linear data structure that stores data in a tree form, where items (Node) are connected with each other using (Edges) like a "family tree"   |
|    "folder structure" etc.                                                                                                                                   |
|                                                                                                                                                              |
|     🔶 Key Terminologies:                                                                                                                                    |
|           🔸 Node:    Box/Item that holds (currentData + links to children).                                                                                 |
|           🔸 Root:    The topmost node.                                                                                                                      |
|           🔸 Parent:  A parent that has children's below                                                                                                     |
|           🔸 Child:   A node directly below a parent                                                                                                         |
|           🔸 Leaf:    A node with no children                                                                                                                |
|           🔸 Edge:    The connection line between a parent and child                                                                                         |
|           🔸 Depth:   How many steps a node from the root                                                                                                    |
|           🔸 Height:  How many steps from a node down to the deepest leaf.                                                                                   |
|                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]
