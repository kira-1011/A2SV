class Solution:

    def minCost(self, n, cost, memo):

        if n >= len(cost):
            return 0
        
        if n not in memo:
            memo[n] = cost[n] + min(self.minCost(n + 1, cost, memo), self.minCost(n + 2, cost, memo))
        
        return memo[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = dict()
        return min(self.minCost(0, cost, memo), self.minCost(1, cost, memo))
