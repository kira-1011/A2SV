# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # start from head
        slow = head
        fast = head

        # move second pointer twice as fast as first pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # fast.next => to handle odd elements
        # fast => to handle even elements
        # interchangine fast and fast.next doesn't work if it's even
         
        return slow
