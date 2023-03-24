class Solution:

    def binarySearch(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                return mid
        
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:

            idx = self.binarySearch(row, target)

            if idx > -1:
                return True
        
        return False
