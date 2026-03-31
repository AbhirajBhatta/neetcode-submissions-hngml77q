class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minleft = prices[0]
        for i in prices:
            minleft = min(i, minleft)
            profit = i-minleft
            res = max(profit, res)
        return res