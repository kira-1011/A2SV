class Solution:

    def __init__(self):
        self.memo = dict()
        self.n = None
        self.target = None
        self.nums = None

    def dp(self, i, _sum):

        if i == self.n:
            return _sum == self.target
        
        if (i, _sum) not in self.memo:
            self.memo[(i, _sum)] = self.dp(i + 1, _sum + self.nums[i]) + self.dp(i + 1, _sum - self.nums[i])
        
        return self.memo[(i, _sum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        self.n = len(nums)
        self.target = target
        self.nums = nums

        return self.dp(0, 0)
