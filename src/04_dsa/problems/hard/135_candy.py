class Solution:
    def candy(self, ratings: list[int]) -> int:
        given_candies = [1] * len(ratings)

        # let's see all the left side ratings
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                given_candies[i] = given_candies[i - 1] + 1

        # let's see all the right side ratings
        for j in reversed(range(len(ratings) - 1)):
            if ratings[j] > ratings[j + 1]:
                given_candies[j] = max(given_candies[j], given_candies[j + 1] + 1)

        return sum(given_candies)


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.candy([1, 0, 2])}")
    print(f"Final Output is: {sol.candy([1, 2, 2])}")
    print(f"Final Output is: {sol.candy([1, 3, 4, 5, 2])}")
