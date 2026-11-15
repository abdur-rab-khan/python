class Solution:
    def max_turbulence_subarray(self, arr: list[int]) -> int:
        max_size = 1

        left_idx = 0
        prev_sign = ""

        for right_idx in range(1, len(arr)):
            if arr[right_idx] != arr[right_idx - 1]:
                is_valid = (
                    prev_sign == ">" and arr[right_idx] > arr[right_idx - 1]
                ) or (prev_sign == "<" and arr[right_idx] < arr[right_idx - 1])

                if prev_sign and not is_valid:
                    left_idx = right_idx - 1

                prev_sign = ">" if arr[right_idx] < arr[right_idx - 1] else "<"
            else:
                prev_sign = ""
                left_idx = right_idx

            max_size = max(max_size, (right_idx - left_idx) + 1)

        return max_size


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.max_turbulence_subarray([100])}")
    print(f"Final Output is: {sol.max_turbulence_subarray([4, 8, 12, 16])}")
    print(
        f"Final Output is: {sol.max_turbulence_subarray([0, 1, 1, 0, 1, 0, 1, 1, 0, 0])}"
    )
    print(
        f"Final Output is: {sol.max_turbulence_subarray([2, 0, 2, 4, 2, 5, 0, 1, 2, 3])}"
    )
    print(
        f"Final Output is: {sol.max_turbulence_subarray([9, 4, 2, 10, 7, 8, 8, 1, 9])}"
    )
