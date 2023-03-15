class Solution:

    def findKth(self, n, k):

        if n == 1:
            return 0
        
        # check if k is less or greater than the previous string length
        prev_len = (2 ** (n - 2))

        # take the previous string kth bit directly
        if k <= prev_len:
            return self.findKth(n - 1, k)
        
        # take the previous string kth bit directly and invert it
        return 1 - self.findKth(n - 1, k - prev_len)

    def kthGrammar(self, n: int, k: int) -> int:

        return self.findKth(n, k)
