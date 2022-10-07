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
        
        ListNode *temp = head -> next;
        ListNode *head2 = new ListNode;
        head2 -> val = head -> val;
        ListNode *temp1 = head2;
        
        while(temp -> next != NULL){
            
            if(temp -> val != temp1 -> val){
                
                temp1 -> next = new ListNode;
                temp1 -> next -> val = temp -> val;
                temp1 = temp1 -> next;
            }
            
            temp = temp -> next;
        }
        
        
        if(temp -> val != temp1 -> val){
                
                temp1 -> next = new ListNode;
                temp1 -> next -> val = temp -> val;
                temp1 = temp1 -> next;
        }
        
        return head2;
    }
};