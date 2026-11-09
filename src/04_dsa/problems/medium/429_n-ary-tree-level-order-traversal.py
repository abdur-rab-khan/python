from collections import deque


class Node:
    def __init__(self, val=0, children: list[Node] = []) -> None:
        self.val = val
        self.children = children


class Solution:
    def level_order(self, root: Node | None) -> list[list[int]]:
        if root is None:
            return []

        level_order_nodes = []
        queue: deque[Node] = deque()
        queue.append(root)

        while len(queue) > 0:
            q_size = len(queue)
            current_nodes = []

            for _ in range(q_size):
                node = queue.popleft()
                current_nodes.append(node.val)
                queue.extend(node.children)

            level_order_nodes.append(current_nodes)

        return level_order_nodes


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.level_order(None)}")
    print(
        f"Final Output is: {sol.level_order(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)]))}"
    )
    print(
        f"Final Output is: {sol.level_order(Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])]))}"
    )
