class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: TreeNode | None) -> bool:
        if root == None:
            return True

        left_height = self.__get_height(root.left)
        right_height = self.__get_height(root.right)

        if abs(right_height - left_height) > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)

    def __get_height(self, root: TreeNode | None) -> int:
        if root == None:
            return 0
        return 1 + max(self.__get_height(root.left), self.__get_height(root.right))


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.is_balanced(None)}")
    print(
        f"Final Output is: {sol.is_balanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17))))}"
    )
    print(
        f"Final Output is: {sol.is_balanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)))}"
    )
