class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for c in range(len(coins)-1, -1, -1):
            newRow = [0]*(amount+1)
            newRow[0]=1
            for amt in range(1, amount+1):
                newRow[amt] = dp[amt]
                if amt - coins[c] >= 0:
                    newRow[amt] += newRow[amt - coins[c]] 
            dp = newRow
        return dp[amount]
                
                

