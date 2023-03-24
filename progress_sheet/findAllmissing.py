class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        missed = []
        size = len(nums)

        for i in range(size):

            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
            i += 1
        
        for i in range(size):

            if nums[i] - 1 != i:
                missed.append(i + 1)

        return missed
