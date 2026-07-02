class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total)%2:
            return False
        dp = set()
        dp.add(0)
        target = total//2
        for i in range(len(nums)-1, -1, -1):
            new  = set()
            for n in dp:
                if n+nums[i] == target:
                    return True
                new.add(n+nums[i])
                new.add(n)
            dp = new
        return True if target in dp else False