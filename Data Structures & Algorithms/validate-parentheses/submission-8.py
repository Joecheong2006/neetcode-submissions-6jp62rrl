class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        m = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stk = []

        for c in s:
            if c in m:
                if len(stk) > 0 and stk[-1] == m[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return len(stk) == 0

