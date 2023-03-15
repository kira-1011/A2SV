class Solution:

    def findKth(self, n , k):

        if n == 1:
            return 0
        
        prev_len = (2 ** (n - 1)) - 1
        
        if (k - prev_len) == 1:
            return 1
        
        if k <= prev_len:
            ans = self.findKth(n - 1, k)
        
        else:
            ans = 1 - self.findKth(n - 1, 2 * (prev_len + 1) - k)
        
        return ans

    def findKthBit(self, n: int, k: int) -> str:

        bit = self.findKth(n , k)

        return str(bit)
