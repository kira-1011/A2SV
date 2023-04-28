class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # Multi source BFS variant
        # Apply BFS starting from all zeroes and calculate the distance to each discovered cell

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inBound = lambda r, c: -1 < r < len(mat) and -1 < c < len(mat[0])  

        queue = deque()
        visited = set()
        level = 0

        # Append the starting positions of each zeroes
        for row in range(len(mat)):
            for col in range(len(mat[0])):

                if mat[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        # Apply BFS from each starting points in the queue and find the distance to each cell
        while queue:

            level_len = len(queue)
            level += 1

            for i in range(level_len):

                row, col = queue.popleft()

                for row_change, col_change in directions:

                    new_row = row + row_change
                    new_col = col + col_change

                    if inBound(new_row, new_col) and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        mat[new_row][new_col] = level

        return mat
