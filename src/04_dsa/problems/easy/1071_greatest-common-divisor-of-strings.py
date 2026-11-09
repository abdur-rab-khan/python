from math import gcd


class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        str_gcd = gcd(len(str1), len(str2))
        sub_str = str1[:str_gcd]

        if (sub_str * (len(str1) // str_gcd)) != str1:
            return ""

        if (sub_str * (len(str2) // str_gcd)) != str2:
            return ""

        return sub_str


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.gcd_of_strings('ABCABC', 'ABC')}")
    print(f"Final Output is: {sol.gcd_of_strings('ABABAB', 'ABAB')}")
    print(f"Final Output is: {sol.gcd_of_strings('LEET', 'CODE')}")
