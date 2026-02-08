#include <stack>
using namespace std;

class MinStack {
private:
    stack<int> reg_stk;
    stack<int> min_stk;
public:
    MinStack() {
    }
    
    void push(int val) {
        this->reg_stk.push(val);
        if (this->min_stk.empty())
        {
            this->min_stk.push(val);
        }
        else
        {
            this->min_stk.push(min(val, this->min_stk.top()));
        }
    }
    
    void pop() {
        this->reg_stk.pop();
        this->min_stk.pop();
    }
    
    int top() {
        return this->reg_stk.top();
    }
    
    int getMin() {
        return this->min_stk.top();
    }
};