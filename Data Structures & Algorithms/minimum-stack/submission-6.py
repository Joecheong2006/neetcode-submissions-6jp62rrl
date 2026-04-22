class MinStack:

    def __init__(self):
        self.minCurr = float("inf")
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.minCurr = min(val, self.minCurr)
        self.minStack.append(self.minCurr)
        self.stack.append(val)

    def pop(self) -> None:
        self.minStack.pop(-1)
        if len(self.minStack) > 0:
            self.minCurr = self.minStack[-1]
        else:
            self.minCurr = float("inf")
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
