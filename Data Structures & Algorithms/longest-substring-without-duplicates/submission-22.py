class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        maxLen = 0

        for r in range(len(s)):
            while s[r] in stringSet:
                beginChar = s[r - len(stringSet)]
                stringSet.remove(beginChar)
            stringSet.add(s[r])
            maxLen = max(maxLen, len(stringSet))

        return maxLen
