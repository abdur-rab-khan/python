class Solution:
    def eval_rpn(self, tokens: list[str]) -> int:
        stack: list[int] = []

        for token in tokens:
            is_operator = token == "+" or token == "-" or token == "*" or token == "/"
            if is_operator:
                first_num = stack.pop()
                second_num = stack.pop()
                if token == "+":
                    stack.append(first_num + second_num)
                elif token == "-":
                    stack.append(first_num - second_num)
                elif token == "*":
                    stack.append(first_num * second_num)
                else:
                    stack.append(second_num // first_num)
            else:
                stack.append(int(token))

        return stack[0]


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.eval_rpn(['2', '1', '+', '3', '*'])}")
    print(f"Final Output is: {sol.eval_rpn(['4', '13', '5', '/', '+'])}")
    print(
        f"Final Output is: {sol.eval_rpn(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])}"
    )
