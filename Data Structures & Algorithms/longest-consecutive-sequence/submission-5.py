class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for i in unique:
            cur = 0
            num = i
            while num in unique:
                cur += 1
                num -= 1
            longest = max(cur, longest)
        return longest
