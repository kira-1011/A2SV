class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        size = len(grid)
        pairs = 0
        column_map = defaultdict(int)

        # Add column arrays as key and its occurenece as value into a dictionary 
        for i in range(size):
            
            col_arr = []

            for row in grid:
                col_arr.append(row[i])
            
            column_map[tuple(col_arr)] += 1
        
        # Look for the row array in the column map
        for row_arr in grid:
            
            row_arr = tuple(row_arr)
            pairs += column_map[row_arr]

        return pairs