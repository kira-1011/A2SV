class Solution:

    def __init__(self):

        self.memo = dict()
        self.nums = []
    
    def findComb(self, i, target):
        
        if target in self.memo:
            return self.memo[target]

        if target == 0:
            return 1

        if target < 0:
            return 0
        
        ways = 0

        for i in range(len(self.nums)):
            ways += self.findComb(i, target - self.nums[i])    
            
        self.memo[target] = ways

        return self.memo[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:

        self.nums = nums

        return self.findComb(0, target)
