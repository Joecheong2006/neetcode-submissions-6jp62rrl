class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        index_m = set()

        for i, n in enumerate(nums):
            index_m.add(n)

        visited = set()

        result = 0
        for n in nums:
            if n in visited:
                continue
            start = n 
            end = n
            visited.add(end)
            while end + 1 in index_m:
                end += 1
                visited.add(end)
            result = max(result, end - start + 1)
        return result
            
        