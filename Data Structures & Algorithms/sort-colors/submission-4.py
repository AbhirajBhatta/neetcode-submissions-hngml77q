class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1

        i = 0
        while i <= r:
            if nums[i]==0:
                self.swap(nums, l, i)
                l+=1
            elif nums[i]==2:
                self.swap(nums, r, i)
                r-=1
                i-=1
            i+=1
        

    def swap(self, arr, l, r):
        tmp = arr[l]
        arr[l] = arr[r]
        arr[r] = tmp
            