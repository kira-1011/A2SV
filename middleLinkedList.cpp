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
    ListNode* middleNode(ListNode* head) {
        int middle = 1;
        ListNode *temp = head;
        
        
        //calculate the total nodes
        while(temp -> next != NULL){
            middle ++;
            temp = temp -> next;
        }
        
        middle = (middle / 2) + 1;
        temp = head;
        
        //search for the middle node
        for(int i = 1; i < middle; i++){
            temp = temp -> next;
        }
        
        return temp;
    }
};