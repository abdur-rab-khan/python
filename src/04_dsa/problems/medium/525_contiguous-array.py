class Solution:
    def find_max_length(self, nums: list[int]) -> int:
        max_length = 0
        running_sum = 0

        track_idx = {}
        track_idx[0] = -1

        for idx, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1

            if running_sum in track_idx:
                max_length = max(max_length, idx - track_idx[running_sum])
            else:
                track_idx[running_sum] = idx

        return max_length


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.find_max_length([0, 1])}")
    print(f"Final Output is: {sol.find_max_length([0, 1, 0])}")
    print(f"Final Output is: {sol.find_max_length([0, 1, 0])}")
    print(f"Final Output is: {sol.find_max_length([0, 1, 0, 1])}")
    print(f"Final Output is: {sol.find_max_length([1, 1, 1, 1, 1, 1, 1, 1])}")
    print(f"Final Output is: {sol.find_max_length([1, 1, 1, 1, 1, 1, 1, 1])}")
    print(f"Final Output is: {sol.find_max_length([0, 1, 1, 1, 1, 1, 0, 0, 0])}")
