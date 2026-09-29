class MinStack {
    std::stack<std::int64_t> stk{};
    int minVal{};
public:
    MinStack() {}
    
    void push(int val) {
        if (stk.empty()) {
            stk.push(0);
            minVal = val;
        }
        else {
            stk.push(static_cast<int64_t>(val) - minVal);
            minVal = min(minVal, val);
        }
    }
    
    void pop() {
        if (stk.empty()) {
            return;
        }
        std::int64_t diff = stk.top();
        stk.pop();
        if (diff < 0) {
            minVal -= diff;
        }
    }
    
    int top() {
        std::int64_t diff = stk.top();
        if (diff < 0) {
            return minVal;
        }
        else {
            return diff + minVal;
        }
    }
    
    int getMin() {
        return minVal;
    }
};
