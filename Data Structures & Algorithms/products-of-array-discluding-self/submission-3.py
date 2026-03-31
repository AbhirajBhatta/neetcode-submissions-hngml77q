class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref = 1
        for n in nums:
            res.append(pref)
            pref *= n
        post = 1
        for i in range(len(nums)-1, 0, -1):
            res[i] *= post
            post *= nums[i]
        res[0] *= post
        return res

        