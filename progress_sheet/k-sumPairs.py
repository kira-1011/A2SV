class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = len(nums) - 1
        max_ops = 0

        nums.sort()

        # find pairs that sum up to k and count operation
        while left < right and nums[left] < k:

            sum = nums[left] + nums[right]

            if sum == k:
                max_ops += 1
                left += 1
                right -= 1
            
            elif sum > k:
                right -= 1
            
            else:
                left += 1
        
        return max_ops