class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        for pos in range(len(nums)-2, -1, -1):
            if nums[pos] + pos >= target:
                target = pos
        return target ==0
