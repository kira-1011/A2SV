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
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {

        vector<int> rev;

        ListNode *temp = head;

        if (head == NULL)
            return NULL;

        if (head->next == NULL)
            return head;

        while (temp != NULL)
        {
            rev.push_back(temp->val);
            temp = temp->next;
        }

        temp = head;

        while (temp != NULL)
        {
            temp->val = rev.back();
            rev.pop_back();
            temp = temp->next;
        }

        return head;
    }
};