test_cases = int(input())

def findSum(board, row, col):

    directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
    checkBound = lambda row, col: -1 < row < len(board) and -1 < col < len(board[0])
    curr_sum = 0

    for direction in directions:

        curr_row, curr_col = row + direction[0], col + direction[1]

        while checkBound(curr_row, curr_col):
            curr_sum += board[curr_row][curr_col]
            curr_row += direction[0]
            curr_col += direction[1]

    return curr_sum + board[row][col]

for _ in range(test_cases):

    n, m = map(int, input().split())
    board = []
    max_sum = 0

    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            max_sum = max(max_sum, findSum(board, row, col))    
    
    print(max_sum)
