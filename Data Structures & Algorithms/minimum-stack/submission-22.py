class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minVal = val
        else:
            self.stack.append(val - self.minVal)
            self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        if pop < 0:
            self.minVal -= pop

    def top(self) -> int:
        topVal = self.stack[-1]
        if topVal > 0:
            return topVal + self.minVal
        else:
            return self.minVal
        
    def getMin(self) -> int:
        return self.minVal
