class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> count;
        std::vector<std::vector<int>> freq;
        freq.resize(nums.size());
        int len = freq.size();

        for (const auto &num : nums) {
            count[num] += 1;
        }

        for (const auto &[num, f] : count) {
            freq[len - f].push_back(num);
        }

        std::vector<int> res;
        for (const auto &items : freq) {
            for (const auto &item : items) {
                res.push_back(item);
                if (res.size() == k) {
                    return res;
                }
            }
        }

        return res;
    }
};
