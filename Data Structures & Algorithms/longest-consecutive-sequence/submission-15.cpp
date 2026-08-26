class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> seen(nums.begin(), nums.end());

        int longest = 0;
        for (const auto &num : seen) {
            if (seen.find(num - 1) == seen.end()) {
                int len = 0;
                while (seen.find(num + ++len) != seen.end());
                longest = max(longest, len);
            }
        }

        return longest;
    }
};
