class Solution {
public:

    string encode(vector<string>& strs) {
        string s;
        for (const auto &str : strs) {
            s.push_back(static_cast<char>(static_cast<int>(str.size()) - 100));
            cout << str.size() << ' ';
            s += str;
        }
        cout << "end\n";
        return s;
    }

    vector<string> decode(string s) {
        std::size_t curr = 0, l = s.size();
        vector<string> strs;

        while (curr < l) {
            int str_len = static_cast<int>(s[curr]) + 100;
            cout << str_len << ' ';
            auto str = s.substr(curr + 1, str_len);
            strs.push_back(std::move(str));
            curr += str_len + 1;
        }

        return strs;
    }
};
