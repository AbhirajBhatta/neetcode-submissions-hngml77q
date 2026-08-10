class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        pos, neg = 1, 1
        for n in nums:
            tmp = pos*n
            pos = max(tmp, neg*n, n)
            neg = min(tmp, neg*n, n)
            res = max(res, pos, neg, n)
        return res