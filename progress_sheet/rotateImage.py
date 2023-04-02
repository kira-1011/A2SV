class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()
        row_len = len(matrix)
        col_len = len(matrix[0])
        new_col = row_len - 1

        # reverse + transpose
        for row in range(row_len):
            for col in range(row + 1, col_len):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
