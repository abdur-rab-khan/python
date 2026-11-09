"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                      TWO POINTERS                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 🟡 In "two pointers" technique we use two indices (pointer) to scan the array, based on condition we smartly increase/decrease pointer indices.                                                                     |
|                                                                                                                                                                                                                     |
| 🟡 Without using "two pointers" we could use "nested loop o(n²)", "two pointers" makes scaning efficient "o(n)".                                                                                                    |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                    TYPES TWO POINTERS                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                     |
| 🔶 Opposite direction (start & end):                                                                                                                                                                                |
|                                                                                                                                                                                                                     |
|    1. One Pointer at the begining, One Pointer at the end.                                                                                                                                                          |
|    2. Moving based on conditions.                                                                                                                                                                                   |
|                                                                                                                                                                                                                     |
|    Used In:                                                                                                                                                                                                         |
|           1. Sorted array problems                                                                                                                                                                                  |
|           2. Pair sum problems                                                                                                                                                                                      |
|           3. Palindrome checking                                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| 🔶 Same direction (slow & fast pointer):                                                                                                                                                                            |
|                                                                                                                                                                                                                     |
|    1. Both pointers starts from the same position.                                                                                                                                                                  |
|    2. Fast pointer (move quickly), slow pointer (move based on conditions).                                                                                                                                         |
|                                                                                                                                                                                                                     |
|    Used In:                                                                                                                                                                                                         |
|           1. Removing Duplicates                                                                                                                                                                                    |
|           2. Removing elements                                                                                                                                                                                      |
|           3. Cycle Detection                                                                                                                                                                                        |
|           4. Rearranging array in place                                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| 🔶 Sliding window (Variable size):                                                                                                                                                                                  |
|                                                                                                                                                                                                                     |
|    1. Window grows and shrinks maintaining condition inside the window.                                                                                                                                             |
|                                                                                                                                                                                                                     |
|    Used In:                                                                                                                                                                                                         |
|           1. Longest Substring                                                                                                                                                                                      |
|           2. Subarray sum problems                                                                                                                                                                                  |
|           3. At most K distinct element                                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| 🔶 Sliding window (Fixed size):                                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
|    1. Window size fixed maintaining fixed distance, both moves together.                                                                                                                                            |
|                                                                                                                                                                                                                     |
|    Used In:                                                                                                                                                                                                         |
|           1. Maximum size of K                                                                                                                                                                                      |
|           2. First negative in window.                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                             🔺 TWO POINTERS EASY PROBLEMS                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""*
    * Reverses an array.
    *
    * Given an array of integers, return the same array in reverse order.
 *
 * Example:
 * Input: vec = {1, 2, 3, 4}
* Output: {4, 3, 2, 1}
 *
 * Time Complexity: O(n) where n is the size of the vector
 * Space Complexity: O(1) in-place
 *
* @param vec Input array to be reversed
 """

# Swapping numbers

"""*
    * Removes duplicate values from a sorted array and prints unique values.
    *
    * Given a sorted array, keep one occurrence of each value and print the
    * resulting unique list.
 *
 * Example:
 * Input: vec = {1, 1, 2, 3, 3}
 * Output: 1 2 3
 *
* Time Complexity: O(n) where n is the array size
 * Space Complexity: O(n) due to constructing a new unique vector for output
 *
