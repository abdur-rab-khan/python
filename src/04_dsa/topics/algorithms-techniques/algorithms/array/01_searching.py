"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                              🔍 TECHNIQUES USE IN SEARCH                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 1️⃣. "Binary Search":                                                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| 2️⃣. "Two Pointers":                                                                                                                                                                                                 |
|                                                                                                                                                                                                                     |
| 3️⃣. "Sliding Window":                                                                                                                                                                                               |
|                                                                                                                                                                                                                     |
| 4️⃣. "Hash Map/Set":                                                                                                                                                                                                 |
|                                                                                                                                                                                                                     |
| 5️⃣. Linear/Prefix Sum:                                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                  🔍 SEARCHING PATTERN                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 🟡 Pattern 1. "Classic Binary Search":                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| 🟡 Pattern 2. "Binary Search on Answer":                                                                                                                                                                            |
|                                                                                                                                                                                                                     |
| 🟡 Pattern 3. "Find First/Last Occurrence":                                                                                                                                                                         |
|                                                                                                                                                                                                                     |
| 🟡 Pattern 4. "Rotated Sorted Array": Normally, Sort array are arranged in an ascending order but in "Rotated Sorted Array" numbers are divided into two part and both two parts are sorted in there own way.       |
|                                      Suppose sorted array looks like this [1, 2, 3, 4, 5, 6, 7], then "rotated array" will looks like this [[4, 5, 6, 7], [1, 2, 3]], We got two parts.                             |
|                                      To solve these problems, We have to find drop point in this case which is "7 and 1" We find using "middle > last" -> "drop is in right direction", "middle" < "last" -> left   |
|                                                                                                                                                                                                                     |
| 🟡 Pattern 5. "Hash Map Search":                                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| 🟡 Pattern 6. "Prefix Sum Search":                                                                                                                                                                                  |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                    🔍 Linear Search                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""*
    * Finds the index of a target value in an unsorted array.
    *
    * Given an array and a target value, return the first index where the
    * target appears. If the value is not present, return -1.
     *
     * Example:
     * Input: numbers = [3, 7, 1, 9, 4, 6, 2, 8], targetValue = 6
     * Output: 5
     *
    * Time Complexity: O(n)
    * Space Complexity: O(1)
     *
     * @param numbers The vector of integers to search through.
     * @param targetValue The integer value to find.
     * @return The 0-based index of the target value, or -1 if not found.
     """

# namespace linearSearch

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                    🔍 Binary Search                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 🔷 Binary Search required array value should be in sorted manner.                                                                                                                                                   |
|                                                                                                                                                                                                                     |
| 🟡 Step by Step Process of Binary Search.                                                                                                                                                                           |
|                                                                                                                                                                                                                     |
|    1. Find "mid" value of the array.                                                                                                                                                                                |
|    2. If "mid" is equal to "targetValue", Simply we return the index of it.                                                                                                                                         |
|    3. If "mid" become greater than "targetValue", mean "targetValue" is smaller so we again Slice into "mid" again step starts from "1".                                                                            |
|    4. If "mid" become smaller than "targetValue", mean "targetValue" is greater so we should have to start step "1" again from "mid + 1" to "right".                                                                |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""*
    * Searches for a target value in a sorted array using binary search.
    *
    * Given a sorted array of integers and a target value, return the index of
    * the target if it exists; otherwise return -1.
     *
     * Example:
    * Input: numbers = [1, 2, 3, 4, 6, 7, 8, 9], targetValue = 4
    * Output: 3
     *
    * Time Complexity: O(log n)
    * Space Complexity: O(1)
     *
    * @param numbers Sorted array of integers
    * @param targetValue Value to search for
    * @return Index of the target value, or -1 if not found
     """

# Updating both pointers based on smaller/greater than "targetValue"

# If "targetValue" not found in this list.

