class Solution:
    def mySqrt(self, x: int) -> int:

        start = 1
        end = x // 2
        candidate = x

        # Find the largest best candidate in the range 1 to half of x
        while start <= end:

            mid = start + (end - start) // 2

            if mid**2 > x:
                end = mid - 1
            
            elif mid**2 < x:
                candidate = mid
                start = mid + 1
            
            else:
                return mid
        
        return candidate
