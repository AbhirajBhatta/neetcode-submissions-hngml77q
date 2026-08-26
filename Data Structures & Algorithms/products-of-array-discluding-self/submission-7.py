class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [i for i in nums]
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix*nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res