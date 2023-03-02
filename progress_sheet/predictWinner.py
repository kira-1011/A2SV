class Solution:

    def findWinner(self, nums, left, right, turn):
        
        # If all elements are consumed or one element remianing
        if left >= right:
            return turn * nums[left]
        
        # choose the left most element and collect the score
        # choose the right most element and collect the score
        left_score = turn * nums[left] + self.findWinner(nums, left + 1, right, -turn)
        right_score = turn * nums[right] + self.findWinner(nums, left, right - 1, -turn)

        # If its player's 2 turn take the minimum possible score since
        # Player 2 tries to maximize its score hence, minimizing player 1's score
        if turn == -1:
            return min(left_score, right_score)
        
        return max(left_score, right_score)

    def PredictTheWinner(self, nums: List[int]) -> bool:

        # When we need to look at different possibilities at the same time
        # and when branching is needed recursion is a good candidate for the solution
        score = self.findWinner(nums,0, len(nums) - 1, 1)

        # Check if player 1 can win the game
        isWinner = score >= 0

        return isWinner
