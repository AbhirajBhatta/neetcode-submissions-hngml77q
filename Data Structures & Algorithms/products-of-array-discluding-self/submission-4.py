class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref = 1
        for i in nums:
            res.append(pref)
            pref *= i
        suff = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suff
            suff = suff* nums[i]
        
        return res