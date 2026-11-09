"""
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                        🌲 Binary Search Tree (BST)                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                          |
| 🟡 Binary Search Tree (BST) is a tree data structure that stores data in a structured manner, like "always left child must be smaller than it's parent", "always right"  |
|    "must be greater than it's parent".                                                                                                                                   |
|                                                                                                                                                                          |
|        8                                                                                                                                                                 |
|       / \                                                                                                                                                                |
|      3  10                                                                                                                                                               |
|     / \  \                                                                                                                                                               |
|    1  6  14                                                                                                                                                              |
|                                                                                                                                                                          |
| 🔷 Look, 3 (left child) < 8 (parent) ⏭️ 10 (right child) > 8 (parent) ⏭️ 1 (left child) < 3 (parent) ⏭️ 6 (right child) > 3 (parent) ⏭️ 14 (right child) > 10 (parent)  |
|                                                                                                                                                                          |
| 🔶 BST Operations:                                                                                                                                                       |
|    🔸 Insert: So the insert here is really simple we find place where "val" fits, either on left/right side.                                                             |
|    🔸 Search: Go either left/right based on the target if greater than left move to right otherwise move to left.                                                        |
|    🔸 Remove: Deleting Node in BST, is little bit tricky because after deleting we need to shift the tree to fill the gap, there will be three conditions while deleting |
|               1. Target don't have any child in this condition, we simple return nullptr no need to shift anything                                                       |
|               2. Target have either left child, right child, it's also simple because once we delete it we simple get once of the child in a place of target.            |
|               3. Target have two child, it's the tricker in this condition we try to find the "min node" replace the removed node data with the "min node" one,          |
|                  and we again delete "min node" data, and always "min node" will going to lie between "case 1, case 2", because the "min node" will always smaller       |
|                  means it's the last node which have only right node, because if they have left node than it never be a "min node".                                      |
|                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Case 1: No Children found

# Case 3: Two Children found

# Case 2: One Children found

class BSTNode:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

def bst_insert(root, value):
    if root is None:
        return BSTNode(value)
    if value < root.value:
        root.left = bst_insert(root.left, value)
    elif value > root.value:
        root.right = bst_insert(root.right, value)
    return root

def bst_search(root, value):
    while root:
        if root.value == value:
            return root
        root = root.left if value < root.value else root.right
    return None
