import java.util.Stack;

class MyQueue {
    private Stack<Integer> s1;
    private Stack<Integer> s2;

    public MyQueue() {
        this.s1 = new Stack<Integer>();
        this.s2 = new Stack<Integer>();
    }
    
    public void push(int x) {
        this.s1.push(x);
    }
    
    public int pop() {
        // Move everything from s1 to s2.
        while (!this.s1.isEmpty())
        {
            this.s2.push(this.s1.pop());
        }
        // Top element in s2 is the first element we pushed into s1.
        int result = this.s2.pop(); 
        // Move everything in s2 back to s1.
        while (!this.s2.isEmpty())
        {
            this.s1.push(this.s2.pop());
        }
        return result;
    }
    
    public int peek() {
        // Move everything from s1 to s2.
        while (!this.s1.isEmpty())
        {
            this.s2.push(this.s1.pop());
        }
        // Top element in s2 is the first element we pushed into s1.
        int result = this.s2.peek(); 
        // Move everything in s2 back to s1.
        while (!this.s2.isEmpty())
        {
            this.s1.push(this.s2.pop());
        }
        return result;
    }
    
    public boolean empty() {
        return this.s1.empty();
    }
}