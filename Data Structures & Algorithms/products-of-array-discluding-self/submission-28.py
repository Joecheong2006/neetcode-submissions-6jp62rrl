class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        productBefore = [1] * l
        productAfter = [1] * l

        prodBefore = 1
        prodAfter = 1
        for i in range(l):
            productBefore[i] = prodBefore
            prodBefore *= nums[i]

            productAfter[l - i - 1] *= prodAfter
            prodAfter *= nums[l - i - 1]

        for i in range(l):
            productBefore[i] *= productAfter[i]

        return productBefore
