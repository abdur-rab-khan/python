"""
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                       HEAP DATA STRUCTURE                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
| 🟡 A heap is a tree-shaped structure, stored as a plain array, that always keeps the smallest (min-heap) or biggest (max-heap) element on top for              |
|    instant access.                                                                                                                                             |
|                                                                                                                                                                |
| 🟡 There are two rule while storing in the heap:                                                                                                               |
|       1:                                                                                                                                                       |
|           🔸 min-heap: Here, Every Parent must be smaller than it's children                                                                                   |
|           🔸 max-heap: Here, Every Parent must be greater than it's children                                                                                   |
|       2:                                                                                                                                                       |
|           🔸 Tree must be filled level by level from ""left to right"", new level only start once previous level is full                                       |
|                                                                                                                                                                |
| 🟡 Using this, it will be guarantee that first element must be either smaller/greater, because of the insertion/deleting/retrieval is so easy and quick.       |
|                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                               OPERATIONS OF HEAP DATA STRUCTURE                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
| 🔶 Insert on Heap o(log n):                                                                                                                                    |
|                   Insert a new value into the heap.                                                                                                            |
|                        1: Push new value at the end                                                                                                            |
|                        2: Compare it's parent                                                                                                                  |
|                        3: Heap rule break swap with it's parent                                                                                                |
|                        4: Repeat until, reach to the root or become valid                                                                                      |
|                                                                                                                                                                |
|                        This is "bubble up" — the new element floats toward the top if it's too small.                                                          ||                                                                                                                                                                |
|                                                                                                                                                                |
| 🔶 Remove on Heap o(log n):                                                                                                                                    |
|                    Remove the top element (smallest) from the heap.                                                                                            |
|                           1: move the last element to the top, shrink the array                                                                                |
|                           2: compare the new top with its smaller child                                                                                        |
|                           3: if heap rule is broken (parent > smaller child), swap and move down                                                               |
|                           4: repeat until rule holds, or we run out of children                                                                                |
|                                                                                                                                                                |
|                       This is "bubble down" — the replacement element sinks toward the leaves if too big.                                                      |
|                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                FORMULAS OF HEAP DATA STRUCTURE                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
| 🔶 Get Parent of a child: (n - 1) / 2;                                                                                                                         |
| 🔶 Get Left Child: (n * 2) + 1;                                                                                                                                |
| 🔶 Get Right Child: (n * 2) + 2;                                                                                                                               |
| 🔶 Get Leaves: (n / 2) - 1;                                                                                                                                    |
|                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# hp.push(1);

# hp.push(2);

# hp.push(3);

# hp.push(11);

# hp.push(8);

# hp.push(2);

import heapq

class MinHeap:
    def __init__(self, values=()):
        self._heap = list(values)
        heapq.heapify(self._heap)
    def push(self, value):
        heapq.heappush(self._heap, value)
    def pop(self):
        return heapq.heappop(self._heap)
    def peek(self):
        return self._heap[0] if self._heap else None
    def __len__(self):
        return len(self._heap)
