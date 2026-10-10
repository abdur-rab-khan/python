def get_combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    current_sum: int = 0
    current_combination: list[int] = []
    all_combinations: list[list[int]] = []

    def backtracking(start_idx: int):
        nonlocal current_sum
        if current_sum >= target:
            if current_sum == target:
                all_combinations.append(current_combination.copy())
            return

        for idx in range(start_idx, len(candidates)):
            current_sum += candidates[idx]
            current_combination.append(candidates[idx])
            backtracking(idx)
            current_sum -= candidates[idx]
            current_combination.pop()

    backtracking(0)
    return all_combinations


if __name__ == "__main__":
    print(get_combination_sum([2], 1))
    print(get_combination_sum([2, 3, 5], 8))
    print(get_combination_sum([2, 3, 6, 7], 7))
