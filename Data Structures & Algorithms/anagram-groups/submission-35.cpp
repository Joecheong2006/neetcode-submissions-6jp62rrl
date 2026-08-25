class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<string>> m;

        string count{};
        count.resize(26);
        for (const auto &s : strs) {
            for (const auto &c : s) {
                count[c - 'a'] += 1;
            }
            m[count].push_back(s);
            count.assign(26, 0);
        }

        std::vector<std::vector<string>> res;
        res.reserve(m.size());

        for (const auto &p : m) {
            res.push_back(std::move(p.second));
        }

        return res;
    }
};
