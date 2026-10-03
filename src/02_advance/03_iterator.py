class LinkedList:
    def __init__(self, val=0, next: LinkedList | None = None) -> None:
        self.val = val
        self.next = next

    def __iter__(self):
        # node = self
        # while node is not None:
        #     yield node.val
        #     node = node.next
        return LinkedListIterator(self)


class LinkedListIterator:
    def __init__(self, node: LinkedList | None = None) -> None:
        self.node = node

    # 🟡 It's a function that returns current object, To call "__next__" once by one to get items one by one.
    def __iter__(self):
        return self

    # 🟡 __next__ is a function that calls again and again for getting items on by one and "StopIteration" to stop
    def __next__(self):
        if self.node == None:
            raise StopIteration
        value = self.node.val
        self.node = self.node.next
        return value


l_list = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
print(
    f"Sum of all numbers in linkedlist is {sum(l_list)}"
)  # working because sum function needs a data-structure that have "iterator" under the hood.

for v in l_list:
    print(v)
