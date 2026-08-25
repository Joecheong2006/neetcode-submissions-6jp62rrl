class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        l = len(nums)

        prefixProduct, subfixProduct = 1, 1
        for i in range(l):
            res[i] *= prefixProduct
            prefixProduct *= nums[i]

            res[l - i - 1] *= subfixProduct
            subfixProduct *= nums[l - i - 1]
        
        return res