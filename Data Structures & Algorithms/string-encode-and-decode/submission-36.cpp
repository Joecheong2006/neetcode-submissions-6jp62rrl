class Solution {
public:

    string encode(vector<string>& strs) {
        string s;
        for (const auto &str : strs) {
            // Substract 100 to fit in range for char otherwise it is UB
            s.push_back(static_cast<char>(static_cast<int>(str.size()) - 100));
            cout << str.size() << ' ';
            s += str;
        }
        return s;
    }

    vector<string> decode(string s) {
        std::size_t curr = 0, l = s.size();
        vector<string> strs;

        while (curr < l) {
            int str_len = static_cast<int>(s[curr]) + 100;
            strs.push_back(s.substr(curr + 1, str_len));
            curr += str_len + 1;
        }

        return strs;
    }
};
