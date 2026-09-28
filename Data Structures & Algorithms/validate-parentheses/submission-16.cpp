class Solution {
public:
    bool isValid(string s) {
        std::stack<int> stk;
        std::unordered_map<char, char> mp;
        mp[')'] = '(';
        mp[']'] = '[';
        mp['}'] = '{';

        for (auto c : s) {
            if (mp.find(c) != mp.end()) {
                if (stk.empty()) {
                    return false;
                }

                int top = stk.top();
                if (top == mp[c]) {
                    stk.pop();
                }
                else {
                    return false;
                }
            }
            else {
                stk.push(c);
            }
        }

        if (!stk.empty()) {
            return false;
        }
        return true;
    }
};
