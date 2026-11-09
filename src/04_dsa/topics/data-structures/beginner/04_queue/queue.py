"""
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                1️⃣ Simple Queue                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                               |
| 🟡 Queue is a data structure that follows "FIFO" model, Data enters from one side (back) and removed from other side (front). Simple Queue uses static array to implement it. |
|                                                                                                                                                                               |
| 🔶 Time complexity:                                                                                                                                                           |
|                                                                                                                                                                               |
|                    🔹 Insertion of an element: o(1)                                                                                                                           |
|                    🔹 Removing of an element: o(n or 1)                                                                                                                       |
|                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Is empty

# Is full

# Add an element at the rear of the query

# Remove an element at the front of the query

# Return front element from the queue

# Return last element from the queue

# Simple Queue

# Adding elements into queue.

# Getting front and rear

# namespace SimpleQueue

"""
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                               2️⃣ Circular Queue                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                               |
| 🟡 Circular Queue is the extended version of "Simple Queue", It is build to reduce the "removing" cost  from "o(n)" to "o(1)". By build Queue as a circular manner.           |
|    So instead of shifting the element we use other method for doing that.                                                                                                     |
|                                                                                                                                                                               |
| 🟡 Instead of shifting or doing anything, We use "%" operator So if [_, _, 1, 2] we got blank space at the start instead of shifting it when new element can will use formula |
|    ["front + size" % capacity], ("2 + 2" % 4) = 0, So the new element will be inserted at 0th index.                                                                          |
|                                                                                                                                                                               |
| 🔶 Time complexity:                                                                                                                                                           |
|                                                                                                                                                                               |
|                    🔹 Insertion of an element: o(1)                                                                                                                           |
|                    🔹 Removing of an element: o(1)                                                                                                                            |
|                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Destructor

# Queue is full

# Queue is empty

# Add element into the queue;

# Remove element from the queue;

# Getting first element from the queue;

# Getting last element from the queue;

# Adding an elements into the queue

# Getting front and back

# Removing elements from the queue

# Adding an element

# namespace CircularQueue

"""
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                  3️⃣ Deque Queue                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# MAIN FUNCTION

# [10]

# [10, 20]

# [5, 10, 20]

# [1, 5, 10, 20]

# Deque: 1 5 10 20

# Removed from front: 1

# Removed from rear: 20

# Deque: 5 10

# Front: 5

# Rear: 10

# namespace Deque

"""
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                4️⃣ Priority Queue                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                               |
| 🟡 Priority Queue is a type of queue where insert/remove element based on priority unlike other queue where follow "FIFO" model.                                              |
|                                                                                                                                                                               |
| 🔶 Type of Priority Queue                                                                                                                                                     |
|                                                                                                                                                                               |
|    1. Max Priority Queue: "High Value High Priority" -> [10, 5, 20] -> [20, 10, 5]                                                                                            |
|    2. Min Priority Queue: "Low Value High Priority" -> [20, 5, 10] -> [5, 10, 20]                                                                                             |
|                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    def enqueue(self, value):
        self._items.append(value)
    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()
    def front(self):
        if not self._items:
            raise IndexError("front of empty queue")
        return self._items[0]
    def is_empty(self):
        return not self._items
    def size(self):
        return len(self._items)
