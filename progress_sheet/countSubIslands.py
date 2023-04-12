class Solution:

    def dfsGrid(self, grid, row, col, visited):

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inBound = lambda r, c: -1 < r < len(grid) and -1 < c < len(grid[0])

        grid[row][col] = 0

        for direction in directions:
            
            new_row = row + direction[0]
            new_col = col + direction[1]

            if inBound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col]:
                self.dfsGrid(grid, new_row, new_col, visited)
  

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        visited1 = set()
        visited2 = set()
        sub_islands = 0

        # remove all the unwanted islands in grid2
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):

                if grid1[row][col] == 0 and grid2[row][col] == 1:
                    self.dfsGrid(grid2, row, col, visited2)
        
        # count sub islands
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):

                if grid2[row][col] == 1:
                    self.dfsGrid(grid2, row, col, visited2)
                    sub_islands += 1

        return sub_islands
