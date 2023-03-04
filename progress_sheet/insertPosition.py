class Solution:

    def binarySearch(self, nums, target):

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid - 1
            
            elif nums[mid] < target:
                start = mid + 1
            
            else:
                return mid
        
        return start

    def searchInsert(self, nums: List[int], target: int) -> int:

        insert_pos = self.binarySearch(nums, target)
        return insert_pos
