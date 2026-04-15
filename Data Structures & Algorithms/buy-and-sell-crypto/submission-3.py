class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minSofar = prices[0]

        for p in prices:
            maxProf = max(maxProf, p - minSofar)
            minSofar = min(minSofar, p)

        return maxProf
