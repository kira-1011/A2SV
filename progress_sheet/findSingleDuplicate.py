class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        duplicate = 0
        size = len(nums)

        for i in range(size):

            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
            if nums[i] - 1 != i:
                duplicate = nums[i]

        return duplicate
