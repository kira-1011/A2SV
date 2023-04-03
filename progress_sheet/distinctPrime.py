class Solution:


    def distinctPrimeFactors(self, nums: List[int]) -> int:


        for num in nums:
            
            factor = 2
            distinct_primes = set()

            while factor * factor <= n:

                # divide while it's possible
                while n % factor == 0:
                    n //= factor
                    distinct_primes.add(factor)
                
                factor += 1
            
            if n > 1:
                distinct_primes.add(n)

        return len(set(distinct_primes))
