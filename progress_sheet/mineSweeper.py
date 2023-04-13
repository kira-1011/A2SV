class Solution:

    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]


    def dfsGrid(self, board, row, col, visited):
        
        visited.add((row, col))
        inBound = lambda r, c: -1 < r < len(board) and -1 < c < len(board[0])
        
        adjacent = 0

        # count adjacent mines
        for direction in self.directions:

            new_row = row + direction[0]
            new_col = col + direction[1]

            if inBound(new_row, new_col) and board[new_row][new_col] == 'M':
                adjacent += 1

        if adjacent:
            board[row][col] = str(adjacent)
            return
        
        else:
            board[row][col] = 'B'

        for direction in self.directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            if inBound(new_row, new_col) and (new_row, new_col) not in visited:
                self.dfsGrid(board, new_row, new_col, visited)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        self.dfsGrid(board, click[0], click[1], set())

        return board
        
