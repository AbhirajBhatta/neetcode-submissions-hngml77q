class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # (i, buying)

        def dfs(i, buying):
            if i>=len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                profit = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] =  max(profit, cooldown)
            else:
                profit = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(profit, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)

