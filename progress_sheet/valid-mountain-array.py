class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        size = len(arr)
        i = 1

        if size < 3:
            return False
        
        # check for strictly increasing subarray starting from 0th index
        while i < size:
            if arr[i - 1] >= arr[i]:
                break

            i += 1
        
        if i >= size or i == 1:
            return False
        
        # check for strictly decreasing subarray starting from 0th index
        while i < size:
            if arr[i - 1] <= arr[i]:
                return False
            i += 1

        
        return True
