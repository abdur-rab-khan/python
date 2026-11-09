"""
 +----------------------------------------------------------------------------------------------------------------------------------------------------------+
 |                                                        🟡 Different View in Tree Data Structure                                                          |
 +----------------------------------------------------------------------------------------------------------------------------------------------------------+
 |                                                                                                                                                          |
 | 🟡 Different Views shows how/what nodes will be visible if we look tree from different angles, it can be either left/right/top/bottom.                   |
 | 🟡 On different views we can see different nodes and some nodes might be hidden due to overlap, let's see all one by one.                                |
 |                                                                                                                                                          |
 |   🔹 Left View:                                                                                                                                          |
 |                 If we look a tree from left side what nodes will be visible and what will be overlap, So only first node from the left will be visible.  |
 |                                                                                                                                                          |
 |   🔹 Right View:                                                                                                                                         |
 |                 If we look a tree from right side what nodes will be visible and what will be overlap, So only first node from the right will be visible |
 |                                                                                                                                                          |
 |   🔷 Example:                                                                                                                                            |
 |                 1                                                                                                                                        |
 |                / \                                                                                                                                       |
 |       👁️      2   3     👁️                                                                                                                              |
 |              / \   \                                                                                                                                     |
 |             5   6   4                                                                                                                                    |
 |                  \   \                                                                                                                                   |
 |                   8   9                                                                                                                                  |
 |                                                                                                                                                          |
 |      👉 If you look from left you can only see 1, 2, 5 and 8, not 3 and 6 because it's overlapping with 5.                                               |
 |      👉 If you look from right you can only see 1, 3, 6 and 8, not 5 because it's overlapping with 6.                                                    |
 |                                                                                                                                                          |
 |   🔹 Top View:                                                                                                                                           |
 |               If we look a tree from top view, what nodes will be visible and what will be overlap.                                                      |
 |                                                                                                                                                          |
 |   🔹 Bottom View:                                                                                                                                        |
 |                 If we look a tree from top view, what nodes will be visible and what will be overlap.                                                    |
 |                                                                                                                                                          |
 |      👉 On above example If you look from top you will be 1, 2, 5, 3 not 6 (hide by 1), 8 (hide by 3), it numbers must be in shorted order my HD.        |
 |         HD (Horizontal Distance) that starts by 0 from the root and for child not will will be (PARENT HD - 1 -> for left), (PARENT HD + 1 -> for right).|
 |                                                                                                                                                          |
 |    🔹 Boundary View:                                                                                                                                     |
 |                     On Boundary view we'll include all the boundary elements:                                                                            |
 |                       🔸 All the left edges nodes                                                                                                        |
 |                       🔸 All the leave edges nodes                                                                                                       |
 |                       🔸 All the right edge nodes (reversed order)                                                                                       |
 |                                                                                                                                                          |
 |      👉 For the above example boundary nodes include [1, 2] (left nodes) + [5, 8, 9] (leave nodes) + [4, 3] (right noes in reversed order)               |
 |                                                                                                                                                          |
 +----------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# namespace

# namespace TreeBoundary

# 🟡 It won't override the data, If we have the same HD (key) below, it will ignore it.

# 🟡 It won't override the data, If we have the same HD (key) below, it will ignore it.

# 🟡 If you override the data with the same hd (key), so the larger HD will be there on the map.

# 🟡 If you override the data with the same hd (key), so the larger HD will be there on the map.

from collections import deque

def left_view(root):
    if root is None: return []
    result, queue = [], deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0: result.append(node.value)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return result

def right_view(root):
    if root is None: return []
    result, queue = [], deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0: last = node.value
            if node.right: queue.append(node.right)
            if node.left: queue.append(node.left)
        result.append(last)
    return result
