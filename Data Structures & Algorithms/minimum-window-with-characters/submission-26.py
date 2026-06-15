class Solution:
    def map_contained(self, m1, m2):
        for key, value in m1.items():
            if (not key in m2) or (m2[key] < value):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        tcounts = defaultdict(int)

        l = 0
        res = 10000

        ress = ""

        for c in t:
            tcounts[c] += 1

        print(tcounts)

        for r in range(len(s)):
            counts[s[r]] += 1

            print(f"{l}, {r}")
            print(counts)

            while self.map_contained(tcounts, counts):
                if r - l + 1 < res:
                    res = r - l + 1
                    ress = s[l:(l+res)]
                print(ress)
                counts[s[l]] -= 1
                l += 1

        return ress