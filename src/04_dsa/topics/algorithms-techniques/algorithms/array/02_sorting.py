"""
+---------------------------------------------------------------------------------------------------------------------------------------+
|                                                             🫧 Bubble Sort                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                       |
| 🟡 Step-by-Step Process:                                                                                                              |
|     1. Start from the first element (index 0)                                                                                         |
|     2. Compare the current element with the next element                                                                              |
|     3. If current element > next element, swap them                                                                                   |
|     4. Move to the next element and repeat steps 2-3                                                                                  |
|     5. After one complete pass, the largest element moves to the end                                                                  |
|     6. Repeat the process for the remaining unsorted elements (reduce range by 1 each pass)                                           |
|     7. Continue until no swaps occur or all elements are sorted                                                                       |
|                                                                                                                                       |
| 🔷 Time Complexity: O(n²) | Space Complexity: O(1)                                                                                    |
|                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------+
"""

# Everything is already sorted.

# namespace bubbleSort

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                    🫳 Selection Sort                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 🟡 Step-by-Step Process:                                                                                                                                                                                            |
|     1. Start with the first element (index 0)                                                                                                                                                                       |
|     2. Find the smallest element in the remaining unsorted array                                                                                                                                                    |
|     3. Swap the smallest element with the current element at index i                                                                                                                                                |
|     4. Move to the next index (i + 1)                                                                                                                                                                               |
|     5. Repeat steps 2-4 until the entire array is sorted                                                                                                                                                            |
|     6. Each iteration places one element in its correct sorted position                                                                                                                                             |
|                                                                                                                                                                                                                     |
| 🔷 Time Complexity: O(n²) | Space Complexity: O(1)                                                                                                                                                                  |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# namespace selectionSort

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                    ➕ Insertion Sort                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 🟡 Step-by-Step Process:                                                                                                                                                                                            |
|     1. Start from the second element (index 1)                                                                                                                                                                      |
|     2. Store the current element in a temporary variable                                                                                                                                                            |
|     3. Compare the current element with elements before it (from right to left)                                                                                                                                     |
|     4. If the previous element is greater, shift it one position to the right                                                                                                                                       |
|     5. Continue shifting until the correct position is found                                                                                                                                                        |
|     6. Insert the current element into its correct position                                                                                                                                                         |
|     7. Move to the next element and repeat steps 2-6                                                                                                                                                                |
|     8. Continue until all elements are sorted                                                                                                                                                                       |
|                                                                                                                                                                                                                     |
| 🔷 Time Complexity: O(n²) | Space Complexity: O(1)                                                                                                                                                                  |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# namespace insertionSort

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                    ✌️ Merge Sort                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 🟡 Step-by-Step Process (Divide and Conquer):                                                                                                                                                                       |
|     Divide Phase:                                                                                                                                                                                                   |
|     1. Divide the array into two equal halves (middle = size/2)                                                                                                                                                     |
|     2. Recursively divide the left half until single elements remain                                                                                                                                                |
|     3. Recursively divide the right half until single elements remain                                                                                                                                               |
|                                                                                                                                                                                                                     |
|     Merge Phase:                                                                                                                                                                                                    |
|     4. Compare the first elements of both sorted subarrays                                                                                                                                                          |
|     5. Place the smaller element in the result array                                                                                                                                                                |
|     6. Move the pointer of the subarray from which element was taken                                                                                                                                                |
|     7. Repeat steps 4-6 until one subarray is exhausted                                                                                                                                                             |
|     8. Copy remaining elements from the non-empty subarray                                                                                                                                                          |
|     9. The merged result is now a sorted array                                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| 🔷 Time Complexity: O(n log n) | Space Complexity: O(n)                                                                                                                                                             |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Step 1. Creating temp vectors.

# Step 2. Copying elements to temp vector.

# Step 3. Merging the elements in a sorted manner

# Step 4. Merging remaining numbers

# Step 1. Base condition

# Step 2. Dividing into two equal parts

# Step 3. Dividing start to mid again.

# Step 4. Dividing mid + 1 to end again.

# Step 5. Merging and sorting both divided array part.

# namespace mergeSort

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                    🏃 Quick Sort                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 🟡 Step-by-Step Process (Divide and Conquer):                                                                                                                                                                       |
|     1. Choose a "pivot" (could be "left", "right") element from the array                                                                                                                                           |
|     2. Partition the array so that:                                                                                                                                                                                 |
|        - All elements smaller than pivot are on the left                                                                                                                                                            |
|        - All elements greater than pivot are on the right                                                                                                                                                           |
|        - Pivot is now in its final sorted position                                                                                                                                                                  |
|     3. Recursively apply steps 1-2 to the left subarray                                                                                                                                                             |
|     4. Recursively apply steps 1-2 to the right subarray                                                                                                                                                            |
|     5. Continue until all subarrays are sorted (base case: array size ≤ 1)                                                                                                                                          |
|                                                                                                                                                                                                                     |
| 🔷 Time Complexity: O(n log n) average, O(n²) worst case | Space Complexity: O(log n)                                                                                                                               |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Step 1. Declaring pivot point as a "left" value.

# Step 2. Arranging smaller than "pivot" element towards pivots "left" and grater towards pivots "right".

# Step 3. Placing pivot element to the correct position.

# Step 1. Base condition (when only single element is there)

# Step 2. Calculating pivot point

# Step 3. Calling recursively quick sort for "left" and "right" side of pivot point

# namespace quickSort

# bubbleSort::main();

# selectionSort::main();

# insertionSort::main();

# mergeSort::main();

def bubble_sort(values):
    arr = values[:]
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(values):
    arr = values[:]
    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr

def insertion_sort(values):
    arr = values[:]
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
