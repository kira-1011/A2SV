class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        size = len(nums)
        
        for i in range(size - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        holder = 0
        seeker = 0

        for i in range(size):
            if nums[seeker] != 0:
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            seeker += 1
        
        return nums
            
