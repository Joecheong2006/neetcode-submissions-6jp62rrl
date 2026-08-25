class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1 for _ in nums]
        subfixProduct = [1 for _ in nums]

        l = len(nums)

        for i in range(1, l):
            prefixProduct[i] *= nums[i - 1] * prefixProduct[i - 1]
            subfixProduct[l - i - 1] *= nums[l - i] * subfixProduct[l - i]

        for i in range(l):
            prefixProduct[i] *= subfixProduct[i]
        
        return prefixProduct