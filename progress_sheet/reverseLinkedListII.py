# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Set dummy to keep track of the starting node
        dummy = ListNode(0, head)

        leftNode = dummy
        rightNode = dummy
        current = head
        
        # Reverse the sublist of the linked list
        for i in range(1, right + 1):

            if i < left:
                rightNode = current
                leftNode = current
                current = current.next

            else:
                temp = current.next
                current.next = rightNode
                rightNode = current
                current = temp
        
        # reconnect the rest of the linked list
        leftNode.next.next = current
        leftNode.next = rightNode
        head = dummy.next
        
        return head
