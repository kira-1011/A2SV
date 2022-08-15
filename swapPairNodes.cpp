/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    
private:
    
    ListNode* reverseLinkedList(ListNode* head, ListNode* tail)
    {
        
        if(head -> next == NULL || head == NULL)
            return head;
        
        ListNode* temp = head;
        
        ListNode* temp1 = temp -> next;
        
        temp -> next = tail;
        
        while(temp1 != tail)
        {
            ListNode* temp2 = temp1 -> next;
            
            temp1 -> next = temp;
            
            temp = temp1;
            
            temp1 = temp2;
        }
        
        return temp;
    }
    
public:
    ListNode* swapPairs(ListNode* head) {
        
        if(head == NULL || head -> next == NULL)
            return head;
        
        ListNode* temp = head;
        
        ListNode* tail =  head -> next -> next;
        
        ListNode* head1 = new ListNode;
        
        ListNode* temp1 = head1;
        
        ListNode* prev = temp1;
        
        int n = 0;
        
        while(temp != NULL)
        {
            n++;
            temp = temp -> next;
        }
        
        temp = head;
        
        while(1)
        {
            head = reverseLinkedList(temp, tail);
            
            temp = tail;
            
            while(head != tail)
            {
                temp1 -> val = head -> val;
            
                temp1 -> next = new ListNode;
                
                prev = temp1;

                temp1 = temp1 -> next;
                
                head = head -> next;
            }
            
            if(n % 2 == 0 && temp == NULL)
                break;
            
            if(n % 2 != 0 && temp -> next == NULL)
                break;
            
            tail = temp -> next -> next; 
        }
        
        
        
        prev -> next = temp;

        return head1;
    }
};