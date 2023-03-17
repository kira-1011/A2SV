class Solution:

    def __init__(self):
        self.solution = []
        self.candidates = []
        self.target = 0

    
    def findCombinationSum(self, combination, idx, curr_sum):

        if curr_sum == self.target:
            self.solution.append(combination.copy())
            return
        
        if curr_sum > self.target:
            return
        
        if idx >= len(self.candidates):
            return
        
        for i in range(idx, len(self.candidates)):

            # Pick and stay on the current element
            combination.append(self.candidates[i])
            curr_sum += self.candidates[i]

            if curr_sum > self.target:
                curr_sum -= combination.pop()
                break

            self.findCombinationSum(combination, i, curr_sum)
            curr_sum -= combination.pop() 


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.candidates = sorted(candidates)
        self.target = target

        self.findCombinationSum([], 0, 0)

        return self.solution
