class Solution:

    def encode(self, strs: List[str]) -> str:
        res = str()
        for s in strs:
            res += chr(len(s)) + s
        return res

    def decode(self, s: str) -> List[str]:
        curr, l = 0, len(s)
        res = []

        while curr < l:
            str_len = ord(s[curr])
            res.append(s[curr+1:curr+str_len+1])
            curr += str_len + 1

        return res
