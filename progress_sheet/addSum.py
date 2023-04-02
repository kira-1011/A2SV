# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum_list = ListNode(0)
        curr_sum = sum_list
        prev_sum = None
        carry = 0

        while l1 or l2 or carry:

            sum_ = carry

            if l1:
                sum_ += l1.val
                l1 = l1.next
            
            if l2: 
                sum_ += l2.val
                l2 = l2.next


            carry = sum_ // 10
            sum_ %= 10

            curr_sum.val = sum_
            prev_sum = curr_sum
            curr_sum.next = ListNode(0)
            curr_sum = curr_sum.next
        
        if carry:
            curr_sum.val = carry
            
        else:
            prev_sum.next = None

        return sum_list
