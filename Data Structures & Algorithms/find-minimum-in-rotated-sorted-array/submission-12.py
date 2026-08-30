class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            mid = (l+r)//2
        
            if nums[mid] >= nums[l]: #left sorted portion
                res = min(nums[l], res)
                l = mid+1
            else:
                res = min(nums[mid], res)
                r = mid -1
        return res