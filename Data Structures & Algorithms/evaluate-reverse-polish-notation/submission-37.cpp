class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> stk;

        for (const auto &token : tokens) {
            if (token == "+") {
                int rhs = stk.top(); stk.pop();
                int lhs = stk.top(); stk.pop();
                stk.push(lhs + rhs);
            }
            else if (token == "-") {
                int rhs = stk.top(); stk.pop();
                int lhs = stk.top(); stk.pop();
                stk.push(lhs - rhs);
            }
            else if (token == "*") {
                int rhs = stk.top(); stk.pop();
                int lhs = stk.top(); stk.pop();
                stk.push(lhs * rhs);
            }
            else if (token == "/") {
                int rhs = stk.top(); stk.pop();
                int lhs = stk.top(); stk.pop();
                stk.push(int(lhs / rhs));
            }
            else {
                stk.push(std::stoi(token));
            }
        }

        return stk.top();
    }
};
