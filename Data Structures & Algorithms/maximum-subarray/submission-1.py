class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        cursum = 0
        for r in range(len(nums)):
            if cursum<0:
                cursum=0
            cursum += nums[r]
            res = max(cursum, res)
        return res