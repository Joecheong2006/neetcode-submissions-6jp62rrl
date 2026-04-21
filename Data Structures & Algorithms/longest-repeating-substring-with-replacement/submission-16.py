class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = defaultdict(int)
        maxCount = 0
        res = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            maxCount = max(maxCount, counts[s[r]])
            replaceCount = (r - l + 1) - maxCount

            while replaceCount > k:
                counts[s[l]] -= 1
                l += 1
                replaceCount = (r - l + 1) - maxCount
            res = max(r - l + 1, res)

        return res