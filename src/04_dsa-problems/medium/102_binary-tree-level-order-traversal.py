from collections import deque


class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        node_by_level: list[list[int]] = []

        queue: deque[TreeNode] = deque()
        queue.append(root)

        while queue:
            level_node = []
            q_size = len(queue)

            for _ in range(q_size):
                node = queue.popleft()
                level_node.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            node_by_level.append(level_node)

        return node_by_level


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.level_order(None)}")
    print(f"Final Output is: {sol.level_order(TreeNode(1))}")
    print(
        f"Final Output is: {sol.level_order(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))}"
    )
