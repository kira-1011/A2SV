class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        row_len = len(mat)
        col_len = len(mat[0])

        # Check if it is possible to reshape the matrix
        if row_len * col_len != r * c:
            return mat

        # Create a new matrix of size r x c
        reshaped = [[0] * c for i in range(r)]

        # Traverse the original matrix
        for row in range(row_len):
            for col in range(col_len):
                
                #calculate the index for the current position.
                idx = row * col_len + col

                # calculate its row and column indices in the original matrix using 
                # integer division and modulo operations on the index
                row_map = idx // c
                col_map = idx % c
                
                reshaped[row_map][col_map] = mat[row][col]

        return reshaped
