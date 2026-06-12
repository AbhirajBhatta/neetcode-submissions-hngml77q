class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = []
        def gen(oc, cc):
            if oc==cc==n:
                res.append("".join(stack))
                return
            
            if oc<n:
                stack.append("(")
                gen(oc+1, cc)
                stack.pop()
            if cc<oc:
                stack.append(")")
                gen(oc, cc+1)
                stack.pop()
        gen(0, 0)
        return res