class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        productBefore = 1
        for i in range(l):
            res[i] = productBefore
            productBefore *= nums[i]

        productAfter = 1
        for i in range(l):
            res[l - i - 1] *= productAfter
            productAfter *= nums[l - i - 1]

        return res
