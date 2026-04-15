class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                seen_window.remove(nums[l])
                l += 1
            if nums[r] in seen_window:
                return True
            seen_window.add(nums[r])

        return False
