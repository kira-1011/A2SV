class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        deletedCols = 0
        row_size = len(strs)
        col_size = len(strs[0])

        for col in range(col_size):

            for row in range(1, row_size):
                if strs[row - 1][col] > strs[row][col]:
                    deletedCols += 1
                    break

        return deletedCols
