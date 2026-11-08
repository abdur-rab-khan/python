class Solution:
    __k_direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def __init__(self) -> None:
        self.word = ""
        self.board: list[list[str]] = []
        self.is_visited: list[list[bool]] = []

    def exist(self, board: list[list[str]], word: str) -> bool:
        idx = 0
        self.word = word
        self.board = board
        self.is_visited = [[False] * len(board[0]) for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.__search_word(row, col, idx):
                    return True

        return False

    def __is_safe(
        self,
        row: int,
        col: int,
        idx: int,
    ) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(self.board)
            and col < len(self.board[0])
            and self.word[idx] == self.board[row][col]
            and not self.is_visited[row][col]
        )

    def __search_word(
        self,
        row: int,
        col: int,
        idx: int,
    ) -> bool:
        if idx == len(self.word):
            return True

        if not self.__is_safe(row, col, idx):
            return False

        self.is_visited[row][col] = True

        is_found = False
        for offset_row, offset_col in self.__k_direction:
            if self.__search_word(row + offset_row, col + offset_col, idx + 1):
                is_found = True
                break

        self.is_visited[row][col] = False
        return is_found


if __name__ == "__main__":
    sol = Solution()

    board: list[list[str]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    print(f"Final Output is: {sol.exist(board, 'SEE')}")
    print(f"Final Output is: {sol.exist(board, 'ABCB')}")
    print(f"Final Output is: {sol.exist(board, 'ABCCED')}")
