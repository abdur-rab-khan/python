class ListNode:
    def __init__(self, val=0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        print_output = ""
        node = self
        print_output += "["
        while node != None:
            print_output += str(node.val)
            node = node.next
            if node:
                print_output += ", "

        print_output += "]"
        return print_output


class Solution:
    def rotate_right(self, head: ListNode | None, k: int) -> ListNode | None:
        if head == None or head.next == None or k <= 0:
            return head

        # Finding the size of the linkedlist
        tail = head
        list_size = 1
        while tail.next != None:
            tail = tail.next
            list_size += 1

        # Rounded off if k become greater than the list_size
        rounded_k = k % list_size
        if rounded_k <= 0:
            return head

        new_tail = head
        for _ in range((list_size - rounded_k) - 1):
            new_tail = new_tail.next

        if not new_tail or new_tail.next == None:
            return None

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head


if __name__ == "__main__":
    sol = Solution()

    linked_list_1 = ListNode(0, ListNode(1, ListNode(2)))
    linked_list_2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print(f"Final Output is: {sol.rotate_right(linked_list_1, 4)}")
    print(f"Final Output is: {sol.rotate_right(linked_list_2, 2)}")
