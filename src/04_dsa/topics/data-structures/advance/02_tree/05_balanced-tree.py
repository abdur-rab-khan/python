"""
 * 🟡 A balanced tree is a type of binary tree data structure, where the height of "left" and "right" isn't greater than "1".
 *
 *       🔸 Balanced Tree:
 *                           4
 *                          / \
 *                         8  20
 *                             \
 *                             80
 *
 *       🔸 Unbalanced Tree:
 *                             1
 *                              \
 *                               2
 *                                \
 *                                 3
 *                                  \
 *                                   4
"""

def height(root):
    if root is None: return 0
    return 1 + max(height(root.left), height(root.right))

def is_balanced(root):
    if root is None: return True
    if abs(height(root.left) - height(root.right)) > 1: return False
    return is_balanced(root.left) and is_balanced(root.right)
