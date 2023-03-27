class Solution:

    def checkMagicSquare(self, grid, row, col):

        distinct_val = set()
        row_sum = [0] * 3
        col_sum = [0] * 3
        diagonal_sum = [0] * 2


        for curr_row in range(row, row + 3):
            for curr_col in range(col, col + 3):

                if grid[curr_row][curr_col] in distinct_val or grid[curr_row][curr_col] not in range(1, 10):
                    return False
                
                distinct_val.add(grid[curr_row][curr_col])
                row_sum[curr_row - row] += grid[curr_row][curr_col]
                col_sum[curr_col - col] += grid[curr_row][curr_col]
                
                if (curr_row - row) == (curr_col - col):
                    diagonal_sum[0] += grid[curr_row][curr_col]
                
                if (curr_row + curr_col - row - col) == 2:
                    diagonal_sum[1] += grid[curr_row][curr_col]
        
        row_sum.extend(col_sum)
        row_sum.extend(diagonal_sum)

        if len(set(row_sum)) == 1:
            return True
        
        return False

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        magic_squares = 0

        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):

                if self.checkMagicSquare(grid, row, col):
                    magic_squares += 1
        
        return magic_squares
