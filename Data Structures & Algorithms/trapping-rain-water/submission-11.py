class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        prefix = [0] * l
        suffix = [0] * l

        prefix[0] = height[0]
        for i in range(1, l):
            prefix[i] = max(prefix[i - 1], height[i])

        suffix[l - 1] = height[l - 1]
        for i in range(l - 2, -1, -1):
            suffix[i] =  max(suffix[i + 1], height[i])
        
        water = 0
        for i in range(l):
            water += min(prefix[i], suffix[i]) - height[i]
        return water