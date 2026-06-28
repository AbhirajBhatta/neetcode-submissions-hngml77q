class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        small, big = 1, 1
        for n in nums:
            tmp = big
            big = max(big*n, small*n, n)
            small = min(tmp*n, small*n, n)
            res = max(res, big, small)
        return res