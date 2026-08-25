class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1 for _ in nums]
        subfixProduct = [1 for _ in nums]

        l = len(nums)

        for i in range(1, l):
            prefixProduct[i] *= nums[i - 1] * prefixProduct[i - 1]

        for i in range(l - 2, -1, -1):
            subfixProduct[i] *= nums[i + 1] * subfixProduct[i + 1]

        for i in range(l):
            prefixProduct[i] *= subfixProduct[i]
        
        return prefixProduct