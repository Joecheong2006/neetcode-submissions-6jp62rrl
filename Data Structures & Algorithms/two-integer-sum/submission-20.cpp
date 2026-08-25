class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen{};
        seen[nums[0]] = 0;

        for (auto i = 1; i < nums.size(); ++i) {
            int addend = target - nums[i];
            if (seen.find(addend) != seen.end()) {
                return { seen[addend], i };
            }
            seen[nums[i]] = i;
        }

        return {};
    }
};
