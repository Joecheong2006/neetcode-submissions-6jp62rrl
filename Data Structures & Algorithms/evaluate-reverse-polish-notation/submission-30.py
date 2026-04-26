class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for token in tokens:
            if token == "-":
                arr[-2] -= arr[-1]
                arr.pop()
            elif token == '+':
                arr[-2] += arr[-1]
                arr.pop()
            elif token == '*':
                arr[-2] *= arr[-1]
                arr.pop()
            elif token == '/':
                arr[-2] = int(arr[-2] / arr[-1])
                arr.pop()
            else:
                arr.append(int(token))

        return arr[0]