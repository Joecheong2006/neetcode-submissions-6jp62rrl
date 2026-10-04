class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        speedMp = {}

        for i in range(len(position)):
            speedMp[position[i]] = speed[i]

        position.sort(reverse=True)
        for p in position:
            stack.append((target - p) / speedMp[p])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

