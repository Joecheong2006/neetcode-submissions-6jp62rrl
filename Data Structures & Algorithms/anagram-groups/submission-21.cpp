class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> m;
        for (const auto &s : strs) {
            int count[26] = {};
            for (const auto &c : s) {
                count[c - 'a']++;
            }
            std::string key = "";
            for (const auto &e : count) {
                key += 'a' + std::to_string(e);
            }
            m[key].push_back(s);
        }

        std::vector<std::vector<std::string>> result;
        for (const auto &p : m) {
            result.push_back(p.second);
        }
        return result;
    }
};
