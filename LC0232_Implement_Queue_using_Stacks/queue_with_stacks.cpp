#include <stack>
using namespace std;

class MyQueue {
private:
    stack<int>* s1;
    stack<int>* s2;
public:
    MyQueue() {
        s1 = new stack<int>;
        s2 = new stack<int>;
    }

    ~MyQueue() {
        delete s1;  
        delete s2;  
    }
    
    void push(int x) {
        s1->push(x);
    }
    
    int pop() {
        // Move everything from s1 to s2.
        int temp;
        while (!s1->empty())
        {
            temp = s1->top();
            s2->push(temp);
            s1->pop();
        }
        int result = s2->top();
        s2->pop();
        // Move everything from s2 back to s1.
        while (!s2->empty())
        {
            temp = s2->top();
            s1->push(temp);
            s2->pop();
        }
        return result;
    }
    
    int peek() {
        // Move everything from s1 to s2.
        int temp;
        while (!s1->empty())
        {
            temp = s1->top();
            s2->push(temp);
            s1->pop();
        }
        int result = s2->top();

        // Move everything from s2 back to s1.
        while (!s2->empty())
        {
            temp = s2->top();
            s1->push(temp);
            s2->pop();
        }
        return result;
    }
    
    bool empty() {
        return s1->empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */