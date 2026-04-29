class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                top = stack.pop()
                result[top] = r - top
            stack.append(r)

        return result