class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # Intialize needed variables 
        min_manhattan = maxsize
        min_idx = -1
        
        # Check valid points and update min_idx based on the minimum manhattan distance
        for index, point in enumerate(points):
            x1 = point[0]
            y1 = point[1]

            # if our point is valid, check the index with the minimum manhattan distance 
            if x == x1 or y == y1:
                manhattan_distance = abs(x - x1) + abs(y - y1)
            
                if min_manhattan > manhattan_distance:
                    min_manhattan = manhattan_distance
                    min_idx = index

                elif min_manhattan == manhattan_distance:
                    min_idx = min(min_idx, index)

        return min_idx
