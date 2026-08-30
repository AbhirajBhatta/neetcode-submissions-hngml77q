class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                pos, height = stack.pop()
                res = max(res, (i-pos)*height)
                start = pos
            stack.append([start, v])
        n = len(heights)
        for i, h in stack:
            res = max(res, h*(n - i))
        return res