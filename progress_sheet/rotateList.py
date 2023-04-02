# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        curr = head
        tail = head
        length = 0

        # find length and the last node
        while curr:
            length += 1
            tail = curr
            curr = curr.next

        # calculate steps to take from the first node        
        step = (length - k) % length

        # move "step" steps
        curr = head

        for i in range(1, step):
            curr = curr.next
        
        if step == 0:
            return head

        # rotate the list
        new_head = curr.next
        curr.next = None
        tail.next = head

        return new_head
