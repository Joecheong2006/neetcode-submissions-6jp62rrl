class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}

        for i, n in enumerate(nums):
            m[n] = 1

        result = 0
        for n in nums:
            if m[n] > 1:
                continue
            start = n 
            end = n
            m[end] += 1
            while end + 1 in m:
                end += 1
                m[end] += 1
            result = max(result, end - start + 1)
        return result
            
        