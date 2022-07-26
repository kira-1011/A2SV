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
    int pairSum(ListNode* head)
    {
        ListNode* temp = head;
        
        ListNode* temp1 = head -> next;
        
        ListNode* temp2 = temp1;
        
        int n = 0;
        
        while(temp != NULL)
        {
            temp = temp -> next;
            n++;
        }
        
        temp = head;
        
        if(n <= 2)
            return (temp -> val + temp1 -> val);
        
        n = n / 2;
        
        temp -> next = NULL;
        
        //Reverse half of the linked list
        
        for(int i = 0; i < n - 1; i++)
        {
            temp2 = temp1 -> next;
            temp1 -> next = temp;
            temp = temp1;
            temp1 = temp2;
        }
        
        head = temp;
        int sum = 0;
        int max = 0;
        
        while(temp != NULL)
        {
            sum = temp -> val + temp1 -> val;
            temp = temp -> next;
            temp1 = temp1 -> next;
            
            if(sum > max)
                max = sum;
        }
        
         return max;
    }
};