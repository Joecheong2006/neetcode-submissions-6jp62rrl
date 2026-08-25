class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        auto l = nums.size();
        unordered_map<int, int> count;
        vector<vector<int>> freq(l);

        vector<int> res;
        res.reserve(k);

        for (const auto &num : nums) {
            count[num] += 1;
        }

        for (const auto &[num, f] : count) {
            freq[l - f].push_back(num);
        }

        for (const auto &items : freq) {
            for (auto num : items) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }

        return res;
    }
};
