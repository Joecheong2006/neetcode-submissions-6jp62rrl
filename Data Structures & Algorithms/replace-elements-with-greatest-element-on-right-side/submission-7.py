class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        rightMaxSoFar = -1

        for i in range(l - 1, -1, -1):
            val = arr[i]
            arr[i] = rightMaxSoFar
            rightMaxSoFar = max(val, rightMaxSoFar)
        
        return arr