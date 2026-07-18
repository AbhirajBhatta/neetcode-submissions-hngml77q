class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, curSum, curSet):
            if curSum==target:
                res.append(curSet.copy())
                return
            if i==len(nums) or curSum>target:
                return
            
            curSet.append(nums[i])
            dfs(i+1, curSum+nums[i], curSet)
            curSet.pop()

            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1, curSum, curSet)
        dfs(0, 0, [])
        return res