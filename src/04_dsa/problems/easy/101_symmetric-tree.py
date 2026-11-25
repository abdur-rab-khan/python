from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode | None = None) -> bool:
        if root == None:
            return False
        return self.__bfs(root.left, root.right)

    def __bfs(self, left_node: TreeNode | None, right_node: TreeNode | None) -> bool:
        if not left_node and not right_node:
            return True

        if not left_node or not right_node:
            return False

        return (
            left_node.val == right_node.val
            and self.__bfs(left_node.left, right_node.right)
            and self.__bfs(left_node.right, right_node.left)
        )


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.is_symmetric(None)}")
    print(
        f"Final Output is: {sol.is_symmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))))}"
    )
    print(
        f"Final Output is: {sol.is_symmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))))}"
    )
