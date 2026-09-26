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

        mpOffset = ord('A')
        maxLen = 0
        maxChar = 0
        l = 0

        # It is fine to use if since we only increment 1 for
        # each steps. Also, we don't need to update the maxChar
        # in the correction block since the code under it doesn't
        # require the most updated maxChar and also due to the fact
        # that the correction block only occur once.
        for r in range(len(s)):
            mp[ord(s[r]) - mpOffset] += 1
            maxChar = max(maxChar, mp[ord(s[r]) - mpOffset])
            if (r - l + 1) - maxChar > k:
                mp[ord(s[l]) - mpOffset] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)

        return maxLen
