class Solution:

    def nthTribonacci(self, n, memo):

        if n == 1 or n == 2:
            return 1
        
        if n == 0:
            return 0
        
        if n not in memo:
            memo[n] = self.nthTribonacci(n - 3, memo) + self.nthTribonacci(n - 2, memo) + self.nthTribonacci(n - 1, memo)
        
        return memo[n]

    def tribonacci(self, n: int) -> int:

        return self.nthTribonacci(n, dict())
