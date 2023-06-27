class Solution:
    
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        glasses = [[0 for i in range(100)] for i in range(100)]

        glasses[0][0] = poured

        for row in range(query_row):

            for col in range(row + 1):
                
                if glasses[row][col] >= 1:

                    overflowed = glasses[row][col] - 1
                    overflowed /= 2.0
                    glasses[row][col] = 1
                    glasses[row + 1][col] += overflowed
                    glasses[row + 1][col + 1] += overflowed

 
        return glasses[query_row][query_glass] if glasses[query_row][query_glass] < 1 else 1
