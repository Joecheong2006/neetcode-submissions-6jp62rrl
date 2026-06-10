class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        maxF = 0
        res = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            maxF = max(counts[s[r]], maxF)

            windowSize = r - l + 1
            while windowSize - maxF > k:
                counts[s[l]] -= 1
                l += 1
                windowSize -= 1
            
            res = max(windowSize, res)

        return res