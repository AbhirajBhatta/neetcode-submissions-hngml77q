class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in nums:
            tmp = i
            if tmp-1 not in nums:
                r = 1
                while tmp+1 in nums:
                    r+=1
                    tmp+=1
                res = max(res, r)
        return res