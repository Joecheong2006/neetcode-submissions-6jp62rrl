class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Map using lowercase English letters offseted by 'a'
        arr = [0] * 26

        for i in range(len(s)):
            arr[ord(s[i]) - 97] += 1;
            arr[ord(t[i]) - 97] -= 1;

        for n in arr:
            if n != 0:
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        m = {} # Map from str len to group position

        for i, s in enumerate(strs):
            l = len(s);
            if l not in m:
                m[l] = len(group)
                group.append([s])
                continue

            strIndex = m[l]
            group[strIndex].append(s)

        for anagrams in group:
            firstStr = anagrams[0];
            i = 1
            firstTime = True
            while i < len(anagrams):
                if not self.isAnagram(firstStr, anagrams[i]):
                    if firstTime:
                        group.append([anagrams[i]]);
                        firstTime = False
                    else:
                        group[-1].append(anagrams[i])
                    anagrams.remove(anagrams[i])
                else:
                    i += 1

        return group