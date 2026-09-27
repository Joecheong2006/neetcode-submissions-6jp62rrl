class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size())
            return false;

        int s1Count[26] = {};
        int s2Count[26] = {};

        for (int i = 0; i < s1.size(); ++i) {
            s1Count[s1[i] - 'a'] += 1;
            s2Count[s2[i] - 'a'] += 1;
        }

        int matches = 0;
        for (int i = 0; i < 26; ++i) {
            if (s2Count[i] == s1Count[i]) {
                matches += 1;
            }
        }

        for (int r = s1.size(); r < s2.size(); ++r) {
            if (matches == 26)
                return true;

            int leftIdx = s2[r - s1.size()] - 'a';
            s2Count[leftIdx] -= 1;
            if (s2Count[leftIdx] == s1Count[leftIdx]) {
                matches += 1;
            }
            else if (s2Count[leftIdx] + 1 == s1Count[leftIdx]) {
                matches -= 1;
            }
            
            int rightIdx = s2[r] - 'a';
            s2Count[rightIdx] += 1;
            if (s2Count[rightIdx] == s1Count[rightIdx]) {
                matches += 1;
            }
            else if (s2Count[rightIdx] - 1 == s1Count[rightIdx]) {
                matches -= 1;
            }
        }

        return matches == 26;
    }
};
