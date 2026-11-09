class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        nums_length = len(nums)
        is_used: list[bool] = [False] * nums_length
        current_permutation: list[int] = []
        all_permutations: list[list[int]] = []

        def build_permutations():
            if len(current_permutation) == nums_length:
                all_permutations.append(current_permutation.copy())
                return

            for idx, num in enumerate(nums):
                if is_used[idx]:
                    continue

                # 1. Choose
                is_used[idx] = True
                current_permutation.append(num)

                # 2. Explore
                build_permutations()

                # 3. Undo
                is_used[idx] = False
                current_permutation.pop()

        build_permutations()
        return all_permutations


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.permute([1])}")
    print(f"Final Output is: {sol.permute([0, 1])}")
    print(f"Final Output is: {sol.permute([1, 2, 3])}")
