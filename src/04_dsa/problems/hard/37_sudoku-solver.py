class Solution:
    def solve_sodoku(self, board: list[list[str]]) -> None:
        board_size = len(board)

        # tracking the cell to check where it's filled or not
        filled_box: list[list[int]] = [[False] * board_size for _ in range(board_size)]
        filled_col: list[list[int]] = [[False] * board_size for _ in range(board_size)]
        filled_row: list[list[int]] = [[False] * board_size for _ in range(board_size)]

        # creates that box idx for handle filled_box
        def get_box_idx(row: int, col: int):
            return (row // 3) * 3 + (col // 3)

        # is safe method gonna check whether current cell is safe to insert current num
        def is_safe(num: int, row: int, col: int):
            return (
                not filled_row[row][num - 1]
                and not filled_col[col][num - 1]
                and not filled_box[get_box_idx(row, col)][num - 1]
            )

        # method that will going to fill the tracking cell
        def place_num(num: int, row: int, col: int):
            filled_row[row][num - 1] = True
            filled_row[col][num - 1] = True
            filled_row[get_box_idx(row, col)][num - 1] = True

        # method that will going to remove the tracking cell
        def remove_num(num: int, row: int, col: int):
            filled_row[row][num - 1] = False
            filled_row[col][num - 1] = False
            filled_row[get_box_idx(row, col)][num - 1] = False

        # filling the filled board based on the current board
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] != ".":
                    place_num(int(board[row][col]), row, col)

        # creating backtracking function to fill all the cells
        def backtracking(row: int, col: int) -> bool:
            if row == board_size:
                return True

            # if all the cells of current row is filled than simply go for next row
            if col == board_size:
                return backtracking(row + 1, 0)

            # if current cell is not blank that simply go for next col
            if board[row][col] != ".":
                return backtracking(row, col + 1)

            for num in range(1, board_size + 1):
                if not is_safe(num, row, col):
                    continue

                board[row][col] = str(num)
                place_num(num, row, col)

                if backtracking(row, col):
                    return True

                board[row][col] = "."
                remove_num(num, row, col)

            return False

        backtracking(0, 0)


if __name__ == "__main__":
    sol = Solution()

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol.solve_sodoku(board)
    print(f"Final Output is: {board}")
