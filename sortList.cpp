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
    ListNode* sortList(ListNode* head) {
        
        ListNode *temp = head;
        vector<int> nums;
        
        while(temp != NULL)
        {
            nums.push_back(temp -> val);
            temp = temp -> next;
        }
        
        temp = head;
        
        sort(nums.begin(), nums.end());
        
        for(auto num: nums)
        {
            temp -> val = num;
            temp = temp -> next;
        }
        
        return head;
    }
};