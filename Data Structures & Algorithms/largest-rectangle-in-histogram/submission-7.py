class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                area = height*(i-idx)
                res = max(res, area)
                start = idx
            stack.append([start, h])
        
        for i, h in stack:
            area = h*(len(heights)-i)
            res = max(res, area)
        return res