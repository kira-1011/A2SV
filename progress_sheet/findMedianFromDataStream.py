class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        
        heappush(self.min_heap, num)

        # check if the top elment in the min heap is greater than the top in the max heap
        if self.max_heap and self.min_heap[0] < -self.max_heap[0]:
            popped = heappop(self.min_heap)
            heappush(self.max_heap, -popped)
        
        # balance the length of the two heaps
        if len(self.max_heap) > len(self.min_heap):
            popped = heappop(self.max_heap)
            heappush(self.min_heap, -popped)
        
        elif len(self.min_heap) - len(self.max_heap) > 1:
            popped = heappop(self.min_heap)
            heappush(self.max_heap, -popped)

    def findMedian(self) -> float:
        
        if len(self.max_heap) == len(self.min_heap):
            return ((-self.max_heap[0] + self.min_heap[0]) / 2)

        return self.min_heap[0] 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
