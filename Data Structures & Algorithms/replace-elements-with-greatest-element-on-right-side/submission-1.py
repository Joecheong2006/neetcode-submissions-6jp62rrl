class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        result = [0] * l
        rightMaxSoFar = -1

        for i in range(l):
            result[l - i - 1] = rightMaxSoFar
            rightMaxSoFar = max(arr[l - i - 1], rightMaxSoFar)
        
        return result