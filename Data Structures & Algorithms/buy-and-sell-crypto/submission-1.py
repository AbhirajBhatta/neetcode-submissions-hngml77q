class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxprofit = 0
        profit = 0
        for i in prices:
            profit = i - minbuy
            minbuy = min(minbuy, i)
            maxprofit = max(maxprofit, profit)
        if maxprofit > 0:
            return maxprofit
        else:
            return 0
        

