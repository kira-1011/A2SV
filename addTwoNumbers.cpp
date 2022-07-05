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
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode *temp1 = l1;
        ListNode *temp2 = l2;
        ListNode *l3 = new ListNode;
        ListNode *temp3 = l3;
        ListNode *prev = NULL;
        
        int carry = 0;
        
        while(temp1 != NULL && temp2 != NULL){
            
            int sum = temp1 -> val + temp2 -> val + carry;
            
            if(sum >= 10)
            {
                int last = sum % 10;
                temp3 -> val = last;
                carry = 1;
                
            }
            
            else{
                temp3 -> val = sum;
                carry = 0;
            }
                
            
            temp3 -> next = new ListNode;
            prev = temp3;
            temp3 = temp3 -> next; 
            temp2 = temp2 -> next; 
            temp1 = temp1 -> next; 
        }
        
        while(temp1 != NULL)
        {
            int sum = temp1 -> val + carry;
            
            if(sum >= 10)
            {
                int last = sum % 10;
                temp3 -> val = last;
                carry = 1;
                
            }
            
            else{
                temp3 -> val = sum;
                carry = 0;
            }
            
            temp3 -> next = new ListNode;
            prev = temp3;
            temp3 = temp3 -> next; 
            temp1 = temp1 -> next; 
        }
        
        while(temp2 != NULL)
        {
            int sum = temp2 -> val + carry;
            
            if(sum >= 10)
            {
                int last = sum % 10;
                temp3 -> val = last;
                carry = 1;
                
            }
            
            else{
                temp3 -> val = sum;
                carry = 0;
            }
            
            temp3 -> next = new ListNode;
            prev = temp3;
            temp3 = temp3 -> next; 
            temp2 = temp2 -> next; 
        }
        
        if(carry)
            temp3 -> val = carry;
        else{
            prev -> next = NULL;
        }
        
        return l3;
    }
    
};