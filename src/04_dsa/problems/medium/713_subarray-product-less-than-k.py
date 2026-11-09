class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if not nums or k <= 0:
            return 0

        prefix_sum = 1
        total_subarray = 0

        left_idx = 0
        for right_idx, num in enumerate(nums):
            prefix_sum *= num

            while prefix_sum >= k:
                prefix_sum /= nums[left_idx]
                left_idx += 1

            total_subarray += right_idx - left_idx + 1

        return total_subarray


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100)}")
    print(f"Final Output is: {sol.numSubarrayProductLessThanK([1, 2, 3], 0)}")
