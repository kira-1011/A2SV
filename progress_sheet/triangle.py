class Solution:

    def __init__(self):
        
        self.memo = dict()
        self.triangle = []
        
    def findMinSum(self, row_idx, col_idx):
        
        if row_idx >= len(self.triangle):
           return 0
        
        if (row_idx, col_idx) not in self.memo:

            choose_left = self.triangle[row_idx][col_idx] + self.findMinSum(row_idx + 1, col_idx)
            choose_right = self.triangle[row_idx][col_idx + 1] + self.findMinSum(row_idx + 1, col_idx + 1)

            self.memo[(row_idx, col_idx)] = min(choose_left, choose_right)

        return self.memo[(row_idx, col_idx)] 

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        self.triangle = triangle

        return triangle[0][0] + self.findMinSum(1, 0)
      
