class Solution:
    def max_area(self, height: list[int]) -> int:
        max_area = 0

        left_idx = 0
        right_idx = len(height) - 1

        while left_idx < right_idx:
            area = min(height[left_idx], height[right_idx]) * (right_idx - left_idx)
            max_area = max(max_area, area)

            if height[left_idx] > height[right_idx]:
                right_idx -= 1
            else:
                left_idx += 1

        return max_area


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.max_area([1, 1])}")
    print(f"Final Output is: {sol.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])}")
