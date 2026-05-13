class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        res = 0

        while l< r:
            if height[l] < height[r]:
                l+=1
                maxl = max(height[l], maxl)
                res += maxl - height[l]
            else:
                r-=1
                maxr = max(height[r], maxr)
                res += maxr - height[r]
        return res
