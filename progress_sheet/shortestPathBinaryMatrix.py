class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0),(-1, 0), 
                    (1, 1),(-1, -1),(1, -1),(-1, 1)]

        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        inBound = lambda r, c: -1 < r < n and -1 < c < n
        levels = 0
        
        # use bfs to discover the shortes path
        while queue:

            level_len = len(queue)

            for i in range(level_len):

                row, col = queue.popleft()

                # if we reached the bottom right cell stop
                if row == n - 1 and col == n - 1:
                    return levels + 1

                for row_change, col_change in directions:

                    new_row = row + row_change
                    new_col = col + col_change

                    if inBound(new_row, new_col) and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            levels += 1
        
        return -1
