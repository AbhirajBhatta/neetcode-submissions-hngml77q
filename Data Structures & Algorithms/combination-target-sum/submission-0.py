class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if subset and sum(subset) == target and i<len(nums):
                res.append(subset.copy())
                return
            if  i>=len(nums) or subset and sum(subset) > target:
                return

            subset.append(nums[i]) 
            dfs(i)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

