class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabitCount = [0] * 26

        for i in range(len(s)):
            sIndex = ord(s[i]) - ord('a')
            tIndex = ord(t[i]) - ord('a')
            alphabitCount[sIndex] += 1
            alphabitCount[tIndex] -= 1

        for count in alphabitCount:
            if count != 0:
                return False
        return True