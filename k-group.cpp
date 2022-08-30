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

    vector<ListNode*> reverseLinkedList(ListNode* head, int k)
    {

        if(head == NULL)
            return {NULL, NULL};
        
        if(head -> next == NULL)
            return {head, NULL};

        ListNode* temp = head;

        ListNode* temp1 = temp -> next;
        
        ListNode* tail = temp;
        
        ListNode* lastNode = temp;
        
        vector<ListNode*> headTail;
        
        while(k > 0 && tail != NULL)
        {
            tail = tail -> next;
            k--;
        }
        
        if(k > 0)
            return {head, tail, lastNode};

        temp -> next = NULL;

        while(temp1 != tail)
        {
            ListNode* temp2 = temp1 -> next;

            temp1 -> next = temp;

            temp = temp1;

            temp1 = temp2;
        }
        
        headTail.push_back(temp);
        headTail.push_back(tail);
        headTail.push_back(lastNode);
        
        return headTail;
    }
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        
        if(head == NULL || head -> next == NULL)
            return head;
        
        ListNode* temp = head;
        
        ListNode* temp1 = temp;
        
        ListNode* prev = temp;
        
        vector<ListNode*> headTail;
        
        headTail = reverseLinkedList(head, k);
        
        head = headTail[0];
        
        temp = headTail[1];
        
        prev = headTail[2];
        
        while(temp != NULL)
        {
            headTail = reverseLinkedList(temp, k);
            temp = headTail[1];
            prev -> next = headTail[0];
            prev = headTail[2];
        }
        
        
        
        
        return head;
        
        
        
    }
};