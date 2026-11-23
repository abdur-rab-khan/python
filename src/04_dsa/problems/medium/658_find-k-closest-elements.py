class Solution:
    def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[int]:
        left_idx = 0
        right_idx = len(arr) - k

        while left_idx < right_idx:
            mid_idx = left_idx + (right_idx - left_idx) // 2

            if x - arr[mid_idx] > arr[mid_idx + k] - x:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx

        return arr[left_idx : left_idx + k]


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.find_closest_elements([1], 1, 1)}")
    print(f"Final Output is: {sol.find_closest_elements([1, 2, 3, 4, 5], 4, 3)}")
    print(f"Final Output is: {sol.find_closest_elements([1, 1, 2, 3, 4, 5], 4, -1)}")
    print(
        f"Final Output is: {sol.find_closest_elements([0, 2, 2, 3, 4, 6, 7, 8, 9, 9], 4, 5)}"
    )
