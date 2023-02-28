class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = self.prefixSum(nums)

    def sumRange(self, left: int, right: int) -> int:
        
        sum =self.nums[right] - self.nums[left - 1]
        return sum
    
    def prefixSum(self, nums):
        
        size = len(nums)
        nums.append(0)

        # Store prefix sum
        for i in range(size):
            nums[i] += nums[i - 1]
        
        return nums


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
