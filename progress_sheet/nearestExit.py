class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        row_len, col_len = len(maze), len(maze[0])
        steps = 0

        inBound = lambda r, c: -1 < r < row_len and -1 < c < col_len
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = deque([(entrance[0], entrance[1])])

        # mark starting point as visited
        maze[entrance[0]][entrance[1]] = '+'
        
        # Apply bfs to find the shortest path to exit
        while queue:

            level_len = len(queue)

            for i in range(level_len):

                row, col = queue.popleft()

                for row_change, col_change in directions:

                    new_row = row + row_change
                    new_col = col + col_change

                    if inBound(new_row, new_col) and maze[new_row][new_col] != '+':

                        # check if we reached any exit point
                        if (new_row == 0) or (row_len - 1 == new_row) or (new_col == 0) or (col_len - 1 == new_col):
                            return steps + 1
                      
                        queue.append((new_row, new_col))
                        
                        # mark as visisted
                        maze[new_row][new_col] = '+'

            steps += 1

        return -1
