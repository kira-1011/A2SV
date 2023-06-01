class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        # 0 1 2 3 4
        # 0 1 1 2 1 

        # dp bottom down approach
        dp = [0 for i in range(n + 1)]
        dp[0] = 0

        if n > 0:
            dp[1] = 1

        for i in range(2, n + 1):

            if i % 2:
                idx = (i - 1) // 2
                dp[i] = dp[idx] + dp[idx + 1]
            
            else:
                idx = i // 2
                dp[i] = dp[idx]
        
        return max(dp)
