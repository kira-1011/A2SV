class MyQueue {

private:
    
    struct ListNode{
        int val;
        
        ListNode *next;
    };
    
    ListNode *head;
    ListNode *temp;
    
    void initialize()
    {
        head = new ListNode;
        temp = head;
        temp -> val = 0;
    }

public:
    MyQueue() 
    {
        initialize();    
    }
    
    void push(int x) 
    {    
        temp -> val = x;
        temp -> next = new ListNode;
        temp = temp -> next;
        temp -> val = 0;
    }
    
    int pop() 
    {
        int val = head -> val;
        head = head -> next;
        return val;
    }
    
    int peek()
    {
        return head -> val;
    }
    
    bool empty() 
    {
        cout << head -> val << endl;
        return (head -> val == 0);
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