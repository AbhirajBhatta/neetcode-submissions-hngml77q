class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = []
        def dfs(cc, oc):
            if oc==cc==n:
                res.append("".join(stack))
                return
            
            if cc < n:
                stack.append("(")
                dfs(cc+1, oc)
                stack.pop()
            if oc < cc:
                stack.append(")")
                dfs(cc, oc+1)
                stack.pop()
        dfs(0, 0)
        return res