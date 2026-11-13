class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        current_subsets: list[int] = []
        final_subsets: list[list[int]] = []

        def backtracking(idx: int):
            final_subsets.append(current_subsets.copy())

            for i in range(idx, len(nums)):
                current_subsets.append(nums[i])
                backtracking(i + 1)
                current_subsets.pop()

        # calling backtracking to get all the possible subsets
        backtracking(0)

        return final_subsets


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.subsets([])}")
    print(f"Final Output is: {sol.subsets([0])}")
    print(f"Final Output is: {sol.subsets([1, 2, 3])}")
