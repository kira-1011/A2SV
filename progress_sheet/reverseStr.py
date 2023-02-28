class Solution:
    
    def reverseStr(self, s, left, right):
        
        # base case if left pointer is greater return 
        if left >= right:
            return
        
        # swap the first and last element
        s[left], s[right] = s[right], s[left]

        # move the left and right pointers and call reverseStr
        self.reverseStr(s, left + 1, right - 1)
        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        self.reverseStr(s, 0, len(s) - 1)
