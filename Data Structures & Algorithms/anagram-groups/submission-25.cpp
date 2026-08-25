class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<string>> m;

        for (const auto &s : strs) {
            string count;
            count.resize(26);
            for (const auto &c : s) {
                count[c - 'a'] += 1;
            }
            m[count].push_back(s);
        }

        std::vector<std::vector<string>> res;
        res.reserve(m.size());

        for (const auto &[_, items] : m) {
            res.push_back(items);
        }

        return res;
    }
};
