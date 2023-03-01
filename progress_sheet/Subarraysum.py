class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = defaultdict(int)
        pre_sum = 0
        subarrays = 0
        size = len(nums)

        # count subarray with sum k and 
        # count subarray by chopping off the current part of subarray having total sum = prefix sum - k
        for i in range(size):

            pre_sum += nums[i]

            if pre_sum == k:
                subarrays += 1

            subarrays += prefix_sum[pre_sum - k]
            prefix_sum[pre_sum] += 1

        return subarrays  
