class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


# DFS version for solving max_depth problem
class Solution:
    def max_depth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        return 1 + max(left_depth, right_depth)


# BFS version for solving max_depth problem


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.max_depth(None)}")
    print(f"Final Output is: {sol.max_depth(TreeNode(1, None, TreeNode(2)))}")
    print(
        f"Final Output is: {sol.max_depth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))}"
    )
