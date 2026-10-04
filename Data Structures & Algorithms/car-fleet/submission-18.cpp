class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        std::vector<float> stk;
        std::vector<std::pair<int, int>> pairs;

        int len = position.size();
        pairs.reserve(len);
        for (int i = 0; i < len; ++i) {
            pairs.emplace_back(position[i], speed[i]);
        }

        std::sort(pairs.begin(), pairs.end(), [](const auto &p1, const auto &p2) {
            return p1.first > p2.first;
        });

        for (const auto &[p, s] : pairs) {
            stk.push_back(float(target - p) / s);
            int size = stk.size();
            if (size > 1 && stk[size - 1] <= stk[size - 2]) {
                stk.pop_back();
            }
        }

        return stk.size();
    }
};
