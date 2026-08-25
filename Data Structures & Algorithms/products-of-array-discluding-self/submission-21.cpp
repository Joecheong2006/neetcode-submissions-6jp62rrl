class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int l = static_cast<int>(nums.size());
        vector<int> res(l, 1);

        int prefixProduct = 1, subfixProduct = 1;
        for (int i = 0; i < l; ++i) {
            res[i] *= prefixProduct;
            prefixProduct *= nums[i];

            res[l - i - 1] *= subfixProduct;
            subfixProduct *= nums[l - i - 1];
        }

        return res;
    }
};
