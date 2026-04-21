class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = 0
        maxS = 0

        for n in nums:
            s += n
            s *= n
            maxS = max(s, maxS)

        return maxS