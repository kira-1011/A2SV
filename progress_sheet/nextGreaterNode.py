# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        # use monostack to find the next greater node
        mono_stack = []
        next_greater = []
        curr = head
        i = 0
        length = 0

        # calculate length
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        next_greater = [0] * length

        # maintain a decreasing monostack to find the next greater element
        while curr:

            while mono_stack and mono_stack[-1][0].val < curr.val:
                next_greater[mono_stack.pop()[1]] = curr.val 

            # append the reference and index pair
            mono_stack.append((curr, i))
            i += 1
            curr = curr.next

        return next_greater
