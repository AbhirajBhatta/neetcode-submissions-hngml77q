class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t=="+":
                stack.append(stack.pop()+stack.pop())
            elif t=="*":
                stack.append(stack.pop()*stack.pop())
            elif t=="-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1-op2)
            elif t=="/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1/op2))
            else:
                stack.append(int(t))
        return stack[0]