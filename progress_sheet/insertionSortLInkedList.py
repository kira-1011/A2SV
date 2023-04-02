# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertNode(self, prev1, prev2, node1, node2):

        # detach node
        prev2.next = node2.next

        # insert node
        node2.next = node1
        prev1.next = node2

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        
        sorted_tail = head
        curr = head.next
        sorted_head = ListNode(0, head)

        while curr:

            if curr.val >= sorted_tail.val:
                sorted_tail = curr
                curr = curr.next
            
            else:
                
                sorted_tail.next = curr.next
                insert_pos = sorted_head

                # find the correct pos to insert
                while insert_pos.next.val <= curr.val:
                    insert_pos = insert_pos.next

                curr.next = insert_pos.next 
                insert_pos.next = curr

                curr = sorted_tail.next
        
        return sorted_head.next
