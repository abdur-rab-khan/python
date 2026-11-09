"""
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                         ➕ PREFIX SUM                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                          |
| 🟡 Prefix Sum of an Array is a sum of element from **start** till **end** it is also called as **Cumulative Sum**.                                                                       |
|                                                                                                                                                                                          |
| 🟡 Prefix Sum of **ith** element will be the sum of element of **0th** element to **(i-1)th** element.                                                                                   |
|                                                                                                                                                                                          |
| 🟡 It's often used to **pre-calculate** array element so that in future we don't need to calculate again and again.                                                                      |
|                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                        ➕ EXAMPLE                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                          |
| originalArray = [3, 7, 2, 5, 8];                                                                                                                                                         |
|                                                                                                                                                                                          |
| 🟡 Prefix Sum                                                                                                                                                                            |
|                                                                                                                                                                                          |
|    0 = 3                                                                                                                                                                                 |
|                                                                                                                                                                                          |
|    1 = 7 + previous(3) = 10                                                                                                                                                              |
|                                                                                                                                                                                          |
|    2 = 2 + previous(10) = 12                                                                                                                                                             |
|                                                                                                                                                                                          |
|    3 = 5 + previous(12) = 17                                                                                                                                                             |
|                                                                                                                                                                                          |
|    4 = 8 + previous(17) = 25                                                                                                                                                             |
|                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Easy Prefix Sum Problems

# 🟡 Instead of handling on edge case (left == 0 ? right : right - left - 1) for finding sum query,

# 🟡 We just creates an empty element [0, 2, 6, 7, 12, 15], Now we can simply handle it without worrying about anything.

# Question 1: Sum Query Range.

# Question 2: Left Right Difference.

# namespace easy

# Medium Prefix Sum Problems

# Question 1. Sub Array Sum

# Question 2. Product Except Self

# namespace medium

# Hard Prefix Sum Problems

def prefix_sum(nums):
    result, running = [], 0
    for value in nums:
        running += value
        result.append(running)
    return result

def range_sum(prefix, left, right):
    return prefix[right] - (prefix[left - 1] if left else 0)
