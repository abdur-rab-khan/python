"""
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                       GREEDY TECHNIQUE                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
| 🟡 Greedy technique is a rule where we pick the current best optimal choice (that looks best right now) that eventually leads us to have global optimal        |
|     solution, So greedy only works when picking the best choice at each step keeps leading to the correct final answer for that problem.                       |
|                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
| 🔵 Example 1 (Matching type):                                                                                                                                  |
|             Suppose we have "n" children with a greed value each, and "k" cookies with a size each, and we want to satisfy as many children as possible.       |
|             The greedy way is to sort children by greed (smallest first) and cookies by size (smallest first), via this we can give the smallest cookies to    |
|             the children with lowest greedy.                                                                                                                   |
|                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
| 🔵 Example 2 (Scheduling type):                                                                                                                                |
|             Suppose you are building a booking system (like a meeting scheduler in your web app, or a timeline of non-overlapping cutscene events in a game). |
|             Each task has a start time and an end time, and you want to fit in the maximum number of non-overlapping tasks.                                    |
|             The greedy way is to sort all tasks by their end time (earliest finishing first), then keep picking the next task only if it starts after the      |
|             end time of the last picked task. Picking the "earliest finishing" task first always leads to the maximum number of tasks fitted.                  |
|                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""
     * Give list of children and the list of cookies.
     * Find the number of children we can fulfill there greed
     """

# Traversing on cookies to get to the best cookie who fulfill the current children greed.

# No cookies left, that can satisfy

"""
     * 👉 For this "LemonadeChange" problem we have greed criteria at with use gives as "$20 bills", here we have to choice to split this.
     * 👉 Either "$5 * 3 = 15" or "$10 + $5 = 15", but our greed say that use "$10 bill" has much as possible don't waste "$5" because "$5" can use with "$10 and $20" both.
     *    We can't afford to loose it.
     """

"""
     * 👉 For this "Jump Game" problem our greed criteria is that, We don't care about the solution I just want to go furthest jump that I can make.
     * 👉 Via this you never go back just visit and update the "maxReach" once maxReach goes beyond the array size that's the position we are looking for.
     * 👉 Unlike backtracking where we would visit to all possible paths and once find dead end we just undo the step but it's not a case with greedy approach.
     """

# 🟡 First approach: Traversing from right to left.

# 🟡 At each step we are checking that if the finalPosition is reachable from current pos.

# 🟡 If it's reachable mean we can now say that if any number each to current reachable position, then they can eventually to go the end

# int finalPosition = static_cast<int>(nums.size() - 1);

# for (int i = nums.size() - 2; i >= 0; --i) {

#     if (nums[i] + i >= finalPosition) {

#         finalPosition = i;

#     }

# }

# return finalPosition == 0;

"""
     * 🟡 Intuition: If total gas is smaller than the cost, mean it's not possible to complete the circuit.
     *               If gas is there means it's possible, to has path just we need to check each gas station,
     *               with the cost need to go to next station.
     """

# Checking the total gas with total cost, to see whether it's possible to complete the circuit

# Checking if "totalGas" become negative we need to reset and start freshly again.

# Question 1

# Question 2

# Question 3

# Question 4

# namespace problems


def activity_selection(activities):
    # activities are (start, finish); choose the maximum compatible set.
    selected, end = [], float("-inf")
    for start, finish in sorted(activities, key=lambda item: item[1]):
        if start >= end:
            selected.append((start, finish))
            end = finish
    return selected
