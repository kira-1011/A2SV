class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # Line sweeping technique

        max_range = 0
        prefix_trips = []

        for trip in trips:
            max_trip = max(trip[1], trip[2])
            max_range = max(max_range, max_trip)
        
        prefix_trips = [0] * (max_range + 2)
        
        # Mark pick up and drop off points
        for trip in trips:
            prefix_trips[trip[1]] += trip[0]
            prefix_trips[trip[2]] -= trip[0]
        
        # sweep the marked points by taking the cumulative sum
        # and check if we have enough seats
        for i in range(len(prefix_trips)):
            prefix_trips[i] += prefix_trips[i - 1]

            if prefix_trips[i] > capacity:
                return False
        
        return True
