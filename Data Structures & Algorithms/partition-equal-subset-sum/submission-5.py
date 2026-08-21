class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)/2
        cache = {}
        def dfs(i, curSum):
            if curSum==target:
                return True
            if i>=len(nums):
                return False
            
            res = dfs(i+1, curSum+nums[i]) or dfs(i+1, curSum)
            return res
        return dfs(0, 0)