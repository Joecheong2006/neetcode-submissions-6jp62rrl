class Solution {
public:
    int trap(vector<int>& height) {
        int len = static_cast<int>(height.size());
        std::vector<int> prefix(len), suffix(len);

        suffix[len - 1] = height[len - 1];
        for (int i = len - 2; i > -1; --i) {
            suffix[i] = max(suffix[i + 1], height[i]);
        }

        int water = 0;
        prefix[0] = height[0];
        for (int i = 1; i < len; ++i) {
            prefix[i] = max(prefix[i - 1], height[i]);
            water += min(prefix[i], suffix[i]) - height[i];
        }

        return water;
    } 
};
