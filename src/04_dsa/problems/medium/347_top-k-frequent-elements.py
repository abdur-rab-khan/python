from collections import Counter
from heapq import heappop, heappush


class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        # Counting the frequncy of the numbers
        ctn_freq: dict[int, int] = Counter(nums)

        heap: list[tuple[int, int]] = []
        for num, ctn in ctn_freq.items():
            heappush(heap, (ctn, num))
            if len(heap) > k:
                heappop(heap)

        result = []
        for _, num in heap:
            result.append(num)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.top_k_frequent([1], 1)}")
    print(f"Final Output is: {sol.top_k_frequent([1, 1, 1, 2, 2, 3], 2)}")
    print(f"Final Output is: {sol.top_k_frequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)}")
