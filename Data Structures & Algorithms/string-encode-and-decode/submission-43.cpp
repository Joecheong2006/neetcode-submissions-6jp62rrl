class Solution {
public:

    string encode(vector<string>& strs) {
        std::string encodedStr;
        for (const auto &s : strs) {
            encodedStr.push_back(
                static_cast<unsigned char>(s.size())
            );
            encodedStr += s;
        }
        return encodedStr;
    }

    vector<string> decode(string s) {
        std::vector<std::string> decodedStrs;
        std::size_t i = 0;
        while (i < s.size()) {
            const unsigned char encodedStrLen = static_cast<unsigned char>(s[i]);
            int strLen = static_cast<int>(encodedStrLen);
            i += 1;
            decodedStrs.push_back(
                s.substr(i, strLen)
            );
            i += strLen;
        }

        return decodedStrs;
    }
};
