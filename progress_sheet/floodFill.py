class Solution:

    def __init__(self):

        self.image = []
        self.color = 0
        self.curr_color = 0

    def dfsGrid(self, row, col, visited):

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        checkBound = lambda r, c : 0 <= r < len(self.image) and 0 <= c < len(self.image[0])

        for direction in directions:

            visited.add((row, col))
            new_row = row + direction[0]
            new_col = col + direction[1]

            if (new_row, new_col) not in visited and checkBound(new_row, new_col) and self.curr_color == self.image[new_row][new_col]:
                self.image[new_row][new_col] = self.color
                self.dfsGrid(new_row, new_col, visited)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        self.image = image
        self.color = color
        self.curr_color = image[sr][sc]
        image[sr][sc] = color
        self.dfsGrid(sr, sc, set())

        return self.image
