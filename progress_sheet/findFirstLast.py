class Solution:

    
    def binarySearchLeft(self, nums, target):

        start = 0
        end = len(nums) - 1
        first_pos = -1

        while start <= end:

            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid - 1
            
            elif nums[mid] < target:
                start = mid + 1
            
            else:
                first_pos = mid
                end = mid - 1
        
        return first_pos

    def binarySearchRight(self, nums, target):

        start = 0
        end = len(nums) - 1
        last_pos = -1

        while start <= end:

            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid - 1
            
            elif nums[mid] < target:
                start = mid + 1
            
            else:
                last_pos = mid
                start = mid + 1
        
        return last_pos

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first_pos = self.binarySearchLeft(nums, target)
        last_pos = self.binarySearchRight(nums, target)

        return [first_pos, last_pos]
