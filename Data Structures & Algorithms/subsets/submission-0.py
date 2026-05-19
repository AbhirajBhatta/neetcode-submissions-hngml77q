class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        sets = []
        def dfs(i):
            if i >= len(nums):
                res.append(sets.copy())
                return
            
            sets.append(nums[i])
            dfs(i+1)

            sets.pop()
            dfs(i+1)
        dfs(0)
        return res