class Solution:

    def __init__(self):
        self.grid = None

    def dfsGrid(self, row, col, visited):

        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        checkBound = lambda r, c: -1 < r < len(self.grid) and -1 < c < len(self.grid[0])

        visited.add((row, col))

        for direction in directions:

            new_row = row + direction[0]
            new_col = col + direction[1]

            if checkBound(new_row, new_col) and (new_row, new_col) not in visited and self.grid[new_row][new_col] == 1:
                self.dfsGrid(new_row, new_col, visited)
                

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        self.grid = grid
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if (row, col) not in visited and self.grid[row][col] == 1:
                    
                    # calculate previously visited total area
                    prev_area = len(visited)

                    self.dfsGrid(row, col, visited)

                    # calculate current visited total area
                    final_area = len(visited)

                    # calculate final visited total area and take the maximum
                    max_area = max(max_area, final_area - prev_area)
        
        return max_area
