class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev_num = str(x)

        rev_num = int(rev_num[::-1])

        return rev_num == x
