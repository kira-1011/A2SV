class Solution:

    def flip_array(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        flip_pos = size - (k % size)
        left = 0
        right = flip_pos - 1

        # flip left subarray
        self.flip_array(nums,left,right)
                
        # flip right subarray
        left = flip_pos
        right = size - 1
        
        self.flip_array(nums,left,right)
                
        # Flip the whole array
        nums.reverse()