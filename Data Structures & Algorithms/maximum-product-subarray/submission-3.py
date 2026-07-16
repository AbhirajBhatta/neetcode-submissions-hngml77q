class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos, neg = 1, 1
        res = max(nums)

        for n in nums:
            temp = pos*n
            pos = max(temp, neg*n, n)
            neg = min(temp, neg*n, n)
            res = max(res, pos, neg)
        
        return res