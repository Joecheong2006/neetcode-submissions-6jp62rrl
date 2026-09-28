class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for c in s:
            if not c in mp:
                stack.append(c)
            else:
                if stack and stack[-1] == mp[c]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True