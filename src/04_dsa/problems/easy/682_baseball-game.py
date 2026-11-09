class Solution:
    def cal_points(self, operations: list[str]) -> int:
        stack: list[int] = []

        for token in operations:
            if token == "+":
                stack.append(stack[-1] + stack[-2])
            elif token == "C":
                stack.pop()
            elif token == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(token))

        return sum(stack)


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.cal_points(['1', 'C'])}")
    print(f"Final Output is: {sol.cal_points(['5', '2', 'C', 'D', '+'])}")
    print(
        f"Final Output is: {sol.cal_points(['5', '-2', '4', 'C', 'D', '9', '+', '+'])}"
    )
