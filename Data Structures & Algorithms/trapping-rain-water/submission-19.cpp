class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = static_cast<int>(height.size()) - 1;
        int leftMax = height[l], rightMax = height[r];

        int water = 0;
        while (l < r) {
            if (leftMax < rightMax) {
                l += 1;
                leftMax = max(leftMax, height[l]);
                water += leftMax - height[l];
            }
            else {
                r -= 1;
                rightMax = max(rightMax, height[r]);
                water += rightMax - height[r];
            }
        }

        return water;
    } 
};
