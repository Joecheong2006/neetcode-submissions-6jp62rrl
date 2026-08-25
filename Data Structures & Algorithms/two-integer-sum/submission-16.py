class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        seen[nums[0]] = 0

        for i in range(1, len(nums)):
            addend = target - nums[i]
            if addend in seen:
                return [seen[addend], i]
            
            seen[nums[i]] = i
        
        return []