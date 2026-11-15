# constructing the list node
class ListNode:
    def __init__(self, val=0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        result = "["

        list = self
        while list:
            result += str(list.val)
            list = list.next
            if list is not None:
                result += ", "

        return result + "]"


class Solution:
    def merge_two_lists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        # return remaining part one one of the list become empty
        if list1 is None or list2 is None:
            return list2 if list1 is None else list1

        if list1.val < list2.val:
            list1.next = self.merge_two_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_lists(list1, list2.next)
            return list2


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.merge_two_lists(None, None)}")
    print(f"Final Output is: {sol.merge_two_lists(None, ListNode(0))}")
    print(
        f"Final Output is: {sol.merge_two_lists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))}"
    )
