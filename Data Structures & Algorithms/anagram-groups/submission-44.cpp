class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;

        string count{};
        count.resize(26);
        for (const auto &s : strs) {
            for (const auto &c : s) {
                count[c - 'a'] += 1;
            }
            m[count].push_back(s);
            count.assign(26, 0);
        }

        vector<vector<string>> res;
        res.reserve(m.size());

        for (auto &p : m) {
            res.push_back(move(p.second));
        }

        return res;
    }
};
