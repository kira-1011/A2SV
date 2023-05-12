class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        max_heap = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                heappush(max_heap, -matrix[row][col])

                if len(max_heap) > k:
                    heappop(max_heap)

        return -max_heap[0]
