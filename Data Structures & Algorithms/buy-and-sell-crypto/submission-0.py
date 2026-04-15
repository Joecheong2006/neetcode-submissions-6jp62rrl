class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minSofar = 1000

        for p in prices:
            minSofar = min(minSofar, p)
            maxProf = max(maxProf, p - minSofar)

        return maxProf
