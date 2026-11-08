from collections import defaultdict


class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        max_freq = 0
        max_substr = 0

        char_freq = defaultdict(int)

        left_idx = 0
        for right_idx in range(len(s)):
            char_freq[s[right_idx]] += 1
            max_freq = max(max_freq, char_freq[s[right_idx]])

            while (right_idx - left_idx + 1) - max_freq > k:
                char_freq[s[left_idx]] -= 1
                left_idx += 1

            max_substr = max(max_substr, (right_idx - left_idx + 1))

        return max_substr


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.character_replacement(s='ABAB', k=2)}")  # 4
    print(f"Final Output is: {sol.character_replacement(s='AABABBA', k=1)}")  # 1
