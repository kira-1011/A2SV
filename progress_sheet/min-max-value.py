class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        prefix_sum = [0] * (len(nums) + 1)
        max_min = 0

        for i in range(len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        prefix_sum.pop()

        for i in range(len(nums)):

            avg = math.ceil(prefix_sum[i] / (i + 1))

            max_min = max(max_min, avg)

        
        return max_min
