class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::array<int, 26> alphabitCount{0};

        constexpr int alphabitOffset = static_cast<int>('a');

        for (std::size_t i = 0; i < s.size(); ++i) {
            int sIndex = static_cast<int>(s[i]) - alphabitOffset;
            int tIndex = static_cast<int>(t[i]) - alphabitOffset;
            alphabitCount[sIndex] += 1;
            alphabitCount[tIndex] -= 1;
        }

        for (const auto &count : alphabitCount) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
};
