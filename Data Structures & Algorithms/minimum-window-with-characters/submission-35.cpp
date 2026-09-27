class Solution {
public:
    string minWindow(string s, string t) {
        if (s.size() < t.size())
            return "";

        std::unordered_map<char, int> tCount, sCount;

        for (auto c : t) {
            tCount[c] += 1;
            sCount[c] = 0;
        }

        int have = 0;
        int l = 0, minL = 0, minLen = std::numeric_limits<int>::max();
        for (int r = 0; r < s.size(); ++r) {
            if (tCount.find(s[r]) == tCount.end())
                continue;

            sCount[s[r]] += 1;
            if (sCount[s[r]] == tCount[s[r]])
                have += 1;
            
            while (have == tCount.size()) {
                if (tCount.find(s[l]) == tCount.end()) {
                    l += 1;
                    continue;
                }
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1;
                    minL = l;
                }

                sCount[s[l]] -= 1;
                if (sCount[s[l]] < tCount[s[l]]) {
                    have -= 1;
                }

                l += 1;
            }
        }

        if (minLen == std::numeric_limits<int>::max())
            return "";
        return s.substr(minL, minLen);
    }
};
