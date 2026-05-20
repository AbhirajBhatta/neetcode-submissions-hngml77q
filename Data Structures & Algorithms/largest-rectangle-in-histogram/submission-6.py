class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []  

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, idx = stack.pop()
                res = max(res, height*(i-idx))
                start = idx
            stack.append((h, start))
        
        for h, i in stack:
            res = max(res, h*(len(heights)- i))
        return res
        

    

