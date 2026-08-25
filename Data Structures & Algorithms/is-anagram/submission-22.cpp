class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
            
        std::array<int, 26> count;

        for (auto i = 0; i < s.size(); ++i) {
            count[s[i] - 'a'] += 1;
            count[t[i] - 'a'] -= 1;
        }

        for (auto &num : count) {
            if (num != 0) {
                return false;
            }
        }
        
        return true;
    }
};
