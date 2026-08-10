class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        res = max(nums)
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            res = max(res, cursum)
            while cursum < 0:
                cursum -= nums[l]
                l+=1
            
        return res