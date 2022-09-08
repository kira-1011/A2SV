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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        ListNode* temp = NULL;
        
        vector<int> nums;
        
        int n = lists.size();
        
        if(n == 0)
            return NULL;
        
        bool empty = true;
        
         for(int i = 0; i < n; i++)
         {
             temp = lists[i];
             
             if(temp != NULL)
             {
                 empty = false;
                 break;
             }
         }
        
        if(empty)
            return NULL;
        
         make_heap(nums.begin(), nums.end(), greater<>());
        
        for(int i = 0; i < n; i++)
        {
            temp = lists[i];
            
            while(temp != NULL)
            {
                nums.push_back(temp -> val);
                push_heap(nums.begin(), nums.end(), greater<>());
                temp = temp -> next;
            }
        }
        
        ListNode* head = new ListNode;
        temp = head;
        ListNode* prev = temp;
        
        n = nums.size();
         
        while(!nums.empty()){            
            temp -> val = nums.front();
            prev = temp;
            temp -> next = new ListNode;
            temp = temp -> next;
            pop_heap(nums.begin(), nums.end(), greater<>());
            nums.pop_back();
        }
        
        prev -> next = NULL;
        
        return head;
        
    }
};