class Solution:

    # calculate the total hours required to eat all bananas in k speed
    def getTotalHours(self, piles, k):
        
        hours = 0
        
        for bananas in piles:
            hours += (math.ceil(bananas / k))
        
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Binary search over the output range of k 1 upto maximum banana piles 
        start = 1
        end =  max(piles)
        min_speed = end

        while start <= end:

            mid = start + (end - start) // 2
            total_hours = self.getTotalHours(piles, mid)

            if total_hours <= h:
                end = mid - 1
                min_speed = mid
            
            else:
                start = mid + 1

        return min_speed
