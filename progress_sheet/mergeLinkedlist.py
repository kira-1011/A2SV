# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list3 = ListNode()
        current1 = list1
        current2 = list2
        current3 = list3

        while current1 and current2:
            
            if current1.val <= current2.val:
                current3.next = ListNode(current1.val, None)
                current1 = current1.next
            
            else:
                current3.next = ListNode(current2.val, None)
                current2 = current2.next
            
            current3 = current3.next

        while current1:
            current3.next = ListNode(current1.val, None)
            current1 = current1.next
            current3 = current3.next
        
        while current2:
            current3.next = ListNode(current2.val, None)
            current2 = current2.next
            current3 = current3.next
        
        return list3.next
