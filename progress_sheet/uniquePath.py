class Solution:

    def __init__(self):
        self.memo = defaultdict(int)
        self.n = 0
        self.m = 0

    def countWays(self, row, col):

        # stop when we go out of bound
        if row >= self.m or col >= self.n:
            return 0

        # stop when we reach the end
        if row == self.m - 1 and col == self.n - 1:
            return 1
        
        if (row, col) not in self.memo:
            self.memo[(row, col)] = self.countWays(row, col + 1) + self.countWays(row + 1, col)

        return self.memo[(row, col)]

    def uniquePaths(self, m: int, n: int) -> int:

        self.n = n
        self.m = m

        return self.countWays(0, 0)
