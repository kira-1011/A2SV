class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        missing = len(nums) + 1

        for i in range(len(nums)):

            while nums[i] > 0 and nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        

        for i in range(len(nums)):

            if nums[i] - 1 != i:
                return (i + 1)
        
        return missing
