class Solution:

    def myPow(self, x: float, n: int) -> float:

        if n == 0 or x == 1:
            return 1

        
        if n < 0:
            return self.myPow(1 / x, -n)

        power = self.myPow(x * x, n // 2)

        if n % 2 != 0:
            power *= x
            
        return power
