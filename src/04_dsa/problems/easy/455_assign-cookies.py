class Solution:
    def find_content_children(self, g: list[int], s: list[int]) -> int:
        sorted_children = sorted(g)
        sorted_cookies = sorted(s)

        child_idx = 0
        for cookie in sorted_cookies:
            if child_idx == len(sorted_children):
                break

            if cookie >= sorted_children[child_idx]:
                child_idx += 1

        return child_idx


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.find_content_children([1, 2, 3], [1, 1])}")
    print(f"Final Output is: {sol.find_content_children([1, 2], [1, 2, 3])}")
