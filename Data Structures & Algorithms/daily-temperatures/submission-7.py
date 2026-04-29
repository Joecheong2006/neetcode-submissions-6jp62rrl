class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        stack = [0] * len(temperatures)
        result = [0] * len(temperatures)

        for r in range(len(temperatures)):
            while l > 0 and temperatures[stack[l - 1]] < temperatures[r]:
                top = stack[l - 1]
                result[top] = r - top
                l -= 1
            stack[l] = r
            l += 1

        return result