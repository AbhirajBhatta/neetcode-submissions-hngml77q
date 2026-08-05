class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, cursum):
            if cursum == target and i == len(nums):
                return 1
            if (i, cursum) in dp:
                return dp[(i, cursum)]
            if i >= len(nums):
                return 0
            
            dp[(i, cursum)] = dfs(i+1, cursum + nums[i]) + dfs(i+1, cursum - nums[i])
            return dp[(i, cursum)]
        return dfs(0, 0)
            