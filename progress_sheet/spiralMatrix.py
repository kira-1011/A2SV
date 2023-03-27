class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        direction = (0, 1)
        row, col = 0, 0
        row_len, col_len = len(matrix), len(matrix[0])
        spiral = []
        visited = set()
        
        checkBound = lambda row, col : -1 < row < row_len  and -1 < col < col_len

        while len(spiral) < (row_len * col_len):

            spiral.append(matrix[row][col])
            visited.add((row, col))

            new_row = row + direction[0]
            new_col = col + direction[1]
            if (new_row, new_col) not in visited and checkBound(new_row, new_col):
                row = new_row
                col = new_col
            
            else:
                direction = (direction[1], -direction[0])
                row, col = row + direction[0], col + direction[1]

        return spiral
