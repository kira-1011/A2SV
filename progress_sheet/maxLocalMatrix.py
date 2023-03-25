class Solution:

    def findLocal(self, grid, row, col):

        max_val = 0

        for curr_row in range(row, row + 3):
            for curr_col in range(col, col + 3):
                max_val = max(max_val, grid[curr_row][curr_col])
        
        return max_val

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)

        max_local = [[0 for i in range(n - 2)] for i in range(n - 2)]

        total_len = (n - 2) * (n - 2)

        for i in range(total_len):

            row = i // (n - 2)
            col = i % (n - 2)

            max_local[row][col] = self.findLocal(grid, row, col)
        
        return max_local
