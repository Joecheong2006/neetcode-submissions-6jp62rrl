class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[r] > nums[m]:
                r = m
            else:
                l = m + 1
        minIndex = r
        l, r = 0, len(nums) - 1

        if target >= nums[minIndex] and target <= nums[r]:
            l = minIndex
        else:
            r = minIndex - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1