class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        maxCur = 0

        res = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            maxCur = max(maxCur, counts[s[r]])
            windowSize = r - l + 1
            replacementCount = windowSize - maxCur

            while replacementCount > k:
                counts[s[l]] -= 1
                l += 1
                for _, value in counts.items():
                    maxCur = max(maxCur, value)
                windowSize = r - l + 1
                replacementCount = windowSize - maxCur

            res = max(windowSize, res)

        return res
