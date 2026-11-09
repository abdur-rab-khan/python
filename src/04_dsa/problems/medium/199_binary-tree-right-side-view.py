from collections import deque


class TreeNode:
    def __init__(
        self, val: int, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def right_side_view(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        right_side_val = []
        queue: deque[TreeNode] = deque()
        queue.append(root)

        while queue:
            q_size = len(queue)
            for i in range(q_size):
                node = queue.popleft()

                if i == q_size - 1:
                    right_side_val.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return right_side_val


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.right_side_view(TreeNode(1, None, TreeNode(3)))}")
    print(
        f"Final Output is: {sol.right_side_view(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))))}"
    )
    print(
        f"Final Output is: {sol.right_side_view(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5)), None), TreeNode(3)))}"
    )
