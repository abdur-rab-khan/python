class Solution:
    def find_content_children(self, g: list[int], s: list[int]) -> int:
        sorted_children = sorted(g)
        sorted_cookies = sorted(s)

        g_ptr = s_ptr = 0
        while g_ptr < len(sorted_children) and s_ptr < len(sorted_cookies):
            if sorted_cookies[s_ptr] >= sorted_children[g_ptr]:
                g_ptr += 1
            s_ptr += 1

        return g_ptr


if __name__ == "__main__":
    sol = Solution()
    print(f"Final Output is: {sol.find_content_children([1, 2, 3], [1, 1])}")
    print(f"Final Output is: {sol.find_content_children([1, 2], [1, 2, 3])}")
