class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse=True)

        left = 1
        right = len(piles) - 1
        max_coins = 0

        while left < right:
            
            max_coins += (piles[left])
            left += 2
            right -= 1
        
        return max_coins
