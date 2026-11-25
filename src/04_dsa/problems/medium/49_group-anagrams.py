from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        mapped_anagram: dict[tuple[str, ...], list[str]] = defaultdict(list)

        for word in strs:
            # sorting string in python to mapped all anagrams in single place
            # """sorted""" function in python is implemented in "C" it's already really fast
            mapped_anagram[tuple(sorted(word))].append(word)

        return list(mapped_anagram.values())


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.group_anagrams([''])}")
    print(f"Final Output is: {sol.group_anagrams(['a'])}")
    print(
        f"Final Output is: {sol.group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])}"
    )
