class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_nums = [set() for i in range(len(board))]
        col_nums = [set() for i in range(len(board))]
        box_nums = [set() for i in range(len(board))]

        validate = lambda num, row, col : num in range(1, 10) and num not in row_nums[row] and num not in col_nums[col] and num not in box_nums[(row // 3) * 3 + (col // 3)]

        # Check if each cell is not in the range of 1-9 and if there exist any duplicate in the same row or col or 3x3 box
        for row in range(len(board)):

            for col in range(len(board[0])):

                if board[row][col] != ".":
                    num = int(board[row][col])
                    idx = (row // 3) * 3 + (col // 3)

                    if not validate(num, row, col):
                        return False
                    
                    row_nums[row].add(num)
                    col_nums[col].add(num)
                    box_nums[idx].add(num)
        
        return True
