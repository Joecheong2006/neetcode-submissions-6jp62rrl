class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case
        if len(s) != len(t):
            return False

        # Map using lowercase English letters offseted by 'a'
        arr = [0] * 26

        for i in range(len(s)):
            arr[ord(s[i]) - 97] += 1;
            arr[ord(t[i]) - 97] -= 1;

        for n in arr:
            if n != 0:
                return False

        return True
        