class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [1] * l

        before = 1
        for i in range(l):
            result[i] = before
            before *= nums[i]

        after = 1
        for i in range(l - 1, -1, -1):
            result[i] *= after
            after *= nums[i]

        return result
