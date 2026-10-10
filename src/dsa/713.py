def find_subarray_product(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0

    total_subarray = 0
    current_product = 1

    left_idx: int = 0
    for right_idx, num in enumerate(nums):
        current_product *= num

        while current_product >= k:
            current_product //= nums[left_idx]
            left_idx += 1

        total_subarray += (right_idx - left_idx) + 1

    return total_subarray


if __name__ == "__main__":
    print(find_subarray_product([10, 5, 2, 6], 100))
    print(find_subarray_product([1, 2, 3], 0))
