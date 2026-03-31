class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        while l<r:
            if height[l]<height[r]:
                maxl = max(maxl, height[l])
                water = maxl - height[l]
                res += water
                l+=1
            else:
                maxr = max(maxr, height[r])
                water = maxr - height[r]
                res += water
                r-=1
        return res