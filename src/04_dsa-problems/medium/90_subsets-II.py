def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    sorted_nums = sorted(nums)
    current_subsets: list[int] = []
    final_subsets: list[list[int]] = []

    def generate_subsets(start_idx: int):
        final_subsets.append(current_subsets.copy())

        for idx in range(start_idx, len(sorted_nums)):
            if idx > start_idx and sorted_nums[idx] == sorted_nums[idx - 1]:
                continue

            current_subsets.append(sorted_nums[idx])
            generate_subsets(idx + 1)
            current_subsets.pop()

    generate_subsets(0)
    return final_subsets


if __name__ == "__main__":
    print(subsets_with_dup([0]))
    print(subsets_with_dup([1, 2, 2]))
