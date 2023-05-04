class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.kth_largest = []

        self.k = k

        # insert the k largest elements in the heap
        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:

        if len(self.kth_largest) != self.k:
            heappush(self.kth_largest, val)
        
        elif val > self.kth_largest[0]:
            heapreplace(self.kth_largest, val)

        return self.kth_largest[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
