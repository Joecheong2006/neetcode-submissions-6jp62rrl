class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        maxLen = 0

        for r in range(len(s)):
            while s[r] in stringSet:
                stringSet.remove(s[r - len(stringSet)])
            stringSet.add(s[r])
            maxLen = max(maxLen, len(stringSet))

        return maxLen
