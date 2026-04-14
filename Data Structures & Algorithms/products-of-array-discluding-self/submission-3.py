class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        products = 1

        for num in nums:
            if num == 0:
                zeros += 1
                if zeros > 1:
                    return [0] * len(nums)
            else:
                products *= num

        result = []
        for num in nums:
            if zeros == 1:
                result.append(products if num == 0 else 0)
            else:
                result.append(products // num)
        return result