"""*
     * Searches for a target value in a sorted array using recursion.
     *
     * Given a sorted array of integers and a target value, return the index of
     * the target if it exists; otherwise return -1.
     *
     * Example:
     * Input: numbers = [1, 2, 3, 4, 6, 7, 8, 9], targetValue = 4
     * Output: 3
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(log n)
     *
     * @param numbers Sorted array of integers
     * @param targetValue Value to search for
     * @param leftIndex Left boundary of the current search interval
     * @param rightIndex Right boundary of the current search interval
     * @return Index of the target value, or -1 if not found
     """

# If "midValue" its equal to targetValue.

# If "midValue" is greater than targetValue.

# If "midValue" is smaller than targetValue.

"""*
     * Runs the binary search examples.
     *
     * Example:
     * Input: numbers = [1, 2, 3, 4, 6, 7, 8, 9], targetValue = 4
     * Output: 3
     """

# namespace binarySearch

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                    😎 Easy Problems                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""*
     * Searches for a target value in a sorted array.
     *
     * Given a sorted array, return the index of the target value if it exists,
     * otherwise return -1.
     *
     * Example:
     * Input: numbers = [2, 5, 8, 12], targetValue = 8
     * Output: 2
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     *
     * @param numbers Sorted array of integers
     * @param targetValue Value to search for
     * @return Index of the target value, or -1 if not found
     """

"""*
     * Finds the insert position for a target in a sorted array.
     *
     * Given a sorted array and a target value, return the index where the target
     * should be inserted to keep the array sorted.
     *
     * Example:
     * Input: numbers = [1, 3, 5, 7], targetValue = 7
     * Output: 3
     * Explanation: The target already exists at index 3.
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     *
     * @param numbers Sorted array of integers
     * @param targetValue Target to search for
     * @return Insert position for the target value
     """

"""*
     * Finds adjacent indices whose values sum to a target.
     *
     * Given an array and a target value, return the pair of neighboring indices
     * whose values add up to the target.
     *
     * Example:
     * Input: numbers = [2, 7, 11, 15], targetValue = 9
     * Output: {0, 1}
     * Explanation: numbers[0] + numbers[1] = 2 + 7 = 9.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     *
     * @param numbers Input array of integers
     * @param targetValue Target sum of two adjacent values
     * @return Pair of indices, or {-1, -1} if no match exists
     """

# Preparing calculation between "i" and "i - 1".

"""*
     * Determines whether an array contains duplicate values.
     *
     * Example:
     * Input: numbers = [1, 2, 3, 1]
     * Output: true
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     *
     * @param numbers Input array of integers
     * @return True if at least one value appears more than once, otherwise false
     """

"""*
     * Finds the maximum average of a contiguous subarray of fixed size.
     *
     * Given an array and a window size, return the maximum average over all
     * contiguous subarrays of that size.
     *
     * Example:
     * Input: numbers = [1, 12, -5, -6, 50, 3], maxSize = 4
     * Output: 12.75
     * Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 12.75.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * @param numbers Input array of integers
     * @param maxSize Fixed window size
     * @return Maximum average across all windows of size maxSize
     """

"""*
     * Finds the first bad version in an ordered list of versions.
     *
     * A "bad" version is any version that is known to fail or violate the required
     * correctness criteria. In this problem, once a version becomes bad, all later
     * versions are also considered bad.
     *
     * The goal is to return the earliest version number that is bad, i.e. the
     * smallest version where the bad condition starts.
     *
     * Example:
     * Input: versions = [1, 2, 3, 4, 5], firstBad = 4
     * Output: 4
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     *
     * @param versions Array of version numbers
     * @param firstBad First bad version number
     * @return The first bad version number
     """

"""*
     * Guesses a secret number in a known range.
     *
     * Given a range from 1 to size, return the secret number if it exists in the
     * range.
     *
     * Example:
     * Input: size = 10, secretNum = 7
     * Output: 7
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     *
     * @param size Upper bound of the search range
     * @param secretNum Secret number to find
     * @return The secret number if found, otherwise -1
     """

# BINARY SEARCH

# SEARCHING INSERT POSITION

# FIND TWO SUM (UNORDERED)

# IS CONTAINING DUPLICATES

# FIND MAXIMUM AVERAGE SUBARRAY

# namespace easyProblems

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                  🤔 Medium Problems                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""*
     * Finds the minimum value in a rotated sorted array.
     *
     * Given a sorted array that has been rotated, return the smallest value in
     * the array.
     *
     * Example:
     * Input: numbers = [3, 4, 5, 6, 7, 1, 2]
     * Output: 1
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     *
     * @param numbers Rotated sorted array
     * @return Minimum value in the array
     """

