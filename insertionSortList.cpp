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
    ListNode* insertionSortList(ListNode* head) {
        
        
        if(head -> next == NULL)
            return head;
        
        vector<int> nums;
        
        ListNode *temp = head;
        
        while(temp != NULL)
        {
            nums.push_back(temp -> val);
            temp = temp -> next;
        }
        
        int i,j;
        for(i = 1; i < nums.size(); i++)
        {
            int key = nums[i];

            j = i - 1;

            while(j >= 0 && nums[j] > key)
            {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = key;
        }
        
        temp = head;
        
        for(auto num : nums)
        {
            temp -> val = num;
            temp = temp -> next;
        }
        
        return head;
        
        
        
        
        
        
    }
};