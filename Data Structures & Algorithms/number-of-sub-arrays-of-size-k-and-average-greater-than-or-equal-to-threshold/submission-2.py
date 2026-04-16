class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = 0
        count = 0

        for i in range(k - 1):
            s += arr[i]

        for r in range(k - 1, len(arr)):
            s += arr[r]

            if s / k >= threshold:
                count += 1
            
            s -= arr[r - k + 1]

        return count