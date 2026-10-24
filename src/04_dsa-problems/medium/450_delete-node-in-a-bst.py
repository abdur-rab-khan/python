from collections import deque


class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        result = []

        queue: deque[TreeNode] = deque()
        queue.append(self)

        while len(queue) > 0:
            current_nodes = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                current_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(current_nodes)

        return str(result)


class Solution:
    def delete_node(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return root

        if key == root.val:
            # node don't have any children
            if root.left is None and root.right is None:
                return None
            elif root.left and root.right:
                min_node = self.get_min_node(root.right)
                root.val = min_node.val
                root.right = self.delete_node(root.right, min_node.val)
            else:
                return root.left if root.right is None else root.right

        if key > root.val:
            root.left = self.delete_node(root.left, key)
        else:
            root.right = self.delete_node(root.right, key)

        return root

    def get_min_node(self, root: TreeNode) -> TreeNode:
        if root.left is None:
            return root

        return self.get_min_node(root.left)


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.delete_node(None, 0)}")
    print(
        f"Final Output is: {sol.delete_node(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 3)}"
    )
