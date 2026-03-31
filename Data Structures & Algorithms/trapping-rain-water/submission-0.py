class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L = 0
        R = len(height)-1
        maxl, maxr = height[L], height[R]
        while(L<R):
            if height[L]<=height[R]:
                L+=1
                water = maxl-height[L]
                res += water if water>0 else 0
                maxl = max(maxl, height[L])
            else:
                R-=1
                water = maxr-height[R]
                res += water if water>0 else 0
                maxr = max(maxr, height[R])
        return res