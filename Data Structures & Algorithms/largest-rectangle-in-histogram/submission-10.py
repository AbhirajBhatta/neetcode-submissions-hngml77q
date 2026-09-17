class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][-1] > v:
                idx, height = stack.pop()
                res = max(res, height*(i-idx))
                start = idx
            stack.append([start, v])
        
        for i, h in stack:
            res= max(res, (len(heights)-i)*h)
        return res