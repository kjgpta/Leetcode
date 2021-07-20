class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            k = sum(accounts[i])
            if k > max_wealth:
                max_wealth = k
        return max_wealth