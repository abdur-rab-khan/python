class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        def check_bst(node: TreeNode | None, min=float("-inf"), max=float("inf")):
            if node is None:
                return True

            if node.val <= min or node.val >= max:
                return False

            return check_bst(node.left, min, node.val) and check_bst(
                node.right, node.val, max
            )

        return check_bst(root)


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.is_valid_bst(TreeNode(2, TreeNode(1), TreeNode(3)))}")
    print(
        f"Final Output is: {sol.is_valid_bst(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))}"
    )
