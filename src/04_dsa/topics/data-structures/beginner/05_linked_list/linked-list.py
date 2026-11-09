"""
 * 🟡 A linked list is a data structure that are form using chain of nodes, these nodes are nothing but an "object" which hold some kind of information. Unlike array data structure that where data is stored into contiguous memory location.
   🟡 In linked list each node have the ""reference of a memory block"" represents the next node. Means these nodes are scattered in memory but connected with there ""reference pointer"".

   🔶 Information stored by node:
        1. "Actual Data"
        2. "Reference Pointer to next node"
        3. "Reference Pointer to previous node (Doubly Linked List)"

   🔷 Types of Linked List:
        1. "Singly Linked List"
        2. "Doubly Linked List"
        3. "Circular Linked List"

   🔶 Key Terminologies
        1. "Node"
        2. "Head"
        3. "Tail"
        4. "Pointer / Next"
        5. "Prev"
        6. "Traversal"
        7. "nullptr / NULL"
"""

"""
     * 🟡 Singly Linked List: In Singly Linked List, Nodes are only pointed to it's next element in the chain and every node has "actual value", "reference pointer to next node".
    """

# Node of singly linked, that will create a memory block where we have ""data"" and ""next node pointer""

# 🟡 Manually, removing once linked list goes out of scope, since we are using smart pointer we don't need this.

# ~SinglyLinkedList() {

#     Node* currentNode = head_;

#     while (currentNode != nullptr) {

#         Node* nextNode = currentNode->next;

#         delete currentNode;

#         currentNode = nextNode;

#     }

# }

# ❌ Did Wrong: Using "current->head != nullptr", that ignores the head

"""
     * 🟡 Doubly Linked List: In Doubly Linked List, Nodes are pointer into both direction and every node in Doubly Linked List has three values, "actual value", "reference pointer to next node", "reference pointer to previous node".
     """

"""
     * 🟡 Circular Linked List: Circular Linked List are similar to Singly Linked List but only difference it the "tail node", always point to "head" node instead of "nullptr".
     """

# 🟡 Singly LinkedList

# 🟡 Doubly LinkedList

# // 🟡 Circular LinkedList

# namespace LinkedListTypes

class Node:
    def __init__(self, value):
        self.value, self.next = value, None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    def traverse(self):
        values, current = [], self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