* @param vec Sorted input array that may contain duplicates
 """

# Printing all unique elements

"""*
        * Finds all pairs in a sorted array whose sum equals a target.
        *
        * Given a sorted array and an integer k, print every pair [a, b] such that
        * a + b = k.
     *
     * Example:
     * Input: numbers = {2, 7, 11, 15}, k = 9
     * Output: [ 2 7 ]
     *
     * Time Complexity: O(n) where n is the vector size
     * Space Complexity: O(p) where p is number of matching pairs stored
     *
     * @param numbers Sorted input vector
     * @param k Target sum value
     """

"""*
        * Checks whether a string is a palindrome.
        *
        * Given a string, determine if it reads the same from left to right and
        * right to left when ignoring non-alphanumeric characters and case.
     *
     * Example:
     * Input: str = "A man, a plan, a canal: Panama"
    * Output: true
     *
     * Time Complexity: O(n) where n is the string length
     * Space Complexity: O(1) auxiliary space
     *
     * @param str Input string to validate as palindrome
     """

# Lambda function: use "auto" or given type or directly use "isalnum"  ==> Learned LAMBDA

# FUNCTION

# Find whether "str" is palindrome or not by look both side.

"""*
        * Removes duplicates from a sorted array.
        *
        * Given a sorted array, return a new array containing only unique values
        * in sorted order.
     *
     * Example:
     * Input: numbers = {1, 1, 2, 3, 3}
     * Output: {1, 2, 3}
     *
     * Time Complexity: O(n) where n is the vector size
    * Space Complexity: O(u) for returned array of u unique elements
     *
     * @param numbers Sorted vector that may contain duplicates
     * @return A vector containing unique elements in sorted order
     """

"""*
        * Moves all zeros to the right while keeping non-zero order.
        *
        * Given an array, place all zero values at the end and keep the relative
        * order of non-zero values unchanged.
     *
     * Example:
     * Input: numbers = {0, 1, 0, 3, 12}
    * Output: rearranged array starts with {1, 3, 12} and zeros move to the end
     *
     * Time Complexity: O(n) where n is the vector size
     * Space Complexity: O(k) for returned prefix vector of k non-zero elements
     *
     * @param numbers Vector to rearrange in place
     * @return Vector containing non-zero values after compaction
     """

# Technique 1;

# Technique 2;

"""*
        * Merges two sorted arrays into one sorted array.
        *
        * Given two sorted arrays, return a single sorted array containing all
        * elements from both inputs.
     *
     * Example:
     * Input: numsOne = {1, 3, 5}, numsTwo = {2, 4}
     * Output: {1, 2, 3, 4, 5}
     *
     * Time Complexity: O(n + m) where n and m are input sizes
     * Space Complexity: O(1) auxiliary (excluding resized output storage)
     *
     * @param numsOne First sorted vector; receives merged values
     * @param numsTwo Second sorted vector
     * @return Merged sorted vector
     """

# We can use two pointer and new vector for achieving this but, space complexity will be

# "O(n)".

# Resizing the vector for merging both vector.

# If numsOne is smaller, then adding all remaining numsTwo elements.

"""*
        * Finds the maximum water container area.
        *
        * Given heights of vertical lines, find two lines that with the x-axis form
        * a container holding the maximum amount of water.
     *
     * Example:
     * Input: heights = {1, 8, 6, 2, 5, 4, 8, 3, 7}
     * Output: 49
     *
     * Time Complexity: O(n) where n is the number of heights
     * Space Complexity: O(1)
     *
     * @param heights Heights of vertical lines
     * @return Maximum area of water that can be contained
     """

"""
            Suppose we have an array that represents heights -> [2, 3, 4, 1, 6];

                           |
                           |
                           |
                           |
            |              |
            |              |
            ----------------

            So the capcity will be min(2, 6) * (width), width = j - i = 4 - 0 = 4;
        """

"""*
        * Returns the sorted squares of a sorted array.
        *
        * Given a non-decreasing array (possibly with negatives), square each value
        * and return the squared values in non-decreasing order.
     *
     * Example:
     * Input: numbers = {-4, -1, 0, 3, 10}
     * Output: 0 1 9 16 100
     *
     * Time Complexity: O(n) where n is the vector size
     * Space Complexity: O(n) for the squared result vector
     *
     * @param numbers Sorted vector that may include negative values
     """

# Edge case: empty array

# Step 1: Find first non-negative index

# Step 2: Merge negative and positive parts

# Step 3: Add remaining negative elements

"""*
        * Runs easy-level two-pointer questions.
        *
        * Executes sample inputs for pair sum, palindrome check, duplicate removal,
        * move zeros, merge sorted arrays, max water area, and sorted squares.
        *
        * Example:
        * Input: predefined sample arrays and strings
        * Output: printed answers for easy-level questions
     *
     * Time Complexity: Depends on each demonstrated function
     * Space Complexity: Depends on each demonstrated function
     """

# Two Sum Problem

# IsPalindrome problem

# Removing duplicates in place

# Moving zero elements towards right

# Merge sorted array

# Container with most water

# Square of sorted array

# namespace easy

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                            🔺 TWO POINTERS MEDIUM PROBLEMS                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""*
     * Finds all unique triplets whose sum equals the target.
     *
        * Given an integer array and a target value, return all distinct triplets
        * [a, b, c] such that a + b + c = target.
     *
     * Example:
     * Input: nums = {-1, 0, 1, 2, -1, -4}, target = 0
     * Output: {{-1, -1, 2}, {-1, 0, 1}}
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1) auxiliary (excluding output)
     *
     * @param nums Input vector of integers
     * @param target Target sum for each triplet
     * @return All unique triplets that sum to target
     """

# Skipping duplicates from left

# Skipping duplicates from right

