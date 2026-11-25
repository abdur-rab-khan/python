class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode | None = None) -> TreeNode | None:
        if root == None:
            return root

        # Permanently swap at the current node
        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.invert_tree(None)}")
    print(f"Final Output is: {sol.invert_tree()}")
    print(f"Final Output is: {sol.invert_tree(None)}")
