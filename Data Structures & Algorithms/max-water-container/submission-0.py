class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(0, len(heights)):
            for j in range(i, len(heights)):
                height = min(heights[i], heights[j])
                width = i-j if i>j else j-i
                cur = height*width
                area = max(area, cur)
        return area
