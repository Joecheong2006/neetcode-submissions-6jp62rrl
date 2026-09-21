class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> group;
        std::vector<std::vector<std::string>> res;

        for (const auto &s : strs) {
            std::string alphabitCount(26, '\0');
            for (const auto &c : s) {
                alphabitCount[c - 'a'] += 1;
            }
            group[alphabitCount].push_back(s);
        }

        for (const auto &[_, anagrams] : group) {
            res.push_back(anagrams);
        }

        return res;
    }
};
