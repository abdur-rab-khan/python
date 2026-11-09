"""
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                      🌲 TREE TRAVERSING                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                              |
| 🟡 DFS (Depth First Search): A DFS is a traversing technique where pick a node and deep as you can until reaches dead end, then check other node.            |
|                                                                                                                                                              |
|    🔶 Types of DFS (One Specify Rule for printing):                                                                                                          |
|                    1. InOrder: Left -> Node (Print) -> Right                                                                                                 |
|                    1. PreOrder: Node (Print) -> Left -> Right                                                                                                |
|                    1. PostOrder: Left -> Right -> Node (Print)                                                                                               |
|                                                                                                                                                              |
|                                                                                                                                                              |
| 🟡 BFS (Breadth First Search): Unlike DFS (go deeper first), In BFS we just go "level-by-level" like reading a book line by line like "left to right"        |
|                                then "top to bottom". To implement this we use "queue " Data Structure.                                                       |
|                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""
                     1
                    / \
                   2   3
                  / \   \
                 4   6  20
                /
               5
         """

"""
                 1
                / \
               2   3
        """

# namespace dfs

# namespace bfs

from collections import deque

def dfs(root):
    if root is None:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return result

def bfs(root):
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return result
