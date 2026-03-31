class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                idx, val = stack.pop()
                area = val*(i-idx)
                res = max(res, area)
                start = idx
            stack.append((start, v))
        
        for i, h in stack:
            res = max(res, h*(len(heights)-i))
        return res