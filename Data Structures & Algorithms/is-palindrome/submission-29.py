class Solution:
    def isPalindrome(self, s: str) -> bool:
        def nextAlphaNumIndex(start: int, increment: int):
            while not s[start].isalnum():
                start += increment
                if start < 0 or start >= len(s):
                    return start
            return start
        
        l, r = 0, len(s) - 1
        while l < r:
            l = nextAlphaNumIndex(l, 1)
            r = nextAlphaNumIndex(r, -1)
            if l >= r:
                return True
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True