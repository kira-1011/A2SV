# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        length = 0
        prev = None
        current = head
        midNode = None

        # Get the length
        while current:
            current = current.next
            length += 1
        
        midLength = length // 2
        current = head

        # Reverse half of the linked list
        for i in range(midLength):
            midNode = current.next
            current.next = prev
            prev = current
            current = midNode

        head = prev

        # Handle the middle node if it's even
        if midNode and length % 2 != 0:
            midNode = midNode.next
        
        # Compare the two half linke lists
        while head and midNode:
            if head.val != midNode.val:
                return False

            head = head.next
            midNode = midNode.next

        return True 
