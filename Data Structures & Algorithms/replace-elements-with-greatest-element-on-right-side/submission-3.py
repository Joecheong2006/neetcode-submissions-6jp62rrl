class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        rightMaxSoFar = -1

        for i in range(l):
            val = arr[l - i - 1]
            arr[l - i - 1] = rightMaxSoFar
            rightMaxSoFar = max(val, rightMaxSoFar)
        
        return arr