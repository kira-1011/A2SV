def crossout(grid, row, col):

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    checkBound = lambda r, c: -1 < r < len(grid) and -1 < c < len(grid[0])
    target = grid[row][col]
    curr_row = row
    curr_col = col

    for direction in directions:

        while checkBound(curr_row, curr_col):
            
            if (curr_row != row or curr_col != col) and grid[curr_row][curr_col] == target:
                return True
            
            curr_row += direction[0]
            curr_col += direction[1]

        curr_row = row
        curr_col = col

    return False

n, m = map(int, input().split())
grid = []
encrypted = []

for _ in range(n):
    row = input()
    grid.append(row)

for row in range(n):
    for col in range(m):

        if crossout(grid, row, col):
            continue

        encrypted.append(grid[row][col])

print(''.join(encrypted))
