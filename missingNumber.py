class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Initialize dictionary
        value_index = {}

        n = len(nums)

        # Insert value-index pair into the value_index dictionary 
        for index in range(n):
            value_index[nums[index]] = index

        # Check the missing number from value_index dictionary
        for i in range(n + 1):
            if i not in value_index:
                return i
