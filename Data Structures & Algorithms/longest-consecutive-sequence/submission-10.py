class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        LCS = 0
        for i in nums:
            cur = 0
            if i-1 not in nums:
                tmp = i
                while tmp+cur in nums:
                    cur+=1
                LCS = max(LCS, cur)
        return LCS