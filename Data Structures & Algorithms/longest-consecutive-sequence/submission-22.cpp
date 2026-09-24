class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> seen(nums.begin(), nums.end());
        int longest = 0;

        for (auto num : nums) {
            if (seen.find(num - 1) != seen.end()) {
                continue;
            }

            int length = 1;
            while (seen.find(num + length) != seen.end()) {
                ++length;
            }
            longest = max(longest, length);
        }

        return longest;
    }
};
