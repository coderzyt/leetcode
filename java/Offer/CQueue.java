package Offer;

import java.util.Collection;
import java.util.Iterator;
import java.util.Queue;
import java.util.Stack;

class CQueue implements Queue {

    private Stack<Integer> stack1;

    private Stack<Integer> stack2;

    public CQueue() {
        this.stack1 = new Stack<>();
        this.stack2 = new Stack<>();
    }

    public void appendTail(int value) {
        stack2.push(value);
    }

    public int deleteHead() {
        if (stack1.isEmpty()) {
            while (!stack2.isEmpty()) {
                stack1.push(stack2.pop());
            }
        }
        if (stack1.isEmpty()) {
            return -1;
        } else {
            return stack1.pop();
        }
    }
}
