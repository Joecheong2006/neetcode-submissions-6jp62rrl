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
                if len(stk) == 0:
                    return False
                e = stk.pop()
                if m[c] != e:
                    return False
            else:
                stk.append(c)

        return len(stk) == 0

