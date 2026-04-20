class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0

        minS = 1e20
        s = nums[l]
        while r < len(nums):
            if s < target:
                r += 1
                if r < len(nums):
                    s += nums[r]
            else:
                minS = min(r - l + 1, minS)
                s -= nums[l]
                l += 1

        return 0 if minS == 1e20 else minS