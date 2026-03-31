class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,v in enumerate(nums):
            if i>0 and v == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r]+v == 0:
                    res.append([v, nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif nums[l]+nums[r]+v > 0:
                    r-=1
                else:
                    l+=1
        return res