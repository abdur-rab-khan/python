class Solution:
    def erase_overlaping_intervals(self, intervals: list[list[int]]) -> int:
        # Fallback to prevent from occuring StopIteration exception
        if len(intervals) == 1:
            return 0

        removed_ctn = 0
        sorted_intervals = iter(sorted(intervals, key=lambda l: l[1]))

        # Iter makes an iterator and next return the current item and move forward by one
        prev_end = next(sorted_intervals)[1]

        for interval in sorted_intervals:
            if prev_end > interval[0]:
                removed_ctn += 1
            else:
                prev_end = interval[1]

        return removed_ctn


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.erase_overlaping_intervals([[1, 2], [2, 3]])}")
    print(
        f"Final Output is: {sol.erase_overlaping_intervals([[1, 2], [1, 2], [1, 2]])}"
    )
    print(
        f"Final Output is: {sol.erase_overlaping_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])}"
    )
    print(
        f"Final Output is: {sol.erase_overlaping_intervals([[1, 100], [11, 22], [1, 11], [2, 12]])}"
    )
