class MinStack:

    def __init__(self):
        self.minCurr = float("inf")
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val - self.minCurr)
            if val < self.minCurr:
                self.minCurr = val
        else:
            self.stack.append(0)
            self.minCurr = val

    def pop(self) -> None:
        if not self.stack:
           return

        diff = self.stack.pop()
        if diff < 0:
            self.minCurr -= diff

    def top(self) -> int:
        top = self.stack[-1]
        if top < 0:
            return self.minCurr
        return top + self.minCurr
        
    def getMin(self) -> int:
        return self.minCurr
