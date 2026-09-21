class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            alphabitCount = [0] * 26
            for c in s:
                alphabitCount[ord(c) - ord('a')] += 1
            group[tuple(alphabitCount)].append(s)
        
        res = []
        for value in group.values():
            res.append(value)
        return res
