class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> res(temperatures.size(), 0);
        std::stack<std::array<int, 2>> stk;

        for (int i = 0; i < res.size(); ++i) {
            while (!stk.empty() && stk.top()[0] < temperatures[i]) {
                int index = stk.top()[1];
                stk.pop();
                res[index] = i - index;
            }

            stk.push({ temperatures[i], i });
        }

        return res;
    }
};
