class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minv, maxv = 1, 1
        res = max(nums)

        for n in nums:
            temp = maxv*n
            maxv = max(temp, minv*n, n)
            minv = min(temp, minv*n, n)
            res = max(minv, maxv, res)
        return res