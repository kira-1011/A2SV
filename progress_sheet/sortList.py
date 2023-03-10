# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        # Divide
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge
        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            
            else:
                curr.next = right
                right = right.next
            
            curr = curr.next
        
        if not left:
            curr.next = right
        
        else:
            curr.next = left
        
        return dummy.next
