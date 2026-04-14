class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            str_len = len(s)
            encoded_str+= chr(str_len) + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            str_len = ord(s[i])
            i += 1
            extract = s[ i : i + str_len ]
            decoded_str.append(extract)
            i += str_len
        
        return decoded_str
