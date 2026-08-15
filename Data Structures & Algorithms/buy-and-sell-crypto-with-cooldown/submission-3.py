class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        res = 0
        res = 0
        def dfs(i, buying):
            nonlocal res
            if i>=len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(res, buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(res, sell, cooldown)
            
            return dp[(i, buying)]
        return dfs(0, True)
