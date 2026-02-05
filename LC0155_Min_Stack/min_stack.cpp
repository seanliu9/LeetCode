#include <limits>
#include <stack>
#include <unordered_map>

using namespace std;

class MinStack {
private:
    stack<int> stk;
    unordered_map<int, int> min_at_level;
    int curr_level;
public:
    MinStack() {
        this->curr_level = -1;
    }
    
    void push(int val) {
        stk.push(val);
        this->curr_level += 1;
        if (this->curr_level == 0)
        {
            this->min_at_level[curr_level] = val;
        }
        else
        {
            this->min_at_level[curr_level] = min(val, this->min_at_level[curr_level - 1]);
        }
    }
    
    void pop() {
        stk.pop();
        this->curr_level -= 1;
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return this->min_at_level[this->curr_level];
    }
};