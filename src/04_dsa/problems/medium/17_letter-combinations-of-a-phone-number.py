from typing import ClassVar


class Solution:
    __keypad_map: ClassVar[dict[str, str]] = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letter_combination(self, digits: str) -> list[str]:
        if not digits:
            return []

        combinations: list[str] = []

        def backtracking(idx: int, current: str):
            # if idx become equal to the length of digits than simply end the recursion
            if idx == len(digits):
                combinations.append(current)
                return

            # looping through each mapped characters
            for char in self.__keypad_map[digits[idx]]:
                backtracking(idx + 1, current + char)

        # calling the backtracking to generate all the possible combinations
        backtracking(0, "")

        return combinations


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.letter_combination('')}")
    print(f"Final Output is: {sol.letter_combination('2')}")
    print(f"Final Output is: {sol.letter_combination('23')}")
    print(f"Final Output is: {sol.letter_combination('234')}")
