class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tCount = defaultdict(int)
        sCount = defaultdict(int)

        for c in t:
            tCount[c] += 1
            sCount[c] = 0
        
        l = 0
        have = 0
        minL = 0
        minLen = float("inf")

        for r in range(len(s)):
            if not s[r] in tCount:
                continue

            sCount[s[r]] += 1
            if sCount[s[r]] == tCount[s[r]]:
                have += 1

            while have == len(tCount):
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    minL = l
                if s[l] in tCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                l += 1
            
        if minLen == float("inf"):
            return ""
        return s[minL:minL+minLen]
