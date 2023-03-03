# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        first_bad = n
        start = 1
        end = n

        # find the left most bad version using binary search
        while start <= end:

            mid = start + (end - start) // 2

            if isBadVersion(mid):
                end = mid - 1
                first_bad = mid
            
            else:
                start = mid + 1
        
        return first_bad
