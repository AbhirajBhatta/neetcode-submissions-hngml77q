class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = (i-idx)*height
                res = max(res, area)
                start = idx
            stack.append([start, h])
        
        for i, h in stack:
            area = (len(heights)-i)*h
            res = max(res, area)
        return res

            