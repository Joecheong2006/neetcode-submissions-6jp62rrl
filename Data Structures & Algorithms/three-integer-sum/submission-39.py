class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)

        result = []

        for i in range(l):
            if nums[i] > 0:
                break
            sumOfTwo = -nums[i]
            lhs, rhs = i + 1, l - 1
            while lhs < rhs:
                cmpSum = nums[lhs] + nums[rhs]
                if cmpSum < sumOfTwo:
                    lhs += 1
                elif cmpSum > sumOfTwo:
                    rhs -= 1
                else:
                    if [nums[i], nums[lhs], nums[rhs]] not in result:
                        result.append([nums[i], nums[lhs], nums[rhs]])
                    rhs -= 1
                    lhs += 1

        return result
