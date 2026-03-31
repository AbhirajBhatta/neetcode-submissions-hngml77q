class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        n = set(nums)
        for i in n:
            if i-1 not in n:
                l = 1
                temp = i
                while temp+1 in n:
                    l+=1
                    temp+=1
                res = max(res, l)
        return res
