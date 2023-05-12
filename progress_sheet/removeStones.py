class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        # make each number negative
        piles = list(map(lambda x: -x, piles))

        heapify(piles)
        
        while piles and k:
            stone = -heappop(piles)
            stone -= (stone // 2)

            heappush(piles, -stone)
            k -= 1
            
        return -sum(piles)
