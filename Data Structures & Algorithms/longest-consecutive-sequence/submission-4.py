class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in s:
                leng = 0
                while((i+leng) in s):
                    leng +=1
                longest = max(longest, leng)
        return longest
