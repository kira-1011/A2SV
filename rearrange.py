class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        # Initialize all needed variables
        positive_nums = []
        negative_nums = []
        pos_index = 0
        neg_index = 0

        # Store positive and negative values
        for num in nums:

            if num < 1:
                negative_nums.append(num)
            
            else:
                positive_nums.append(num)
        
        # Store positive values at even index and negative at odd index
        for i, num in enumerate(nums):

            if i % 2 == 0:
                nums[i] = positive_nums[pos_index]
                pos_index += 1
        
            else:
                nums[i] = negative_nums[neg_index]
                neg_index += 1
        
        return nums