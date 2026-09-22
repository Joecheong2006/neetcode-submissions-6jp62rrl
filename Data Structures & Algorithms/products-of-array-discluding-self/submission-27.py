class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        preProducts = [1] * l
        postProducts = [1] * l

        preP = 1
        postP = 1
        for i in range(l):
            preProducts[i] = preP
            preP *= nums[i]

            postProducts[l - i - 1] *= postP
            postP *= nums[l - i - 1]

        for i in range(l):
            preProducts[i] *= postProducts[i]

        return preProducts
