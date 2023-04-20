class Solution:

    def __init__(self):
        self.directions = None

    def inBound(self, board, row, col):
        return -1 < row < len(board) and -1 < col < len(board[0])

    def dfs(self, board, row, col, visited):
        
        board[row][col] = "#"
        visited.add((row, col))

        for row_change, col_change in self.directions:

            new_row = row + row_change
            new_col = col + col_change

            if self.inBound(board, new_row, new_col) and (new_row, new_col) not in visited and board[new_row][new_col] != 'X':
                self.dfs(board, new_row, new_col, visited)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.directions = [(0, 1), (0, -1), (1, 0), (-1 ,0)]

        # find edges with 'O' mark and mark the connected cells with it as '#'
        for row in range(len(board)):

            if board[row][0] == 'O':
                self.dfs(board, row, 0, set())
            
            if board[row][len(board[0]) - 1] == 'O':
                self.dfs(board, row, len(board[0]) - 1, set())
        
        for col in range(len(board[0])):

            if board[0][col] == 'O':
                self.dfs(board, 0, col, set())
            
            if board[len(board) - 1][col] == 'O':
                self.dfs(board, len(board) - 1, col, set())


        # retrun the '#' cells back to 'O' and mark the other spots as 'X'
        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col] == '#':
                    board[row][col] = 'O'
                
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                
