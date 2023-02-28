class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = float('inf')
        length = len(nums)
        currSum = 0
        left = 0
        
        # Move right pointer until our sum is greataer than target
        for right in range(length):

            currSum += nums[right]
            
            # minimize the length by shrinking the window
            while currSum >= target:
                min_length = min(min_length, right - left + 1)
                currSum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0
        
        return min_length
