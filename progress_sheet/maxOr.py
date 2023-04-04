class Solution:

    def __init__(self):

        self.nums = []
        self.max_or = 0
        self.solution = []
        self.subset_count = 0

    def findMaxOr(self, idx, curr_list):

        if idx >= len(self.nums):
            return
        
        curr_list.append(self.nums[idx])
        
        curr_or = 0

        # caculate current or
        for num in curr_list:
            curr_or |= num
        
        if curr_or == self.max_or:
            self.subset_count += 1

        self.solution.append(curr_list.copy())
        self.findMaxOr(idx + 1, curr_list)
        curr_list.pop()

        self.findMaxOr(idx + 1, curr_list)

    def countMaxOrSubsets(self, nums: List[int]) -> int:

        self.nums = nums

        max_or = 0

        for num in nums:
            max_or |= num

        self.max_or = max_or

        self.findMaxOr(0, [])

        return self.subset_count
