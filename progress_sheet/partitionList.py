# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # two new linkedlists to store lesser and greater values of x
        lesserNodes = ListNode()
        greaterNodes = ListNode()

        current1 = lesserNodes
        current2 = greaterNodes

        # partition lesser and greater values of x 
        while head:
            newNode = ListNode(head.val)

            if head.val < x:
                current1.next = newNode
                current1 = current1.next 
            else:
                current2.next =  newNode
                current2 = newNode

            head = head.next

        current1.next = greaterNodes.next
        head = lesserNodes.next
        
        return head
