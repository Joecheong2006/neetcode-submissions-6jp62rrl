class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = {}
        for i, n in enumerate(nums):
            count[n] = 1

        result = 0
        for n in nums:
            if count[n] > 1:
                continue
            end = n
            count[end] += 1
            while end + 1 in count:
                end += 1
                count[end] += 1
            result = max(result, end - n + 1)
        return result
            
        