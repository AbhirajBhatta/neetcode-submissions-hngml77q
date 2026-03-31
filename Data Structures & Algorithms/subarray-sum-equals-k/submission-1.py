class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = sum = 0
        prefSums = {0:1}
        for i in nums:
            sum += i
            if sum - k in prefSums:
                res += prefSums[sum-k]
            prefSums[sum] = 1 + prefSums.get(sum, 0)
        return res
