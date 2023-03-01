class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        row_len = len(matrix)
        col_len = len(matrix[0])

        # Store the prefix sum of each row
        for row in range(row_len):
            for col in range(1, col_len):
                matrix[row][col] += matrix[row][col - 1]
        
        # Store the prefix sum of each column
        for col in range(col_len):
            for row in range(1, row_len):
                matrix[row][col] += matrix[row - 1][col]

        # Append 0 row array to handle the first row,when row - 1 is accessed        
        matrix.append([0] * col_len)

        # Append 0 column array to handle the first column,when col - 1 is accessed        
        for row_arr in matrix:
            row_arr.append(0)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        # Exclude the prefix sum above the topleft row
        # Exclude the prefix sum that is to the left of the topleft column
        # To extract the sum of the required region
        total_sum = self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        total_sum -= (self.matrix[row2][col1 - 1] - self.matrix[row1 - 1][col1 - 1])
        return total_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
