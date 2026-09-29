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

        top = self.stack.pop()

        if top < 0:
            self.minVal -= top

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.minVal
        else:
            return self.stack[-1] + self.minVal

    def getMin(self) -> int:
        return self.minVal
        
