class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;

        for (std::size_t i = 0; i < nums.size(); ++i) {
            if (seen.find(target - nums[i]) != seen.end()) {
                return {
                    seen[target - nums[i]],
                    static_cast<int>(i)
                };
            }

            seen[nums[i]] = static_cast<int>(i);
        }

        return {};
    }
};
