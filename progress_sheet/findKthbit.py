class Solution:

    def invert(self, s):

        inverted_str = []
        
        for i in range(len(s)):
            if s[i] == "0":
                inverted_str.append("1")
            
            else:
                inverted_str.append("0")
        
        return inverted_str
    
    def nthBitString(self, n):

        if n == 1:
            return ["0"]
        
        binary_str = self.nthBitString(n - 1)

        inverted_str = self.invert(binary_str)
        inverted_str.reverse()
        
        binary_str.append("1")
        binary_str += inverted_str

        return binary_str
    

    def findKthBit(self, n: int, k: int) -> str:

        kth_bit = self.nthBitString(n)
        return kth_bit[k - 1]
