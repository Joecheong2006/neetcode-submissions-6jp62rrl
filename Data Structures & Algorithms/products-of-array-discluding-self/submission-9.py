class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [0] * l
        products_before = [0] * l
        products_after = [0] * l

        products_before[0] = products_after[l - 1] = 1

        for i in range(1, l):
            products_before[i] = nums[i - 1] * products_before[i - 1]

        for i in range(l - 2, -1, -1):
            products_after[i] = nums[i + 1] * products_after[i + 1]

        for i in range(l):
            result[i] = products_before[i] * products_after[i]

        return result
