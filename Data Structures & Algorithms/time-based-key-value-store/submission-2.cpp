class TimeMap {
    std::unordered_map<std::string,
           std::vector<std::pair<int, std::string>>> mp;
public:
    void set(string key, string value, int timestamp) {
        mp[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        std::string res = "";
        const auto &values = mp[key];

        int l = 0, r = static_cast<int>(values.size()) - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (values[m].first <= timestamp) {
                res = values[m].second;
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }

        return res;
    }
};
