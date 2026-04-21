class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            nums[i] -= val

        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l] = nums[i] + val
                l += 1

        return l