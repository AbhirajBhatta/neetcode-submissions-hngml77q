class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        num0 = nums[1:]
        num1 = nums[:-1]
        return max(self.robber(num0), self.robber(num1))
    
    def robber(self, nums):
        nums.append(0)
        for i in range(len(nums)-3, -1, -1):
            nums[i] = max(nums[i+1], nums[i]+nums[i+2])
        return nums[0]
        