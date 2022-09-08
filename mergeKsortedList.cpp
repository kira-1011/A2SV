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
    
    ListNode* divideAndMerge(vector<ListNode*>& lists, int start, int end)
    {
        if(start >= end)
            return lists[start];
        
        int mid = (start + end) / 2;
        
        ListNode* left =  divideAndMerge(lists, start, mid);
        ListNode* right = divideAndMerge(lists, mid + 1, end);
        
        return merge(left, right);
        
    }
    
    ListNode* merge(ListNode* left, ListNode* right)
    {
        ListNode* leftItr = left;
        ListNode* rightItr = right;
        ListNode* head = new ListNode;
        ListNode* temp1 = head;
        ListNode* prev = temp1;
        
        if(leftItr == NULL && rightItr == NULL)
            return NULL;
        
        if(leftItr == NULL)
            return rightItr;
        
        if(rightItr == NULL)
            return leftItr;
        
        while(leftItr != NULL && rightItr != NULL)
        {
           
            if(leftItr -> val <= rightItr -> val)
            {
                temp1 -> val = leftItr -> val;
                temp1 -> next = new ListNode;
                prev = temp1;
                temp1 = temp1 -> next;
                leftItr = leftItr -> next;
            }
            else
            {
                temp1 -> val = rightItr -> val;
                temp1 -> next = new ListNode;
                prev = temp1;
                temp1 = temp1 -> next;
                rightItr = rightItr -> next;
            }
        }
        
        while(leftItr != NULL)
        {
            temp1 -> val = leftItr -> val;
            temp1 -> next = new ListNode;
            prev = temp1;
            temp1 = temp1 -> next;
            leftItr = leftItr -> next;
        }
        
        while(rightItr != NULL)
        {
            temp1 -> val = rightItr -> val;
            temp1 -> next = new ListNode;
            prev = temp1;
            temp1 = temp1 -> next;
            rightItr = rightItr -> next;
        }
        
        prev -> next = NULL;
        
        return head;
        
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        if(lists.size() == 0)
            return NULL;
        
        return  divideAndMerge(lists, 0 , lists.size() - 1);
    }
};