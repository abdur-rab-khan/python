from heapq import heappop, heappush


class Solution:
    def find_kth_largest(self, nums: list[int], k: int) -> int:
        # if k is greater then the nums size mean it's not possible
        if len(nums) < k:
            return -1

        heap = []

        # looping through each items of the num
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)

        return heap[0]


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.find_kth_largest([3, 2, 1, 5, 6, 4], 2)}")
    print(f"Final Output is: {sol.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)}")
