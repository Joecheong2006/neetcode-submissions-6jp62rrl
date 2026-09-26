class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mp = defaultdict(int)
        l = 0

        for s in s1:
            mp[s] += 1
        
        for r in range(len(s2)):
            if not s2[r] in mp:
                while l < r:
                    mp[s2[l]] += 1
                    l += 1
                l = r + 1
                continue

            mp[s2[r]] -= 1
            if mp[s2[r]] < 0 or r - l + 1 > len(s1):
                mp[s2[l]] += 1
                l += 1

            res = True
            for count in mp.values():
                if count != 0:
                    res = False
            if res:
                return res

                    
        return False
