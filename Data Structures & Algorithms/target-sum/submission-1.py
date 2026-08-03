class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        cache = {}
        def dfs(i, curVal):
            nonlocal res
            if curVal==target and i==len(nums):
                return 1
            if (i, curVal) in cache:
                return cache[(i, curVal)]
            if i==len(nums):
                return 0
            res =  (dfs(i+1, curVal+nums[i]) + dfs(i+1, curVal-nums[i]))
            cache[(i, curVal)] = res
            return cache[(i, curVal)]
        
        return dfs(0, 0)