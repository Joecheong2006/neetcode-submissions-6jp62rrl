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
        if zeros == 1:
            for num in nums:
                if num == 0:
                    result.append(products)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(products // num)
        return result