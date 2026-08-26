class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest = 0
        for num in seen:
            if (num - 1) not in seen:
                l = 1
                while (num + l) in seen:
                    l += 1
                longest = max(longest, l)
                
        return longest
