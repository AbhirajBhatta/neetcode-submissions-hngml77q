class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = 1
        res = []
        for i in nums:
            res.append(pref)
            pref *= i

        post = 1
        idx = len(nums)-1
        for i in range(len(nums)-1, 0, -1):
            post *= nums[i]
            idx -= 1
            res[idx] *= post
        return res
