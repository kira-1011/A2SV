class Solution:

    def __init__(self):
        
        self.n = 0
        self.k = 0
        self.solution = []
    
    def findCombination(self, curr, combination):

        if len(combination) == self.k:
            self.solution.append(combination.copy())
            return
        
        if curr > self.n:
            return

        for i in range(curr, self.n + 1):

            # select element and move to the next element
            combination.append(i)
            self.findCombination(i + 1, combination) 
            combination.pop() 

    def combine(self, n: int, k: int) -> List[List[int]]:

        self.n = n
        self.k = k

        self.findCombination(1, [])

        return self.solution
