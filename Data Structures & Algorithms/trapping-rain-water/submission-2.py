class Solution:
    def trap(self, height: List[int]) -> int:
        totalwater = 0
        l, r = 0, len(height)-1
        maxl, maxr = l, r

        while l<r:
            if height[l]<height[r] and l<r:
                l+=1
                h = height[maxl] - height[l]
                totalwater += h if h>0 else 0
                maxl = l if h<0 else maxl
            else:
                r-=1
                h = height[maxr] - height[r]
                totalwater += h if h>0 else 0
                maxr = r if h<0 else maxr
        
        return totalwater
