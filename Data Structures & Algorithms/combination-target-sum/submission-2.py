class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        cur = []
        def dfs(i, cur, curSum):
            if curSum==target:
                res.append(cur.copy())
                return
            if curSum>target or i==len(nums):
                return
            
            cur.append(nums[i])
            dfs(i, cur, curSum+nums[i])
            cur.pop()
            dfs(i+1, cur, curSum)
        dfs(0, [], 0)
        return res