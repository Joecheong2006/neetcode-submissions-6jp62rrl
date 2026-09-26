class Solution {
public:
    int characterReplacement(string s, int k) {
        std::array<int, 26> mp{};
        int maxLen = 0, l = 0;
        int maxChar = 0;

        for (int r = 0; r < s.size(); ++r) {
            mp[s[r] - 'A'] += 1;
            maxChar = max(maxChar, mp[s[r] - 'A']);
            if (r - l + 1 - maxChar > k) {
                mp[s[l++] - 'A'] -= 1;
            }

            maxLen = max(maxLen, r - l + 1);
        }

        return maxLen;
    }
};
