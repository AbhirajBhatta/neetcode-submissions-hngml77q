class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for i,v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                idx, val = stack.pop()
                output[idx] = i-idx
            stack.append([i, v])
        return output



            