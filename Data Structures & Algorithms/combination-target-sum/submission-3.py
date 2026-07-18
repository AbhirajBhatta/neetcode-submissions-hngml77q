class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curSet, curSum):
            if curSum==target:
                res.append(curSet.copy())
                return
            if curSum>target or i==len(nums):
                return
            
            curSet.append(nums[i])
            dfs(i, curSet, curSum+nums[i])
            curSet.pop()
            dfs(i+1, curSet, curSum)
        dfs(0, [], 0)
        return res