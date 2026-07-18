class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            newDP = dp.copy()
            for s in dp:
                if s==target:
                    return True
                newDP.add(nums[i]+s)
            dp = newDP
        return True if target in dp else False
        
