class Solution:

    def GCD(self, a, b):

        if b == 0:
            return a
        
        return self.GCD(b, a % b)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        count = Counter(deck)

        curr_gcd = 0

        for occurenece in count.values():
            curr_gcd = self.GCD(curr_gcd, occurenece)
        
        if curr_gcd == 1:
            return False
        
        return True
