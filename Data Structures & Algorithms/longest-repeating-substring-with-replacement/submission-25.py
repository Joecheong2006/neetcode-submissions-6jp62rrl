class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = [0] * 26
        # we need to find the max number in mp and that
        # char will be our target uppercase English then
        # we can now unrder this window how many replacements
        # are needed and check update the max len if the number
        # of replacements are less than or euqal to k.
        # We need a l tp indicate the left of the window, and
        # update it accordingly if the window is invalid, which
        # the replacementCount is <= k.

        maxLen = 0
        maxChar = 0
        l = 0
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            mp[idx] += 1
            maxChar = max(maxChar, mp[idx])
            while (r - l + 1) - maxChar > k:
                mp[ord(s[l]) - ord('A')] -= 1
                l += 1
                maxChar = max(mp)
            maxLen = max(maxLen, r - l + 1)

        return maxLen
