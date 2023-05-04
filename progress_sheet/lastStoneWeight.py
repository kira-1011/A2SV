class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = list(map(lambda x: -x, stones))

        heapify(stones)

        # choose the heaviest stones and smash them until stones array is empty or 1 element remains
        while len(stones) > 1:

            stone1 = heappop(stones)
            stone2 = heappop(stones)

            if stone1 != stone2:
                smashed = stone1 - stone2
                heappush(stones, smashed)

        if stones:
            return -stones[-1]
        
        return 0
