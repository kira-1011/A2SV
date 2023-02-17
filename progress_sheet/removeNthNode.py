  dummy = ListNode(0, head)
        offset = 0

        # find the length
        while head:
            offset += 1
            head = head.next
        
        offset -= n
        head = dummy

        # find the node to be deleted
        for i in range(offset):
            head = head.next
        
        # delete node
        head.next = head.next.next
        head = dummy.next

        return head
