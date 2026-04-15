class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l = 0
        maxSq = 0

        for r in range(len(s)):
            if s[r] in m:
                l = max(m[s[r]] + 1, l)
            m[s[r]] = r
            maxSq = max(maxSq, r - l + 1)

        return maxSq