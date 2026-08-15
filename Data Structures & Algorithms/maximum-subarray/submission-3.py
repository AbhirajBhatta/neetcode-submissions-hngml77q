class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prvSum = 0
        res = nums[0]
        for n in nums:
            if prvSum < 0:
                prvSum=0
            prvSum = prvSum + n
            res = max(res, prvSum)
        return res