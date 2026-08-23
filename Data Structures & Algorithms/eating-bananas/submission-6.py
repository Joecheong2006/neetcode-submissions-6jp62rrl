class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            count = 0

            k = l + (r - l) // 2
            for pile in piles:
                count += math.ceil(pile / k)
            
            if count > h:
                l = k + 1
            else:
                r = k

        return r
