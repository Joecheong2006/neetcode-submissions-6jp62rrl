class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            while l < r and m[s[r]] > 0:
                m[s[l]] -= 1
                l += 1
            m[s[r]] += 1
            res = max(res, r - l + 1)

        return res