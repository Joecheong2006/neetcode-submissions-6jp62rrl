class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l < r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                # totalTime += (p + m - 1) // m
                totalTime += math.ceil(p / m)
            
            if totalTime <= h:
                res = m
                r = m
            else:
                l = m + 1

        return res