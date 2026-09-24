class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        longestLen = 0
        for num in nums:
            if num - 1 in seen:
                continue

            length = 1
            while num + length in seen:
                length += 1

            longestLen = max(longestLen, length)

        return longestLen
        