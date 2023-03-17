class Solution:

    def __init__(self):
        self.solution = set()
        self.candidates = []
        self.target = 0

    def findCombinationSum(self, combination, idx, curr_sum):

        if curr_sum == self.target:
            self.solution.add(tuple(combination.copy()))
            return
        
        if idx >= len(self.candidates):
            return

        if curr_sum > self.target:
            return
        
        if tuple(combination) in self.solution:
            return

        for i in range(idx, len(self.candidates)):

            if i > idx and self.candidates[i - 1] == self.candidates[i]:
                continue

            # Pick and move
            combination.append(self.candidates[i])
            curr_sum += self.candidates[i]

            if curr_sum > self.target:
                curr_sum -= combination.pop()
                return

            self.findCombinationSum(combination, i + 1, curr_sum)            
            curr_sum -= combination.pop()

        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.candidates = sorted(candidates)
        self.target = target
        self.findCombinationSum([], 0, 0)

        return self.solution
