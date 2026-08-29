class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []

        for i in range(l):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, l - 1
            while left < right:
                s = nums[left] + nums[right]
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    res.append([nums[left], nums[right], -target])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res
