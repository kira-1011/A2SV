class Solution:

    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    
    def inBound(self, board, r, c):
        return -1 < r < len(board) and -1 < c < len(board[0])

    def countMines(self, board, row, col):
        
        adjacent = 0

        # count adjacent mines
        for row_change, col_change in self.directions:

            new_row = row + row_change
            new_col = col + col_change

            if self.inBound(board, new_row, new_col) and board[new_row][new_col] == 'M':
                adjacent += 1

        return adjacent

    def dfsGrid(self, board, row, col, visited):
        
        visited.add((row, col))

        # count adjacent mines
        adjacent = self.countMines(board, row, col)

        if adjacent:
            board[row][col] = str(adjacent)
            return
        
        else:
            board[row][col] = 'B'

        for row_change, col_change in self.directions:
            new_row = row + row_change
            new_col = col + col_change

            if self.inBound(board, new_row, new_col) and (new_row, new_col) not in visited:
                self.dfsGrid(board, new_row, new_col, visited)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        self.dfsGrid(board, click[0], click[1], set())

        return board
