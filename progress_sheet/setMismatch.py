class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        lost = []
        size = len(nums)

        for i in range(size):

            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
            i += 1
        
        for i in range(size):

            if nums[i] - 1 != i:
                lost.append(nums[i])
                lost.append(i + 1)
                break

        return lost
