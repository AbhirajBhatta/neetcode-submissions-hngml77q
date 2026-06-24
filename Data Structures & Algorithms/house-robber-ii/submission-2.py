class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.roball(nums[1:]), self.roball(nums[:-1]))
    def roball(self, nums):
        r1, r2 = 0, 0
        for n in nums:
            temp = max(r1+n, r2)
            r1 = r2
            r2 = temp
        return r2