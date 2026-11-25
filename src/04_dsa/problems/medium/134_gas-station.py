class Solution:
    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        gas_ctr = 0
        start_pos = 0
        for i in range(len(gas)):
            gas_ctr += gas[i]
            gas_ctr -= cost[i]

            if gas_ctr < 0:
                start_pos = i + 1
                gas_ctr = 0

        return -1 if gas_ctr < 0 else start_pos


if __name__ == "__main__":
    sol = Solution()
    print(
        f"Final Output is: {sol.can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])}"
    )
    print(f"Final Output is: {sol.can_complete_circuit([2, 3, 4], [3, 4, 3])}")
