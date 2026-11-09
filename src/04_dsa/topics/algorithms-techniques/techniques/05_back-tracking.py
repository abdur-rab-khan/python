"""
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                         BACK TRACKING                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
| 🟡 Backtracking is a recursive technique used to find a solution by trying one path at a time. If a path leads to a dead-end, it goes back (undo) and tries a  |
|    different path, instead of checking every single path fully. The undo step is the main idea behind backtracking.                                            |
|                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
| 🔵 Example:                                                                                                                                                    |
|            Suppose we have a maze puzzle, and we want to reach the end. We pick a direction and walk that path. If we hit a wall (dead-end), we walk back to   |
|            the last point where we had a choice, and try a different direction. We repeat this until we reach the end.                                         |
|                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# CHOOSE: add nums[index] into the path

# EXPLORE: go deeper look element only after i

# UNCHOOSE: remove nums[i] before trying to next option

# CHOOSE: Push into the tempList

# BACKTRACK: "backTracking" to call the function

# UNCHOOSE: Pop from tempList mainly to skip and create permutation

# Solve subset problem using backtracking

# Solve Permutation problem using backtracking

# namespace Problems

def permutations(values):
    result, path, used = [], [], [False] * len(values)
    def backtrack():
        if len(path) == len(values):
            result.append(path[:])
            return
        for i, value in enumerate(values):
            if used[i]:
                continue
            used[i] = True
            path.append(value)
            backtrack()
            path.pop()
            used[i] = False
    backtrack()
    return result
