class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minL = prices[0]

        for p in prices:
            profit = p - minL
            if minL > p:
                minL = p 
            if profit > res:
                res = profit
        return res