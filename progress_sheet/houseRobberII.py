class Solution:

    def __init__(self):

        self.memo = dict()
        self.nums = []

    def dp(self, i, chosen):
        
        #base cases

        if chosen and i == len(self.nums) - 1:
            return 0

        if i >= len(self.nums):
            return 0

        if (i,chosen) not in self.memo:

            if i == 0:
                choose = self.nums[i] + self.dp(i + 2, True)

            else:
                choose = self.nums[i] + self.dp(i + 2, chosen)
            
            skip = self.dp(i + 1, chosen)

            self.memo[(i, chosen)] = max(choose, skip)

        return self.memo[(i, chosen)]

    def rob(self, nums: List[int]) -> int:

        self.nums = nums
        
        return self.dp(0, False)
