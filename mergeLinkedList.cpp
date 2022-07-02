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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        
        if(list1 == NULL && list2 == NULL)
            return NULL;
        
//         if(list1 -> next == NULL && list2 == NULL)
//             return list1;
        
//          if(list2 -> next == NULL && list1 == NULL)
//              return list2;
        
        ListNode *list3 = new ListNode;
        
        ListNode *temp3 = list3;
        
        ListNode *temp1 = list1;
        
        ListNode *temp2 = list2;
        
        while(temp1 != NULL && temp2 != NULL){
            
            if(temp1 -> val <= temp2 -> val)
            {
                temp3 -> val = temp1 -> val;
                
                temp1 = temp1 -> next;
            }
            
            else
            {
                temp3 -> val = temp2 -> val;
                
                temp2 = temp2 -> next;
            }
            
                temp3 -> next = new ListNode;
                
                temp3 = temp3 -> next;  
        }
        
        ListNode *prev = NULL;
        
        while(temp1 != NULL)
        {
            cout << temp1 -> val << " ";
            temp3 -> val = temp1 -> val;
            temp3 -> next = new ListNode;
            prev = temp3;
            temp3 = temp3 -> next;
            temp1 = temp1 -> next;
        }
        
        if( prev != NULL)
             prev -> next = NULL;
       
        
        while(temp2 != NULL)
        {
            temp3 -> val = temp2 -> val;
            temp3 -> next = new ListNode;
            prev = temp3;
            temp3 = temp3 -> next; 
            temp2 = temp2 -> next;
        }
        
        if( prev != NULL)
             prev -> next = NULL;
        
        delete temp1;
        delete temp2;
        delete temp3;
        
        return list3;
        
    }
};