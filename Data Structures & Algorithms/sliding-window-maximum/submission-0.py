class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(0, len(nums)-k+1):
            temp = -10001
            for j in range(i, i+k):
                temp = max(temp, nums[j])
            res.append(temp)
        return res