class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, s = 0, 0
        minS = float("inf")

        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                minS = min(r - l + 1, minS)
                s -= nums[l]
                l += 1

        return 0 if minS == float("inf") else minS