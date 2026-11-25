class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        write_idx = len(nums) - 1
        num_squares: list[int] = [0] * len(nums)

        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx < right_idx:
            left_square = nums[left_idx] * nums[left_idx]
            right_square = nums[right_idx] * nums[right_idx]

            if left_square < right_square:
                num_squares[write_idx] = right_square
                right_idx -= 1
            else:
                num_squares[write_idx] = left_square
                left_idx += 1

            write_idx -= 1

        return num_squares


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.sorted_squares([-4, -1, 0, 3, 10])}")
    print(f"Final Output is: {sol.sorted_squares([-7, -3, 2, 3, 11])}")
