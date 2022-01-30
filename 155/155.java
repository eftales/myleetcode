class MinStack {
    Deque<Integer> xStack;
    Deque<Integer> minStack;
    public MinStack() {
        xStack = new LinkedList<Integer>();
        minStack = new LinkedList<Integer>();
        minStack.push(Integer.MAX_VALUE);

    }

    public void push(int val) {
        xStack.push(val);
        if(val<minStack.peek()){
            minStack.push(val);
        }
        else{
            minStack.push(minStack.peek());
        }
    }

    public void pop() {
        xStack.pop();
        minStack.pop();
    }

    public int top() {
        return xStack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}