class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, maxP = 0;

        for (int r = 1; r < prices.size(); ++r) {
            if (prices[r] > prices[l]) {
                maxP = max(maxP, prices[r] - prices[l]);
            }
            else {
                l = r;
            }
        }

        return maxP;
    }
};
