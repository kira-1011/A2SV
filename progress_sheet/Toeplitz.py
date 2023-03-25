class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        row_len = len(matrix)
        col_len = len(matrix[0])

        for row in range(1, row_len):
            for col in range(1, col_len):

                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False

        return True
