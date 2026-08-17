class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r<len(nums)-1:
            res+=1
            jump = max(nums[l:r+1])
            l = r+1
            r += jump
        return res
