class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0 , len(height)-1
        maxl, maxr = height[l], height[r]
        while l<r:
            if height[l] < height[r] and l<r:
                l+=1
                maxl = max(height[l], maxl)
                water = maxl - height[l]
                res += water
                
            else:
                r-=1
                maxr = max(height[r], maxr)
                water = maxr - height[r]
                res += water
                
        return res



                