class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::size_t l = nums.size();
        std::vector<int> res(l, 1);

        int productBefore = 1;
        for (std::size_t i = 0; i < l; ++i) {
            res[i] = productBefore;
            productBefore *= nums[i];
        }

        int productAfter = 1;
        for (std::size_t i = 0; i < l; ++i) {
            res[l - i - 1] *= productAfter;
            productAfter *= nums[l - i - 1];
        }

        return res;
    }
};
