class MyLinkedList {
    
private:
    
    struct ListNode{
        int val;
        ListNode *next;
    };
    
    ListNode *head = NULL;
    
    
public:
    MyLinkedList() 
    {
        
    }
    
    int get(int index) {
        
        if(index >= length())
            return -1;
        
        ListNode *temp = head;
        
        for(int i = 0; i < index; i++)
        {
            temp = temp -> next;
        }
        
        return temp -> val;
    }
    
    void addAtHead(int val) {
        
        ListNode *newNode = new ListNode;
        newNode -> val = val;
        
        if(head == NULL)
        {
            head = newNode;
            newNode -> next = NULL;
            return;
        }
        
        newNode -> next = head;
        head = newNode;
    }
    
    void addAtTail(int val) 
    {
        ListNode *temp = head;
        ListNode *newNode = new ListNode;
        newNode -> val = val;
        newNode -> next = NULL;
        
        if(head == NULL)
        {
            head = newNode;
            return;
        }
        
        while(temp -> next != NULL)
        {
            temp = temp -> next;
        }
        
        
        temp -> next = newNode;
    }
    
    void addAtIndex(int index, int val) {
        
        ListNode *temp = head;
        ListNode *newNode = new ListNode;
        newNode -> val = val;
        
        if(index == length())
        {
             addAtTail(val);
            return;
        }
           
        
        if(index == 0)
        {
            addAtHead(val);
            return;
        }
        
        if(index > length())
            return;
        
        for(int i = 0; i < index - 1; i++)
        {
                
            temp = temp -> next;
        }
            
        newNode -> next = temp -> next;
        temp -> next = newNode;
        
    }
    
    void deleteAtIndex(int index) {
        
        ListNode *temp = head;
        
        if(index >= length())
            return;
        
        if(index == 0)
        {
            head = head -> next;
            return;
        }
        
        for(int i = 0; i < index - 1; i++)
        {
            temp = temp -> next;
        }
        
        ListNode *temp1 = temp -> next;
        temp -> next = temp1 -> next;
        delete temp1;
    }
    
    int length()
    {
        int length = 0;
        ListNode *temp = head;
        
        while(temp != NULL)
        {
            length++;
            temp = temp -> next;
        }

        return length ;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */