class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            if val <= self.minstack[-1]:
                self.minstack.append(val)

    def pop(self) -> None:
        if self.minstack[-1]==self.stack[-1]:
            self.minstack.pop()
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
