class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                temp = prices[i+1] - prices[i]
                profit+= temp
        return profit
