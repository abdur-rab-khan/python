from collections import deque


class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zig_zag_level_order(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        level_order_nodes = []
        queue: deque[TreeNode] = deque()
        queue.append(root)

        while len(queue) > 0:
            q_size = len(queue)
            current_nodes = [0] * q_size

            for i in range(q_size):
                node = queue.popleft()

                node_idx = i if len(level_order_nodes) % 2 == 0 else q_size - i - 1
                current_nodes[node_idx] = node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            level_order_nodes.append(current_nodes)

        return level_order_nodes


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.zig_zag_level_order(None)}")
    print(
        f"Final Output is: {sol.zig_zag_level_order(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))}"
    )
    print(f"Final Output is: {sol.zig_zag_level_order(TreeNode(1))}")
