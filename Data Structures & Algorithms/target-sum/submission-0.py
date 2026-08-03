class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def dfs(i, curVal):
            nonlocal res
            if curVal==target and i==len(nums):
                res+=1
                return
            if i< len(nums):
                dfs(i+1, curVal+nums[i])
                dfs(i+1, curVal-nums[i])
        dfs(0, 0)
        return res