"""*
     * Finds all unique quadruplets whose sum equals k.
     *
        * Given an integer array and k, return all distinct quadruplets
        * [a, b, c, d] such that a + b + c + d = k.
     *
     * Example:
     * Input: nums = {1, 0, -1, 0, -2, 2}, k = 0
     * Output: {{-2, -1, 1, 2}, {-2, 0, 0, 2}, {-1, 0, 0, 1}}
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(1) auxiliary (excluding output)
     *
     * @param nums Input vector of integers
     * @param k Target sum for each quadruplet
     * @return All unique quadruplets that sum to k
     """

# 1.

# Skip duplicate for i

# 2.

# Skip duplicate for j

# 3.

"""*
        * Finds the minimum length subarray with sum at least target.
        *
        * Given a positive integer array and a target, return the smallest length
        * of a contiguous subarray whose sum is greater than or equal to target.
     *
     * Example:
     * Input: nums = {2, 3, 1, 2, 4, 3}, target = 7
     * Output: 2
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * @param nums Input vector of positive integers
     * @param target Required subarray sum threshold
     * @return Minimum valid subarray length, or 0 if not found
     """

"""*
        * Calculates total trapped rain water.
        *
        * Given an elevation map where each value is bar height, compute total
        * water units trapped after rainfall.
     *
     * Example:
     * Input: heights = {3, 0, 2, 0, 4}
     * Output: 7
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * @param heights Elevation map heights
     * @return Total units of trapped water
     """

"""
            Example 1:
                    arr = [3, 0, 2, 0, 4]

                    * Array elements represents the height of the vertical line.
                    * Water will trap between vertical lines so we have to evaluate the thing.
        """

# You alway do wrong here please consider this "leftIndex <= rightIndex"

"""*
        * Sorts an array containing only 0, 1, and 2.
        *
        * Given an array of only three values (0, 1, 2), reorder it so that all
        * 0s come first, then 1s, then 2s.
     *
     * Example:
     * Input: nums = {2, 0, 2, 1, 1, 0}
     * Output: {0, 0, 1, 1, 2, 2}
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * @param nums Vector containing only 0, 1, and 2
     """

# Moving 0 towards front

# Reseting rightIdx

# Moving 1 towards front

"""*
        * Placeholder for three-pointer Dutch National Flag question.
        *
        * Given an array of values 0, 1, and 2, the goal is to sort it in one pass
        * with constant extra space.
        *
        * Example:
        * Input: colors = {2, 0, 2, 1, 1, 0}
        * Output: {0, 0, 1, 1, 2, 2}
     *
    * Time Complexity: O(1) currently (placeholder implementation)
     * Space Complexity: O(1)
     *
     * @param colors Vector to be sorted in Dutch Flag order
     """

"""*
        * Finds a duplicate number in an array.
        *
        * Given an array containing numbers in a limited index range with one
        * repeated value, return the duplicate number.
     *
     * Example:
     * Input: nums = {1, 3, 4, 2, 2}
     * Output: 2
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * @param nums Vector with at least one duplicate in valid index range
     * @return Duplicate number detected by cycle entry
     """

# It's move 1 steps per iteration.

# It's move 2 steps per iteration.

# If any cycle exists eventually it will meet after some iteration.

"""*
        * Counts contiguous subarrays with product less than k.
        *
        * Given a positive integer array and k, count how many contiguous
        * subarrays have product strictly less than k.
     *
     * Example:
     * Input: nums = {10, 5, 2, 6}, k = 100
     * Output: 8
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * @param nums Input vector of positive integers
     * @param k Product upper bound (exclusive)
     * @return Number of valid contiguous subarrays
     """

"""*
        * Runs medium-level two-pointer questions.
        *
        * Executes sample inputs for three-sum, four-sum, minimum subarray length,
        * trapped rain water, Dutch flag ordering, duplicate finding, and
        * subarray product counting.
        *
        * Example:
        * Input: predefined sample arrays and targets
        * Output: printed answers for medium-level questions
     *
     * Time Complexity: Depends on each demonstrated function
     * Space Complexity: Depends on each demonstrated function
     """

# find three sum

# find four sum

# Sum of minimum subarray

# Sum of minimum subarray

# Evaluating total trapped water

# Solving Dutch Flag

# Finding Duplicates (Floyd's cycle)

# Count Total Subarray products

# namespace medium

"""
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                              🔺 TWO POINTERS HARD PROBLEMS                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""*
        * Entry point for hard-level two-pointer questions.
     *
        * This is a placeholder section for future hard problems.
        *
        * Example:
        * Input: none
        * Output: currently no hard problem output
     *
     * Time Complexity: O(1)
     * Space Complexity: O(1)
     """

# CALLING ALL THE METHOD

# namespace hard

def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []

def reverse_array(nums):
    nums = nums[:]
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
