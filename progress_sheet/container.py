class Solution:
    def maxArea(self, height: List[int]) -> int:

        size = len(height)
        max_amount = 0
        left = 0
        right = size - 1

        # find the maximum amount using colliding two pointers
        while left < right:
            amount = min(height[left], height[right]) * (right - left)
            max_amount = max(max_amount, amount)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_amount
