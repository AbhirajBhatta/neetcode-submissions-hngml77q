class MinStack:

    def __init__(self):
        self.s = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.minVal:
            self.minVal.append(val)
        else:
            val = min(val, self.minVal[-1])
            self.minVal.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.minVal.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
