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
    ListNode* reverseLinkedList(ListNode* head)
    {
        ListNode* temp = head;
        ListNode* temp1 = temp -> next;
        
        if(head -> next == NULL)
            return head;
        
        temp -> next = NULL;
        
        while(temp1 != NULL)
        {
            ListNode* temp2 = temp1 -> next;
            
            temp1 -> next = temp;
            
            temp = temp1;
            
            temp1 = temp2;
        }
        
        return temp;
    }
public:
    void reorderList(ListNode* head) {
        
        if(head == NULL || head -> next == NULL || head -> next -> next == NULL)
            return;
        
        int n = 0;
        
        ListNode *temp = head;
        ListNode *head1 = NULL;
        ListNode*temp1 = head;
        
        while(temp != NULL)
        {
            n++;
            temp = temp -> next;
        }
        
        for(int c = 0, k = ceil(n / (float)2); c < k; c++)
        {
             temp = temp1;
             temp1 = temp1 -> next;
        }
        
        temp -> next = NULL;
        
        head1 = reverseLinkedList(temp1);
        
        temp1 = head1;
        
        temp = head;
        
        while(temp1 != NULL)
        {
            ListNode* temp2 = temp -> next;
            ListNode* temp3 = temp1 -> next;
            
            temp -> next = temp1;
            temp1 -> next = temp2;
            
            temp = temp2;
            temp1 = temp3;
        }
    }
};