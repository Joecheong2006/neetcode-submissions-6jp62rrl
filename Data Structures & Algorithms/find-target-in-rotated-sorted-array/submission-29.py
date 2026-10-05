class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                # Move left to mid + 1:
                # If target is on the left portion then we
                # check nums[m] < target.
                # If target is on the right portion then we
                # check nums[l] > target.
                # Move right to mid - 1 otherwise.
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # Move right to mid - 1:
                # If target is on the right portion then we
                # check nums[m] > target.
                # If target is on the left portion then we
                # check nums[r] < target.
                # Move left to mid + 1 otherwise.
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1


        return -1
