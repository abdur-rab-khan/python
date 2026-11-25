class Solution:
    def remove_duplicates(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.remove_duplicates('abbaca')}")
    print(f"Final Output is: {sol.remove_duplicates('azxxzy')}")
