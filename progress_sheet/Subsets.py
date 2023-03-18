class Solution:

    def __init__(self):
        self.nums = []
        self.solution = []

    def findSubsets(self, idx, subsets):

        if idx >= len(self.nums):
            return
        
        subsets.append(self.nums[idx])
        self.solution.append(subsets.copy())
        self.findSubsets(idx + 1, subsets)
        subsets.pop()

        self.findSubsets(idx + 1, subsets)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.nums = nums

        self.findSubsets(0, [])

        self.solution.append([])
        
        return self.solution
