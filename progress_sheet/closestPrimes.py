class Solution:

    def sieve_prime(self, start, n):

        d = 2
        is_prime = [True for i in range(n + 1)]
        is_prime[0] = is_prime[1] = False
        primes = []

        while d * d <= n:

            if is_prime[d]:

                i = d * d

                while i <= n:
                    is_prime[i] = False
                    i += d

            d += 1

        # filter only the prime numbers
        for i in range(start, n + 1):

            if is_prime[i]:
                primes.append(i)

        return primes

    def closestPrimes(self, left: int, right: int) -> List[int]:

        primes = self.sieve_prime(left, right) 
        min_diff = float('inf')
        ans = [-1, -1]

        for i in range(len(primes) - 1):
            
            curr_diff = primes[i + 1] - primes[i]

            if curr_diff < min_diff:
                min_diff = curr_diff
                ans = [primes[i], primes[i + 1]]

        return ans
