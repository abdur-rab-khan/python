class Solution:
    def num_subarray_with_sum(self, nums: list[int], goal: int) -> int:
        def count_subarray(target: int) -> int:
            if target < 0:
                return 0

            prefix_sum = 0
            total_subarray = 0

            left_idx = 0
            for right_idx, num in enumerate(nums):
                prefix_sum += num

                while prefix_sum > target:
                    prefix_sum -= nums[left_idx]
                    left_idx += 1

                total_subarray += right_idx - left_idx + 1

            return total_subarray

        return count_subarray(goal) - count_subarray(goal - 1)


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.num_subarray_with_sum([1, 0, 1, 0, 1], 2)}")
    print(f"Final Output is: {sol.num_subarray_with_sum([0, 0, 0, 0, 0], 0)}")
