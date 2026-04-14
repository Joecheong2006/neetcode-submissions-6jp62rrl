class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i

        for i in range(len(nums)):
            n = target - nums[i]
            if n in m and m[n] != i:
                return [ i, m[n] ]
        return []