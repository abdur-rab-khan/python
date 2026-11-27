class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return (
            p.val == q.val
            and self.is_same_tree(p.left, q.left)
            and self.is_same_tree(p.right, q.right)
        )


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.is_same_tree(None, None)}")
    print(
        f"Final Output is: {sol.is_same_tree(TreeNode(1, None, TreeNode(2)), TreeNode(1, TreeNode(2), None))}"
    )
    print(
        f"Final Output is: {sol.is_same_tree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))}"
    )
    print(
        f"Final Output is: {sol.is_same_tree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2)))}"
    )
