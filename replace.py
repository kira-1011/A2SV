class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        # Intialize needed variables
        nums_index_map = {}
        nums_len = len(nums)

        # Copy the value of nums as key and its index as value
        for index, num in enumerate(nums):
            nums_index_map[num] = index
        
        # Replace elements in nums_index_map
        for operation in operations:
            index = nums_index_map.pop(operation[0])
            nums_index_map[operation[1]] = index
        
        # Copy the replaced values to nums
        for num, index in nums_index_map.items():
            nums[index] = num
        
        return nums