# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # Find the mid point using floyd's algorithm
        slow = head
        fast = head
        curr = head
        prev = None
        twin_sum = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse half part of the linked list
        while curr != slow:
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Find the max twin sum
        while prev and curr:
            twin_sum = max(twin_sum, prev.val + curr.val)
            prev = prev.next
            curr = curr.next

        return twin_sum
