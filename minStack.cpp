class MinStack
{
private:
    // Create a node for a linked list holding the minimum numbers

    struct minimum
    {
        int num;

        minimum *next;
    };

    // Create two pointers pointing to the node holdinh the current minimum number
    // and prevMin holding the previous minimum number to the linked list
    // of minimum numbers

    minimum *min = new minimum;
    minimum *prevMin = min;

    // Create a stack
    vector<int> stack;

    // Method for updating the current minimum
    // and the previous minimum number
    void updateMin(int val)
    {

        // If stack is initially empty set min
        // and prevMin to the top value in the stack
        if (stack.size() == 0)
        {
            min->num = val;
            prevMin->num = val;
            min->next = NULL;
        }

        // If the new pushed number is less than
        // the current minimum number
        // update min and prevMin
        else if (min->num >= val)
        {

            prevMin = min;
            min = new minimum;
            min->num = val;
            min->next = prevMin;
        }
    }

public:
    MinStack()
    {
    }

    // Method for pushing element into the stack
    // And update the minimum number before pushing
    void push(int val)
    {

        updateMin(val);

        stack.push_back(val);
    }

    void pop()
    {

        if (top() == min->num && min->next != NULL)
        {

            minimum *temp = min;
            min = prevMin;
            delete temp;

            if (prevMin->next != NULL)
                prevMin = prevMin->next;
        }

        stack.pop_back();
    }

    int top()
    {

        int top = stack.back();

        return top;
    }

    int getMin()
    {
        return min->num;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */