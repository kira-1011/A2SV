class StockSpanner:

    def __init__(self):
        
        self.mono_stack = []
            
    def next(self, price: int) -> int:
        
        total_span = 0

        while self.mono_stack and self.mono_stack[-1][0] <= price:
                total_span += self.mono_stack.pop()[1]
        
        total_span += 1

        self.mono_stack.append((price, total_span))

        return total_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
