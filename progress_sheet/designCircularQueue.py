class MyCircularQueue:

    def __init__(self, k: int):

        self.k = k
        self.front = 0
        self.rear = 0
        self.queue = [-1] * k

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False
        
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.k

        return True
        
    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
  
        self.queue[self.front] = -1
        self.front = (self.front + 1) % self.k

        return True

    def Front(self) -> int:

        if self.isEmpty():
            return -1
        
        return self.queue[self.front]
        

    def Rear(self) -> int:

        if self.isEmpty():
            return -1
        
        return self.queue[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        
        if self.front == self.rear and self.queue[self.front] == -1:
            return True
        
        return False

    def isFull(self) -> bool:

        if self.front == self.rear and self.queue[self.front] != -1:
            return True
        
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
