class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = len(t)
        char_freq = [0] * 128

        # Increasing the count for character in target
        for c in t:
            char_freq[ord(c) - ord("A")] += 1

        start_idx = 0
        end_idx = len(t) + 1

        left_idx = 0
        for right_idx in range(len(s)):
            if char_freq[ord(s[right_idx]) - ord("A")] > 0:
                window -= 1
            char_freq[ord(s[right_idx]) - ord("A")] -= 1

            while window == 0:
                if end_idx - start_idx > right_idx - left_idx:
                    start_idx = left_idx
                    end_idx = right_idx

                char_freq[ord(s[left_idx]) - ord("A")] += 1
                if char_freq[ord(s[left_idx]) - ord("A")] > 0:
                    window += 1

                left_idx += 1

        return "" if end_idx == len(t) + 1 else s[start_idx : end_idx + 1]


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.minWindow('a', 'a')}")
    print(f"Final Output is: {sol.minWindow('a', 'aa')}")
    print(f"Final Output is: {sol.minWindow('abc', 'b')}")
    print(f"Final Output is: {sol.minWindow('aa', 'aa')}")
    print(f"Final Output is: {sol.minWindow('ADOBECODEBANC', 'ABC')}")
