class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Swap the last two elements continously
        size = len(s)
        half_size = size // 2

        for i in range(half_size):
            s[i], s[size - i - 1] = s[size - i - 1], s[i]
        
        return s