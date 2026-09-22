class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += chr(len(s)) + s
            print(len(s))
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        l = len(s)

        while i < l:
            wordLen = ord(s[i])
            i += 1
            strs.append(s[i:i+wordLen])
            i += wordLen

        return strs
