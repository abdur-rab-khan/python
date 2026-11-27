class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert_into_bst(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insert_into_bst(root.left, val)
        else:
            root.right = self.insert_into_bst(root.right, val)

        return root


if __name__ == "__main__":
    sol = Solution()
    print(
        f"Final Output is: {sol.insert_into_bst(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5)}"
    )
    print(
        f"Final Output is: {sol.insert_into_bst(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5)}"
    )
    print(
        f"Final Output is: {sol.insert_into_bst(TreeNode(40, TreeNode(20, TreeNode(10), TreeNode(30)), TreeNode(60, TreeNode(50), TreeNode(70))), 25)}"
    )
