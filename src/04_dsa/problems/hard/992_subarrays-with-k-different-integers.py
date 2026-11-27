from collections import defaultdict


class Solution:
    def subarrays_with_k_distinct(self, nums: list[int], k: int) -> int:
        def ctn_subarray(t: int) -> int:
            if t == 0:
                return 0

            total_subarray = 0
            num_ctr = defaultdict(int)

            left_idx = 0
            for right_idx, num in enumerate(nums):
                num_ctr[num] += 1

                while len(num_ctr) > t:
                    num_ctr[nums[left_idx]] -= 1
                    if num_ctr[nums[left_idx]] == 0:
                        num_ctr.pop(nums[left_idx])
                    left_idx += 1

                total_subarray += (right_idx - left_idx) + 1

            return total_subarray

        return ctn_subarray(k) - ctn_subarray(k - 1)


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.subarrays_with_k_distinct([1, 2, 1, 2, 3], 2)}")
    print(f"Final Output is: {sol.subarrays_with_k_distinct([1, 2, 1, 3, 4], 3)}")
