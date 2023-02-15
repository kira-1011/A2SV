class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        left = 0
        right = len(people) - 1
        boats = 0

        # sort in increasing order
        people.sort()

        # find the best candidates that can 
        # fit on the boat and count the number of boats used
        while left <= right:

            sum = people[left] + people[right]

            if sum <= limit:
                left += 1
            
            boats += 1
            right -= 1
        
        return boats
