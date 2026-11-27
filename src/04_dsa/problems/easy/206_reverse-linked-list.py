class ListNode:
    def __init__(self, val=0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head

        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.reverse_list(None)}")
    print(f"Final Output is: {sol.reverse_list(ListNode(1, ListNode(2)))}")
    print(
        f"Final Output is: {sol.reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))}"
    )
