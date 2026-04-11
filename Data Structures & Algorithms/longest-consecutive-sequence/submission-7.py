class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        res = 0
        for i in values:
            if i-1 not in values:
                curr = 1
                tmp = i
                while tmp+1 in values:
                    tmp+=1
                    curr+=1
                res = max(res, curr)

        return res
