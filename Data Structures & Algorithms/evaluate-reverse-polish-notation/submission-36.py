class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        res = 0
        for token in tokens:
            if token == "+":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs + rhs)
            elif token == "-":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs - rhs)
            elif token == "*":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs * rhs)
            elif token == "/":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(int(lhs / rhs))
            else:
                stack.append(int(token))

        return stack[0]

