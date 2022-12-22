class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # Initialize dictionary that contains value and count of occurenece pair
        occurence = {}
        pairs = 0

        # Count the number of occurences for each value in nums
        for i in nums:
            if i in occurence:
                occurence[i] += 1
            else:
                occurence[i] = 1 
        
        # Count the number of pairs that can be formed
        for key in occurence:
            count = occurence[key]
            count = count * (count - 1) // 2
            pairs += count
        
        return pairs