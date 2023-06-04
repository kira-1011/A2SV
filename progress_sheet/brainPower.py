class Solution:

    def __init__(self):
        
        self.questions = []
        self.memo = dict()

    def getMaxPoint(self, i):

        if i >= len(self.questions):
            return 0
        
        if i not in self.memo:

            solve = self.questions[i][0] + self.getMaxPoint(i + self.questions[i][1] + 1)
            skip = self.getMaxPoint(i + 1)

            self.memo[i] = max(solve, skip)
        
        return self.memo[i]
       
    def mostPoints(self, questions: List[List[int]]) -> int:

        self.questions = questions
        
        return self.getMaxPoint(0)
