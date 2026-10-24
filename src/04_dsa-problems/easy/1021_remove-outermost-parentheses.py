class Solution:
    def remove_outer_parentheses(self, s: str) -> str:
        result = ""
        opened_parentheses = 0

        for ch in s:
            opened_parentheses += 1 if ch == "(" else -1
            if (
                ch == "("
                and opened_parentheses > 1
                or ch == ")"
                and opened_parentheses > 0
            ):
                result += ch

        return result


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.remove_outer_parentheses('()()')}")
    print(f"Final Output is: {sol.remove_outer_parentheses('(()())(())')}")
    print(f"Final Output is: {sol.remove_outer_parentheses('(()())(())(()(()))')}")
