class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] - val != 0:
                nums[l] = nums[i]
                l += 1

        return l