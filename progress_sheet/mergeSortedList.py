# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeList(self, head, curr1, curr2):
       
       # if we reach at the end stop and link the remaining part 
        if curr1 == None:
            head.next = curr2
            return

        if curr2 == None:
            head.next = curr1
            return

        # add the smaller node to the new linked list
        if curr1.val <= curr2.val:
            head.next = curr1
            self.mergeList(head.next, curr1.next, curr2)
        
        else:
            head.next = curr2
            self.mergeList(head.next, curr1, curr2.next)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()

        self.mergeList(head, list1, list2)

        return head.next
