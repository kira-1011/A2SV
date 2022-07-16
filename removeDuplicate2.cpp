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
    ListNode* deleteDuplicates(ListNode* head) {
        
        if(head == NULL || head -> next == NULL)
            return head;
        
        ListNode *temp1 = head;
        ListNode *temp2 = head -> next;
        
        ListNode *head1 = new ListNode;
        head1 -> val = -101;
        ListNode *temp3 = head1;
        ListNode *prev = temp3;
        
        int prevDuplicated = -101;
        
        
        while(temp2 != NULL)
        {
            if(temp1 -> val == temp2 -> val || temp1 -> val == prevDuplicated)
            {
                prevDuplicated = temp1 -> val;
                temp2 = temp2 -> next;
                temp1 = temp1 -> next;
                
            }
                
            else
            {
                temp3 -> val = temp1 -> val;
                temp3 -> next = new ListNode;
                temp1 = temp1 -> next;
                temp2 = temp2 -> next;
                prev = temp3;
                temp3 = temp3 -> next;
            }
            
        }
        
        if(temp1 -> val != prevDuplicated)
        {
            temp3 -> val = temp1 -> val;
            temp3 -> next = NULL;
            return head1;
        }
        
        if(head1 -> val == -101)
            return NULL;
        
        prev -> next = NULL;
        
        return head1;
    }
};