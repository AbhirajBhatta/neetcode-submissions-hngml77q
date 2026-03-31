class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                idx, value = stack.pop()
                area = value*(i-idx)
                res = max(res, area)
                start = idx
            stack.append((start, v))
        
        for i, h in stack:
            res = max(res, h*(len(heights)-i))
        return res