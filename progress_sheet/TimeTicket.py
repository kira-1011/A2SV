class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        queue = deque([i for i in range(len(tickets))])
        total_time = 0

        while tickets[k] > 0:

            front = queue.popleft()

            tickets[front] -= 1
            
            if tickets[front] > 0:
                queue.append(front)
        
            total_time += 1
        
        return total_time
