class Solution {
public:
    int maxArea(vector<int>& heights) {
        int area = 0;
        int l = 0, r = static_cast<int>(heights.size()) - 1;

        while (l < r) {
            area = max(area, (r - l) * min(heights[l], heights[r]));
            if (heights[l] < heights[r]) {
                ++l;
            }
            else {
                --r;
            }
        }

        return area;
    }
};
