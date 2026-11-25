class Solution:
    def solve_queens(self, n: int) -> list[list[str]]:
        placed_queens: list[int] = []
        all_possibilities: list[list[str]] = []

        # method that gonna check whether the current cell is safe or not
        def is_safe(row: int, col: int) -> bool:
            for r in range(row):
                if placed_queens[r] == col:
                    return False

                if abs(row - 1) == abs(placed_queens[r] - col):
                    return False

            return True

        def backtracking(row: int, current: list[list[str]]):
            if row == n:
                all_possibilities.append(["".join(a) for a in current])
                return

            for col in range(n):
                if not is_safe(row, col):
                    continue

                current[row][col] = "Q"
                placed_queens.append(col)

                backtracking(row + 1, current)

                placed_queens.pop()
                current[row][col] = "."

        # calling the backtracking method to general all the possibilities
        backtracking(0, [["."] * n for _ in range(n)])

        return all_possibilities


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.solve_queens(1)}")
    print(f"Final Output is: {sol.solve_queens(4)}")
