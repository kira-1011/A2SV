class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix_sum = defaultdict(int)
        size = len(nums)
        subarrays = 0
        running_sum = 0

        # finding subarrays with sum equals goal and
        # subarrays that have running sum - goal meaning that 
        # could be chopped off the current subarray

        for i in range(size):
            
            running_sum += nums[i]

            if running_sum == goal:
                subarrays += 1
            
            subarrays += prefix_sum[running_sum - goal]
            prefix_sum[running_sum] += 1
        
        return subarrays
