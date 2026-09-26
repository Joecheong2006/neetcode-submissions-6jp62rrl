class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, maxLen = 0;
        std::unordered_map<int, int> mp;

        for (int r = 0; r < s.size(); ++r) {
            // Making sure to filter out the old 
            // characters outside of the window.
            if (mp.find(s[r]) != mp.end() && mp[s[r]] >= l) {
                l = mp[s[r]] + 1;
            }
            mp[s[r]] = r;
            maxLen = max(maxLen, r - l + 1);
        }

        return maxLen;
    }
};
