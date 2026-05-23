class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combination = []
        def dfs(i):
            if sum(combination) == target:
                res.append(combination.copy())
                return
            if sum(combination) > target or i==len(nums):
                return
            
            combination.append(nums[i])
            dfs(i)
            combination.pop()
            dfs(i+1)
        dfs(0)
        return res