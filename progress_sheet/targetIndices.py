class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        target_indices = []
        size = len(nums)
        nums.sort()

        for index in range(size):
            
            if nums[index] > target:
                break

            if nums[index] == target:
                target_indices.append(index)
        
        return target_indices