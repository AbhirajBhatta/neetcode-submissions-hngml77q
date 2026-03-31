class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t=="+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif t=="*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif t=="-":
                op2, op1 = int(stack.pop()), int(stack.pop())
                stack.append(op1-op2)
            elif t=="/":
                op2, op1 = int(stack.pop()), int(stack.pop())
                stack.append(int(op1/op2))
            else:
                stack.append(t)
        return int(stack[0])
