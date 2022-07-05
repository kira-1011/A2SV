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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if(head -> next == NULL)
            return NULL;
        
        int length = 0;
        
        ListNode *temp = head;
        
        while(temp != NULL)
        {
            length++;
            temp = temp -> next;
        }
        
        temp = head;
        
        if(n == length)
        {
            head = head -> next;
            return head;
        }
        
        for(int i = 1, end = length - n; i < end; i++)
        {
            temp = temp -> next;
        }
        
        if(temp -> next -> next == NULL)
            temp -> next = NULL;
        
        else
        {
            ListNode *temp1 = temp -> next;
            temp -> next = temp -> next -> next;
            delete temp1;
        }
        
        return head;
        
    }   
};