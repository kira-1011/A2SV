class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        candidates = [i * i for i in range(floor(sqrt(c)) + 1)]

        # Store the best candidates taking their squares that may sum up to c 
        left = 0
        right = floor(sqrt(c))
        
        # Use colliding pointers to check if two numbers squared could sum up to c
        while left <= right:

            sqr_sum = candidates[left] + candidates[right]
            
            if sqr_sum == c:
                return True

            if sqr_sum > c:
                right -= 1
                
            else:
                left += 1
        
        return False
