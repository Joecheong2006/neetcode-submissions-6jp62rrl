class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)

        while l < len(nums) - 1:
            if nums[l] == nums[l + 1]:
                nums.pop(l)
                print(nums)
                n -= 1
            else:
                l += 1
        return n