# Means "second" half is at left direction.

"""*
     * Searches for a target value in a rotated sorted array.
     *
     * Given a rotated sorted array and a target value, return the index of the
     * target if it exists; otherwise return -1.
     *
     * Example:
     * Input: numbers = [4, 5, 6, 7, 0, 1, 2], target = 0
     * Output: 4
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     *
     * @param numbers Rotated sorted array
     * @param target Target value
     * @return Index of the target value, or -1 if not found
     """

# Check which half is sorted

# Left half is sorted

# target is in left half

# target is in right half

# Right half is sorted

# target is in right half

# target is in left half

"""*
     * Finds the minimum length of a contiguous subarray whose sum reaches a target.
     *
     * Given a positive integer array and a target, return the smallest length
     * of a contiguous subarray whose sum is greater than or equal to the target.
     *
     * Example:
     * Input: numbers = [1, 4, 4], target = 4
     * Output: 1
     * Explanation: The subarray [4] has the shortest valid length.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * @param numbers Input array of positive integers
     * @param target Target sum
     * @return Minimum valid subarray length, or INT_MAX if none exists
     """

"""*
     * Finds the minimum eating speed needed to finish all banana piles within h hours.
     *
     * Given banana piles and a number of hours, return the minimum integer speed
     * required to finish all bananas.
     *
     * Example:
     * Input: piles = [3, 6, 7, 11], h = 8
     * Output: 4
     *
     * Time Complexity: O(n * log(max(piles)))
     * Space Complexity: O(1)
     *
     * @param piles Array of banana piles
     * @param h Maximum hours allowed
     * @return Minimum eating speed
     """

"""*
     * Finds the maximum length of a contiguous subarray whose sum is at most k.
     *
     * Given an integer array and an upper bound k, return the longest contiguous
     * subarray whose total sum does not exceed k.
     *
     * Example:
     * Input: numbers = [1, 2, 1, 0, 1], k = 4
     * Output: 4
     * Explanation: Window [1, 2, 1, 0] gives sum 4 with max length 4.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * @param numbers Input array of integers
     * @param k Maximum allowed sum
     * @return Maximum valid window length
     """

"""*
     * Finds all unique triplets in an array that sum to zero.
     *
     * Given an integer array, return all unique triplets [a, b, c] such that
     * a + b + c = 0.
     *
     * Example:
     * Input: numbers = [-1, 0, 1, 2, -1, -4]
     * Output: [[-1, -1, 2], [-1, 0, 1]]
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1) excluding output
     *
     * @param numbers Input array of integers
     * @return All unique triplets that sum to zero
     """

# FINDING MINIMUM IN ROTATED SORTED ARRAY.

# SEARCHING IN AN ROTATED SORTED ARRAY

# MIN SIZE SUBARRAY

# MINIMUM BANANA SPEED

# piles of bananas

# minimHours

# FIND LONGEST LENGTH OF SUM OF SUBARRAY EQUAL TO K

# THREE SUM EQUAL TO ZERO

# namespace mediumProblems

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                   😶 Hard Problems                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# PROBLEMS

# namespace hardProblems

# Problems

def linear_search(values, target):
    for i, value in enumerate(values):
        if value == target:
            return i
    return -1

def binary_search(values, target):
    left, right = 0, len(values) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
