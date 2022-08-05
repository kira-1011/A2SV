class Solution {

private:
    
    struct ListNode{
        int val;
        ListNode *next;
    };
    
public:
    int findTheWinner(int n, int k) {
        
        int length = n;
        ListNode *head = new ListNode;
        ListNode *current = head;
        ListNode *prev = current;
        
        for(int i = 1; i <= n; i++)
        {
            current -> val = i;
            prev = current;
            current -> next = new ListNode;
            current = current -> next;
        }
        
        prev -> next = NULL;
        prev -> next = head;        
        current = head;
        prev = head;
        int c = 1;
        
    
        
        while(length > 1)
        {
            while(c < k)
            {
                prev = current;
                current = current -> next;
                c++;
            }
            
            c = 1;
            prev -> next = current -> next;
            current = prev -> next;
            length--;
        }
        

        
        return current -> val;
        
    }
};