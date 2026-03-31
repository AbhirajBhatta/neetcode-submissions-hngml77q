class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minleft = prices[0]
        for p in prices:
            profit = p - minleft
            if profit > res:
                res = profit
            if profit <=0:
                minleft = p
        return res