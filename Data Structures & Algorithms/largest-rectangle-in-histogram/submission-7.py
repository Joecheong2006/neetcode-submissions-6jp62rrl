class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        widths = [1] * len(heights)
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                widths[index] += i - index - 1
            stack.append(i)
        
        while stack:
            index = stack.pop()
            widths[index] += len(heights) - index - 1

        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                widths[index] += index - i - 1
            stack.append(i)
            
        while stack:
            index = stack.pop()
            widths[index] += index

        for i in range(len(widths)):
            maxArea = max(maxArea, widths[i] * heights[i])

        return maxArea