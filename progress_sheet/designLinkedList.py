class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.head = self.dummy.next
        self.length = 0    

    def get(self, index: int) -> int:
        curr = self.dummy.next

        if index >= self.length:
            return -1

        for i in range(index):
            curr = curr.next
        
        return curr.val

        
    def addAtHead(self, val: int) -> None:
        curr = self.dummy
        curr.next = Node(val, curr.next)
        self.head = self.dummy.next
        self.length += 1

    def addAtTail(self, val: int) -> None:
        curr = self.dummy

        while curr and curr.next:
            curr = curr.next
        
        curr.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy.next
        prev = self.dummy

        for i in range(index):
           
            if curr == None:
                return

            prev = curr
            curr = curr.next
        
        prev.next = Node(val, curr)
        self.head = self.dummy.next
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:

        prev = self.dummy
        curr = self.dummy.next

        if index >= self.length:
            return

        for i in range(index):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        self.head = self.dummy.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
