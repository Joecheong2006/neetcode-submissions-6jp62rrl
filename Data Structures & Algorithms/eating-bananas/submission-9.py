class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            count = 0

            k = l + (r - l) // 2
            for pile in piles:
                count += math.ceil(float(pile) / k)
            
            if count > h:
                # Since k have failed which means [1, k) also failed,
                # thus we set l to k + 1 for a better guess
                l = k + 1
            else:
                # We set r to k since k - 1 may fail which implies r always success
                r = k

        # Return the case always success
        return r
