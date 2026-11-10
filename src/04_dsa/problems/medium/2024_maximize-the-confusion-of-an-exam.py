class Solution:
    def max_consecutive_answers(self, answer_key: str, k: int) -> int:
        max_consecutive = 0

        true_count = 0
        false_count = 0
        max_answer_count = 0

        left_idx = 0
        for right_idx, key in enumerate(answer_key):
            if key == "T":
                true_count += 1
            else:
                false_count += 1
            max_answer_count = max(true_count, false_count)

            while (right_idx - left_idx + 1) - max_answer_count > k:
                if answer_key[left_idx] == "T":
                    true_count -= 1
                else:
                    false_count -= 1
                left_idx += 1

            max_consecutive = max(max_consecutive, right_idx - left_idx + 1)

        return max_consecutive


if __name__ == "__main__":
    sol: Solution = Solution()

    print(sol.max_consecutive_answers("TFFT", 1))
    print(sol.max_consecutive_answers("TTFF", 2))
    print(sol.max_consecutive_answers("TTFTTFTT", 1))
