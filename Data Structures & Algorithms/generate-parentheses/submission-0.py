class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def dfs(opencount, closecount):
            if opencount==closecount==n:
                res.append("".join(stack.copy()))
                return
            if opencount < n:
                stack.append("(")
                dfs(opencount+1, closecount)
                stack.pop()
            if closecount < opencount:
                stack.append(")")
                dfs(opencount, closecount+1)
                stack.pop()
        dfs(0, 0)
        return res
