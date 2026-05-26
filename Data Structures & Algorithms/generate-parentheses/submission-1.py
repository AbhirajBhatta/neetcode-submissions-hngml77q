class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        res = []

        def backTrack(openC, closedC):
            if openC==closedC==n:
                res.append("".join(stack))
            
            if openC<n:
                stack.append("(")
                backTrack(openC+1, closedC)
                stack.pop()
            if closedC<openC:
                stack.append(")")
                backTrack(openC, closedC+1)
                stack.pop()
        backTrack(0,0)
        return res