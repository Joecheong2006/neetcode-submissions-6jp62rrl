class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minSofar = prices[0]

        for p in prices:
            minSofar = min(minSofar, p)
            maxProf = max(maxProf, p - minSofar)

        return maxProf
