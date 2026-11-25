class Solution:
    def count_odds(self, low: int, high: int) -> int:
        def count(e: int) -> int:
            end = e if e % 2 == 0 else e + 1
            return end // 2

        return count(high) - count(low - 1)


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.count_odds(3, 7)}")
    print(f"Final Output is: {sol.count_odds(8, 10)}")
