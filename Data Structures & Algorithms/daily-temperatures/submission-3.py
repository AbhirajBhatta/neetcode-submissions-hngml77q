class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            res[i] = stack[-1][1] - i if stack else 0
            stack.append((temperatures[i], i))
        return res