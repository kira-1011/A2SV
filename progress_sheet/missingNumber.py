class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        size = len(nums)
        missed = size

        for i in range(size):

            while nums[i] < size and nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            
            if nums[i] != i:
                missed = i
            
            i += 1

        return missed
