# building binary tree
class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowest_common_ancestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        # directly return none is root or p or q is none
        if root is None or p is root or q is root:
            return root

        left_node = self.lowest_common_ancestor(root.left, p, q)
        right_node = self.lowest_common_ancestor(root.right, p, q)

        # if we found both left_node and right_node means the closest node is current node otherwise left or right
        if left_node and right_node:
            return root
        else:
            return left_node if left_node else right_node


if __name__ == "__main__":
    sol = Solution()

    tree = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, TreeNode(0), TreeNode(8)),
    )

    print(
        f"Final Output is: {sol.lowest_common_ancestor(tree, tree.left, tree.right).val}"
    )
    print(
        f"Final Output is: {sol.lowest_common_ancestor(tree, tree.left, tree.left.left).val}"
    )
