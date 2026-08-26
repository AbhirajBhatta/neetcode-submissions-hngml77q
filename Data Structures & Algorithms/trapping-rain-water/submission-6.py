class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        while l<r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                water = maxL - height[l]
                res += water
                l+=1
            else:
                maxR = max(maxR, height[r])
                water = maxR - height[r]
                res += water
                r-=1
        return res

