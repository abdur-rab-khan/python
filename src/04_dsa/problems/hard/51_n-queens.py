class Solution:
    def solve_queens(self, n: int) -> list[list[str]]:
        is_placed: list[int] = []
        current: list[str] = ["."] * n
        answer: list[list[str]] = [["."] * n for _ in range(n)]

        def is_safe(row, col):
            for r in range(row):
                # checking whether queen is exists in the col
                if is_placed[r] == col:
                    return False

                # checking whether queen is exists in the diagonal
                if abs(row - r) == abs(is_placed[r] - col):
                    return False

            return True

        def solve(row: int, col: int):
            if row == n:
                answer.append(current.copy())
                return

            if col > n:
                return solve(row + 1, 0)

            for c in range(col, n):
                if not is_safe(row, c):
                    continue

                is_placed.append(c)
                current[row][c] = "Q"

                solve(row, col + 1)

                is_placed.pop()
                current[row][c] = "."

        solve(0, 0)
        return answer


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.solve_queens(1)}")
    print(f"Final Output is: {sol.solve_queens(4)}")
