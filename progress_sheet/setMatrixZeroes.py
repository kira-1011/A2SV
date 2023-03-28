class Solution:


    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])

        # Check rows
        for row in range(row_len):
            for col in range(col_len):
                
                if matrix[row][col] == 0:

                    # mark cells to make them zeroes
                    for new_col in range(0, col_len):

                        if matrix[row][new_col] == 0:
                            continue

                        matrix[row][new_col] = float('inf')
                    
                    break

        # Check cols
        for col in range(col_len):
            for row in range(row_len):

                if matrix[row][col] == 0:

                    # return back and mark cells to make them zeroes
                    for new_row in range(0, row_len):

                        if matrix[new_row][col] == 0:
                            continue

                        matrix[new_row][col] = float('inf')
                    
                    break
        
        # Change cells to zeroes if marked
        for row in range(row_len):
            for col in range(col_len):
                
                # return back and mark cells to make them zeroes
                if matrix[row][col] == float('inf'):
                    matrix[row][col] = 0
