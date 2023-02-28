class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        size = len(nums)

        # Append 0 to handle the first element
        nums.append(0)

        # Store running nums
        for i in range(size):
            nums[i] += nums[i - 1]
        
        nums.pop()
        return nums
